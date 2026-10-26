# Public commitments

Ouroboros pre-registers every experiment in a private, hash-chained ledger before it runs. This folder lets anyone check, later, that a commitment to a pre-registration was public in a fixed form by a known publication time, without publishing the private evaluation, task content or methods.

## What is published

| File | What it is | When |
|---|---|---|
| `experiments/EXP-NNNN.commitment.json` | A salted SHA-256 commitment to one experiment's pre-registration | Before the experiment runs |
| `ledger-checkpoints.json` | The hash of the newest ledger entry, which fixes every earlier entry | When results are published |
| `commitment.py` | The commit, reveal and verify tool (Python standard library only) | Now |
| `examples/` | A toy pre-registration with everything revealed, so the whole process can be checked end to end | Now |

## How a commitment works

1. Each top-level field of the pre-registration (hypothesis, decision rule, evaluation suites and so on) gets its own random 32-byte salt.
2. Each field becomes a leaf: `SHA-256(0x00 || salt || canonical JSON of {field: value})`.
3. The leaves, in sorted field order, are combined into a Merkle tree (`SHA-256(0x01 || left || right)`; an unpaired node moves up unchanged). The commitment file publishes the root, the field names and the time.
4. The salts stay private, outside this repository (the tool refuses to write them here). Without them, a commitment reveals nothing about the content, even for short or guessable fields.

A commitment is pushed to this repository before the run starts. GitHub records when each push arrives, independently of the commit's own date.

From EXP-0050 on, each commitment is submitted to OpenTimestamps before the run. The proof sits beside the commitment as `<name>.ots`. A new proof remains pending until a calendar supplies its path to a Bitcoin attestation, usually within a few hours. From `public-commitments`, install the standard client with `pip install opentimestamps-client`, inspect the proof with `ots info experiments/EXP-0050.commitment.json.ots`, upgrade it in place with `ots upgrade experiments/EXP-0050.commitment.json.ots`, and verify it with `ots verify experiments/EXP-0050.commitment.json.ots`. Bitcoin verification with client 0.7 requires access to a Bitcoin Core node. Without one, `python3 anchors.py check experiments/*.ots` checks each proof against the Bitcoin blocks it names: the proof must commit to the SHA-256 of the file beside it, and every attestation's merkle root must equal that block's header merkle root as two public block explorers (mempool.space and blockstream.info) report it. It prints the earliest confirming block and when it was mined. That proves the file existed no later than that block; it trusts the explorers for the header, which `ots verify` against your own node does not.

From EXP-0050 amendment 2 on, the work a commitment governs does not start until its proof is confirmed in a Bitcoin block. The earlier EXP-0050 proofs below were each submitted before the work they govern and confirmed by Bitcoin after that work had begun, so for them the OpenTimestamps calendar receipt and the GitHub push time, not the block, show that they came first.

## How it can be checked later

- **Selected fields, in public.** For a published result, the project can reveal chosen fields (for example the hypothesis and the decision rule) with their salts and Merkle paths. Anyone runs `python3 commitment.py verify COMMITMENT.json REVEAL.json`. Fields that stay private, such as evaluation details, stay hidden and are still bound by the same root.
- **Everything, in private.** An independent auditor can be given the full pre-registration and its salts and run `verify-full`. Nothing needs to become public.
- **The ledger.** An auditor given the private ledger runs `verify-ledger LEDGER.jsonl ledger-checkpoints.json`, which recomputes the hash chain and checks every published checkpoint.

Try it on the example:

```bash
cd public-commitments
python3 commitment.py verify examples/EXAMPLE-0001.commitment.json examples/EXAMPLE-0001.reveal.json
python3 commitment.py verify-full examples/EXAMPLE-0001.commitment.json examples/EXAMPLE-0001.prereg.json examples/EXAMPLE-0001.salts.json
```

Both print `OK`. Change one character in the reveal or the pre-registration and they fail.

## Commitments made under this process

1. Every experiment committed here gets a published outcome, including negative and inconclusive ones. A commitment with no outcome is itself visible.
2. A commitment is never edited or deleted. A corrected pre-registration is a new commitment that names the one it replaces, before the run.
3. When a result is published, the hypothesis and decision rule are revealed for verification, unless revealing them would disclose protected methods; the result page then says what was withheld.

## What this does and does not prove

It proves that the commitment was publicly present, unchanged, no later than the time it reached GitHub, and that each revealed field is exactly one field bound by it. A whole pre-registration is verified only through a full reveal or a private audit.

It does not prove that no trial run happened before the commitment, that the private evaluation is sound, or that published numbers are correct. The author controls both the ledger and the timing. It narrows what an author could change after seeing a result; it does not replace independent replication.

