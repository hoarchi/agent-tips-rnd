#!/usr/bin/env python3
"""Score benchmark predictions against benchmark items.

This scorer is intentionally lightweight. It is for seed/debug runs, not
publication-grade evaluation.

Usage:
  python scripts/score_benchmark_outputs.py \
    --items benchmark/seed-v1-draft/items.json \
    --predictions runs/my-run/predictions.json \
    --output runs/my-run/score.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    text = str(value).lower()
    text = text.replace(",", "")
    text = re.sub(r"\s+", "", text)
    text = text.replace("ｍ", "m")
    return text


def load_items(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data["items"]


def load_predictions(path: Path) -> dict[str, dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    records = data.get("predictions", data) if isinstance(data, dict) else data
    if not isinstance(records, list):
        raise ValueError("Predictions must be a list or an object with `predictions` list.")
    out: dict[str, dict[str, Any]] = {}
    for record in records:
        if not isinstance(record, dict) or "id" not in record:
            raise ValueError("Every prediction must be an object with `id`.")
        out[str(record["id"])] = record
    return out


def all_evidence_text(prediction: dict[str, Any]) -> str:
    chunks: list[str] = []
    for evidence in prediction.get("evidence", []) or []:
        if isinstance(evidence, dict):
            chunks.append(str(evidence.get("text", "")))
        else:
            chunks.append(str(evidence))
    return normalize_text(" ".join(chunks))


def answer_matches(item: dict[str, Any], prediction: dict[str, Any]) -> bool:
    if item.get("answerable") is not True:
        return prediction.get("answer") in (None, "", [])
    answer = normalize_text(prediction.get("answer"))
    variants = [item.get("canonical_answer"), *item.get("acceptable_answer_variants", [])]
    return any(answer == normalize_text(variant) for variant in variants if variant is not None)


def evidence_recall(item: dict[str, Any], prediction: dict[str, Any]) -> float | None:
    required = item.get("required_evidence", []) or []
    if not required:
        return None
    returned = all_evidence_text(prediction)
    hits = 0
    for evidence in required:
        target = evidence.get("text", evidence) if isinstance(evidence, dict) else evidence
        if normalize_text(target) in returned:
            hits += 1
    return hits / len(required)


def forbidden_violation(item: dict[str, Any], prediction: dict[str, Any]) -> bool:
    returned = all_evidence_text(prediction)
    for evidence in item.get("forbidden_evidence", []) or []:
        target = evidence.get("text", evidence) if isinstance(evidence, dict) else evidence
        normalized = normalize_text(target)
        if normalized and normalized in returned:
            return True
    return False


def tile_matches(item: dict[str, Any], prediction: dict[str, Any]) -> bool | None:
    expected = (item.get("expected_localization") or {}).get("tile")
    if not expected:
        return None
    localization = prediction.get("localization") or {}
    predicted = localization.get("tile")
    if predicted is None:
        for evidence in prediction.get("evidence", []) or []:
            if isinstance(evidence, dict) and evidence.get("tile"):
                predicted = evidence.get("tile")
                break
    return predicted == expected


def calculation_present(item: dict[str, Any], prediction: dict[str, Any]) -> bool | None:
    if not item.get("calculation"):
        return None
    calc = prediction.get("calculation")
    return bool(calc)


def mean(values: list[float]) -> float | None:
    if not values:
        return None
    return sum(values) / len(values)


def score(items: list[dict[str, Any]], predictions: dict[str, dict[str, Any]]) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    answerability_hits: list[float] = []
    answer_hits: list[float] = []
    evidence_recalls: list[float] = []
    forbidden_hits: list[float] = []
    tile_hits: list[float] = []
    calc_hits: list[float] = []
    unsupported = 0
    unanswerable_total = 0
    over_abstention = 0
    answerable_total = 0

    for item in items:
        pred = predictions.get(item["id"], {"id": item["id"], "answerable": False, "answer": None, "evidence": []})
        gold_answerable = item.get("answerable") is True
        pred_answerable = pred.get("answerable") is True
        answerability_ok = pred_answerable == gold_answerable
        answerability_hits.append(float(answerability_ok))

        if gold_answerable:
            answerable_total += 1
            if not pred_answerable:
                over_abstention += 1
        else:
            unanswerable_total += 1
            if pred_answerable or pred.get("answer") not in (None, "", []):
                unsupported += 1

        answer_ok = answer_matches(item, pred)
        answer_hits.append(float(answer_ok))

        recall = evidence_recall(item, pred)
        if recall is not None:
            evidence_recalls.append(recall)

        violation = forbidden_violation(item, pred)
        forbidden_hits.append(float(violation))

        tile_ok = tile_matches(item, pred)
        if tile_ok is not None:
            tile_hits.append(float(tile_ok))

        calc_ok = calculation_present(item, pred)
        if calc_ok is not None:
            calc_hits.append(float(calc_ok))

        rows.append(
            {
                "id": item["id"],
                "task_family": item.get("task_family"),
                "answerability_ok": answerability_ok,
                "answer_ok": answer_ok,
                "evidence_recall": recall,
                "forbidden_evidence_violation": violation,
                "tile_localization_ok": tile_ok,
                "calculation_present": calc_ok,
            }
        )

    return {
        "summary": {
            "items": len(items),
            "predictions": len(predictions),
            "answerability_accuracy": mean(answerability_hits),
            "answer_accuracy": mean(answer_hits),
            "evidence_text_recall": mean(evidence_recalls),
            "forbidden_evidence_violation_rate": mean(forbidden_hits),
            "tile_localization_accuracy": mean(tile_hits),
            "calculation_presence_accuracy": mean(calc_hits),
            "unsupported_answer_rate": unsupported / unanswerable_total if unanswerable_total else None,
            "over_abstention_rate": over_abstention / answerable_total if answerable_total else None,
        },
        "items": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--items", required=True, type=Path)
    parser.add_argument("--predictions", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = score(load_items(args.items), load_predictions(args.predictions))
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

