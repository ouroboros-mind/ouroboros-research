# Ouroboros in one page

*For journalists, analysts and anyone who wants the short version. Free to quote with attribution.*

## Summary

Ouroboros asks whether an AI can develop like an individual instead of being replaced like software. The project is designed to separate the persistent mind from the underlying language model, so that memories, skills, self-knowledge and eventually learned capabilities could survive upgrades to the AI's neural cortex. That separation has not yet been tested across models. Current experiments test whether successive generations can produce verified capability improvements without losing previous strengths.

In its most recent experiment, EXP-0044, three seeded skill lineages on one model each went through two rounds of gated training, where a new version was kept only if it beat the current one on held-out tasks and passed a forgetting check. All three finished higher on a 600-task held-out test, by 8.2, 6.8 and 6.5 percentage points, with no regression on the whole task territory beyond base noise and measured forgetting below 0.01. Two difficulty levels dipped inside those gains. The experiment did not identify which part of the process caused the gain, and it did not measure transfer to other kinds of tasks. Whether the gains transfer, and whether improved generations become better at improving, are the next questions.

## Key facts

| | |
|---|---|
| What it is | A research program on lifelong, model-independent AI |
| Central idea | The mind is durable. The cortex is replaceable |
| Demonstrated so far | Narrow skill gains over two gated rounds, on one model, in one task territory |
| Not yet demonstrated | Model independence; lifelong operation; transfer; recursive improvement |
| Evidence standard | Every experiment pre-registered in a private, author-maintained ledger; negative results published |
| Experiments to date | 44, all listed with their outcomes |
| Next result | EXP-0045: one mind on two different model families (being built, has not run) |
| Hardware | A GX10-class (NVIDIA GB10) research workstation; gaming-class GPUs are a long-term direction |
| Code and data | Private. This public repository holds the research record |

## What Ouroboros does not claim

Not AGI. Not sentient. Not unrestricted or indefinite self-improvement. Not the first system to use the mechanisms it builds on; see [PRIOR_ART.md](../PRIOR_ART.md).

## Suggested language

Accurate: "lifelong AI research", "persistent artificial mind", "model-independent cognitive architecture (in development)", "verified self-improvement research", "continual capability growth", "replaceable neural cortex".

Inaccurate for this project: "sentient AI", "self-aware AI", "superintelligence", "AGI achieved", "recursively self-improving without limit".
