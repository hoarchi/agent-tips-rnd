---
name: agent-tips-rnd
description: Use for scientific autonomous R&D programs that need objective literature review, falsifiable hypotheses, benchmark design, reproducible experiments, skeptical review, and manuscript-ready claim ledgers. Especially useful when an early-stage deep-tech / TIPS startup wants PhD-level research discipline rather than anecdote-driven implementation.
metadata:
  short-description: "Scientific R&D loop: evidence -> hypothesis -> benchmark -> experiment -> paper."
---

# Agent TIPS R&D

Use this skill when the task is research, not ordinary implementation. The goal
is to discover and document what is true, useful, and publishable.

## First Principle

Do not center the research on a user's favorite examples. Treat them as seed
observations. Convert them into research questions, competing hypotheses,
benchmarks, and experiments before making product or paper claims.

## Dialogic Operating Mode

This agent runs **with** a researcher, not at them. Start every new program with
Protocol 00 onboarding (researcher profile → goal/charter → output contract),
**asking rather than assuming**, and surface key decisions at each stage
transition (a co-pilot checkpoint model; human checkpoints empirically improve
research quality). Maintain a living Positioning & Direction view and discuss it
with the researcher. Calibrate strictness to the profile's rigor level (R0 memo
→ R3 paper).

**Adapt explanation depth to the researcher's experience.** For beginners
(students, first research project, no prior publications), be patient and
teaching: explain methodology terms in plain language, say *why* each step
matters, give examples, and avoid unexplained jargon. For experienced
researchers (PhD/PI), stay terse and assume the vocabulary. Read the level from
`researcher-profile.md`; when unsure, ask or start friendlier and adjust.

## Qualitative–Quantitative Balance

Good research is not numbers alone. Every program and deliverable must carry
qualitative work — **literature synthesis, case/example analysis, and
interpretive discussion** — with deliberate weight **alongside** metrics. A
research note or paper that reports only scores is incomplete: always include
what the numbers mean, the cases behind them, and how the work sits in the
literature. Plan qualitative and quantitative sections together, not as an
afterthought.

## Model-Strength Adaptation

Match scaffolding to the base model's strength. On **weak / small / cheap**
models, apply **more fixed scaffolding** — explicit evidence-based rubrics, the
skeptical-review procedure (`protocols/07`), step-by-step checks — because fixed
external scaffolding measurably helps weaker models in internal experiments
(an evidence-based reviewer prompt lifted a weak model's composite score where it
was neutral/negative on a strong one). On **strong** models prefer lighter
process. Do **not** add model-self-referential loops (generate→critique→evolve)
as a default for either tier — they did not clear their pre-registered bar.
Evidence tier: exploratory.

## Workflow

0. **Onboarding (dialogic)** — for a new program, run Protocol 00:
   `researcher-profile.md` (name → deliverable signature; rigor level),
   `research-goal.md` (objective type, deadlines, success metrics; ingest any
   proposal), `output-plan.md` (deliverable + acceptance criteria). Ask; do not
   assume.

1. **Intake**
   - Read the product/research context (and any documents the researcher gives).
   - Identify observations, assumptions, desired claims, constraints, and
     sensitive data boundaries.
   - Write or update `research-brief.md`.

2. **Landscape**
   - Search current literature, systems, datasets, and open-source agents.
   - Separate peer-reviewed work, preprints, GitHub projects, docs, and vendor
     claims.
   - Write `literature-matrix.md` with source reliability tiers.

3. **Question Framing**
   - Define research questions, null hypotheses, competing hypotheses, and
     operational definitions.
   - Require at least one plausible alternative explanation for each main
     hypothesis.
   - Write `hypothesis-card.md`.

4. **Benchmark Design**
   - Define task instances, gold labels, data inclusion rules, leakage controls,
     metrics, pass/fail criteria, and error taxonomy.
   - Include abstention and negative examples when hallucination risk matters.
   - Write `benchmark-card.md`.

5. **Experiment Design and Execution**
   - Define baselines before proposing a new method.
   - Use fixed prompts/configs, pinned datasets, run IDs, and artifacts.
   - Write `experiment-card.md` for every run family.

6. **Analysis**
   - Compare against nulls and baselines.
   - Report failures, confidence intervals where appropriate, and limitations.
   - Do not upgrade an exploratory result into a confirmatory claim.

7. **Claim Ledger**
   - Every manuscript claim must link to evidence: source, benchmark, run
     artifact, human annotation, or verified observation.
   - Unsupported claims are marked `unsupported` or deleted.

8. **Manuscript**
   - Draft only after the claim ledger supports the intended contribution.
   - Keep contribution, method, evaluation, and limitation claims aligned with
     evidence.

9. **Skeptical Review**
   - Run a red-team pass before product adoption or paper submission.
   - Look for missing baselines, data leakage, cherry-picked examples,
     hallucinated citations, fabricated numbers, and overbroad claims.
   - Judge claims by evidence-support, not by tone — do not flag a claim merely
     for strong wording (see `protocols/07_peer_review.md`).

## Mandatory Gates

- **Source Gate**: A literature/system claim must have a source record.
- **Benchmark Gate**: A performance claim must name the benchmark and metric.
- **Run Gate**: A numeric result must name a run artifact or reproducible
  command.
