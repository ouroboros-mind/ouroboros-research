# Roadmap

The public roadmap is organized around research questions, not features. Each stage has a status taken from the [experiment ledger](EXPERIMENTS.md). Nothing is marked done because it is planned.

**Status words:** *Supported* (a pre-registered experiment passed), *Partial* (some of it passed), *In progress* (being built or run), *Not started*, *Hypothesis*, *Moonshot*.

## Stage A: A persistent mind

*Can one individual keep its memory and identity over time and across changes?*

- **Partial.** A long-horizon memory gate passed on synthetic text: the model wrote its own memory from twelve days of documents, kept corrections, and gave identical answers after its memory moved to a clean store ([EXP-0031](EXPERIMENTS.md#exp-0031) to [EXP-0033](EXPERIMENTS.md#exp-0033)).
- **Built and first tested (EXP-0045):** Cognitive Kernel v0, the Experience Bus and a portable genome format.
- **Not yet shown:** the same on real-world text, on long histories, or for learned capability across model families (Stage E). EXP-0045 was only a first small cross-family continuity test.

## Stage B: Lifelong learning

*Can the system learn new skills from its own verified experience without forgetting old ones?*

- **Supported:** small adapters can learn without forgetting beyond noise on the measured probes ([EXP-0009](EXPERIMENTS.md#exp-0009), [EXP-0014](EXPERIMENTS.md#exp-0014)).
- **Partial:** skills learned from verified experience hold in their own domain, but transfer to new task families failed ([EXP-0034](EXPERIMENTS.md#exp-0034) to [EXP-0041](EXPERIMENTS.md#exp-0041)).
- **Not supported, parked:** nightly consolidation of facts into weights was unreliable across seeds ([EXP-0027](EXPERIMENTS.md#exp-0027)). Retrieval is the memory path for now.

## Stage C: Gated growth

*Can a skill keep improving across generations when every change must beat the current version?*

- **Supported on one model, inside one trained territory:** three seeded lineages, two accepted generations each, +8.2, +6.8 and +6.5 points on 600 held-out tasks ([EXP-0044](results/EXP-0044.md)). The cause of the gain within the pipeline was not isolated. EXP-0043, a single ungated round, had a negative pre-registered decision.
- **Next: transfer.** Do improved roots beat their ancestors outside their own territories? This is the next valuable public milestone.

## Stage D: Breeding

*Do improved generations become better at producing improved generations?*

- **Hypothesis, not yet measured.** Results will be shown as offspring success rates per generation when they exist.

## Stage E: Cortex migration

*Does the mind survive a change of language model?*

- **First form supported.** EXP-0045 ran one mind on two models from different families; it kept its identity, memory, procedures and calibration. No weights moved, and the held-out tasks were too easy to measure skill effects.
- **Later:** a mature mind migrates to a new model.

## Stage F: Intelligence density

*How much of a mature mind's capability can be made cheap enough to run on hardware an individual owns?*

- **Not started.** A long-term research direction with no fixed memory target. Today's runtime is a GX10-class research workstation. See [docs/consumer-hardware.md](docs/consumer-hardware.md).

## Stage G: Recursive improvement

*Can the learning process itself improve, so that each generation learns better than the last?*

- **Not started.** EXP-0044 is not evidence of this: the improvement process stayed fixed. This stage requires the improvement process to change and the protected evaluation plane to show that the change helped.

## Moonshot

*Can this process eventually produce a mature personal intelligence, runnable on hardware an individual owns, with frontier-like effective capability, that keeps becoming more capable throughout its lifetime?*

- **Moonshot.** An aspiration that sets direction. It is not a claim and it has no date.

## Near-term sequence

1. EXP-0045: one mind, two model families (done: first form supported).
2. A neural skill learned through the Mind ABI on an open-weight model.
3. Transfer and breeding experiments for grown roots.
4. Migration of a mature mind to a new cortex.

## Planned demonstrations

Short, evidence-first demos, each released only after the underlying experiment is recorded. None reveal private mechanics.

| Demo | Shows | Status |
|---|---|---|
| An AI lineage that improved twice | EXP-0044's three lineages, start to final | Ready to prepare from recorded results |
| Same mind, different cortex | One mind answering about its own history, goals and skills on two model families | After EXP-0045 |
| Fresh versus mature | A mature instance against its frozen seed on new tasks | Later |
| A mind on consumer hardware | Running a mature mind on gaming-class hardware | Long-term |

## Metrics we report

Lineages, accepted generations, held-out task counts, capability change with significance, regression rate, forgetting, generation acceptance rate, and, as the experiments arrive, transfer score, cross-cortex retention, improvement-of-improvement rate and hardware footprint. We do not report stars, downloads or other vanity numbers as progress.
