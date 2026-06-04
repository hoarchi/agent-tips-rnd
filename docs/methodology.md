# Methodology

## Scientific Guardrails

### Observation vs. Claim

Observation:

> A current prototype answered a balcony level-difference question correctly on
> one drawing.

Claim:

> Evidence-bound GraphRAG improves architectural drawing QA accuracy.

The first can start a research thread. The second requires benchmark evidence.

### Exploratory vs. Confirmatory

Exploratory work can discover task families, failure modes, and promising
methods. Confirmatory work must use predeclared data, metrics, baselines, and
decision criteria.

Do not mix the two in a paper without labeling them.

### Baselines

For drawing QA, candidate baselines include:

- direct multimodal prompt over page image
- PDF text extraction plus prompt
- text chunk RAG
- vector RAG over extracted evidence
- graph retrieval without generation
- hybrid retrieval without verifier
- hybrid retrieval with verifier
- human reviewer timing/accuracy when available

The strongest simple baseline should be taken seriously. If it wins, the
research should say so.

### Metrics

Use metrics that match risk:

- answer accuracy
- evidence precision
- evidence recall
- abstention accuracy
- hallucination rate
- calculation accuracy
- localization error
- latency
- cost
- reviewer correction burden

For compliance workflows, hallucination and abstention deserve first-class
status. A system that gives confident wrong answers is worse than one that says
"not enough evidence".

### Labeling

Gold labels should capture:

- answerability
- canonical answer
- acceptable answer variants
- required evidence
- forbidden evidence
- calculation steps
- target entity or spatial scope
- expected localization
- ambiguity notes

Label disagreements are data. Record them instead of forcing premature
agreement.

### Statistics

Use simple reporting first:

- sample count per task family
- mean and confidence interval where appropriate
- per-family breakdown
- confusion matrix for answerable vs. unanswerable
- error taxonomy counts

Avoid decorative statistics on tiny samples. Small benchmark seeds are for
debugging, not final claims.

### Paper Claims

A paper claim should be no broader than the evidence:

- "On our 20-question seed benchmark" is not "on architectural drawings".
- "Improves abstention on unanswerable cases" is not "solves hallucination".
- "Works on apartment accessibility drawings" is not "works on all CAD PDFs".

