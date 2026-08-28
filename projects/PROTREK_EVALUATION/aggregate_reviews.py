#!/usr/bin/env python3
"""Aggregate the curated ProTrek prediction reviews into summary statistics.

Reads every ``*-protrek-predictions-review.yaml`` under genes/, cross-references
each assessed prediction with its ProTrek rank and score from the raw retrieval
output, and reports assessment counts, confidence scores, error types, and the
relationship between ProTrek score and assessment outcome.

No numbers are hard-coded: everything is recomputed from the committed files.

Usage:
  uv run python projects/PROTREK_EVALUATION/aggregate_reviews.py \
      --out projects/PROTREK_EVALUATION/argo50_assessment_summary.json
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import statistics
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CALLS = Path(__file__).parent / "argo50_protrek_go_calls.csv"
CS = {"COR": 2, "CNN": 2, "LSP": 2, "UNC": 1, "PLI": 0, "NPI": 0, "REP": 0}
ORDER = ["COR", "CNN", "LSP", "UNC", "PLI", "NPI", "REP"]


def score_thresholds(scored: list[tuple[float, int]]) -> dict:
    """Precision of the assessed predictions above and below ProTrek score cutoffs.

    "Concordant" counts CS=2 (COR/CNN/LSP); the denominator at each cutoff is
    every assessed prediction at or above it, so this measures what a user would
    get by accepting all hits above a threshold.
    """
    out = {}
    for cut in (10, 12, 14, 15, 16, 18):
        above = [cs for sc, cs in scored if sc >= cut]
        below = [cs for sc, cs in scored if sc < cut]
        out[f">={cut}"] = {
            "n": len(above),
            "concordant_pct": round(100 * sum(1 for c in above if c == 2) / len(above), 1) if above else None,
            "discordant_pct": round(100 * sum(1 for c in above if c == 0) / len(above), 1) if above else None,
        }
        out[f"<{cut}"] = {
            "n": len(below),
            "concordant_pct": round(100 * sum(1 for c in below if c == 2) / len(below), 1) if below else None,
            "discordant_pct": round(100 * sum(1 for c in below if c == 0) / len(below), 1) if below else None,
        }
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    calls = list(csv.DictReader(CALLS.open()))
    rank_by = {(r["accession"], r["pred_id"]): (int(r["rank"]), float(r["protrek_score"]),
                                                r["match_category"], r["aspect"])
               for r in calls if r["pred_id"]}

    files = sorted(glob.glob(str(ROOT / "genes/*/*/*-protrek-predictions-review.yaml")))
    scored: list[tuple[float, int]] = []
    counts = Counter()
    errors = Counter()
    per_protein = {}
    scores_by_cs: dict[int, list[float]] = defaultdict(list)
    by_match: dict[str, Counter] = defaultdict(Counter)
    by_aspect: dict[str, Counter] = defaultdict(Counter)
    by_rank: dict[int, Counter] = defaultdict(Counter)
    unmatched = []
    cs_values = []

    for path in files:
        data = yaml.safe_load(Path(path).read_text())
        acc = data["id"]
        local = Counter()
        for pred in data["predictions"]:
            a = pred["review"]["assessment"]
            counts[a] += 1
            local[a] += 1
            cs_values.append(CS[a])
            if pred["review"].get("error_type"):
                errors[pred["review"]["error_type"]] += 1
            key = (acc, pred["predicted_term"]["id"])
            if key in rank_by:
                rank, score, match, aspect = rank_by[key]
                scores_by_cs[CS[a]].append(score)
                scored.append((score, CS[a]))
                by_match[match][a] += 1
                by_aspect[aspect][a] += 1
                by_rank[rank][a] += 1
            else:
                unmatched.append(f"{acc}:{pred['predicted_term']['id']}")
        per_protein[acc] = dict(local)

    total = sum(counts.values())
    summary = {
        "n_proteins": len(files),
        "n_assessed_predictions": total,
        "assessments": {k: counts.get(k, 0) for k in ORDER if counts.get(k)},
        "assessment_pct": {k: round(100 * counts.get(k, 0) / total, 1) for k in ORDER if counts.get(k)},
        "mean_confidence_score": round(statistics.mean(cs_values), 3),
        "concordant_cs2": sum(counts[k] for k in ("COR", "CNN", "LSP")),
        "uncertain_cs1": counts.get("UNC", 0),
        "discordant_cs0": sum(counts[k] for k in ("PLI", "NPI", "REP")),
        "error_types": dict(errors.most_common()),
        "score_by_confidence": {
            str(cs): {"n": len(v), "median": round(statistics.median(v), 2),
                      "mean": round(statistics.mean(v), 2),
                      "min": round(min(v), 2), "max": round(max(v), 2)}
            for cs, v in sorted(scores_by_cs.items())
        },
        "score_thresholds": score_thresholds(scored),
        "by_goa_match_category": {k: dict(v.most_common()) for k, v in sorted(by_match.items())},
        "by_aspect": {k: dict(v.most_common()) for k, v in sorted(by_aspect.items())},
        "by_rank": {str(k): dict(v.most_common()) for k, v in sorted(by_rank.items())},
        "predictions_not_in_top5_calls": unmatched,
    }
    args.out.write_text(json.dumps({"summary": summary, "per_protein": per_protein}, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
