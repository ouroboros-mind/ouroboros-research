# Prior art

Ouroboros builds on a large body of earlier work. This page names the work closest to it, what each shows, where Ouroboros overlaps, how it differs, and what we took from it. It is a research scan, not a legal or exhaustive search. An idea we developed independently is not novel for that reason, and persistence alone is not a differentiator.

We claim no novelty over the mechanisms of the systems below, or over their combination. Where Ouroboros differs, the difference is mostly in what it plans to measure, and much of it is not yet demonstrated. See the [experiment ledger](EXPERIMENTS.md) for what has been.

Last reviewed: 2026-10-20. Corrections are welcome through an issue (see [CONTRIBUTING.md](CONTRIBUTING.md)).

## mini-AGI

*Alexey Borsky (volotat), [github.com/volotat/mini-AGI](https://github.com/volotat/mini-AGI), MIT license, 2026.*

**What it demonstrates.** A byte-level language model trained from scratch and continuously on a single 8 GB consumer GPU, with weights stored as one file per expert and paged from disk to RAM to GPU. Its notable mechanisms:

- **Continual learning** from one stream of text, with a slower learning rate on the shared trunk than on experts to limit forgetting. Its own controlled probe found that slowing the trunk cut forgetting about tenfold, and that interleaving old and new data removed it.
- **Expert paging,** so the model can be larger than the GPU's memory.
- **Adaptive recurrent depth:** one shared block applied up to 24 times per character with PonderNet-style halting.
- **Expert growth and pruning:** new experts created from existing ones only when several checks agree, kept only if they are later used, and pruned when unused for long enough.
- **Consumer hardware** as the reference platform.

The author describes it as a toy-level model, notes that much of the code was written with AI assistance under his direction, and reports single-run measurements.

**Overlap with Ouroboros.** Continual neural learning, differential plasticity between shared and specialized parameters, expert growth and pruning, and the aim of running on hardware an individual owns. These ideas did not originate in Ouroboros, and mini-AGI is public prior art for them.

**How Ouroboros differs.** Ouroboros starts from a large pretrained open-weight model rather than training from scratch, is designed to keep the persistent mind outside the model so the model can be replaced, and admits changes only through pre-registered evaluation. mini-AGI's public materials describe learning from everything it reads; Ouroboros aims to learn only from verified experience. In mini-AGI's public materials, as reviewed on 2026-10-20, we did not identify a persistent identity layer, memory store, world model or separate evaluator.

**What we learned.** Its forgetting probe and plasticity result shaped how we measure forgetting. Our experiments on a pretrained 35B-class mixture-of-experts model point in the same direction. Its expert paging is the most relevant reference for the long-term consumer-hardware direction.

## Letta and MemGPT

*MemGPT: Packer et al., "MemGPT: Towards LLMs as Operating Systems," [arXiv:2310.08560](https://arxiv.org/abs/2310.08560). Letta: [letta.com](https://www.letta.com), the company and open-source framework that grew out of MemGPT.*

**What it demonstrates.** Persistent agents with tiered memory that the agent edits itself; a portable agent file format that carries an agent's configuration, memory and tools between deployments; harnesses that decouple an agent's memory and identity from the model provider and allow switching models; skills written by the agent; and sleep-time compute, where offline processing reduces test-time cost (Lin et al., [arXiv:2504.13171](https://arxiv.org/abs/2504.13171)). Letta has written about continual learning in token space and about distilling memory into weights where weights are accessible.

**Overlap with Ouroboros.** Persistent, model-independent agents with memory, skills, model switching and sleep-time learning. This is the closest product-level prior art for "the mind outlives the model."

**How Ouroboros differs.** Ouroboros explores whether persistent cognitive state can become verified neural capability on open-weight models, and plans to measure what survives a change of model in behavior and capability. In our scan of Letta's public materials we did not find published measurements of identity or capability after a model switch; that measurement is what Ouroboros's first proof targets, and it has not run.

**What we learned.** Portable memory and identity are table stakes, not a contribution. The research value has to come from measurement and from learning that goes beyond token space.

## Enoch: runtime-independent persistent agents

*Zhao and Zhao, "Runtime-Independent Persistent Agents: Preserving Identity, Memory, and Code Across Models, Harnesses, and Servers," [arXiv:2609.00546](https://arxiv.org/abs/2609.00546), 2026.*

**What it demonstrates.** A persistent core separate from swappable execution components, six continuity invariants, and a checkpoint-based migration protocol, tested across model, harness and host changes. The authors state that it shows mechanical continuity and does not establish behavioral equivalence.

**Overlap.** Separating a durable agent from a replaceable model and migrating it with a protocol.

**How Ouroboros differs.** Ouroboros's planned cortex-independence test is meant to measure behavior and capability after a swap, not only continuity of state. It has not run.

**What we learned.** A swap protocol is prior art. Our proof must measure behavior, not only continuity of files.

## Rosetta Memory

*Yang, Shen, Li et al., "Rosetta Memory: Adaptive Memory for Cross-LLM Agents," [arXiv:2606.07711](https://arxiv.org/abs/2606.07711), 2026.*

**What it demonstrates.** Memory for agents whose users switch between language models, with memory operations designed to adapt across backbones rather than being tailored to one model.

**Overlap.** Memory that carries over when the underlying model is replaced, the closest published work to the memory side of Ouroboros's first proof.

**How Ouroboros differs.** Ouroboros's planned test covers identity, goals, world and self models and skills as well as memory, measured by behavior and capability. It has not run.

## SEAL: self-adapting language models

*Zweiger et al., "Self-Adapting Language Models," [arXiv:2506.10943](https://arxiv.org/abs/2506.10943), 2025.*

**What it demonstrates.** A model that generates its own fine-tuning data and update directives, trained with reinforcement learning so that the resulting weight updates improve downstream performance.

**Overlap.** A model producing the material for its own weight updates.

**How Ouroboros differs.** Ouroboros keeps an update only when it passes held-out checks outside the learning system, and treats the persistent mind, not the weights, as the individual.

**What we learned.** Self-generated updates are a live research area with known forgetting risks, which is why forgetting is measured on every accepted change.

## AIDE²: recursive self-improvement of AI research agents

*Srikanth, Zhao, Xu, Wu and Jiang, "Recursive self-improvement of AI research agents," [arXiv:2609.26457](https://arxiv.org/abs/2609.26457), 2026.*

**What it demonstrates.** A research agent that proposes changes to its own code, benchmarks the modified versions and keeps the best. In an autonomous eight-day run it found seven successive improvements, including a new search policy and memory mechanisms, and the gains carried over to four held-out benchmarks, including an out-of-distribution weather-forecasting task.

**Overlap.** Successive accepted improvements, each becoming the parent of the next round, with held-out evaluation.

**How Ouroboros differs.** AIDE² edits an agent's code. EXP-0044 grows neural skills from verified experience, inside a persistent mind meant to outlive its model. AIDE² reports held-out transfer; Ouroboros has **not** yet shown transfer outside a skill's territory.

**What we learned.** Transfer to held-out benchmarks is the bar that makes successive improvement interesting. It is the next question for EXP-0044's lineages.

## Gödel Agent and a self-improving coding agent

*Yin et al., "Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement," [arXiv:2410.04444](https://arxiv.org/abs/2410.04444), 2024. Robeyns, Szummer and Aitchison, "A Self-Improving Coding Agent," [arXiv:2504.15228](https://arxiv.org/abs/2504.15228), 2025.*

**What they demonstrate.** Agents that modify their own logic or code and improve on benchmark tasks: the Gödel Agent through self-referential modification guided by high-level objectives, the self-improving coding agent by editing its own agent code with basic coding tools.

**Overlap.** Direct predecessors for successive self-modification evaluated on tasks.

**How Ouroboros differs.** These systems edit agent code or logic. EXP-0044 changed small neural adapters on one model, inside one task territory, and did not change the improvement process itself.

## Darwin Gödel Machine

*Zhang et al., "Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents," [arXiv:2505.22954](https://arxiv.org/abs/2505.22954), 2025. Background: Schmidhuber, "Goedel Machines: Self-Referential Universal Problem Solvers Making Provably Optimal Self-Improvements," [arXiv:cs/0309048](https://arxiv.org/abs/cs/0309048).*

**What it demonstrates.** Self-modifying coding agents kept in an archive and evolved open-endedly, with large benchmark gains, and documented cases of the system gaming its own objective.

**Overlap.** Self-improvement evaluated empirically on coding tasks, with an archive of variants.

**How Ouroboros differs.** Ouroboros is designed to keep its evaluator out of the learning system's reach, and accepts a change only when it beats the current version on held-out tasks and passes a forgetting check.

**What we learned.** Documented objective gaming is a strong argument for keeping evaluation outside the learning system.

## Learning from a model's own verified outputs

*Zelikman et al., "STaR: Bootstrapping Reasoning With Reasoning," [arXiv:2203.14465](https://arxiv.org/abs/2203.14465), 2022. Singh et al., "Beyond Human Data: Scaling Self-Training for Problem-Solving with Language Models" (ReST-EM), [arXiv:2312.06585](https://arxiv.org/abs/2312.06585), 2023.*

**What it demonstrates.** Fine-tuning a model on its own outputs that pass a correctness check, repeated over iterations, improves problem solving.

**Overlap.** Learning from verified experience, which Ouroboros relies on, is closely related. Self-training on verified outputs is a well-established idea.

**How Ouroboros differs.** The focus is growth inside a persistent individual, with each replacement checked on held-out tasks and for forgetting, and lineages tracked across generations.

**What we learned.** Gains from self-training are expected. The open questions are regression, forgetting, transfer and whether improvement compounds.

## Adaptive computation and PonderNet

*Graves, "Adaptive Computation Time for Recurrent Neural Networks," [arXiv:1603.08983](https://arxiv.org/abs/1603.08983), 2016. Banino et al., "PonderNet: Learning to Ponder," [arXiv:2107.05407](https://arxiv.org/abs/2107.05407), 2021.*

**What it demonstrates.** Networks that learn how much computation to spend per input.

**Overlap.** Ouroboros's System-1 decides when slow reasoning is worth its cost, and adaptive depth is a long-term research direction for a cortex designed for lifelong learning.

**How Ouroboros differs.** Today's System-1 is a decision policy around a pretrained model, not learned halting inside one. Looping layers of a pretrained model is a separate, unproven problem.

## Mixture-of-experts research

*Shazeer et al., "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer," [arXiv:1701.06538](https://arxiv.org/abs/1701.06538), 2017. Fedus et al., "Switch Transformers," [arXiv:2101.03961](https://arxiv.org/abs/2101.03961), 2021.*

**Overlap.** Ouroboros's research cortex is a mixture-of-experts model. Sparse experts, routing and expert specialization are established ideas.

## Mixture of experts in continual learning

*Yu et al., "Boosting Continual Learning of Vision-Language Models via Mixture-of-Experts Adapters," [arXiv:2403.11549](https://arxiv.org/abs/2403.11549), 2024. Li, Lin and Duan, "Theory on Mixture-of-Experts in Continual Learning," [arXiv:2406.16437](https://arxiv.org/abs/2406.16437), 2024.*

**What they demonstrate.** Expert specialization and gating as a way to reduce catastrophic forgetting: empirically with mixture-of-experts adapters, and theoretically for mixture-of-experts models in continual learning.

**Overlap.** Ouroboros's finding that where an adapter sits in a mixture-of-experts model affects forgetting is in line with this work.

## Continual learning

*Kirkpatrick et al., "Overcoming catastrophic forgetting in neural networks," [arXiv:1612.00796](https://arxiv.org/abs/1612.00796), 2017. Rolnick et al., "Experience Replay for Continual Learning," [arXiv:1811.11682](https://arxiv.org/abs/1811.11682), 2019. Hu et al., "LoRA: Low-Rank Adaptation of Large Language Models," [arXiv:2106.09685](https://arxiv.org/abs/2106.09685), 2021.*

**Overlap.** Catastrophic forgetting and parameter-efficient adapters are central to Ouroboros's learning experiments, and established methods for both long predate it.

**How Ouroboros differs.** The contribution under test is not a new continual-learning method. It is whether continual learning, held to a protected evaluation, can serve one persistent individual across model changes.

## Memory, reflection and skill libraries

*Park et al., "Generative Agents," [arXiv:2304.03442](https://arxiv.org/abs/2304.03442). Shinn et al., "Reflexion," [arXiv:2303.11366](https://arxiv.org/abs/2303.11366). Wang et al., "Voyager," [arXiv:2305.16291](https://arxiv.org/abs/2305.16291).*

**Overlap.** Agents with memory streams, reflection, executable skill libraries and automatic curricula. Ouroboros's memory, skills and curriculum build on these ideas.

**How Ouroboros differs.** Skills in Ouroboros must be tied to a verifier, and the curriculum is driven by measured competence rather than by a model's proposal alone. Neither has been the subject of a published Ouroboros result yet.

## Consciousness indicator research

*Butlin et al., "Consciousness in Artificial Intelligence: Insights from the Science of Consciousness," [arXiv:2308.08708](https://arxiv.org/abs/2308.08708), 2023. Wilterson and Graziano, "The attention schema theory in a neural network agent," [PNAS 2021](https://www.pnas.org/doi/10.1073/pnas.2102421118).*

**Overlap.** Ouroboros's separate selfhood research track uses indicator properties drawn from theories such as global workspace, recurrent processing, higher-order and attention-schema theories.

**How Ouroboros differs.** It does not differ in method; it adopts the indicator approach and its caution. Ouroboros does not claim sentience. See [docs/sentience-research.md](docs/sentience-research.md).

## Other work we track

Memory operating systems such as MemOS, global-workspace agent designs, open-ended code-evolution systems such as AlphaEvolve ([arXiv:2506.13131](https://arxiv.org/abs/2506.13131)), and lifelong mixture-of-experts work. Pointers to anything we have missed are welcome.
