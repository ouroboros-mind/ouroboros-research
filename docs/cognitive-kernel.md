# The Cognitive Kernel

The Cognitive Kernel is the persistent mind: the part of Ouroboros that is meant to stay the same individual while the language model underneath it changes. This page explains, conceptually, what it holds and why. Implementation details are private.

## Why a kernel at all

A language model is good at reasoning over what is in front of it. It is not, by itself, an individual: it has no lasting history of its own, no record of what it has learned or got wrong, and nothing that survives being replaced. The kernel provides that continuity. The cortex reasons; the kernel remembers, keeps commitments, tracks what it can do and decides what to learn next; the evaluation plane decides what is true about its progress.

## What it holds

- **Identity and lineage.** Who this individual is, its values and commitments, and every generation it has passed through.
- **Memory,** in several kinds: autobiographical (what happened to it), semantic (what it knows about the world), procedural (how to do things) and relationship memory. Every memory carries evidence and a privacy class.
- **A world model.** An explicit, persistent model of entities, states and cause and effect, separate from the cortex's context. It is trusted only as far as its predictions come true.
- **A self-model.** What it knows about itself: its current cortex, its measured strengths and weaknesses, what it recently learned, and where its predictions about itself were wrong.
- **A competency map.** A measured map of what it can do on each cortex, with uncertainty and history.
- **A global workspace.** A bounded working frame that holds goals, the current task, relevant memories, world and self state and candidate actions. The cortex reasons over this frame rather than an ever-growing transcript.
- **System-1.** Fast, cheap decisions, such as whether a task deserves slow, deliberate reasoning. The first promoted generation of Ouroboros (GEN-0001) was a policy of this kind.
- **The Experience Bus.** The append-only record of what the individual experiences.

## What it does not do

The kernel does not grade itself. Evaluation and promotion live in the protected evaluation plane, which is designed to be outside the kernel's reach. The kernel proposes; the evaluation plane decides.

## Status

Cognitive Kernel v0 is built in the private codebase. It is a design under test, not a demonstrated individual, with a first world model, competency map, workspace, System-1 and self-model, and it passed an acceptance session on one cortex. That is an engineering milestone, not a research result. The first experiment that tests the kernel as a persistent individual across two model families is EXP-0045, which has not run.
