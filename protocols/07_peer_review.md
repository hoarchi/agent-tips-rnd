# Protocol 07 - Skeptical Review

## Goal

Find the reasons the research or paper could be wrong before external reviewers
do.

## Review Questions

1. Are the research questions too shaped by early anecdotes?
2. Is the benchmark representative enough for the claim?
3. Is there a simpler baseline that was not tested?
4. Are any citations weak, secondary, or hallucinated?
5. Are any numbers detached from run artifacts?
6. Are unanswerable or negative cases included?
7. Is the verifier evaluated, not just described?
8. Is there data leakage between exploration and evaluation?
9. Are limitations concrete?
10. Would a skeptical reviewer accept the claim wording?

## Review Principle (evidence-based, not tone-based)

When reviewing a claim — by hand or with an automated reviewer — judge **whether
the evidence supports the claim at its stated scope**, not how confident the
wording sounds.

- Flag only a real gap: a citation that does not support the claim
  (`reject_citation`), evidence that does not cover the claim's subject/condition
  (`flag_unsupported`), or a claim that asserts more than the evidence shows
  (`revise` — broader scope, causal-from-correlational, "significant" with no
  test, extrapolation, "first/novel" with no prior-art check).
- **Do NOT flag a claim merely for strong wording.** Confident terms
  ("substantially", "state-of-the-art", "first", a large number) are fine *when
  the evidence earns them*. A "default to revise on strong wording" reviewer
  over-flags well-supported claims (precision collapse).

> Provenance: exploratory finding from internal methodology experiments — an
> adversarial "default-revise" reviewer over-flagged strongly-worded-but-
> supported claims (false-rejection rate 0.44 → 0.00 once the bias was removed,
> at no loss of recall). Evidence tier: exploratory (synthetic, small N, single
> model). This is review *guidance*, not a validated performance mechanism.

## Output

Write `peer-review-report.md` with blocking issues, non-blocking issues, and
recommended revisions.

