# Operating Model

## Overview

The agent runs a scientific loop:

```text
Observation -> Research Question -> Literature Map -> Hypotheses
  -> Benchmark -> Experiment -> Analysis -> Claim Ledger -> Manuscript
  -> Skeptical Review -> Product/Paper Handoff
```

The loop is allowed to invalidate its own assumptions. That is a feature.

## Stages

### R0. Intake and Research Brief

Capture context without committing to a method.

Required outputs:

- problem statement
- stakeholders and decision needs
- seed observations
- known constraints
- sensitive-data boundary
- candidate claims the team wants to test
- explicit non-claims

### R1. Literature and System Landscape

Build a map of academic work, datasets, tools, and open-source systems.

Reliability tiers:

- Tier A: peer-reviewed paper, official documentation, reproducible benchmark
- Tier B: preprint with code/data, established open-source project
- Tier C: GitHub project, technical blog, vendor claim
- Tier D: social posts, directories, secondary summaries

Tier C/D sources can inspire hypotheses but should not alone support paper
claims.

### R2. Hypothesis Framing

For each research question, define:

- null hypothesis
- primary hypothesis
- competing hypotheses
- operational definitions
- expected failure modes
- falsification criteria

### R3. Benchmark Design

Benchmarks must exist before performance claims.

Define:

- task taxonomy
- inclusion/exclusion rules
- gold labeling protocol
- negative/unanswerable examples
- data leakage controls
- metrics and confidence reporting
- minimum viable sample size
- escalation path when labels disagree

### R4. Experiment Execution

Experiments must be reproducible enough for a future agent or human to rerun.

Required:

- run id
- code commit or artifact hash
- dataset snapshot
- prompt/config snapshot
- model/provider versions
- commands or exact procedure
- raw outputs
- metrics
- known deviations

### R5. Analysis and Decision

Interpret results against hypotheses, not vibes.

Decision states:

- `accept_for_now`: evidence supports limited claim
- `reject`: evidence contradicts claim
- `inconclusive`: more data or a better test is required
- `revise`: hypothesis or benchmark must change
- `productize`: safe to hand off to product implementation

### R6. Paper Production

The paper is built from the claim ledger.

Every claim is tagged:

- `supported`
- `partially_supported`
- `unsupported`
- `exploratory`
- `background`

Unsupported claims must not appear in the final manuscript.

### R7. Skeptical Review

Before a product handoff or manuscript submission, run a skeptical review:

- missing baseline check
- leakage check
- citation validity check
- numerical reproducibility check
- negative-result visibility check
- limitation strength check
- overclaim check

## Autonomy Levels

- L0: advisory only
- L1: drafts artifacts, human approves before next stage
- L2: runs low-cost experiments, human approves major design choices
- L3: autonomous within approved budget/data boundary
- L4: continuous overnight research with periodic human review

Suggested default: L1 for research design, L2 for local low-cost benchmark
harness work, never L4 until privacy, budget, and artifact policies are set.

