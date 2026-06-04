# runs/

One folder per **experiment run**. A run is a single timestamped study that
belongs to exactly one program.

```
runs/
  {YYYY-MM-DD}-{program-short-name}-{run-name}/
    README.md            # points back to the owning program_id; states the question
    experiment-card.md   # or experiment-card.json — methods, configs, run IDs
    *.json               # predictions, scores, diagnostics (the run artifacts)
    analysis.md          # results vs baselines/nulls, error analysis, decision
```

## Rules

- Every run README must name its `program_id`.
- Every number in `analysis.md` must trace to a run artifact in the same folder
  (Run Gate).
- Use fixed prompts/configs and record them, so the run is reproducible.

Validate JSON artifacts with `scripts/validate_artifacts.py <run-dir>`.
