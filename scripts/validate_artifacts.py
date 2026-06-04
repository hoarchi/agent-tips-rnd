#!/usr/bin/env python3
"""Lightweight artifact validator for agent-rnd-phd.

The script intentionally uses only the Python standard library. It checks
machine-readable JSON artifacts for the minimum fields needed by the research
protocols. It is not a full JSON Schema validator; use it as a quick guardrail.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


REQUIRED_BY_KIND = {
    "source_record": ["id", "title", "url", "source_type", "reliability_tier", "captured_at", "claims"],
    "research_question": ["id", "question", "null_hypothesis", "candidate_hypotheses"],
    "benchmark_card": ["id", "name", "purpose", "task_families", "metrics", "baselines"],
    "benchmark_items": ["benchmark_id", "version", "items"],
    "experiment_card": ["id", "hypothesis_id", "benchmark_id", "methods", "runs", "decision"],
    "claim_ledger": ["claims"],
}

IGNORED_DIR_NAMES = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".venv",
    ".venv-paddleocr",
    "__pycache__",
    "node_modules",
    "site-packages",
}


def infer_kind(path: Path, data: object) -> str | None:
    name = path.name.lower()
    for kind in REQUIRED_BY_KIND:
        if kind in name:
            return kind
    if isinstance(data, dict):
        if "source_type" in data and "reliability_tier" in data:
            return "source_record"
        if "runs" in data and "methods" in data:
            return "experiment_card"
        if "task_families" in data and "metrics" in data:
            return "benchmark_card"
        if "benchmark_id" in data and "items" in data:
            return "benchmark_items"
        if "candidate_hypotheses" in data:
            return "research_question"
        if "claims" in data and isinstance(data["claims"], list):
            return "claim_ledger"
    return None


def validate_file(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"{path}: invalid JSON: {exc}"]

    kind = infer_kind(path, data)
    if kind is None:
        return []

    if not isinstance(data, dict):
        return [f"{path}: expected object for {kind}"]

    for field in REQUIRED_BY_KIND[kind]:
        if field not in data:
            errors.append(f"{path}: missing required field `{field}` for {kind}")

    if kind == "claim_ledger":
        for idx, claim in enumerate(data.get("claims", [])):
            if not isinstance(claim, dict):
                errors.append(f"{path}: claims[{idx}] must be object")
                continue
            if not claim.get("evidence") and claim.get("status") not in {"unsupported"}:
                errors.append(f"{path}: claims[{idx}] has no evidence")

    if kind == "benchmark_card":
        families = data.get("task_families", [])
        if isinstance(families, list) and not families:
            errors.append(f"{path}: benchmark must define at least one task family")

    if kind == "benchmark_items":
        items = data.get("items", [])
        if not isinstance(items, list) or not items:
            errors.append(f"{path}: benchmark_items must contain at least one item")
        for idx, item in enumerate(items if isinstance(items, list) else []):
            if not isinstance(item, dict):
                errors.append(f"{path}: items[{idx}] must be object")
                continue
            for field in ["id", "question", "task_family", "answerable", "evidence_sufficiency"]:
                if field not in item:
                    errors.append(f"{path}: items[{idx}] missing `{field}`")
            if item.get("answerable") is True and not item.get("required_evidence"):
                errors.append(f"{path}: items[{idx}] is answerable but has no required_evidence")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_artifacts.py <artifact-dir>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1])
    if not root.exists():
        print(f"Path does not exist: {root}", file=sys.stderr)
        return 2

    if root.is_file():
        paths = [root]
    else:
        paths = sorted(
            path
            for path in root.rglob("*.json")
            if not any(part in IGNORED_DIR_NAMES or part.startswith(".venv") for part in path.parts)
        )
    errors: list[str] = []
    for path in paths:
        errors.extend(validate_file(path))

    if errors:
        print("Artifact validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Artifact validation passed for {len(paths)} JSON file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
