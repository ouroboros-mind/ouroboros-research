# Ouroboros in one page

*For journalists, analysts and anyone who wants the short version. Free to quote with attribution.*

## Summary

Ouroboros asks whether an AI can develop like an individual instead of being replaced like software. The project is designed to separate the persistent mind from the underlying language model, so that memories, skills, self-knowledge and eventually learned capabilities could survive upgrades to the AI's neural cortex. EXP-0048 found that a cache regrown from the new model's own verified passes beat that new model alone. EXP-0050 found that a re-presented frame helped on familiar families, but the combined artifact regressed on unseen ones. Transfer of learned capability and general model independence remain unproven.

In its most recent growth experiment, EXP-0044, three seeded skill lineages on one model each went through two rounds of gated training, where a new version was kept only if it beat the current one on held-out tasks and passed a forgetting check. All three finished higher on a 600-task held-out test, by 8.2, 6.8 and 6.5 percentage points, with no regression on the whole task territory beyond base noise and measured forgetting below 0.01. Two difficulty levels dipped inside those gains. The experiment did not identify which part of the process caused the gain, and it did not measure transfer to other kinds of tasks. Whether the gains transfer, and whether improved generations become better at improving, are the next questions.

## Key facts

| | |
|---|---|
| What it is | A research program on lifelong, model-independent AI |
| Central idea | The mind is durable. The cortex is replaceable |
| Demonstrated so far | Narrow skill gains over two gated rounds, on one model, in one task territory; first-form continuity across two model families (EXP-0045); a one-model neural-skill gain with the kernel and non-cache records unchanged (EXP-0046); continuity and rollback through one mature-mind migration (EXP-0047); one skill regrown from the new model's verified passes that beat that model alone (EXP-0048); a trained artifact combining a re-presented frame with its regrown skill that beat raw on familiar task families but regressed on unseen ones (EXP-0050). The presentation-contribution gate did not pass |
| Not yet demonstrated | General model independence; a regrown skill accepted in quarantine that helps on unseen task families; transfer beyond the registered families and this model; lifelong operation; recursive improvement |
| Evidence standard | Every experiment pre-registered in a private, author-maintained ledger; negative results published |
| Experiments to date | 50, all listed with their outcomes |
| Latest result | EXP-0050: re-presenting the working frame, not supported. The familiar-family gain did not hold on unseen families, and both regrown skills were refused in quarantine |
| Next question | Proposed, owner decision pending: why the regrown skill hurt unseen families and failed quarantine while the presentation alone helped |
| Hardware | A GX10-class (NVIDIA GB10) research workstation; gaming-class GPUs are a long-term direction |
| Code and data | Private. This public repository holds the research record |

## What Ouroboros does not claim

Not AGI. We have no evidence that Ouroboros is sentient, and we make no such claim. Not unrestricted or indefinite self-improvement. No novelty claimed for the established mechanisms it builds on; see [PRIOR_ART.md](../PRIOR_ART.md).

## Suggested language

Accurate: "lifelong AI research", "persistent artificial mind", "model-independent cognitive architecture (in development)", "verified self-improvement research", "continual capability growth", "replaceable neural cortex".

Inaccurate for this project: "sentient AI", "self-aware AI", "superintelligence", "AGI achieved", "recursively self-improving without limit".
