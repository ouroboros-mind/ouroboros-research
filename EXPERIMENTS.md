# Public experiment ledger

This is the public summary of the Ouroboros experiment ledger. The private ledger is append-only and hash-chained, and every experiment is pre-registered before it runs. Rejected, null and aborted runs stay in the record. Negative results are evidence.

The ledger itself, the task sets, the training procedure and raw results are private. Pre-registration timing and ledger integrity are author-reported and cannot be verified from this repository. The author reports that, from EXP-0046 on, pre-registrations were committed by hash before they ran; from EXP-0050 on, those commitments, and from 2026-10-26 the ledger checkpoints, are also submitted to OpenTimestamps. Once a proof confirms in a Bitcoin block, it makes the corresponding record tamper-evident ([how it works](README.md#anchored-in-bitcoin)). See [what you can and cannot verify](README.md#what-you-can-and-cannot-verify).

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
| **PENDING** | Pre-registered, has not run. Not counted in the totals |

## Totals (EXP-0001 to EXP-0050)

| SUPPORTED | PARTIAL | NOT SUPPORTED | INCONCLUSIVE | INFRASTRUCTURE | Total |
|---:|---:|---:|---:|---:|---:|
| 14 | 8 | 18 | 1 | 9 | 50 |

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
| [EXP-0045](#exp-0045) | 2026-10-21 | One mind, two model families | SUPPORTED |
| [EXP-0046](#exp-0046) | 2026-10-22 | A neural skill without changing the mind | SUPPORTED |
| [EXP-0047](#exp-0047) | 2026-10-22 | Brain migration | NOT SUPPORTED |
| [EXP-0048](#exp-0048) | 2026-10-23 | Skill regrowth after migration | PARTIAL |
| [EXP-0049](#exp-0049) | 2026-10-24 | Validating the working frame | NOT SUPPORTED |
| [EXP-0050](#exp-0050) | 2026-10-28 | Re-presenting the working frame | NOT SUPPORTED |

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
2026-10-21 · SUPPORTED
- **Question.** Can one persistent mind run on two cortices from different model families (a Qwen-derived model and GLM-4.7-Flash) and keep its identity, memories, skills and world model?
- **Result.** The pre-registered decision rule passed (five gates). On a withheld 15-item continuity battery, the mind scored 15 on its original model and 15 on GLM-4.7-Flash, against 1 for a newly born mind and 4 for a different genome on GLM. Every task frame on GLM carried its compiled procedure, and its tool predictions stayed calibrated (Brier 0.0032 against 0.0635 for the newborn). Held-out tasks were at ceiling for every arm, so the effect of the skills is unmeasured. No weights moved.
- **What changed.** Identity, memory, procedures and calibration belonged to the genome, not the model, in this first small test.
- **Next question.** Can neural learning on one model improve skill without corrupting the mind's records?
- **Full write-up.** [results/EXP-0045.md](results/EXP-0045.md)

### EXP-0046
2026-10-22 · SUPPORTED
- **Question.** Can a mind turn its own verified experience into a neural skill on one model, with everything it owns outside that skill left byte-identical and its other model unaffected?
- **Result.** The pre-registered decision rule passed (six gates). With its new adapter the mind passed 246 of 400 held-out tasks against 221 for the plain model (+6.25 points, one-sided exact McNemar p 0.0023; the repeated plain model scored 230, a +2.25-point movement). Its kernel code, identity, memories and other records were byte-identical before and after (its experience record only gained promotion, training and registration records), all 63 training lines traced to its own verified passes, and the second model never received the adapter; 84 of its 100 answers ran out of their budget and it scored near its floor, so this check could barely detect harm. A pipeline bug was fixed after pre-registration and is recorded as a deviation. Its [public commitment](public-commitments/experiments/EXP-0046.commitment.json) was published before the run, and four revealed fields verify against it.
- **What changed.** Neural learning can be requested by the mind and attached to it without touching its kernel or its other records, in this first small test.
- **Next question.** Can a mature mind's learned skills be carried to, or regrown on, a new model?
- **Full write-up.** [results/EXP-0046.md](results/EXP-0046.md)

### EXP-0047
2026-10-22 · NOT SUPPORTED
- **Question.** When the model under a mature mind is replaced by a newer one that cannot load its learned cache, can the mind keep who it is, regrow what it learned from records it owns, and roll back?
- **Result.** The pre-registered decision was negative: the mind lost capability in migration, not continuity. The 12-question battery about its lived history scored 12 of 12 on Qwen3.8-27B with the mind and 12 of 12 on Seed-0 with the mind, against 0 of 12 for Qwen3.8-27B without the mind. The kernel hash and every existing record were unchanged (four declared migration records were appended), and every training line traced to a verified reply with no trained task in a held-out set. Rollback onto Seed-0 scored 64 against 63 of 100 for Seed-0 with its cache. But the cache regrown from the mind's own records scored 124 against 147 of 200 for Qwen3.8-27B without it, so the safety rule refused it. On the 400-task final test, the learned-increment gate failed: Seed-0 with its EXP-0046 cache gained +4.5 points over raw Seed-0, while the migrated mind's cache arm on Qwen3.8-27B (no cache attached) lost 10.5 points against raw Qwen3.8-27B; the procedure-only arm lost 9.5. The refused cache was used only in its check and never registered. A request timeout required a second drained window; three runtime settings changed, with no change to a gate, threshold, data set, model or kernel code. Its [public commitment](public-commitments/experiments/EXP-0047.commitment.json) was published before the run, and four revealed fields verify against it.
- **What changed.** Identity and records carried across this model replacement in a first small test. A skill compiled on the weaker model did not automatically help the stronger one, and the quarantine rule rejected the harmful regrowth as designed.
- **Next question.** Can a migrated mind regrow a skill from the new model's own verified experience?
- **Full write-up.** [results/EXP-0047.md](results/EXP-0047.md)

### EXP-0048
2026-10-23 · PARTIAL
- **Question.** After moving to a stronger model, can the mind find out which skills still help, stop using the ones that do not, and regrow its skill from its own verified experience on the new model, doing at least as well as the new model alone?
- **Result.** Classified PARTIAL. The pre-registered decision was "the skill regrew to match the new cortex, but validation did not remove the frame's cost". On 200 held-out validation tasks, the raw new model scored 165, the mind's frame with its old procedure scored 147, and without it scored 142, so the procedure was kept because it no longer hurt. The mind then lived 300 new tasks, with 203 first-attempt passes. Its new cache used only those verified passes from the new model. It scored 171 against 148 of 200 without it in its safety check and was accepted. On the 400-task final test, raw Qwen3.8-27B scored 326 and its raw repeat scored 322. The mind's frame without the cache scored 293, failing the frame-cost gate by 8.25 points. With its regrown cache it scored 351, a +14.5-point gain over the frame (p 1.3e-10) and +6.25 points over the raw model (52 tasks gained, 27 lost; one-sided p 0.0033). The kernel and pre-existing records were unchanged, every training line traced to a verified pass on the new model, the old model was unaffected (62 against 63 of 100 with its own cache), and the continuity battery scored 12 of 12 after the second session. No deviations occurred. Its [public commitment](public-commitments/experiments/EXP-0048.commitment.json) was published before the run, and four revealed fields verify against it.
- **What changed.** A skill can regrow from the new model's own verified experience and beat that new model alone in this first test. The remaining cost is in the mind's working frame, not the old procedure.
- **Next question.** Which part of the working frame costs the new model, and can frame parts be validated per model?
- **Full write-up.** [results/EXP-0048.md](results/EXP-0048.md)

### EXP-0049
2026-10-24 · NOT SUPPORTED
- **Question.** On the new model, which parts of the mind's working frame help or hurt, and can a validated, model-specific frame stay close to the raw model while the regrown skill adds on top?
- **Result.** Classified NOT SUPPORTED. A balanced 16-configuration test of five frame parts on 200 fresh development tasks used one common request path, with prefix caching off and raw-model repeat runs. A frozen rule removed the procedure (-3.2 points) and thinking/resources line (-3.4), and kept the goal, self line and memories (memories +1.8). On 400 fresh final tasks, raw Qwen3.8-27B scored 340 and its repeat 339. The old full frame scored 308. The validated frame scored 311, 7.1 points below raw, so its frame gate failed. It gained 30 tasks and lost 27 against the old frame (p 0.40), so that gate also failed. Its regrown cache added 8.25 points inside the validated frame (50 gained, 17 lost; p 3.4e-5), but scored 344 against raw's 340. A secret rotating test across four unseen task families passed for the frame (147 against raw's 141); the cache added 1.5 points there (p 0.39), so transfer was not shown. General capability checks, the 12-of-12 identity battery, the frozen selection rule and the unchanged stored mind all passed. Five pre-registration amendments were each committed before the code they fixed ran. The candidate profile was not activated. Its [public commitment](public-commitments/experiments/EXP-0049.commitment.json), amendments and selection commitment were published before their governed work, and four revealed fields verify against the original commitment.
- **What changed.** The frame still costs the new model. Removing parts one at a time did not remove that cost. In a post hoc comparison, the skill added more inside the full frame where it grew than inside the validated one, which is consistent with frame and skill co-adaptation.
- **Next question.** Proposed, owner decision pending: change the frame's placement, compression and memory policy, with the skill regrown inside each candidate frame. Cross-family skill regrowth waits for that.
- **Full write-up.** [results/EXP-0049.md](results/EXP-0049.md)

### EXP-0050
2026-10-28 · NOT SUPPORTED
- **Question.** On the new model, can a model-specific presentation of the mind's working frame, chosen before any skill is grown, plus a skill regrown from the mind's verified experience inside that presentation, beat the raw model with a separate contribution from both presentation and skill?
- **Result.** Classified NOT SUPPORTED. Several presentations of the same stored mind were compared on 200 fresh development tasks without a skill. A frozen rule chose one, and its hash was published before the test. Practice inside the chosen presentation and the old frame produced one regrown skill from each. Both were refused in a separate 200-task quarantine check: the new-presentation skill scored 184 with the skill against 187 without, and the old-frame skill scored 158 against 157. Nothing was promoted and the stored mind stayed unchanged. On 800 fresh final tasks, raw scored 675 and its repeat 666. The old frame scored 585, its regrown skill 595, the old frame with EXP-0048's skill 714, the new presentation 734 and its regrown skill 744. Against the average raw reference, the combined new artifact gained 9.2 points and passed its gate. The presentation alone gained 18.6 points against the old frame, but that gate required both skills to be accepted in quarantine, so it did not pass. The regrown skill added 1.25 points inside the new presentation and passed its corrected comparison. On 200 unseen tasks across four hidden families, the combined artifact scored 141 against raw's 156 and failed. General capability checks, the 12-of-12 identity battery, the selection rule and the unchanged stored mind passed. EXP-0048's skill inside the old frame also passed its replication comparison. Four amendments were published as hash commitments before the code each fixed ran. A recorded-reply replay after a token-counter crash produced 0 verdict differences; a practice crash was aborted before any result was seen; a training path error stopped training before it began; and an incomplete final session was rerun fresh before any final result was written or read. A report-only comparison failed because its skill was never loaded; it was not used for selection or any gate. The first amendment, pre-registration and selection proofs confirmed after their governed work began. Amendments 2 through 4 confirmed before their work started. Its [public commitment](public-commitments/experiments/EXP-0050.commitment.json), amendments and selection were published before their governed work, and four revealed fields verify against the original commitment.
- **What changed.** Re-presenting the same stored mind turned a 10.7-point cost into a 7.9-point gain on familiar task families. The regrown skill added little there, was not accepted in quarantine, and most of the loss on unseen families came with it. The migration claim is not supported.
- **Next question.** Proposed, owner decision pending: why did the regrown skill hurt unseen families and fail quarantine while the presentation alone helped? Options include more varied experience, more than one training run per presentation, and checking unseen-family transfer before accepting any skill.
- **Full write-up.** [results/EXP-0050.md](results/EXP-0050.md)

---

## How to read this ledger

- One-line results compress pre-registered decisions. Each result states the decision first; favorable details underneath a negative decision do not change its label.
- Benchmark contents, private task sets, prompts, datasets, adapter weights and training settings are not published.
- New entries are appended at the bottom and the totals are updated. Old entries are never rewritten. Corrections are added as dated notes.
- From EXP-0046 on, each pre-registration is committed by hash in [public-commitments/](public-commitments/README.md) before it runs.
