# Protocol 01 - Evidence Review

## Goal

Build a reliable map of what is already known and what remains unproven.

## Source Handling

Classify every source:

- peer-reviewed paper
- preprint
- official documentation
- benchmark/dataset
- GitHub project
- technical blog
- vendor claim
- social/secondary source

## Steps

1. Search broadly.
2. Resolve identifiers where possible: DOI, arXiv ID, ACL Anthology ID, GitHub
   repo URL, docs URL.
3. For any novelty / "first" / "unprecedented" claim, run an automated prior-art
   check (`scripts/novelty_check.py --query "..."`, OpenAlex) and attach the
   retrieved related works as evidence. The tool retrieves, it does not decide —
   read the results before asserting novelty. Use only legal open sources
   (OpenAlex / arXiv / Unpaywall); never Sci-Hub or paywalled scraping.
4. Record source reliability tier.
4. Extract claims, methods, metrics, datasets, and limitations.
5. Identify contradictions and missing baselines.
6. Write `literature-matrix.md`.

## Refusal Rule

Do not cite a source you have not inspected enough to characterize.

