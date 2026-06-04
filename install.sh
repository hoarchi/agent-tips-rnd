#!/usr/bin/env bash
# Install agent-tips-rnd as a skill for Claude Code and/or OpenAI Codex.
#
#   curl -fsSL https://raw.githubusercontent.com/hoarchi/agent-tips-rnd/main/install.sh | bash
#   # or, from a local clone:
#   ./install.sh
#
# Idempotent: safe to re-run. update.sh calls this to re-link after pulling.
set -euo pipefail

REPO_URL="${AGENT_TIPS_RND_REPO:-https://github.com/hoarchi/agent-tips-rnd.git}"
INSTALL_DIR="${AGENT_TIPS_RND_HOME:-$HOME/.agent-tips-rnd}"
SKILL_NAME="agent-tips-rnd"

info() { printf '  %s\n' "$*"; }
ok()   { printf '  \033[32m✓\033[0m %s\n' "$*"; }
warn() { printf '  \033[33m!\033[0m %s\n' "$*"; }

# --- Resolve the source tree ------------------------------------------------
# If this script sits next to SKILL.md, use that clone. Otherwise bootstrap by
# cloning (or fast-forwarding) INSTALL_DIR.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" 2>/dev/null && pwd || true)"
if [ -n "${SCRIPT_DIR:-}" ] && [ -f "${SCRIPT_DIR}/SKILL.md" ]; then
  SRC="$SCRIPT_DIR"
else
  if [ -d "${INSTALL_DIR}/.git" ]; then
    info "Updating existing clone at ${INSTALL_DIR}"
    git -C "$INSTALL_DIR" pull --ff-only
  else
    info "Cloning ${REPO_URL} -> ${INSTALL_DIR}"
    git clone --depth 1 "$REPO_URL" "$INSTALL_DIR"
  fi
  SRC="$INSTALL_DIR"
fi

VERSION="$(cat "${SRC}/VERSION" 2>/dev/null || echo "unknown")"
printf '\nInstalling agent-tips-rnd %s from %s\n\n' "$VERSION" "$SRC"

# --- Link the skill into each detected agent --------------------------------
link_skill() {
  local base="$1" label="$2"
  local skills_dir="${base}/skills"
  mkdir -p "$skills_dir"
  local target="${skills_dir}/${SKILL_NAME}"
  ln -sfn "$SRC" "$target"
  ok "${label}: ${target} -> ${SRC}"
}

linked=0
# Claude Code
if [ -d "${HOME}/.claude" ] || [ "${AGENT_TIPS_RND_FORCE_CLAUDE:-0}" = "1" ]; then
  link_skill "${HOME}/.claude" "Claude Code"; linked=1
fi
# OpenAI Codex
CODEX_BASE="${CODEX_HOME:-$HOME/.codex}"
if [ -d "$CODEX_BASE" ] || [ "${AGENT_TIPS_RND_FORCE_CODEX:-0}" = "1" ]; then
  link_skill "$CODEX_BASE" "Codex"; linked=1
fi

if [ "$linked" = "0" ]; then
  warn "No ~/.claude or ${CODEX_BASE} found. Linking Claude Code by default."
  link_skill "${HOME}/.claude" "Claude Code"
fi

# --- Optional: put update on PATH ------------------------------------------
for bindir in "${HOME}/.local/bin" "/usr/local/bin"; do
  if [ -d "$bindir" ] && [ -w "$bindir" ]; then
    ln -sfn "${SRC}/update.sh" "${bindir}/agent-tips-rnd-update"
    ok "Update command: agent-tips-rnd-update  (-> ${SRC}/update.sh)"
    break
  fi
done

printf '\nDone. In your agent, invoke the "%s" skill (or point it at %s/SKILL.md).\n' "$SKILL_NAME" "$SRC"
printf 'Update later with:  %s/update.sh\n' "$SRC"
printf 'Python deliverables need: python -m pip install python-docx\n'
