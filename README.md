# agent-tips-rnd

**A research agent for TIPS startups that need PhD-level R&D discipline.**

This is not a one-shot paper generator. It is an operating system for turning
uncertain product observations into defensible research claims — through
literature review, benchmark construction, controlled experiments, skeptical
review, and manuscript-ready evidence ledgers.

It is built for early-stage deep-tech teams (TIPS and adjacent R&D startups) who
need to move from "we think our approach works" to "here is the benchmarked,
reproducible, citable evidence that it works" — without hiring a research lab.

Works as a skill/agent package for **Claude Code** and **OpenAI Codex**.

---

## What it gives you

- **A research loop, not a prose machine.** Observations → falsifiable
  questions → competing hypotheses → benchmarks → reproducible experiments →
  claim ledger → manuscript. Each stage leaves a structured artifact.
- **Evidence gates.** Every literature claim needs a source record, every
  number needs a run artifact, every paper claim needs a ledger entry. The agent
  refuses to inflate anecdotes into conclusions.
- **Two submission-grade DOCX deliverables out of the box:**
  - **연구노트 (research note)** — a Korean R&D lab-notebook (the format TIPS/
    national-R&D reporting expects), generated from a JSON spec.
  - **논문 (manuscript)** — an academic paper (IMRaD), Korean or English, also
    from a JSON spec.
- **Templates + JSON schemas** for every artifact, so outputs are
  machine-checkable and repeatable.

## Layout

| Path | What it is |
|---|---|
| `SKILL.md` | Skill entrypoint (Claude Code / Codex). |
| `AGENTS.md` | Operating rules when the folder is opened as an agent workspace. |
| `docs/` | Operating model, methodology, and an external-agent survey. |
| `protocols/` | Stage-by-stage procedures (intake → peer review). |
| `schemas/` | JSON schemas for structured research artifacts. |
| `templates/` | Markdown artifact templates + the two DOCX spec templates. |
| `scripts/` | DOCX generators, artifact validator, and benchmark scorers. |
| `registry/` | Machine-readable index of your research programs. |
| `programs/` | One folder per long-running research program. |
| `runs/` | Timestamped experiment runs, each naming its owning program. |
| `examples/` | A worked generic example program to copy from. |

> A **research program** is a long-lived line of inquiry (one core question,
> many runs). A **run** is a single timestamped experiment inside a program.
> This is research-methodology terminology, deliberately distinct from a
> product "project".

---

## Install

The package installs as a skill into your agent's skills directory.

### One-liner

```bash
curl -fsSL https://raw.githubusercontent.com/hoarchi/agent-tips-rnd/main/install.sh | bash
```

This clones the repo to `~/.agent-tips-rnd` and links it into every agent it
detects:

- **Claude Code** → `~/.claude/skills/agent-tips-rnd`
- **OpenAI Codex** → `$CODEX_HOME/skills/agent-tips-rnd` (defaults to
  `~/.codex/skills/agent-tips-rnd`)

### Manual

```bash
git clone https://github.com/hoarchi/agent-tips-rnd.git ~/.agent-tips-rnd
cd ~/.agent-tips-rnd && ./install.sh
```

Then, in your agent, invoke the `agent-tips-rnd` skill (or point the agent at
`SKILL.md`).

### For teams

Every teammate runs the same one-liner on their own machine — that is the whole
onboarding. The install is per-user (it links into each person's
`~/.claude/skills` / `~/.codex/skills`), while the research itself lives in your
project repos. Nothing is shared implicitly; everyone pulls the same versioned
package and tracks their work in the project's `vibe-harness/kanban.json`.

> If this repo is still **private**, the `curl | bash` one-liner cannot read the
> raw URL. Either make the repo public, or add teammates as collaborators and
> have them use the **Manual** clone (their `git` credentials handle auth).

## Update

Already installed? Update in place — no reinstall:

```bash
agent-tips-rnd-update      # if install added it to your PATH
# or
~/.agent-tips-rnd/update.sh
```

How it works: the installer **symlinks** the skill directories to a managed git
clone at `~/.agent-tips-rnd`. `update.sh` runs `git pull --ff-only` on that
clone, re-links (so new files are picked up), and prints what changed since your
installed `VERSION`. Because the skill is a symlink to the clone, the pull is the
update — there is nothing to copy. Your own `programs/` and `runs/` are never
touched; the install lives separately from your working research.

> Compared to a copy-based skill installer (e.g. Vibe-Harness, which copies
> files and registers a launch agent on setup), this package is symlink +
> `git pull`: lighter, and updates are just a pull.

## Python dependency

The DOCX generators need `python-docx`:

```bash
python -m pip install python-docx
```

---

## Quick start

1. Read `SKILL.md` and `AGENTS.md`.
2. Copy `examples/` into a new `programs/<your-program>/` and register it in
   `registry/programs.json`.
3. Start a run: `runs/<date>-<program>-<run-name>/` and work the protocols in
   `protocols/` in order.
4. Produce a research note with
   `scripts/create_research_note_docx.py` (spec: `templates/research-note.json`)
   or a paper with `scripts/create_manuscript_docx.py`
   (spec: `templates/manuscript.json`). See `templates/README.md` for the full
   field reference.

## Progress tracking is mandatory

This agent **requires** progress to be tracked in `vibe-harness/kanban.json`
(and durable decisions in `vibe-harness/decisions.json`), git-tracked in your
project. A starter `vibe-harness/` ships with the package, so tracking starts
on day one. The loop: add a task → `in_progress` before you start → `done` with
`details` and `git diff --numstat` line stats when finished. One `in_progress`
task per person; never reuse a `next_id`.

It is **JSON-first**: you do not need any server or extra tool — the agent edits
the JSON directly. If you separately install the Vibe-Harness skill, its Board
UI at `localhost:4242` simply renders these same files. Full rules:
`protocols/08_progress_tracking.md`.

## License

MIT — see `LICENSE`.