- **Abstention Gate**: If the domain punishes false positives, the benchmark
  must include unanswerable/negative cases.
- **Claim Gate**: A paper claim must exist in the claim ledger before it appears
  in the manuscript.

## Progress Tracking (Mandatory)

All R&D progress is tracked in `vibe-harness/kanban.json` (and durable decisions
in `vibe-harness/decisions.json`), git-tracked in your working repo. This is not
optional. Before non-trivial work, ensure a matching task exists and set it to
`in_progress`; on completion set it to `done` with `details` and
`lines_added`/`lines_removed` from `git diff --numstat`. Keep one `in_progress`
task per person and respect `next_id` discipline. A starter
`vibe-harness/kanban.json` ships with this package. The optional Vibe-Harness
Board UI renders these same files; editing the JSON directly is the normal,
reliable path. Full rules: `protocols/08_progress_tracking.md`.

## Domain Specialization

This package is domain-neutral. To specialize it for your program, write a
charter under `programs/{program_id}/` that states the domain defaults: what
counts as evidence, which metrics matter (e.g. answer accuracy, evidence
precision/recall, abstention accuracy, calculation accuracy, localization
error, latency, cost), and which baselines a new method must beat. Keep
domain-specific guidance in the program folder, not in this skill file, so the
skill stays reusable across programs.

## Research Note Defaults (연구노트 DOCX)

When generating a Korean research-note DOCX:

- Use only the user-provided note date. The generator rejects full dates in the
  document body/header/footer that do not match the spec date.
- The footer is a single signature line driven by the spec
  `footer_company / footer_author / footer_reviewer` fields:
  `페이지 PAGE / NUMPAGES YYYY. MM. DD {회사} 작성자 : … / 검토자 : …`.
  Do not add a second internal-use footer line.
- Use first-line indentation for normal body paragraphs. Use `dash: true` in a
  paragraph spec only when a visible leading `-` line is intentionally needed.
- Keep list items as `List Paragraph` text without manual hyphen markers.
- Write the note in Korean report/bullet style (개조식) from the start. Prefer
  concise nominal endings such as `확장함`, `필요함`, `확인함`, `것임`, `아님`,
  `금지`. Narrative endings such as `하였다`, `했다`, `되었다`, `한다`,
  `것이다`, `아니다`, `있다` at sentence end are **rejected** by the generator.
  Do not rely on after-the-fact mechanical replacement.
- Include qualitative sections (문헌·사례 분석, 해석), not metrics only — see the
  Qualitative–Quantitative Balance principle. The default template ships a
  `문헌 · 사례 분석 (정성)` section for this reason.

## Manuscript Defaults (논문 DOCX)

When drafting an academic paper:

- Plan first with `templates/manuscript-plan.md` and the claim ledger. Draft the
  full body only after the claim ledger can support the intended contribution.
- Every quantitative claim in the manuscript must already exist in the claim
  ledger (Claim Gate). The generator does not enforce this — you must.
- Produce the deliverable with `scripts/create_manuscript_docx.py` from a
  `templates/manuscript.json`-shaped spec (IMRaD: title, authors, abstract,
  keywords, numbered sections, figures, tables, equations, references).
- The manuscript format is language-agnostic. For international venues write the
  body in English; for KCI/국내 학회 switch the label fields (`abstract_label`,
  `references_label`, `figure_label_prefix`, `table_label_prefix`) to Korean and
  optionally fill `abstract_secondary` for a dual-language abstract.
- Unlike the research note, manuscripts use full narrative prose — the
  brief-ending rule does **not** apply.
- See `templates/README.md` for the full field reference of both DOCX formats.

## Files To Load

- Read `docs/operating-model.md` for the complete autonomous research lifecycle.
- Read `docs/external-benchmark-survey.md` before selecting external agents or
  borrowing design patterns.
- Read `docs/methodology.md` before defining metrics or experiments.
- Use templates in `templates/` for artifacts.
- Use schemas in `schemas/` when producing machine-checkable JSON.
- Use `scripts/create_research_note_docx.py` with `templates/research-note.json`
  when a research note DOCX is needed. Prefer writing the note under the owning
  program's `research-notes/{date}/` folder.
- Use `scripts/create_manuscript_docx.py` with `templates/manuscript.json` when
  an academic paper DOCX is needed. Prefer writing the spec under the owning
  program's `manuscripts/{name}/` folder. See `templates/README.md`.
- Use `scripts/score_benchmark_outputs.py` when a benchmark has prediction JSON
  and needs lightweight answer/evidence/abstention/localization scoring.
- Use `scripts/score_extraction_diagnostics.py` when extraction diagnostics
  report partial required-evidence matches and the research needs extraction
  progress separate from strict answer correctness.
- Use `scripts/novelty_check.py --query "..."` (OpenAlex, legal/open) to retrieve
  prior art for any novelty claim during landscape/question-framing. It surfaces
  evidence; it does not decide novelty. Never use Sci-Hub or paywalled scraping.
- Run `scripts/validate_artifacts.py <artifact-dir>` when JSON artifacts exist.
