# Protocol 08 - Progress Tracking (Vibe-Harness, Mandatory)

## Goal

Every user of this agent — solo or on a team — tracks R&D progress the same way,
so work is visible, resumable, and reviewable across people and sessions.

**This protocol is mandatory.** The agent must keep the kanban current; it is not
optional book-keeping.

## Source of Truth

Progress lives in git-tracked JSON under the working repo:

- `vibe-harness/kanban.json` — tasks (`todo` / `in_progress` / `done`)
- `vibe-harness/decisions.json` — durable decisions and their rationale

The Vibe-Harness server / Board UI (`localhost:4242`) is an optional convenience.
It does **not** need to be running. When it is off, edit the JSON directly — that
is the normal, reliable path. If you have the `vibe-harness` skill installed, its
UI simply renders these same files.

## Rules

1. **Before** starting any non-trivial work, ensure a matching task exists. If
   not, add it as `todo`, then move it to `in_progress` (set `started_at`).
2. **One `in_progress` task per person** at a time. Park others back to `todo`.
3. **On completion**, move the task to `done` and fill, at minimum:
   - `details` — what changed (files), key decisions, follow-ups.
   - `lines_added` / `lines_removed` — measured via `git diff --numstat`.
   - `completed_at`, and bump `updated_at`.
4. **`next_id` discipline.** A new task uses the current `next_id` as its `id`,
   then increment `next_id`. Never reuse an id; never let two tasks share one.
5. **Record durable decisions** in `decisions.json` with a one-line rationale.

## Task shape

```json
{
  "id": 1, "title": "...", "status": "todo|in_progress|done",
  "category": "backend|frontend|infra|data|docs|qa",
  "details": "", "lines_added": 0, "lines_removed": 0,
  "started_at": "", "completed_at": "",
  "created_at": "", "updated_at": "", "phase": "", "priority": "high"
}
```

`title`, `status`, `category` are always required; `details` and the line stats
are required when a task is `done`.

## Commit discipline

Commit `vibe-harness/kanban.json` together with the code/docs it describes — code
and its progress record land in the same commit, never split.

## Output

A current `vibe-harness/kanban.json` (and `decisions.json`) at every meaningful
stopping point. A result that is not recorded here is not considered done.
