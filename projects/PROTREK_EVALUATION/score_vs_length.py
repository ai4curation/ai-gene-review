#!/usr/bin/env python3
"""Relate ProTrek top-1 score to query length across both cohorts.

Motivated by the observation that the lowest-scoring ARGO139 genes are all very
long. The result is that length alone is a poor predictor: the correlation is
weak, and long proteins built from many copies of one domain (NOTCH1, Dscam1)
score normally while large multi-domain proteins with no dominant repeat
(LRRK2, TOR1, BRCA2, HTT) fall below the abstention threshold.

Usage:
  uv run python projects/PROTREK_EVALUATION/score_vs_length.py \
      --out projects/PROTREK_EVALUATION/score_vs_length.json
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from pathlib import Path

HERE = Path(__file__).parent
COHORTS = ("argo50", "argo139")
BINS = [(0, 200), (200, 400), (400, 700), (700, 1200), (1200, 4000)]


def spearman(pairs: list[tuple[float, float]]) -> float:
    n = len(pairs)

    def ranks(vals: list[float]) -> list[float]:
        order = sorted(range(n), key=lambda i: vals[i])
        out = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and vals[order[j + 1]] == vals[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                out[order[k]] = avg
            i = j + 1
        return out

    rx, ry = ranks([p[0] for p in pairs]), ranks([p[1] for p in pairs])
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    return num / den if den else float("nan")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()

    rows = []
    for cohort in COHORTS:
        seqs = {r["accession"]: r for r in
                csv.DictReader((HERE / f"{cohort}_sequences.tsv").open(), delimiter="\t")}
        for r in csv.DictReader((HERE / f"{cohort}_protrek_go_calls.csv").open()):
            if r["rank"] != "1" or r["accession"] not in seqs:
                continue
            q = seqs[r["accession"]]
            rows.append({
                "cohort": cohort,
                "name": f"{q['species_dir']}/{q.get('symbol') or q['accession']}",
                "length": int(q["length"]),
                "top1_score": float(r["protrek_score"]),
            })

    pairs = [(r["length"], r["top1_score"]) for r in rows]
    by_bin = {}
    for lo, hi in BINS:
        vals = [s for l, s in pairs if lo <= l < hi]
        if vals:
            by_bin[f"{lo}-{hi}"] = {"n": len(vals),
                                    "median_top1": round(statistics.median(vals), 2),
                                    "mean_top1": round(statistics.mean(vals), 2)}

    lowest = sorted(rows, key=lambda r: r["top1_score"])[:10]
    longest = sorted(rows, key=lambda r: -r["length"])[:10]
    summary = {
        "n_queries": len(rows),
        "spearman_length_vs_top1_score": round(spearman(pairs), 3),
        "by_length_bin": by_bin,
        "lowest_top1_scores": [{k: r[k] for k in ("name", "length", "top1_score")} for r in lowest],
        "longest_queries": [{k: r[k] for k in ("name", "length", "top1_score")} for r in longest],
    }
    args.out.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
