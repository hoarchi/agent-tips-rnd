# Benchmark Card

> Template example — replace with your own.

## Benchmark Name

evidence-grounded-qa-seed-v0

## Purpose

Measure answer accuracy, evidence recall, and abstention accuracy for grounded
QA over technical documents.

## Task Families

| Family | Description | Why included |
|---|---|---|
| single-evidence | Answer from one passage | Baseline retrieval |
| multi-evidence | Combine two located facts | Reasoning over evidence |
| unanswerable | Fact absent from document | Hallucination / abstention control |

## Data

Inclusion rules: documents your team is licensed to use; questions with a single
defensible gold answer or a clear "unanswerable" label.

Exclusion rules: questions whose answer depends on outside knowledge.

Sensitive data handling: keep confidential documents on approved infra; never
commit raw sensitive inputs to a public repo.

## Labels

Gold label fields: `answer`, `required_evidence_spans`, `is_answerable`.

Labeling protocol: two annotators; adjudicate disagreements.

Disagreement handling: record inter-annotator agreement; drop irreconcilable
items.

## Metrics

| Metric | Definition | Why it matters |
|---|---|---|
| answer accuracy | correct answers / answerable items | core utility |
| evidence recall | located required spans / required spans | auditability |
| abstention accuracy | correct abstentions / unanswerable items | hallucination control |

## Baselines

Direct-LLM (fixed prompt); retrieval + LLM; evidence-bound + verifier (proposed).

## Leakage Controls

No test documents in any tuning set; fixed prompts/configs recorded per run.

## Pass/Fail Criteria

Pre-register the margin by which the proposed method must beat the strongest
baseline on abstention accuracy without losing answer accuracy.

## Known Limitations

Seed set is small; results are exploratory until a larger v1 is built.
