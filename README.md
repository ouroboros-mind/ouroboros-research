<p align="center">
  <img src="assets/mark.svg" width="88" alt="Ouroboros mark: an open ring whose leading end approaches its tail">
</p>

<h1 align="center">OUROBOROS</h1>

<p align="center"><strong>Research toward a lifelong, model-independent artificial mind</strong></p>
<p align="center"><em>The mind is durable. The cortex is replaceable.</em></p>

<p align="center">
  Research Preview 0.1 ·
  <a href="results/EXP-0044.md">Latest result</a> ·
  <a href="EXPERIMENTS.md">Experiment ledger</a> ·
  <a href="ROADMAP.md">Roadmap</a> ·
  <a href="ARCHITECTURE.md">Architecture</a> ·
  <a href="PRIOR_ART.md">Prior art</a> ·
  <a href="FAQ.md">FAQ</a>
</p>

Ouroboros is a research project exploring whether one persistent artificial intelligence can grow throughout its lifetime, become measurably more capable from verified experience, and preserve the same evolving mind while its underlying AI models are upgraded or replaced. Can an AI grow up instead of being replaced?

> **Where the evidence stands.** Model independence and lifelong operation are the project's research goals. **Neither has been demonstrated yet.** What has been shown so far is narrow: skill gains over two gated training rounds, on one Qwen-family model, inside one family of programming tasks. The first test of one mind on two different models (EXP-0045) has not run.

<p align="center">
  <img src="assets/architecture.svg" alt="Conceptual architecture: a persistent Cognitive Kernel above a Mind ABI and replaceable model cortices, with a learning plane and a protected evaluation plane" width="100%">
</p>

## Current status

| | |
|---|---|
| **Latest result** | [EXP-0044](results/EXP-0044.md), gated multi-round growth: **supported** (its pre-registered decision rule passed for all three seeded lineages) |
| **Record so far** | 44 pre-registered experiments, every one listed in the [ledger](EXPERIMENTS.md) with its outcome, including the 15 that did not support their hypothesis |
| **Built, not yet tested by experiment** | Mind ABI, Experience Bus, a portable genome format and Cognitive Kernel v0 |
| **Next question** | EXP-0045 (in progress, has not run): can one persistent mind run on two different model families and keep its memories, identity and skills? |

### Known limits

