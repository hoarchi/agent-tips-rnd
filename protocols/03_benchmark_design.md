# Protocol 03 - Benchmark Design

## Goal

Create a benchmark that measures the research question rather than the agent's
favorite demo cases.

## Steps

1. Define task families.
2. Define data sources and inclusion/exclusion rules.
3. Define labeling instructions.
4. Include answerable and unanswerable cases.
5. Include easy, medium, and hard examples.
6. Define metrics and failure taxonomy.
7. Define leakage controls.
8. Define minimum sample size for each stage.
9. Write `benchmark-card.md`.

## Example Metric Families (evidence-grounded QA)

Adapt to your domain. For an evidence-grounded QA/compliance program these
families are a strong default:

- answer correctness
- evidence correctness
- calculation correctness
- abstention correctness
- localization quality
- decision utility
- latency and cost

