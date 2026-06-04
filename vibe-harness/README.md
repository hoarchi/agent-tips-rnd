# vibe-harness/

**Progress tracking is mandatory for this agent.** See
`protocols/08_progress_tracking.md` for the full rules.

- `kanban.json` — tasks (`todo` / `in_progress` / `done`). Source of truth,
  git-tracked. Starts empty; add your tasks here.
- `decisions.json` — durable decisions and their rationale.

You do **not** need any server to use this. The agent (and you) edit these JSON
files directly — that is the normal path. If you also install the separate
`vibe-harness` skill, its Board UI at `localhost:4242` renders these same files.

## The loop

1. Add a task as `todo`, move it to `in_progress` before starting (set
   `started_at`).
2. Keep **one** `in_progress` task per person.
3. On finish: `done` + `details` + `lines_added`/`lines_removed`
   (`git diff --numstat`) + `completed_at`.
4. New task id = current `next_id`, then increment `next_id`. Never reuse ids.
5. Commit `kanban.json` in the same commit as the work it describes.
