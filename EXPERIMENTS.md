# Public experiment ledger

This is the public summary of the Ouroboros experiment ledger. The private ledger is append-only and hash-chained, and every experiment is pre-registered before it runs. Rejected, null and aborted runs stay in the record. Negative results are evidence.

The ledger itself, the task sets, the training procedure and raw results are private. Pre-registration timing and ledger integrity are author-reported and cannot be verified from this repository. See [what you can and cannot verify](README.md#what-you-can-and-cannot-verify).

This page lists **every** experiment, in order, including the failures. Where a protocol touches material under IP review, the entry gives a safe summary and says so. Dates are pre-registration dates (UTC).

## Outcome labels

Labels follow each experiment's pre-registered decision rule, not how useful the result turned out to be.

| Label | Meaning |
|---|---|
| **SUPPORTED** | The pre-registered decision rule passed |
| **PARTIAL** | Mixed: some pre-registered hypotheses or gates passed and others failed |
| **NOT SUPPORTED** | The pre-registered decision was negative. Kept in full |
| **INCONCLUSIVE** | A pre-registered validity check failed, so the decision was void |
| **INFRASTRUCTURE** | Measurement, tooling or calibration work. Not a capability claim |
| **PENDING** | Built or being built, has not run |

## Totals (EXP-0001 to EXP-0044)

| SUPPORTED | PARTIAL | NOT SUPPORTED | INCONCLUSIVE | INFRASTRUCTURE | Total |
|---:|---:|---:|---:|---:|---:|
| 12 | 7 | 15 | 1 | 9 | 44 |

Experiments vary widely in scope, and seeds within an experiment are not independent replications, so these counts are not a success rate.

## Index

| ID | Date | Title | Outcome |
|---|---|---|---|
| [BASE-0001](#base-0001) | 2026-10-03 | Project baseline recorded | Milestone |
| [EXP-0001](#exp-0001) | 2026-10-03 | First launch of the seed model | INFRASTRUCTURE |
| [EXP-0002](#exp-0002) | 2026-10-03 | Second launch attempt | INFRASTRUCTURE |
| [EXP-0003](#exp-0003) | 2026-10-03 | The seed model serves | INFRASTRUCTURE |
| [EXP-0004](#exp-0004) | 2026-10-03 | Full-speed characterization | INFRASTRUCTURE |
| [EXP-0005](#exp-0005) | 2026-10-04 | The canary benchmark | INFRASTRUCTURE |
| [EXP-0006](#exp-0006) | 2026-10-04 | Calibration before freezing the contract | INFRASTRUCTURE |
| [SEED-0](#seed-0) | 2026-10-04 | Generation 0 frozen | Milestone |
| [EXP-0007](#exp-0007) | 2026-10-04 | First training attempt | INFRASTRUCTURE |
| [EXP-0008](#exp-0008) | 2026-10-04 | Training works | SUPPORTED |
| [EXP-0009](#exp-0009) | 2026-10-04 | An adapter that does not forget | SUPPORTED |
| [EXP-0010](#exp-0010) | 2026-10-05 | Independent cross-check | SUPPORTED |
| [EXP-0011](#exp-0011) | 2026-10-05 | Canary check of the adapters | PARTIAL |
| [EXP-0012](#exp-0012) | 2026-10-05 | Second seed | PARTIAL |
| [EXP-0013](#exp-0013) | 2026-10-05 | Longer training | PARTIAL |
| [EXP-0014](#exp-0014) | 2026-10-05 | Replay protects memory | SUPPORTED |
| [EXP-0015](#exp-0015) | 2026-10-05 | First generation-1 candidate | NOT SUPPORTED |
| [EXP-0016](#exp-0016) | 2026-10-05 | Generation 1 promoted | SUPPORTED |
| [GEN-0001](#gen-0001) | 2026-10-06 | Generation 1 in the ledger | Milestone |
| [EXP-0017](#exp-0017) | 2026-10-06 | Can trained facts be recalled? | NOT SUPPORTED |
| [EXP-0018](#exp-0018) | 2026-10-07 | Question-style training | NOT SUPPORTED |
| [EXP-0019](#exp-0019) | 2026-10-07 | Were the facts stored at all? | NOT SUPPORTED |
| [EXP-0020](#exp-0020) | 2026-10-07 | Capacity found | SUPPORTED |
| [EXP-0021](#exp-0021) | 2026-10-07 | Learning to say UNKNOWN | SUPPORTED |
| [EXP-0022](#exp-0022) | 2026-10-07 | Scaling up the facts | SUPPORTED |
| [EXP-0023](#exp-0023) | 2026-10-08 | First sleep cycle | INCONCLUSIVE |
| [EXP-0024](#exp-0024) | 2026-10-08 | Why did the canary drop? | INFRASTRUCTURE |
| [EXP-0025](#exp-0025) | 2026-10-08 | Sleep cycle, safer mix | NOT SUPPORTED |
| [EXP-0026](#exp-0026) | 2026-10-08 | Is the collapse stable? | PARTIAL |
| [EXP-0027](#exp-0027) | 2026-10-09 | Three seeds of sleep | NOT SUPPORTED |
| [EXP-0028](#exp-0028) | 2026-10-09 | The retrieval gap | INFRASTRUCTURE |
| [EXP-0029](#exp-0029) | 2026-10-09 | Linked retrieval | SUPPORTED |
| [EXP-0030](#exp-0030) | 2026-10-10 | Entity-based retrieval on a fresh world | SUPPORTED |
| [EXP-0031](#exp-0031) | 2026-10-10 | The model writes its own memory | NOT SUPPORTED |
| [EXP-0032](#exp-0032) | 2026-10-10 | Sleep rewrites the notes | PARTIAL |
| [EXP-0033](#exp-0033) | 2026-10-10 | Long-horizon memory gate passed | PARTIAL |
| [EXP-0034](#exp-0034) | 2026-10-11 | First skill: the memory writer | PARTIAL |
| [EXP-0035](#exp-0035) | 2026-10-11 | Two training domains | NOT SUPPORTED |
| [EXP-0036](#exp-0036) | 2026-10-11 | A gate to catch bad seeds | NOT SUPPORTED |
| [EXP-0037](#exp-0037) | 2026-10-12 | A stricter gate | NOT SUPPORTED |
| [EXP-0038](#exp-0038) | 2026-10-12 | A no-slack gate | SUPPORTED |
| [EXP-0039](#exp-0039) | 2026-10-13 | The writer on real notes | NOT SUPPORTED |
| [EXP-0040](#exp-0040) | 2026-10-16 | Training on real-note extractions | NOT SUPPORTED |
| [EXP-0041](#exp-0041) | 2026-10-17 | A skill with a hard verifier | NOT SUPPORTED |
| [EXP-0042](#exp-0042) | 2026-10-18 | Routed roots | NOT SUPPORTED |
| [EXP-0043](#exp-0043) | 2026-10-19 | One growth round | NOT SUPPORTED |
| [EXP-0044](#exp-0044) | 2026-10-20 | Gated multi-round growth | SUPPORTED |
| [EXP-0045](#exp-0045) | not yet registered | One mind, two model families | PENDING |

---

## Era 1: Getting the seed running

Goal: prove that a 35B-class open-weight model can run, be measured and be restored cleanly on one research workstation.

### BASE-0001
2026-10-03 · Milestone
- **Question.** What exactly are we starting from?
- **Result.** The baseline went into the tamper-evident ledger: hardware, model, licenses and rules of evidence.
- **What changed.** Every later claim is checked against this frozen starting point.
- **Next question.** Can the seed model start at all?

### EXP-0001
2026-10-03 · INFRASTRUCTURE
- **Question.** Can the seed model start on the workstation alongside its other workloads?
- **Result.** The memory watchdog stopped the launch 35 seconds before it could serve. The machine was restored cleanly.
- **What changed.** Research runs need a cleared machine. The safety tooling worked on day one.
- **Next question.** Does lowering memory use fix the launch?

### EXP-0002
2026-10-03 · INFRASTRUCTURE
- **Question.** Does lowering memory use fix the launch?
- **Result.** No. The server miscounted available memory, and a community container image crashed.
- **What changed.** Fixed memory settings and the right image matter more than tuning.
- **Next question.** With a fixed memory budget, does it serve?

### EXP-0003
2026-10-03 · INFRASTRUCTURE
- **Question.** With a fixed memory budget, does the seed serve?
- **Result.** Yes: about 17 tokens a second while sharing the machine, 7 of 10 smoke checks passed.
- **What changed.** The inference path is proven.
- **Next question.** How fast and how far can it go on a cleared machine?

### EXP-0004
2026-10-03 · INFRASTRUCTURE
- **Question.** How fast and how far can it go on a cleared machine?
- **Result.** 63 tokens a second for one stream, 172 across four, and a needle found in a 259K-token context 10 of 10 times.
- **What changed.** There is headroom for training and for long memory.
- **Next question.** Can general ability be measured reliably?

### EXP-0005
2026-10-04 · INFRASTRUCTURE
- **Question.** Can we measure the model's general ability reliably?
- **Result.** Two runs of a 120-item canary benchmark agreed on 115 of 120 items.
- **What changed.** A stable yardstick exists, so later damage can be detected.
- **Next question.** How much do measurements wobble on their own?

### EXP-0006
2026-10-04 · INFRASTRUCTURE
- **Question.** How much do measurements wobble on their own?
- **Result.** Noise floors were set. One consistency check missed its tolerance, so the record was rejected as pre-registered and the check was fixed.
- **What changed.** Know the noise before claiming a gain.
- **Next question.** Freeze generation 0 and start learning.

### SEED-0
2026-10-04 · Milestone
- **Result.** Generation 0 recorded in the ledger with its benchmark contract and hashes. Every later generation is compared to it.

## Era 2: Learning without forgetting

Goal: train small adapters that learn new things without erasing what the parent model knows.

### EXP-0007
2026-10-04 · INFRASTRUCTURE
- **Question.** Can adapters be trained on this machine at all?
- **Result.** The model loader ran out of memory and nothing trained. Serving with adapters worked.
- **What changed.** A custom loader is needed.
- **Next question.** With a new loader, do the adapter variants train?

### EXP-0008
2026-10-04 · SUPPORTED
- **Question.** With a new loader, do all three adapter variants train?
- **Result.** All three trained and served. One variant already showed forgetting.
- **What changed.** Training is feasible, and where an adapter is placed matters.
- **Next question.** Which placement learns without forgetting?

### EXP-0009
2026-10-04 · SUPPORTED
- **Question.** Which adapter placement learns without forgetting?
- **Result.** At matched learning, one placement forgot nothing beyond noise on five known areas; another forgot badly. Detailed protocol withheld while IP review is ongoing.
- **What changed.** A forgetting-safe placement became the default. The direction agrees with mini-AGI's published result on a much smaller model trained from scratch ([PRIOR_ART.md](PRIOR_ART.md#mini-agi)).
- **Next question.** Is the forgetting real or a measurement artifact?

### EXP-0010
2026-10-05 · SUPPORTED
- **Question.** Is the forgetting real, or an artifact of the serving stack?
- **Result.** An independent check in a different framework reproduced it area by area.
- **What changed.** The measurement can be trusted.
- **Next question.** Do the adapters hurt general ability?

### EXP-0011
2026-10-05 · PARTIAL
- **Question.** Do the adapters hurt general ability on the canary?
- **Result.** The default adapter was clean. A mixed variant missed its bound by one item. Active adapters halved decode speed.
- **What changed.** Small side effects exist, and the canary catches them.
- **Next question.** Do the results hold with a new random seed?

### EXP-0012
2026-10-05 · PARTIAL
- **Question.** Do the results hold with a new random seed?
- **Result.** The main results replicated. One secondary hypothesis failed.
- **What changed.** Replication across seeds became standard practice.
- **Next question.** Does the safe adapter stay clean when trained longer?

### EXP-0013
2026-10-05 · PARTIAL
- **Question.** Does the safe adapter stay clean when trained longer on facts?
- **Result.** It learned more, but late checkpoints started to forget.
- **What changed.** Long training needs protection.
- **Next question.** Can a change to the training data prevent it?

### EXP-0014
2026-10-05 · SUPPORTED
- **Question.** Does a change to the training data stop the forgetting?
- **Result.** Yes: no forgetting beyond noise on either probe, and more learning than before.
- **What changed.** A training setup without measurable forgetting on these probes became the default. Details withheld.
- **Next question.** Can a trained change earn promotion to generation 1?

## Era 3: The first generation

Goal: promote the first improved generation, under strict gates.

### EXP-0015
2026-10-05 · NOT SUPPORTED
- **Question.** Does a trained structured-output adapter earn promotion?
- **Result.** No: 2 of 20 on the structured canary items, and no gain on a private held-out task.
- **What changed.** Training alone did not fix a reasoning-format problem. Generation 1 was not promoted.
- **Next question.** Can a change with no weight training do better?

### EXP-0016
2026-10-05 · SUPPORTED
- **Question.** Does a policy that decides when to use slow reasoning, with no weight change, earn promotion?
- **Result.** Yes: 20 of 20 on the structured canary items (base 1 of 20) and 20 of 20 on the private held-out task (base 1 of 20). Routed items cost about 11 times the tokens.
- **What changed.** The first generation beyond the seed came from a decision policy, not from training. The promotion machinery works end to end.
- **Next question.** Can the model store new facts in its weights?

### GEN-0001
2026-10-06 · Milestone
- **Result.** Generation 1 recorded: the seed plus the decision policy. Generations advance only through gates.

## Era 4: Memory in the weights

Goal: store a day's facts directly in the weights through a nightly sleep cycle.

### EXP-0017
2026-10-06 · NOT SUPPORTED
- **Question.** Does the forgetting-safe adapter recall its trained facts without notes?
- **Result.** Barely: 2 of 120. It also invented answers for made-up names more often than the base.
- **What changed.** Training on prose does not create recallable memory.
- **Next question.** Does question-and-answer training fix recall?

### EXP-0018
2026-10-07 · NOT SUPPORTED
- **Question.** Does training on question-and-answer forms fix recall?
- **Result.** No recall, and more confabulation.
- **What changed.** Wrong format, too few exposures, or both.
- **Next question.** Were the facts stored at all?

### EXP-0019
2026-10-07 · NOT SUPPORTED
- **Question.** Did training store the facts in any form?
- **Result.** Not stored: chance level even on its own training questions. Format and vocabulary were learned; facts were not.
- **What changed.** The dose was far too low.
- **Next question.** With more capacity and repetition, can an adapter store facts?

### EXP-0020
2026-10-07 · SUPPORTED
- **Question.** With different training settings, can an adapter store facts at all?
- **Result.** Yes: 172 of 177 trained questions and 58 of 59 facts asked in new wording.
- **What changed.** Storing facts in an adapter is possible with the right settings. Settings withheld.
- **Next question.** Can it also learn to refuse what it does not know?

### EXP-0021
2026-10-07 · SUPPORTED
- **Question.** Can it learn to answer UNKNOWN for made-up names without losing recall?
- **Result.** Yes: invented answers fell to the base model's level (7 of 60 against 8 of 60) while recall held.
- **What changed.** Honest abstention can be trained alongside recall.
- **Next question.** Does it scale to more facts?

### EXP-0022
2026-10-07 · SUPPORTED
- **Question.** Does the recipe hold at 240 facts with fewer exposures?
- **Result.** Narrowly: 86.7% of trained wording, abstention within its bar, no forgetting.
- **What changed.** Scaling is possible but thin.
- **Next question.** Can a whole day go through memory and one night of training?

### EXP-0023
2026-10-08 · INCONCLUSIVE
- **Question.** Does a whole day of facts survive a memory store, consolidation and one night of training, with the canary intact?
- **Result.** Recall was excellent (145 of 150), but the canary fell from 88 to 47 and a serving-fidelity check failed, so the decision was null as pre-registered.
- **What changed.** Consolidating into weights can cost general ability.
- **Next question.** Is the damage caused by the dose or by the data mix?

### EXP-0024
2026-10-08 · INFRASTRUCTURE
- **Question.** Is the canary loss caused by the dose or the mix?
- **Result.** The mix, not the dose.
- **What changed.** The data mix decides the side effects.
- **Next question.** Does a safer mix keep the canary?

### EXP-0025
2026-10-08 · NOT SUPPORTED
- **Question.** Does the safer mix keep the canary?
- **Result.** No: corrections were not learned and the canary fell to 67.
- **What changed.** Weight-based sleep is fragile.
- **Next question.** Is the collapse stable across seeds?

### EXP-0026
2026-10-08 · PARTIAL
- **Question.** Is the canary loss a format collision, and is it stable across seeds?
- **Result.** It varies by seed. One variant kept the canary but lost abstention.
- **What changed.** Results that swing by seed cannot be trusted.
- **Next question.** Does the sleep cycle pass reliably across three seeds?

### EXP-0027
2026-10-09 · NOT SUPPORTED
- **Question.** Does the sleep cycle pass reliably across three seeds?
- **Result.** No: one seed of three failed the canary. Facts were reliable on all three.
- **What changed.** Weight consolidation was parked. Retrieval became the memory path.
- **Next question.** Where does multi-step recall actually fail?

### EXP-0028
2026-10-09 · INFRASTRUCTURE
- **Question.** Where does two-step recall actually fail?
- **Result.** In retrieval, not the model: with perfect notes it answered 52 of 54, with a single search 14 of 54.
- **What changed.** Fix retrieval before any more weight work.
- **Next question.** Does following links between facts close the gap?

## Era 5: Memory you can look up

Goal: make memory a store the model writes and searches, and pass a long-horizon memory gate.

### EXP-0029
2026-10-09 · SUPPORTED
- **Question.** Does following links between facts fix two-step recall?
- **Result.** Yes: 54 of 54 on the day's facts and 55 of 60 on a held-out set.
- **What changed.** Memory as a linked store works.
- **Next question.** Does it hold on a brand-new world?

### EXP-0030
2026-10-10 · SUPPORTED
- **Question.** Does entity-based retrieval hold on a fresh, never-seen world?
- **Result.** Yes: close to the perfect-store ceiling (single facts 115 against 119 with perfect notes; two-step 59 against 60).
- **What changed.** The retrieval design generalizes across synthetic worlds.
- **Next question.** Can the model write its own memory?

### EXP-0031
2026-10-10 · NOT SUPPORTED
- **Question.** Can the model build its own memory from twelve days of raw text?
- **Result.** Close but no: recall reached 0.75 to 0.88 of a perfect store, against a bar of 0.85. Moving the memory to a clean store gave identical answers.
- **What changed.** Self-written memory is nearly usable, and memory migration works.
- **Next question.** Does a nightly rewrite of its notes help?

### EXP-0032
2026-10-10 · PARTIAL
- **Question.** Does a nightly rewrite of its own notes help?
- **Result.** Sleep helped (107 against 94 known answers on day 12, p = 0.002), but the gate failed on abstention on one day.
- **What changed.** Sleep in memory form, not in weights, can help.
- **Next question.** With guards, does it pass the long-horizon gate on a fresh world?

### EXP-0033
2026-10-10 · PARTIAL
- **Question.** On a fresh world, does guarded sleep pass the long-horizon memory gate?
- **Result.** Mixed, as pre-registered: the long-horizon gate passed on synthetic text (recall 0.90 to 0.92 of a perfect store, 36 of 36 corrections, identical answers after migration), but the sleep hypothesis failed: sleep's extra gain from EXP-0032 did not replicate.
- **What changed.** The pre-registered twelve-day synthetic-memory gate passed. Real text is next.
- **Next question.** Can the model learn a real skill from its own verified work?

## Era 6: First skill, the memory writer

Goal: teach the model a real skill (writing its own memory) from its own verified work, and see whether it transfers.

### EXP-0034
2026-10-11 · PARTIAL
- **Question.** Does training on its own verified work teach a memory-writing skill that transfers?
- **Result.** Learned in its own domain on all three seeds (recall on an unseen world of the same kind rose from 0.83 to between 0.93 and 0.96). Transfer to a new domain cleared the bar on two of three seeds.
- **What changed.** Skills from self-verified data are real but uneven.
- **Next question.** Does training on two domains make transfer reliable?

### EXP-0035
2026-10-11 · NOT SUPPORTED
- **Question.** Does training on two domains make transfer to a third reliable?
- **Result.** No: still two of three seeds.
- **What changed.** Some seeds are simply bad, so they must be caught before use.
- **Next question.** Can a development gate catch the bad seed?

### EXP-0036
2026-10-11 · NOT SUPPORTED
- **Question.** Does a development gate catch the failing seed?
- **Result.** No: every new seed passed the gate and one still failed the test.
- **What changed.** The gate was too loose.
- **Next question.** Does a stricter gate work?

### EXP-0037
2026-10-12 · NOT SUPPORTED
- **Question.** Does a stricter twelve-day gate with a loop guard catch it?
- **Result.** No: a seed passed at the limit and failed the test.
- **What changed.** Any slack lets bad seeds through.
- **Next question.** What about a gate with no slack at all?

### EXP-0038
2026-10-12 · SUPPORTED
- **Question.** Does demanding at least the base model's score on every measure make the writer reliable?
- **Result.** All four selected seeds passed a new test world. Because the rejected seed also passed, the experiment did not show that the gate detects bad seeds.
- **What changed.** A strict development gate became the working standard for later skill experiments.
- **Next question.** Do synthetic gains carry to real text?

### EXP-0039
2026-10-13 · NOT SUPPORTED
- **Question.** Do the writer's synthetic gains carry to real, private notes? (The notes are not published.)
- **Result.** No: one adapter stayed as faithful as the base only by writing a third as much; both recalled less than the base.
- **What changed.** Synthetic worlds overstate real gains. No promotion.
- **Next question.** Does training on real-note extractions help?

### EXP-0040
2026-10-16 · NOT SUPPORTED
- **Question.** Does training on the model's own verified work on real notes beat the base?
- **Result.** The pre-registered decision was negative: training did not beat the base. Two seeds gained on mixed-topic notes (+33% and +23% supported facts, fewer unsupported), but all three failed on dense technical notes.
- **What changed.** Real-text skills need a hard verifier, and notes do not have one.
- **Next question.** What happens with a skill that has a hard verifier?

## Era 7: Verified skills and growing roots

Goal: grow skills that have automatic correctness checks, use each only in its own territory, and let them grow round after round.

### EXP-0041
2026-10-17 · NOT SUPPORTED
- **Question.** Does a coding skill learned from verified experience transfer to new task families?
- **Result.** The pre-registered decision was negative: it does not transfer. Two seeds gained +20 and +13.5 points on their own families (p < 0.001), but every seed lost 6 to 11 points on unseen families. A control stayed flat.
- **What changed.** A verified skill is a narrow specialist. It should only serve its own territory.
- **Next question.** If each skill is used only in its own territory, is the outside cost gone?

### EXP-0042
2026-10-18 · NOT SUPPORTED
- **Question.** If each small per-family skill is used only in its own territory, does the in-domain gain stay without the outside cost?
- **Result.** The pre-registered decision was negative: the small roots did not reliably keep the gain (+1.5 to +2.5 points). Keeping each root to its own territory removed the outside cost. A larger mixed root, used only in its territory, gained +24.5 points with no outside cost (reported as a control).
- **What changed.** Keeping a skill to its territory works in this setting; root size matters. Method withheld.
- **Next question.** Can a root grow from its own new verified successes?

### EXP-0043
2026-10-19 · NOT SUPPORTED
- **Question.** Does a root learn more from its own new verified successes than from more training on old data?
- **Result.** The pre-registered decision was negative: one growth round does not beat more training on old data. Only 1 of 3 seeds passed every gate, because the strongest starting root regressed below its start. Underneath the decision, the growth arms scored above their matched old-data controls in all three seeds (pooled +4.9 points), and two roots rose +9.25 and +15.75 points.
- **What changed.** Growth from new verified successes looked promising, and a strong root needed protection from regression.
- **Next question.** If every round must beat the current root before replacing it, can roots grow for several rounds?

### EXP-0044
2026-10-20 · SUPPORTED
- **Question.** Can roots grow for two rounds, keeping a change only when it beats the current root?
- **Result.** The pre-registered decision rule passed for 3 of 3 seeded lineages. On 600 held-out territory tasks the final roots beat their starting roots by +8.17, +6.83 and +6.50 points (one-sided exact McNemar p from 2.6e-6 to 1.9e-5), with no regression on the whole territory beyond base noise and measured forgetting below 0.01. Two difficulty levels dipped inside the gains. Every round accepted a candidate. No ungated control was run, so the cause of the gain is not identified.
- **What changed.** A skill can finish two successive gated generations above its start, inside its territory, on one model.
- **Next question.** Do the gains transfer outside the territory, and do better roots become better breeders?
- **Full write-up.** [results/EXP-0044.md](results/EXP-0044.md)

## Model independence

Goal: show that the persistent mind, not the model, is the individual.

### EXP-0045
Not yet registered · PENDING
- **Question.** Can one persistent mind run on two cortices from different model families (a Qwen-derived model and a GLM-family model) and keep its memories, identity, goals, world and self models, and skills?
- **Status.** The prerequisites are built: the Mind ABI, the Experience Bus, a versioned genome format and Cognitive Kernel v0. The experiment is being built. It has not run, and nothing here is a result. Its test design is withheld.

---

## How to read this ledger

- One-line results compress pre-registered decisions. Each result states the decision first; favorable details underneath a negative decision do not change its label.
- Benchmark contents, private task sets, prompts, datasets, adapter weights and training settings are not published.
- New entries are appended at the bottom and the totals are updated. Old entries are never rewritten. Corrections are added as dated notes.
