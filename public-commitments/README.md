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
- Per-experiment commitments: [EXP-0046](experiments/EXP-0046.commitment.json), committed 2026-10-21 after its pre-registration and before its run. It is the first.
- A third-party timestamp (for example OpenTimestamps) for each commitment is planned and not yet in place.
