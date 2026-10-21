"""Ouroboros public commitments, format ouroboros-commitment-v1. Standard library only.

commit:  python3 commitment.py commit PREREG.json EXP-ID PUBLIC_DIR PRIVATE_DIR
         writes PUBLIC_DIR/EXP-ID.commitment.json and PRIVATE_DIR/EXP-ID.salts.json (keep private;
         refused if PRIVATE_DIR is inside this repository)
reveal:  python3 commitment.py reveal PREREG.json SALTS.json FIELD [FIELD ...] > EXP-ID.reveal.json
verify:  python3 commitment.py verify COMMITMENT.json REVEAL.json      (selected fields)
         python3 commitment.py verify-full COMMITMENT.json PREREG.json SALTS.json
ledger:  python3 commitment.py verify-ledger LEDGER.jsonl ledger-checkpoints.json   (for an auditor given the ledger)
"""
import hashlib
import json
import os
import secrets
import sys
from datetime import datetime, timezone

FORMAT = "ouroboros-commitment-v1"


def canonical(obj) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def h(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def leaf(field: str, value, salt_hex: str) -> bytes:
    return h(b"\x00" + bytes.fromhex(salt_hex) + canonical({field: value}))


def levels(leaves: list[bytes]) -> list[list[bytes]]:
    out = [leaves]
    while len(out[-1]) > 1:
        row = out[-1]
        out.append([h(b"\x01" + row[i] + row[i + 1]) if i + 1 < len(row) else row[i] for i in range(0, len(row), 2)])
    return out


def path(tree: list[list[bytes]], index: int) -> list[dict]:
    steps = []
    for row in tree[:-1]:
        sib = index ^ 1
        if sib < len(row):
            steps.append({"side": "left" if sib < index else "right", "hash": row[sib].hex()})
        index //= 2
    return steps


def root_from(leaf_hash: bytes, index: int, steps: list[dict], count: int) -> bytes | None:
    """The root a Merkle path leads to, or None when the path's shape does not fit the tree."""
    node, width, used = leaf_hash, count, 0
    while width > 1:
        if index ^ 1 < width:
            if used >= len(steps):
                return None
            s, used = steps[used], used + 1
            side = "left" if index % 2 else "right"
            if s.get("side") != side or len(bytes.fromhex(s["hash"])) != 32:
                return None
            sib = bytes.fromhex(s["hash"])
            node = h(b"\x01" + sib + node) if side == "left" else h(b"\x01" + node + sib)
        index, width = index // 2, (width + 1) // 2
    return node if used == len(steps) else None


def commit(prereg: dict, experiment_id: str, committed_at: str | None = None) -> tuple[dict, dict]:
    fields = sorted(prereg)
    salts = {f: secrets.token_hex(32) for f in fields}
    tree = levels([leaf(f, prereg[f], salts[f]) for f in fields])
    public = {"format": FORMAT, "experiment_id": experiment_id,
              "committed_at": committed_at or datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "fields": fields, "merkle_root": tree[-1][0].hex()}
    return public, {"format": FORMAT, "experiment_id": experiment_id, "salts": salts}


def reveal(prereg: dict, salts: dict, wanted: list[str]) -> dict:
    fields = sorted(prereg)
    tree = levels([leaf(f, prereg[f], salts["salts"][f]) for f in fields])
    return {"format": FORMAT, "experiment_id": salts["experiment_id"], "revealed": [
        {"field": f, "value": prereg[f], "salt": salts["salts"][f], "index": fields.index(f),
         "path": path(tree, fields.index(f))} for f in wanted]}


def verify(public: dict, rev: dict) -> list[str]:
    problems = []
    if public.get("format") != FORMAT or rev.get("format") != FORMAT:
        problems.append("unknown format")
    if rev.get("experiment_id") != public.get("experiment_id"):
        problems.append("experiment_id differs")
    if not rev.get("revealed"):
        problems.append("no fields revealed")
    for r in rev.get("revealed", []):
        if not isinstance(r.get("index"), int) or not 0 <= r["index"] < len(public["fields"]) \
                or public["fields"][r["index"]] != r["field"]:
            problems.append(f"{r['field']}: index does not match the committed field list")
            continue
        got = root_from(leaf(r["field"], r["value"], r["salt"]), r["index"], r["path"], len(public["fields"]))
        if got is None or got.hex() != public["merkle_root"]:
            problems.append(f"{r['field']}: does not match the committed root")
    return problems


def verify_full(public: dict, prereg: dict, salts: dict) -> list[str]:
    if sorted(prereg) != public["fields"]:
        return ["field list differs from the commitment"]
    tree = levels([leaf(f, prereg[f], salts["salts"][f]) for f in public["fields"]])
    return [] if tree[-1][0].hex() == public["merkle_root"] else ["document does not match the committed root"]


def verify_ledger(lines: list[str], checkpoints: list[dict]) -> list[str]:
    problems, prev, heads = [], "0" * 64, {}
    for i, line in enumerate(l for l in lines if l.strip()):
        e = json.loads(line)
        if e.get("seq") != i:
            problems.append(f"entry {i}: seq {e.get('seq')} out of order")
        if e.get("prev_entry_sha256") != prev:
            problems.append(f"entry {i}: chain broken" + (" (does not start at genesis)" if i == 0 else ""))
        if hashlib.sha256(canonical(e.get("payload"))).hexdigest() != e.get("payload_sha256"):
            problems.append(f"entry {i}: payload hash differs")
        if hashlib.sha256(canonical({k: v for k, v in e.items() if k != "entry_sha256"})).hexdigest() != e.get("entry_sha256"):
            problems.append(f"entry {i}: entry hash differs")
        prev = e.get("entry_sha256"); heads[e.get("seq")] = prev
    for c in checkpoints:
        if c.get("entries") != c["seq"] + 1:
            problems.append(f"checkpoint seq {c['seq']}: entry count {c.get('entries')} is not seq + 1")
        if heads.get(c["seq"]) != c["entry_sha256"]:
            problems.append(f"checkpoint seq {c['seq']} ({c['date']}): not found in this ledger")
    return problems


def _load(p):
    with open(p, encoding="utf-8") as fh:
        return json.load(fh)


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__); return 2
    cmd, args = argv[1], argv[2:]
    if cmd == "commit":
        repo = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
        private = os.path.realpath(args[3])
        if os.path.commonpath([repo, private]) == repo:
            print(f"refused: {args[3]} is inside the public repository; keep salts private"); return 2
        pub, sal = commit(_load(args[0]), args[1])
        for path, obj in ((os.path.join(args[2], f"{args[1]}.commitment.json"), pub),
                          (os.path.join(args[3], f"{args[1]}.salts.json"), sal)):
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(json.dumps(obj, indent=2, ensure_ascii=False) + "\n")
        print(pub["merkle_root"]); return 0
    if cmd == "reveal":
        print(json.dumps(reveal(_load(args[0]), _load(args[1]), args[2:]), indent=2, ensure_ascii=False)); return 0
    if cmd == "verify-ledger":
        with open(args[0], encoding="utf-8") as fh:
            problems = verify_ledger(fh.readlines(), _load(args[1])["checkpoints"])
        print("OK" if not problems else "\n".join(problems)); return 0 if not problems else 1
    problems = verify(_load(args[0]), _load(args[1])) if cmd == "verify" else \
        verify_full(_load(args[0]), _load(args[1]), _load(args[2])) if cmd == "verify-full" else ["unknown command"]
    print("OK" if not problems else "\n".join(problems))
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
