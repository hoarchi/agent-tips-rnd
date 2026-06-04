# Research Brief

> Template example — replace every field with your own research.

## Program

Name: Evidence-Grounded Document QA

Date: 2026-01-01

Owner: your-team

Autonomy level: L1 design, L2 local low-cost experiments after approval

## Problem Statement

Question answering over technical documents needs answers that are grounded in
located evidence and that abstain when the evidence is absent. Free-form LLM
answers are fluent but cannot be audited and tend to answer even when the
document does not support an answer.

## Decision Need

Decide whether an evidence-bound retrieval/verifier architecture improves
reliability over a strong direct-LLM baseline enough to justify building it.

## Seed Observations

| Observation | Source | Confidence | Why it matters | Not a claim because |
|---|---|---:|---|---|
| Some questions are answerable directly from a single passage. | team handoff | Medium | Tests simple retrieval | One example is not a task family. |
| Some questions should abstain when the document lacks the fact. | team handoff | Medium | Tests hallucination control | Needs a negative-case benchmark. |
| Some questions require combining two located facts. | team handoff | Medium | Tests multi-evidence reasoning | Needs many such cases to measure. |

## Candidate Research Questions

1. What evidence representation best supports grounded QA with answer,
   evidence, and abstention requirements?
2. Does explicit verification reduce hallucination versus a direct-LLM baseline?

## Assumptions

| Assumption | Evidence | Risk if wrong | How to test |
|---|---|---|---|
| Located evidence improves auditability. | none yet | Wasted architecture effort | Compare evidence-recall across methods. |

## Sensitive Data Boundary

State which inputs are confidential and must not leave local/approved infra.

## Non-Goals

- Not a general chatbot.
- Not a production feature until the benchmark and verifier are accepted.

## Next Artifact

`hypothesis-card.md`
