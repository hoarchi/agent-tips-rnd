# Protocol 00 - Intake & Dialogic Onboarding

## Goal

When a researcher starts a new program, **converse first, assume nothing.**
Capture who the researcher is, what they want, and what the deliverable is —
through a short Q&A — before any literature or experiments. This makes the agent
fit the researcher, and it fills concrete downstream fields (e.g. the research
note signature line) from the start.

This protocol runs **dialogically**: ask, record the answer, confirm, move on.
Do not silently guess. If the researcher provides documents (a proposal,
연구계획서, prior reports), ingest and analyze them, then confirm your reading.

## Stage 0a — Researcher profile

Ask (skip what is already known; never invent):

1. Name and affiliation? (→ goes on the research-note footer / manuscript authors)
2. Role, degree, and research experience? (student / engineer / MS / PhD / PI)
3. Prior publications or R&D track record, if any?
4. Working language for notes and deliverables? (e.g. Korean note + English paper)
5. **Desired rigor level** (calibrates how strict the agent is):
   - `R0` exploratory memo — fast, low formality
   - `R1` internal report — feature-level rigor
   - `R2` funded / TIPS deliverable — full reproducibility + claim ledger
   - `R3` peer-reviewed paper — all gates + manuscript

→ Write `researcher-profile.md`. The rigor level sets defaults for which gates
are enforced and how much process overhead to apply.

## Stage 0b — Goal & charter

Ask / ingest:

1. **Objective type** (one or more): peer-reviewed paper · TIPS R&D deliverable ·
   internal report · SW / algorithm / model · dataset / benchmark.
2. **Deadline(s)** for each objective and any interim milestones.
3. **Success metrics**: is there a quantitative target (a KPI, an accuracy bar,
   a funding/acceptance criterion)? If qualitative, what does "done well" mean?
4. **Proposal ingestion**: if a research proposal / 연구계획서 / grant doc exists,
   read it and extract objectives, scope, and stated metrics; confirm with the
   researcher before treating them as the goal.

→ Write `research-goal.md` (the program charter). Convert relative deadlines to
absolute dates.

## Stage 0c — Output contract

Decide, by Q&A, what the program produces and how it will be judged:

1. Final deliverable: paper (→ `create_manuscript_docx.py`) · report
   (→ `create_research_note_docx.py`) · algorithm/model (→ code + experiment
   cards) · dataset/benchmark (→ benchmark card + items).
2. Acceptance criteria for that deliverable.
3. Revisit clause: the output contract can change; record when it does and why.

→ Write `output-plan.md`.

## Stage 1 — Research brief (as before)

With 0a–0c recorded, extract observations, candidate research questions,
assumptions, and the sensitive-data boundary. Write `research-brief.md`.

## Ongoing — positioning dialogue

Once the landscape exists, keep a living **Positioning & Direction** view
(in `literature-matrix.md`): where this work sits relative to prior art and
where it is heading. Raise it with the researcher at each stage transition; the
direction is a conversation, not a fixed line.

## Output Checklist

- `researcher-profile.md` (name → deliverable signature; rigor level)
- `research-goal.md` (objective type, deadlines, success metrics)
- `output-plan.md` (deliverable + acceptance criteria)
- `research-brief.md` (problem, seed observations, RQs, assumptions, boundary)
- Positioning & direction recorded and discussed
