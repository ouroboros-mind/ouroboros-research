# Publication policy

What this repository publishes, what it withholds, and why.

## Published

- The research question, thesis and success criteria.
- The architecture at a conceptual level: the parts and what they are for.
- Every experiment in the ledger, including null and failed results, with a one-paragraph summary.
- Detailed results for selected experiments: counts, significance, noise floors, regression, forgetting and limitations.
- The roadmap with statuses taken from evidence.
- Prior art, with what each work shows and how Ouroboros differs.

## Withheld

- Source code, model weights, adapters and training data.
- Evaluation task content, task and verifier construction, and private benchmarks. Publishing them would contaminate future evaluations.
- Training recipes, hyperparameters, growth-data selection, candidate construction, acceptance rules beyond their plain-language summary, and thresholds.
- Prompts and routing methods.
- Information about infrastructure, and personal information.

Where a protocol is withheld, the page says so. Withholding a method never changes the reported outcome, and negative results are not withheld.

## What a reader can and cannot verify

Because code, data, task sets, training procedures and the ledger are private, readers cannot reproduce experiments or verify pre-registration timing from this repository. Pre-registration, contamination checks and ledger integrity are author-reported. Readers can check internal consistency (for example, that p-values recompute from published paired counts) and test the claims independently on their own tasks and models.

## Rules for adding a result

1. The experiment is recorded in the private ledger first. Public numbers are copied from the recorded analysis.
2. The ledger entry is added to [EXPERIMENTS.md](../EXPERIMENTS.md), whatever the outcome.
3. Limitations are written before the interpretation is published.
4. Status changes on the [roadmap](../ROADMAP.md) cite a ledger entry.
5. Each public file is reviewed before release for withheld material.
