# Architecture

> **The mind should survive replacement of the cortex.**

This page describes the intended Ouroboros architecture at a conceptual level: what the parts are for and how they relate. It is a design, not a claim of general model independence; EXP-0045 was a first small cross-family continuity test. Algorithms, data formats, selection rules and training methods are private and not described here.

<p align="center">
  <img src="assets/architecture.svg" alt="Conceptual architecture diagram" width="100%">
</p>

## The persistent mind

The persistent mind is the individual. It is everything that should stay the same when the language model underneath it changes. In Ouroboros it is held by the **Cognitive Kernel**, and it is designed to be exportable as a portable, versioned bundle (the "genome").

| Part | Role |
|---|---|
| **Identity and lineage** | Who this individual is, where it came from, and every generation it has passed through. Two instances installed from the same seed become separate individuals with a common ancestor |
| **Autobiographical memory** | What happened to this individual, in order, with evidence |
| **Semantic memory** | What it knows about the world, with sources and corrections |
| **Procedures and skills** | What it knows how to do, each skill tied to a way of checking it |
| **World model** | An explicit model of entities, states and cause and effect that is trusted only as far as its predictions come true |
| **Self-model** | What it knows about itself: its current cortex, its measured strengths and weaknesses, what it recently learned, and where it was wrong about itself |
| **Competency map** | A measured map of what it can do, per cortex, which also guides what it should learn next |
| **Global workspace** | A bounded working frame that the cortex reasons over, instead of an ever-growing transcript |
| **System-1** | Fast, cheap decisions, such as whether a task needs slow, deliberate reasoning |
| **Experience Bus** | An append-only record of what the individual experiences: conversations, tool results, test results, corrections and model swaps |

Detail: [docs/cognitive-kernel.md](docs/cognitive-kernel.md) and [docs/persistent-identity.md](docs/persistent-identity.md).

## The Mind ABI

The Mind ABI is one contract between the mind and any language model. The kernel is designed to talk to models only through it, with model-specific code behind it, so that replacing the model would not mean rewriting the mind.

What the mind can change depends on how open the model is. With a closed, hosted model it can only change its own memory, skills and orchestration. With an open-weight model it can also grow neural adapters. With a model designed for lifelong learning, much more would be possible. Detail: [docs/mind-abi.md](docs/mind-abi.md).

## The cortex

The cortex is the language model that performs high-level neural reasoning. It is a replaceable component.

| Cortex | Status |
|---|---|
| Qwen family (open-weight, 35B-class mixture of experts) | Today's research cortex. All learning experiments so far ran on it |
| GLM family | Second cortex (GLM-4.7-Flash) in the first model-independence test, EXP-0045 |
| Future open models | Expected as they appear; each change is meant to follow a migration protocol with rollback |
| Ouroboros-native cortex | Research direction only. It would be considered only after the proofs show which properties matter |

Anything learned only inside one model's weights, such as an adapter, is tied to that model.

## The Experience Bus

The Experience Bus is designed as the mind's raw history: an append-only log of events with their source, time and outcome. Memory and skills are derived from it.

## The learning plane

The learning plane turns experience into cheaper, faster forms of intelligence: memory, then procedures, then skills, and on open-weight cortices small neural specializations. Each step down that ladder is a promotion that must pass the evaluation plane. Detail, conceptual only: [docs/learning-stack.md](docs/learning-stack.md).

## The protected evaluation plane

The evaluation plane sits outside the mind. Evaluation material, promotion rules and rollback are designed to be out of the learning system's reach. The mind proposes; the evaluation plane decides what survives. This is a design property of a private system that has not been independently audited. Detail: [docs/evaluation-philosophy.md](docs/evaluation-philosophy.md).

## What is built

| Component | State (2026-10-21) |
|---|---|
| Experiment ledger with pre-registration | Built and in use since the first experiment |
| Protected evaluation plane | Built and in use |
| Mind ABI with a conformance suite | Built |
| Experience Bus v1 and genome bundle v2 (identity, lineage, memory, skills) | Built |
| Cognitive Kernel v0 (world model v0, competency map v0, workspace, System-1, self-model v1) | Built; one acceptance session on one cortex passed |
| Running one mind on two model families | First form supported (EXP-0045) |
| Neural skill compilation through the ABI | First form supported (EXP-0046) |
| Migration of a mature mind to a new cortex | Partial (EXP-0048): skill regrowth on the new model passed, but the working frame had a cost |
| Ouroboros-native cortex | Research direction only |

"Built" means implemented and tested in the private codebase. It does not mean the capability has been shown in a pre-registered experiment. The [experiment ledger](EXPERIMENTS.md) is where capability claims live.
