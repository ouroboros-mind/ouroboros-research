# The Mind ABI

The Mind ABI is the single contract between the persistent mind and any language model. "ABI" borrows from operating systems: a stable interface that lets the part above it outlive the parts below it.

## Why it exists

If the mind called a particular model's API directly, scattered through its code, replacing that model would mean rewriting the mind. Ouroboros is designed to keep model-specific detail behind one boundary, and an automated test in the private codebase checks that kernel code does not call a model directly.

## What it promises

- **The mind should not depend on one model's internals.** A model is plugged in through a driver that implements the contract.
- **A model is checked before it is trusted.** Capabilities a model claims are tested before the mind relies on them.
- **Learning depends on openness.** With a closed, hosted model only the mind's own memory and skills can change. With an open-weight model, small neural adapters are also possible.
- **Weights are model-bound.** Anything learned inside one model's weights is tied to that model. Whether such capability can be carried to a new model is an open research question.

## Status

The Mind ABI and its conformance suite are built, and the existing evaluation code was moved behind it with identical recorded results. One cortex has passed conformance for the capabilities it claims. Running the same mind through the ABI on two model families is EXP-0045, which has not run.

Driver interfaces, capability definitions and conformance tests are withheld.
