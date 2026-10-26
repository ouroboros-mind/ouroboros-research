# Evaluation philosophy

> Ouroboros does not accept a change because the AI says it is better.

A program about self-improvement is only as credible as its measurements. These are the principles every Ouroboros experiment follows. They describe the author's practice; the private ledger and evaluation code have not been externally audited, so treat them as author-reported (see [what you can and cannot verify](../README.md#what-you-can-and-cannot-verify)).

1. **Pre-registration.** Each experiment's hypothesis, gates and decision rule are recorded in an append-only, hash-chained ledger before it runs. From EXP-0046 on, a hash of the pre-registration is published before the run, and from EXP-0050 on that hash is also anchored to the Bitcoin blockchain through OpenTimestamps, a tamper-evident public record. For the first EXP-0050 commitment, its amendment 1 and its selection, the confirming block came after the governed work began; from amendment 2 on, the work waits for the block. Decisions are final; a rejected idea is retried as a new experiment.
2. **Hard checks first.** Automatic, deterministic correctness checks are preferred. Model judges are used only where no hard check exists, and count as weaker evidence.
3. **Protected evaluation.** Evaluation material and promotion rules are kept outside the learning system and are designed to be unreachable from it.
4. **Held-out checks before replacement.** A candidate replaces the current version only if it beats it on held-out tasks and passes a forgetting check.
5. **Regression, forgetting and noise.** Every evaluation measures what got worse as well as what got better, and compares changes with the evaluation's own measured noise.
6. **Controls and seeds.** Experiments use controls where they make sense and several training seeds, because results that swing by seed cannot be trusted. Seeds are not independent replications.
7. **What it cannot tell us.** Every result is recorded with a plain statement of its limits.
8. **Negative results stay.** Rejected, null and inconclusive outcomes remain in the [ledger](../EXPERIMENTS.md).
9. **Human promotion and rollback.** Generation zero is frozen. A new generation is a recorded human decision that cites accepted experiments, and every change can be rolled back.

Evaluation construction (task sets, verifiers, controls, thresholds and selection rules) is withheld.
