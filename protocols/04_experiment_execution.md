# Protocol 04 - Experiment Execution

## Goal

Run controlled experiments that future researchers can inspect and repeat.

## Required Before Running

- benchmark card
- baseline list
- fixed prompt/config snapshots
- run artifact directory
- cost/time budget
- stop criteria

## Steps

1. Create run ID.
2. Snapshot code, data, prompts, and model/provider versions.
3. Run baseline(s) first.
4. Run proposed method(s).
5. Store raw outputs.
6. Score with the same evaluator.
7. Record deviations.
8. Write `experiment-card.md`.

## Failure Handling

Failures are data. Record them as:

- infrastructure failure
- model/tool failure
- data/label failure
- method failure
- hypothesis failure