## Status

- Ledger checkpoint 2026-10-21: entry 92 of the private ledger, covering EXP-0001 to EXP-0045. Those 45 experiments were pre-registered in the private ledger before this folder existed, so their pre-run timing remains author-reported. The checkpoint fixes their records from 2026-10-21 on.
- Per-experiment commitments: [EXP-0046](experiments/EXP-0046.commitment.json), committed 2026-10-21 after its pre-registration and before its run, the first. Its [reveal](experiments/EXP-0046.reveal.json) opens four fields (experiment id, creation time, status "planned", decision "pending"); the hypothesis and decision rule stay private because they contain training settings and gate thresholds. These fields prove only that they were bound by the pre-run commitment; they do not verify the withheld hypothesis, decision rule, methods or outcome.
- Ledger checkpoint 2026-10-22: entry 94, covering EXP-0001 to EXP-0046.
- Per-experiment commitments: [EXP-0047](experiments/EXP-0047.commitment.json), committed 2026-10-22 after its pre-registration and before its run. Its [reveal](experiments/EXP-0047.reveal.json) opens the same four fields. The commitment root is `d5544317650f2148cfe55bf3e5b866a4fa1b94a3ca37e94d9cd089dac2f7a5e5`. These fields prove only that they were bound by the pre-run commitment; they do not verify the withheld hypothesis, decision rule, methods or outcome.
- Ledger checkpoint 2026-10-22: entry 96, covering EXP-0001 to EXP-0047.
- Per-experiment commitments: [EXP-0048](experiments/EXP-0048.commitment.json), committed 2026-10-22 after its pre-registration and before its run. Its [reveal](experiments/EXP-0048.reveal.json) opens the same four fields. The commitment root is `8ac7c70dcb86f4607bd1e71d5a8bf75103bf3c52b170b1155df9e5adf6222c61`. These fields prove only that they were bound by the pre-run commitment; they do not verify the withheld hypothesis, decision rule, methods or outcome.
- Ledger checkpoint 2026-10-23: entry 98, covering EXP-0001 to EXP-0048.
- Per-experiment commitments: [EXP-0049](experiments/EXP-0049.commitment.json), committed 2026-10-23 after its pre-registration and before its run. Its [reveal](experiments/EXP-0049.reveal.json) opens the same four fields. Five [amendments](experiments/) and a [selection commitment](experiments/EXP-0049.selection.json) were published before the work each governed. These fields prove only that they were bound by the pre-run commitment; they do not verify the withheld hypothesis, decision rule, methods or outcome.
- Ledger checkpoint 2026-10-24: entry 105, covering EXP-0001 to EXP-0049.
- Per-experiment commitments: [EXP-0050](experiments/EXP-0050.commitment.json), committed 2026-10-25 after its pre-registration and before its run, with its OpenTimestamps proof [EXP-0050.commitment.json.ots](experiments/EXP-0050.commitment.json.ots), the first commitment submitted for a third-party timestamp, confirmed in Bitcoin block 973045 (mined 2026-10-25 08:55:04 UTC). The commitment root is `cdcce98fcce503a0e06ac05bb782f4240ee56cd2f138524fc1ef8fca95e5e1b4`. Its [selection commitment](experiments/EXP-0050.selection.json) was published before the work it governs, with its OpenTimestamps proof [EXP-0050.selection.json.ots](experiments/EXP-0050.selection.json.ots), confirmed in Bitcoin block 973088 (mined 2026-10-25 15:21:36 UTC).
- [EXP-0050 amendment 1](experiments/EXP-0050.amendment1.commitment.json), committed 2026-10-25 before the work it governs, with its OpenTimestamps proof [EXP-0050.amendment1.commitment.json.ots](experiments/EXP-0050.amendment1.commitment.json.ots), confirmed in Bitcoin block 973077 (mined 2026-10-25 13:45:40 UTC). The commitment root is `2249f6e28719279d4d327e69b7d8b2346923a5ccc853fc88fc3c25ebade328b8`.
- [EXP-0050 amendment 2](experiments/EXP-0050.amendment2.commitment.json), committed 2026-10-26 before the work it governs, with its OpenTimestamps proof [EXP-0050.amendment2.commitment.json.ots](experiments/EXP-0050.amendment2.commitment.json.ots), confirmed in Bitcoin block 973246 (mined 2026-10-26 14:00:59 UTC) before the work it governs started. The commitment root is `799c1c93dc4c93f27132d534f18456f5655ea50795c5b1cfd4a23079dfa15a8e`.
- Commitments before EXP-0050 rely on GitHub push times only; they have no third-party timestamp.
