#!/usr/bin/env bash
# Update an installed agent-tips-rnd: fast-forward the clone, re-link skills,
# and report what changed. Your programs/ and runs/ are never touched.
#
#   ~/.agent-tips-rnd/update.sh
#   # or, if install.sh put it on your PATH:
#   agent-tips-rnd-update
set -euo pipefail

SRC="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"

if [ ! -d "${SRC}/.git" ]; then
  printf 'Not a git clone: %s\n' "$SRC" >&2
  printf 'Re-run install.sh to set up a managed clone.\n' >&2
  exit 1
fi

OLD_VERSION="$(cat "${SRC}/VERSION" 2>/dev/null || echo unknown)"
OLD_REV="$(git -C "$SRC" rev-parse HEAD 2>/dev/null || echo none)"

printf 'Updating agent-tips-rnd in %s ...\n' "$SRC"
git -C "$SRC" pull --ff-only

NEW_VERSION="$(cat "${SRC}/VERSION" 2>/dev/null || echo unknown)"
NEW_REV="$(git -C "$SRC" rev-parse HEAD 2>/dev/null || echo none)"

if [ "$OLD_REV" = "$NEW_REV" ]; then
  printf '\nAlready up to date (version %s).\n' "$NEW_VERSION"
  exit 0
fi

printf '\nUpdated %s -> %s\n' "$OLD_VERSION" "$NEW_VERSION"
printf '\nChanges:\n'
git -C "$SRC" log --oneline "${OLD_REV}..${NEW_REV}" | sed 's/^/  /'

# Re-link skills (idempotent) so any new files/targets are picked up.
printf '\nRe-linking skills...\n'
"${SRC}/install.sh"
