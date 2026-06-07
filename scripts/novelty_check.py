#!/usr/bin/env python3
"""Automated novelty / prior-art check via the OpenAlex API (open, legal, no key).

Given a query — a research question, a novelty claim, or a working title —
retrieve the most related prior works and summarize whether prior art exists.

  python scripts/novelty_check.py --query "evidence-bound review benchmark for LLM research agents"
  python scripts/novelty_check.py --query "..." --k 10 --since 2020 --output novelty.json

IMPORTANT (Source Gate): this tool RETRIEVES evidence; it does NOT decide
novelty. A "first / novel / unprecedented" claim must be backed by reading these
results. Uses only OpenAlex (legal open metadata) — never Sci-Hub or paywalled
scraping. Optionally augments with Semantic Scholar if a key is set
(SEMANTIC_SCHOLAR_API_KEY); S2 is rate-limited without one.
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.parse
import urllib.request
from pathlib import Path

OPENALEX = "https://api.openalex.org/works"
MAILTO = os.environ.get("OPENALEX_MAILTO", "help@derev.ai")
S2 = "https://api.semanticscholar.org/graph/v1/paper/search"


def _get(url: str, headers: dict | None = None) -> dict:
    req = urllib.request.Request(url, headers=headers or {})
    return json.loads(urllib.request.urlopen(req, timeout=30).read())


def reconstruct_abstract(inv: dict | None) -> str:
    if not inv:
        return ""
    pos = {}
    for word, idxs in inv.items():
        for i in idxs:
            pos[i] = word
    return " ".join(pos[i] for i in sorted(pos))[:400]


def openalex_search(query: str, k: int, since: int | None) -> tuple[int | None, list]:
    params = {"search": query, "per-page": k, "mailto": MAILTO}
    if since:
        params["filter"] = f"from_publication_date:{since}-01-01"
    d = _get(OPENALEX + "?" + urllib.parse.urlencode(params))
    works = []
    for w in d.get("results", []):
        works.append({
            "title": w.get("title"),
            "year": w.get("publication_year"),
            "authors": [a["author"]["display_name"] for a in (w.get("authorships") or [])[:4]],
            "cited_by": w.get("cited_by_count"),
            "doi": w.get("doi"),
            "oa_url": (w.get("open_access") or {}).get("oa_url")
                      or (w.get("primary_location") or {}).get("landing_page_url"),
            "abstract": reconstruct_abstract(w.get("abstract_inverted_index")),
        })
    return d.get("meta", {}).get("count"), works


def s2_search(query: str, k: int) -> list:
    key = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
    headers = {"x-api-key": key} if key else {}
    url = S2 + "?" + urllib.parse.urlencode(
        {"query": query, "limit": k, "fields": "title,year,citationCount,url"})
    try:
        d = _get(url, headers)
        return [{"title": x.get("title"), "year": x.get("year"),
                 "cited_by": x.get("citationCount"), "url": x.get("url")}
                for x in d.get("data", [])]
    except Exception as e:  # 429 without key, etc.
        return [{"_error": f"Semantic Scholar unavailable ({type(e).__name__}); set SEMANTIC_SCHOLAR_API_KEY"}]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--query", required=True)
    ap.add_argument("--k", type=int, default=8)
    ap.add_argument("--since", type=int, default=None)
    ap.add_argument("--with-s2", action="store_true", help="also query Semantic Scholar (needs key for reliability)")
    ap.add_argument("--output", type=Path, default=None)
    a = ap.parse_args()

    total, works = openalex_search(a.query, a.k, a.since)
    assessment = ("prior_art_likely" if (total or 0) >= 5
                  else "sparse_prior_art" if total else "none_found")
    result = {
        "query": a.query,
        "source": "OpenAlex" + (" + Semantic Scholar" if a.with_s2 else ""),
        "total_matches": total,
        "assessment_heuristic": assessment,
        "note": "Retrieval only — NOT a novelty verdict. Read these works before asserting any 'first/novel' claim (Source Gate).",
        "related_works": works,
    }
    if a.with_s2:
        result["semantic_scholar"] = s2_search(a.query, a.k)
    out = json.dumps(result, ensure_ascii=False, indent=2)
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(out)
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
