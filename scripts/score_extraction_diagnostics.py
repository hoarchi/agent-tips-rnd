#!/usr/bin/env python3
"""Score extraction diagnostic JSON against required evidence strings.

This is for OCR/VLM extraction probes that report `required` and
`matched_required` per item. It complements the answer scorer by preserving
partial evidence recovery instead of collapsing everything into abstention.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any


def load_items(path: Path | None) -> dict[str, dict[str, Any]]:
    if path is None:
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {str(item["id"]): item for item in data.get("items", [])}


def load_records(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        if isinstance(data.get("diagnostics"), list):
            return data["diagnostics"]
        if isinstance(data.get("records"), list):
            return data["records"]
    if isinstance(data, list):
        return data
    raise ValueError("Diagnostic input must contain `diagnostics`, `records`, or be a list.")


def score(records: list[dict[str, Any]], items: dict[str, dict[str, Any]]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    strict_hits = 0
    total_items = 0
    required_total = 0
    matched_total = 0
    by_family: dict[str, Counter[str]] = {}

    for record in records:
        item_id = str(record.get("id", ""))
        item = items.get(item_id, {})
        if items and item.get("answerable") is not True:
            continue

        required = [str(value) for value in record.get("required", []) or []]
        matched = [str(value) for value in record.get("matched_required", []) or []]
        if not required:
            continue

        total_items += 1
        required_total += len(required)
        matched_total += len(matched)
        full_match = len(matched) == len(required)
        if full_match:
            strict_hits += 1

        family = str(item.get("task_family") or record.get("task_family") or "unknown")
        fam = by_family.setdefault(family, Counter())
        fam["items"] += 1
        fam["required"] += len(required)
        fam["matched"] += len(matched)
        fam["full_match"] += int(full_match)

        rows.append(
            {
                "id": item_id,
                "task_family": family,
                "required_count": len(required),
                "matched_count": len(matched),
                "partial_recall": len(matched) / len(required),
                "full_match": full_match,
                "missing_required": [value for value in required if value not in matched],
            }
        )

    return {
        "summary": {
            "items_with_required_evidence": total_items,
            "strict_full_match_items": strict_hits,
            "strict_full_match_rate": strict_hits / total_items if total_items else None,
            "required_evidence_strings": required_total,
            "matched_required_evidence_strings": matched_total,
            "partial_evidence_recall": matched_total / required_total if required_total else None,
        },
        "by_task_family": {
            family: {
                "items": counts["items"],
                "strict_full_match_rate": counts["full_match"] / counts["items"] if counts["items"] else None,
                "partial_evidence_recall": counts["matched"] / counts["required"] if counts["required"] else None,
            }
            for family, counts in sorted(by_family.items())
        },
        "items": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="Diagnostic JSON")
    parser.add_argument("--items", type=Path, help="Benchmark items JSON")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = score(load_records(args.input), load_items(args.items))
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
