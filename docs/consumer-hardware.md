# Consumer hardware

## Today

All Ouroboros experiments run on a GX10-class (NVIDIA GB10) desk-side research workstation. It is the laboratory and the primary runtime. Its large unified memory lets a 35B-class open-weight mixture-of-experts model be served, measured and fitted with small adapters on one machine.

## The objective: intelligence density

A persistent mind is most valuable if its owner can run it on hardware they control. The objective is to raise **intelligence density**, the capability a mind delivers per unit of compute, memory and energy, so that increasingly capable mature minds can run on practical hardware that individuals can own.

No hardware ceiling is chosen in advance. A fixed memory target set now would be a guess. Instead, from EXP-0046 on, each generation records what it actually used, and the experiments will show where the practical envelope lies.

## Stored mind and active working set

These are different quantities and are tracked separately.

- **The stored mind** is everything the individual owns: its experience record, memories, procedures and skills, world model and self-model, and learned caches for each cortex it has used. It can grow large over a lifetime, and it lives on ordinary storage.
- **The active working set** is what must be in fast memory at a given moment: the cortex in use, the caches loaded for the current task, the bounded workspace frame and the model's working state. The kernel brings in only what a task needs.

A large stored mind does not imply a large active working set. In EXP-0045, for example, the workspace frames for each 16-task session totalled about 17,000 to 24,000 tokens, where carrying the full transcript would have taken 177,000 to 200,000.

## What each generation records

| Measure | Examples |
|---|---|
| Compute | wall-clock time, accelerator time per task |
| Accelerator memory | peak VRAM or unified memory while serving and while learning |
| System memory | peak RAM |
| Storage | size of the stored mind, of each cache, of the experience record |
| Latency | time to first token and per task |
| Efficiency | capability per unit of active memory, per token and per unit of compute |

Pre-registrations already set resource budgets. Recording all of these measures for every generation starts with EXP-0046; earlier experiments recorded some of them.

## Status

- No compression or distillation work has started. Nothing here claims progress toward consumer deployment.
- **Prior art.** mini-AGI shows continual learning with expert paging on an 8 GB laptop GPU for a small model trained from scratch ([PRIOR_ART.md](../PRIOR_ART.md#mini-agi)). Mixture-of-experts sparsity and expert paging are the most relevant existing techniques.

## Questions this direction would answer

1. Which of a mature mind's capabilities can be distilled into a smaller cortex without losing what the mind has learned?
2. Does the persistent mind make a smaller cortex more useful than the same cortex alone?
3. How does the active working set grow as the stored mind grows?
4. What is the right measure of intelligence density for a mind that keeps learning?

Status on the [research ladder](../README.md#research-ladder): long-term research direction.
