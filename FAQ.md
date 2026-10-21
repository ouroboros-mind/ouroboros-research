# FAQ

### What is Ouroboros?

A research program asking whether one persistent AI can grow throughout its lifetime, become measurably more capable from verified experience, and keep the same evolving mind when its underlying language model is upgraded or replaced. Short version: can an AI grow up instead of being replaced?

### Is it an LLM?

No. Ouroboros uses language models as a replaceable **cortex**. The persistent part, the Cognitive Kernel, holds identity, memory, skills, a world model, a self-model and a measured map of competencies, and is designed to talk to whichever model it uses through one contract, the Mind ABI. A first small cross-family continuity test (EXP-0045) is supported, but general model independence and the transfer of learned capability remain unproven. See [ARCHITECTURE.md](ARCHITECTURE.md).

### Why not just memory or RAG?

Memory is part of it, and retrieval is the main memory path in our experiments today. But stored memory alone does not make a system more capable. Ouroboros studies whether verified experience can become procedures, skills and, on open-weight models, neural capability, and whether that development could survive a model change. See [docs/learning-stack.md](docs/learning-stack.md).

### Does it work with any LLM?

That is the design goal, and it has not been demonstrated. So far every learning experiment ran on one open-weight Qwen-family model. A first small test on a second model family (EXP-0045) kept the mind's identity, memory, procedures and calibration across the swap; it trained nothing, so carrying learned capability is still undemonstrated.

### Is it self-improving?

Only in a narrow, measured sense. In EXP-0044, three seeded skill lineages on one model each went through two rounds of gated training, and all three finished above their starting point on a held-out test inside their task territory. The experiment did not isolate what caused the gain, the improvement process itself did not change, and gains outside the territory were not measured.

### Has recursive self-improvement been proven?

No. EXP-0044 shows score gains over two gated generations inside one territory, on one model. Recursive improvement would require the learning process to get better at improving, measured independently. That is Stage G of the [roadmap](ROADMAP.md) and has not started.

### Is it AGI?

No. Ouroboros is a research program with a moonshot of eventually reaching frontier-like effective capability on hardware an individual owns. Nothing here claims that has happened or is close.

### Is it sentient?

No, and we do not claim it is. A separate research track studies measurable computational properties associated with theories of consciousness, under strict evidence rules. Their presence would not by itself establish phenomenal consciousness. See [docs/sentience-research.md](docs/sentience-research.md).

### Why use a GX10?

A GX10-class (NVIDIA GB10) research workstation has enough unified memory to serve a 35B-class open-weight model, measure it and train small adapters on it on one desk-side machine. That makes fast, controlled, local experiments possible.

### Will it run on normal gaming hardware?

Not today. Running a mature mind on gaming-class GPUs is a long-term research direction. No fixed memory target is set and no compression work has started. See [docs/consumer-hardware.md](docs/consumer-hardware.md).

### How is it different from Letta?

Letta (which grew out of MemGPT) already provides persistent, model-switchable agents with memory, skills and sleep-time compute. Ouroboros overlaps with that and does not claim novelty over it. Its research focus is whether persistent cognitive state can become verified neural capability on open-weight models, and measuring behavior and capability after a model change. Neither has been demonstrated yet. See [PRIOR_ART.md](PRIOR_ART.md#letta-and-memgpt).

### How is it different from mini-AGI?

mini-AGI is a small model trained from scratch on a consumer GPU that learns continually, pages experts from disk, adapts its depth and grows and prunes experts. Those ideas are mini-AGI's and earlier work's, not Ouroboros's. Ouroboros starts from large pretrained models and is designed to keep the mind outside the model so the model can be replaced. See [PRIOR_ART.md](PRIOR_ART.md#mini-agi).

### Will it be open source?

The core implementation is private and there are no current plans to release it. This repository publishes the research program, results, methods at a conceptual level and prior art. If individual components are released in the future, they will be announced here with their own license.

### Can I reproduce the experiments?

No. Code, task sets, datasets, training procedures, weights and the ledger are private, so experiments cannot be reproduced or audited from this repository, and pre-registration timing cannot be verified. The general claims can still be tested independently on your own tasks and models. Replication reports, positive or negative, are welcome; see [CONTRIBUTING.md](CONTRIBUTING.md).

### How can researchers get involved?

Open a discussion or an issue with a research question, a replication report, a benchmark suggestion or a prior-art reference.
