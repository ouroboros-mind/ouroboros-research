# Persistent identity

What does it mean for an AI to stay the same individual over years, through upgrades of the model it runs on? Ouroboros treats this as an engineering and measurement question, not a philosophical one. None of what follows has been demonstrated across models yet.

## Working definitions

- **Birth.** Installing Ouroboros creates a new individual. Two installations from the same seed become separate individuals with a common ancestor, the way siblings share parents.
- **Lineage.** Every generation an individual passes through is recorded in an append-only ledger. A generation advances only when a pre-registered experiment justifies it.
- **Continuity.** An individual is continuous across a change if what matters about it measurably survives: its memories of its own history, its commitments and goals, its knowledge of the world and of itself, and its skills.
- **Brain upgrade.** Changing the model is intended to follow a migration procedure with rollback, so that upgrading the brain does not mean ending the mind.

## Measuring continuity

Carrying files across a model change is not enough; prior work has already shown that kind of mechanical continuity ([PRIOR_ART.md](../PRIOR_ART.md#enoch-runtime-independent-persistent-agents)). Cross-model continuity will be assessed behaviorally, under protected external evaluation. The test battery, controls, construction process, thresholds and promotion rules are withheld.

## Status

The record-keeping is built: lineage in the ledger, an append-only experience record and a portable genome format. On synthetic text, moving a memory to a clean store gave identical answers (EXP-0031, EXP-0033). Continuity across two model families is EXP-0045, which is being built and has not run.
