# programs/

One folder per **research program** — a long-lived line of inquiry with one
core question and many runs over time. This is the unit that survives across
experiments; individual experiments live in `runs/`.

```
programs/
  {program_id}/
    README.md            # program index: question, status, key claims, run log
    research-notes/      # optional: dated 연구노트 DOCX specs + outputs
    manuscripts/         # optional: paper drafts (manuscript.json specs + DOCX)
    benchmark/           # optional: program-owned benchmark versions
```

## Start a new program

1. Copy `examples/example-evidence-grounded-qa/` artifacts as a starting point.
2. Create `programs/{your_program_id}/README.md`.
3. Register it in `registry/programs.json` (give it a unique `program_id`).
4. Open a first run under `runs/{date}-{short-name}-{run-name}/`.

Keep program-specific assumptions (domain defaults, sensitive-data boundaries,
which baselines to beat) in the program README — not in the shared `SKILL.md`
or `AGENTS.md`, which stay domain-neutral and reusable.