- **One model family.** Every learning result so far used one Qwen-family model.
- **Narrow and short.** The growth result covers two rounds, inside one internally generated territory of programming tasks.
- **Transfer unmeasured.** Gains outside the trained territory were not measured, and an earlier transfer test was negative ([EXP-0041](EXPERIMENTS.md#exp-0041)).
- **Forgetting was measured, not zero.** It stayed below 0.01 on the forgetting probe for every accepted candidate. That does not rule out forgetting outside the probe.
- **Not publicly auditable.** The ledger, task sets, training procedure, code and raw results are private. See [what you can and cannot verify](#what-you-can-and-cannot-verify).

## Why this exists

Many AI assistants keep conversation state or external memory, and some systems already support persistent agents that can switch between models (see [PRIOR_ART.md](PRIOR_ART.md)). What usually does not carry over when the model changes is learned capability. Ouroboros asks whether verified behavioral capability, not only stored state, can grow over a lifetime and survive model replacement.

| Typical lifecycle | Ouroboros research lifecycle |
|---|---|
| Train a model | Install a persistent mind |
| Release it | Accumulate verified experience |
| Use it mostly as it shipped | Develop skills and measurable capabilities |
| Replace it when a better one appears | Upgrade the cortex, keep the identity and history, continue developing |

The right-hand column is the research goal, not a description of a working system.

## Core architecture

Four layers, kept deliberately separate. Detail: [ARCHITECTURE.md](ARCHITECTURE.md).

- **Persistent Cognitive Kernel.** The individual: identity, autobiographical and semantic memory, procedures and skills, a world model, a self-model, a map of measured competencies, a bounded workspace and a record of what it experiences. It is designed not to belong to any one model.
- **Mind ABI.** One contract between the mind and any language model, so the model can change without rewriting the mind.
- **Replaceable cortex.** The language model that does high-level neural reasoning. Today a Qwen-family open-weight model; next, a model from a different family.
- **Learning and growth plane.** Turns verified experience into cheaper, faster forms: memory, procedures, skills and, on open-weight models, small neural adapters. A protected evaluation plane outside the mind decides what is kept.

## Design hypotheses and evidence status

Most of these ideas exist in earlier work ([PRIOR_ART.md](PRIOR_ART.md)). Ouroboros does not claim the combination is novel. It tests whether the combination works when held to pre-registered measurement.

| Hypothesis | Status |
|---|---|
| A persistent individual with its own history and lineage | Partial: memory over a twelve-day synthetic run passed its gate; kernel built |
| A replaceable cortex: behavior and capability survive a model swap | Planned (EXP-0045 has not run) |
| Verified learning: changes are kept only when held-out checks say so | In use on one model (author-reported) |
| Capability compilation: recurring reasoning becomes cheaper skills | Partial: narrow skills learned; transfer not shown |
| Multi-timescale learning with different safeguards per speed | Partial: memory and adapter tiers exercised; slower tiers not started |
| Protected evaluation outside the learning system's reach | In use (author-reported; not externally audited) |
| Local deployment on hardware an individual owns | Long-term direction, not started |

## Latest result: EXP-0044

On one internally generated territory of programming tasks with automatic correctness checks, three seeded skill adapters ("roots") each went through two rounds of gated training. In each round a candidate replaced the current version only if it beat it on held-out tasks and passed a forgetting check. All three finished above where they started on a separate 600-task test. This did not test other task families or another model.

<table>
<tr><td>

**EXP-0044 · Gated multi-round growth · SUPPORTED**

*Can roots grow for two rounds, keeping a change only when it beats the current root?*

| | Lineage A | Lineage B | Lineage C |
|---|:---:|:---:|:---:|
| Accepted generations | 2 of 2 | 2 of 2 | 2 of 2 |
| Held-out territory tasks passed, start → final (of 600) | 486 → 535 | 521 → 562 | 489 → 528 |
| **Change** | **+8.2 pts** | **+6.8 pts** | **+6.5 pts** |
| One-sided exact McNemar p | 2.8e-6 | 1.9e-5 | 2.6e-6 |

**3 of 3** seeded lineages improved on the aggregate territory score · **2** successive accepted generations each · **600**-task final test · every **p < 1e-4** · no regression on the whole territory beyond base noise, though one difficulty level dipped in each of two lineages · forgetting measured **below 0.01** for every accepted candidate

**Next:** does it transfer outside the trained territory? Do better roots become better breeders?

</td></tr>
</table>

<p align="center">
  <img src="assets/exp-0044-lineages.svg" alt="EXP-0044: for each of three lineages, held-out passes rose from start to final root, with a gain at every accepted round" width="100%">
</p>

Three seeded lineages each completed two successive rounds of gated self-training. All three improved on the aggregate territory score, with no regression on the whole territory beyond base noise and with measured forgetting below 0.01; two difficulty levels dipped inside those gains. The next major questions are whether the gains transfer beyond the trained territories and whether improved generations become better at producing further improvements.

**What this shows**

- Under the EXP-0044 pipeline, a skill finished above its starting point after two successive accepted generations, in all three lineages.
- Each accepted generation served as the parent of the next round.
- No lineage repeated the aggregate regression seen in [EXP-0043](EXPERIMENTS.md#exp-0043), whose pre-registered decision was negative.

**What this does not show**

- **What caused the gain.** EXP-0044 had no matched ungated or old-data control, so it does not identify which part of the pipeline produced the improvement.
- **Transfer** outside the trained territory. Not measured here; an earlier test was negative.
- **Better breeders.** Two rounds do not show that later generations are better at producing improvements.
- **Duration.** Whether gains continue over many rounds is open.
- **Model independence.** All of this ran on one model, and the learned adapters are tied to its weights.
- **Recursive self-improvement** in any unrestricted sense. Ouroboros does not claim it.

Full write-up: [results/EXP-0044.md](results/EXP-0044.md).

## Research ladder

<p align="center">
  <img src="assets/research-ladder.svg" alt="Research ladder with statuses from the experiment ledger" width="100%">
</p>

| Rung | Status | Evidence |
|---|---|---|
| Persistent memory and identity | Partial | Twelve-day synthetic memory gate passed ([EXP-0033](EXPERIMENTS.md#exp-0033)); kernel v0 built. Not yet tested across models |
| Verified skill learning | Partial | Skills learned in their own domain; transfer to unseen task families failed ([EXP-0041](EXPERIMENTS.md#exp-0041)) |
| Multi-round gated growth | Supported on one model, inside one territory | [EXP-0044](results/EXP-0044.md) |
| Cross-territory transfer | Open question | Not established |
| Better breeders | Hypothesis | Not yet measured |
| Cross-cortex continuity | In progress | EXP-0045 is being built and has not run |
| Consumer-hardware mind | Long-term research direction | No work started; no fixed memory target |
| Recursive meta-improvement | Moonshot | Not started |
| Frontier-like local AI | Moonshot | Not started |

## Open research questions

1. Do grown skills transfer outside the territory they were trained on?
2. Are later generations better at producing successful successors than earlier ones?
3. Do memories, identity and capabilities survive a change of model, measured by behavior rather than by stored files?
4. How much of a mature mind's capability can be compressed onto hardware an individual can own?
5. Can a world model and a self-model stay accurate when the model underneath them is upgraded?

More: [RESEARCH_QUESTION.md](RESEARCH_QUESTION.md).

## What you can and cannot verify

The raw data, task sets, training procedure, code and the experiment ledger itself are private. Numbers on these pages are copied from that author-maintained ledger. Pre-registration timing, contamination checks and ledger integrity are author-reported and cannot be checked from this repository.

| You can | You cannot |
|---|---|
| Check internal consistency, for example that the EXP-0044 p-values recompute from the published gained and lost task counts | Reproduce any experiment from this repository |
| See every experiment, including negative and inconclusive ones | Inspect the task sets, the training procedure or raw results |
| Test the claims independently on your own tasks and models | Verify when an experiment was pre-registered |

Replication reports, positive or negative, are welcome: see [CONTRIBUTING.md](CONTRIBUTING.md).

## Hardware

Experiments run on a GX10-class (NVIDIA GB10) desk-side research workstation, which can serve and adapt a 35B-class open-weight model on one machine. Deployment on gaming-class GPUs is a long-term research direction with no fixed memory target. See [docs/consumer-hardware.md](docs/consumer-hardware.md).

## Research philosophy

**Ouroboros does not accept a change because the AI says it is better.** Experiments are pre-registered before they run. Hard, automatic checks come before model judges. A candidate replaces the current version only if it beats it on held-out tasks and passes a forgetting check. Regression and forgetting are measured against the evaluation's own noise. Negative results stay in the record. More: [docs/evaluation-philosophy.md](docs/evaluation-philosophy.md).

## Prior art

Ouroboros builds on earlier work and claims no novelty over it, including [mini-AGI](https://github.com/volotat/mini-AGI), Letta and MemGPT, Enoch, Rosetta Memory, SEAL, AIDE², the Gödel Agent, the Darwin Gödel Machine, a self-improving coding agent, STaR and ReST-EM, PonderNet and adaptive computation, mixture-of-experts and continual-learning research, and indicator-based research on consciousness in AI. What each shows and how Ouroboros differs: [PRIOR_ART.md](PRIOR_ART.md).

## Follow the research

- **Discussions** (planned categories: Announcements, Experiment Discussion, Research and Papers, Architecture, Q&A) for questions, critiques and paper pointers.
- **Issues** for research questions, replication reports, prior-art references and documentation fixes. See [CONTRIBUTING.md](CONTRIBUTING.md).

The core implementation is private and does not accept outside code contributions. Research collaboration, independent replication, and strategic inquiries are welcome.

---

<sub>Ouroboros Research Preview 0.1, by Christopher Ayers. See [NOTICE.md](NOTICE.md) for what is and is not covered. Cite with [CITATION.cff](CITATION.cff).</sub>
