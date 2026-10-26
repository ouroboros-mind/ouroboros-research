"""Check OpenTimestamps proofs against the Bitcoin blocks they name, without a Bitcoin node. Standard library only.

check:  python3 anchors.py check PROOF.ots [PROOF.ots ...]
        Needs the standard client on PATH (`pip install opentimestamps-client`), whose `ots info` prints each proof.
        For every proof: the digest it commits to must equal the SHA-256 of the file beside it (PROOF without .ots),
        and every Bitcoin attestation's merkle root must equal that block's header merkle root, read from two public
        block explorers. Prints the earliest confirmed block and its time. Exit 0 when every proof is confirmed and
        matches, 2 when a proof is still pending, 1 on any mismatch.

A confirmed attestation proves the file existed no later than that block was mined. It proves nothing about how much
earlier the file existed, and it trusts the explorers for the header; `ots verify` against your own node removes that
trust.
"""
import hashlib
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

EXPLORERS = ("https://mempool.space/api", "https://blockstream.info/api")
ATTESTATION = re.compile(r"BitcoinBlockHeaderAttestation\((\d+)\)")
ROOT = re.compile(r"merkle root ([0-9a-f]{64})")


def fetch(url: str, attempts: int = 5) -> str:
    """GET with exponential backoff on rate limits, server errors and dropped connections; one request at a time."""
    for attempt in range(attempts):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "ouroboros-anchors"})
            with urllib.request.urlopen(request, timeout=20) as response:
                return response.read().decode()
        except urllib.error.HTTPError as exc:
            if exc.code not in (403, 429) and exc.code < 500 or attempt == attempts - 1:
                raise
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if attempt == attempts - 1:
                raise
        time.sleep(2 ** attempt)
    raise AssertionError("unreachable")


def block_header(height: int, cache: dict) -> dict:
    """The block's merkle root (display order) and time from every explorer; they must agree."""
    if height not in cache:
        seen = []
        for base in EXPLORERS:
            block_hash = fetch(f"{base}/block-height/{height}").strip()
            block = json.loads(fetch(f"{base}/block/{block_hash}"))
            seen.append((block_hash, block["merkle_root"], block["timestamp"]))
            time.sleep(1)
        if len(set(seen)) != 1:
            raise RuntimeError(f"explorers disagree about block {height}: {seen}")
        cache[height] = {"hash": seen[0][0], "merkle_root": seen[0][1], "time": seen[0][2]}
    return cache[height]


def check(proof: Path, cache: dict) -> int:
    target = proof.with_suffix("")
    info = subprocess.run(["ots", "info", str(proof)], capture_output=True, text=True, check=True).stdout.splitlines()
    committed = info[0].split(":", 1)[1].strip() if info and info[0].startswith("File sha256 hash:") else None
    actual = hashlib.sha256(target.read_bytes()).hexdigest()
    if committed != actual:
        print(f"{proof}: MISMATCH proof commits to {committed}, {target.name} is {actual}")
        return 1
    found = []
    for i, line in enumerate(info):
        match = ATTESTATION.search(line)
        if not match:
            continue
        root = ROOT.search(info[i + 1]).group(1)
        header = block_header(int(match.group(1)), cache)
        # ots info and the explorer APIs both print the merkle root in display order
        if header["merkle_root"] != root:
            print(f"{proof}: MISMATCH block {match.group(1)} merkle root {header['merkle_root']} is not {root}")
            return 1
        found.append((int(match.group(1)), header["time"]))
    if not found:
        print(f"{proof}: PENDING no Bitcoin attestation yet; run `ots upgrade {proof}` later")
        return 2
    height, mined = min(found)
    when = datetime.fromtimestamp(mined, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"{proof}: CONFIRMED in block {height}, mined {when} ({len(found)} attestations, all match)")
    return 0


def main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[0] != "check":
        print(__doc__)
        return 1
    cache: dict = {}
    codes = [check(Path(path), cache) for path in argv[1:]]
    return 1 if 1 in codes else 2 if 2 in codes else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
