# The learning stack

This page describes, conceptually, how Ouroboros intends experience to become capability. It is a research design; most steps are not yet demonstrated. Selection rules, training methods, data construction and thresholds are private.

## From experience to capability

```
experience  →  memory  →  procedure  →  skill  →  neural specialization  →  core capability
```

- **Experience** is everything the individual encounters, recorded once with its outcome.
- **Memory** is what is worth keeping from it: facts, events, corrections.
- **A procedure** is a reusable way of doing something that worked more than once.
- **A skill** is a procedure tied to a way of checking it, with a measured success rate.
- **A neural specialization** is a skill compiled into the weights of an open-weight cortex, for example as a small adapter, so it becomes faster and cheaper.
- **A core capability** is what several specializations might eventually consolidate into.

Each arrow is a promotion that must pass the protected evaluation plane. The research question is whether intelligence can move down this ladder and become cheaper, faster and more general while staying verified. The idea in one line: expensive cognition today should become cheap intuition tomorrow.

## Multiple timescales

| Speed | What changes | How often |
|---|---|---|
| Instant | The working frame | Every step |
| Fast | Memory and measurements | Every event |
| Medium | Procedures, skills and policies | Between sessions |
| Slow | Neural specializations | In dedicated training windows |
| Generational | The learning process itself | Only through a recorded generation change |

Plasticity falls as you go down: memory changes easily, the shared model barely at all. Using different learning rates for shared and specialized parameters is established prior art ([PRIOR_ART.md](../PRIOR_ART.md#mini-agi)).

## What the evidence says so far

| Step | Evidence |
|---|---|
| Experience → memory | Works on synthetic text, including corrections and abstention (EXP-0029 to EXP-0033) |
| Memory → weights (nightly consolidation) | Not supported: unreliable across seeds; parked (EXP-0023 to EXP-0027) |
| Verified experience → skill adapter | Learned inside a skill's own territory; did not transfer to unseen task families (EXP-0034 to EXP-0042) |
| Skill → better skill, repeatedly | One ungated round: negative pre-registered decision (EXP-0043). Two gated generations finished above their start in 3 of 3 seeded lineages, inside one territory, on one model (EXP-0044) |
| Specialization → core capability | Not started |
| Improving the learning process | Not started |

See the [experiment ledger](../EXPERIMENTS.md) for each entry.
