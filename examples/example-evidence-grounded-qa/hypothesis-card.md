# Hypothesis Card

> Template example — replace with your own.

## Research Question

Does an evidence-bound method (retrieve located evidence, then verify) answer
technical-document questions more reliably than a direct-LLM baseline?

## Null Hypothesis

The evidence-bound method does not improve answer accuracy or abstention
accuracy over the direct-LLM baseline.

## Primary Hypothesis

The evidence-bound method improves abstention accuracy on unanswerable cases
without losing answer accuracy on answerable cases.

## Competing Hypotheses

1. A strong direct-LLM with a good prompt already abstains well enough; the
   evidence layer adds cost without reliability gains.
2. Retrieval errors dominate, so binding to located evidence hurts more than it
   helps on multi-evidence questions.

## Operational Definitions

| Term | Definition | Measurement |
|---|---|---|
| Answerable | Document contains the fact(s) needed | gold label |
| Abstention | Model declines when no evidence exists | exact match to "abstain" gold |
| Evidence recall | Fraction of required evidence located | per-item overlap with gold spans |

## Expected Evidence

Higher abstention accuracy on negative cases; comparable answer accuracy on
positive cases; non-trivial evidence recall.

## Falsification Criteria

If abstention accuracy does not exceed the baseline by a pre-registered margin,
reject the primary hypothesis for this benchmark.

## Risks and Confounds

Benchmark too small; retrieval tuned to the test set (leakage); baseline prompt
under-tuned, inflating the apparent gain.
