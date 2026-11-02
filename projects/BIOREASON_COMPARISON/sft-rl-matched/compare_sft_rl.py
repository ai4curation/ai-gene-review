#!/usr/bin/env python3
"""Matched SFT-vs-RL comparison of BioReason-Pro Functional Summaries on the
ARGO139 genes whose SFT narrative exists in the HF ``protein_catalogue``.

Inputs (all committed):
  sft-rl-matched-ratings.csv   rater-B scores for the SFT summary and a same-rater
                               re-score of the RL summary for each matched gene
  ../benchmark-genes.csv       first-rater (rater-A) RL scores and strata

Usage (from repo root):
    uv run python projects/BIOREASON_COMPARISON/sft-rl-matched/compare_sft_rl.py

Writes ``sft-rl-matched-summary.json`` and prints Markdown tables. Nothing is
hard-coded; all numbers are computed from the two CSVs.

Three comparisons are reported, in order of interpretability:
  1. same_rater: SFT vs RL, both scored by rater B (the primary matched result)
  2. rater_calibration: rater-B RL re-score vs rater-A RL score (same text)
  3. cross_rater: SFT (rater B) vs RL (rater A) -- confounded by rater; shown only
     to quantify how misleading an unmatched comparison would be.
"""

import csv
import json
from collections import Counter
from pathlib import Path
from statistics import mean

from scipy.stats import wilcoxon

HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent


def qwk(a, b, lo=1, hi=5):
    """Quadratic-weighted Cohen's kappa for two integer rating lists."""
    k = hi - lo + 1
    n = len(a)
    obs = [[0] * k for _ in range(k)]
    for x, y in zip(a, b):
        obs[x - lo][y - lo] += 1
    ra = Counter(a)
    rb = Counter(b)
    num = den = 0.0
    for i in range(k):
        for j in range(k):
            w = (i - j) ** 2 / (k - 1) ** 2
            exp = ra.get(i + lo, 0) * rb.get(j + lo, 0) / n
            num += w * obs[i][j]
            den += w * exp
    return 1 - num / den if den else None


def load():
    first = {
        (r["organism"], r["gene"]): r
        for r in csv.DictReader(open(PROJECT / "benchmark-genes.csv"))
        if r["benchmark"] == "argo139_rl_narrative"
    }
    rows = []
    for r in csv.DictReader(open(HERE / "sft-rl-matched-ratings.csv")):
        a = first[(r["species"], r["gene"])]
        rows.append(
            {
                "species": r["species"],
                "gene": r["gene"],
                "sft_c": int(r["sft_correctness"]),
                "sft_k": int(r["sft_completeness"]),
                "rlB_c": int(r["rl_rescore_correctness"]),
                "rlB_k": int(r["rl_rescore_completeness"]),
                "rlA_c": int(a["correctness"]),
                "rlA_k": int(a["completeness"]),
                "seen": r["first_rater_rl_seen_before_rescore"] == "true",
                "performance_included": a["performance_included"] == "true",
                "input_quality": a["input_quality"],
                "reference_status": a["reference_status"],
            }
        )
    return rows


def paired(rows, x, y):
    xs = [r[x] for r in rows]
    ys = [r[y] for r in rows]
    d = [p - q for p, q in zip(xs, ys)]
    p = wilcoxon(xs, ys).pvalue if any(d) else None
    return {
        "n": len(rows),
        "mean_x": round(mean(xs), 3),
        "mean_y": round(mean(ys), 3),
        "mean_diff_x_minus_y": round(mean(d), 3),
        "x_higher": sum(v > 0 for v in d),
        "y_higher": sum(v < 0 for v in d),
        "tied": sum(v == 0 for v in d),
        "exact_agreement": sum(v == 0 for v in d),
        "within_one": sum(abs(v) <= 1 for v in d),
        "quadratic_weighted_kappa": round(qwk(xs, ys), 3),
        "wilcoxon_p": None if p is None else float(f"{p:.3g}"),
        "x_distribution": {str(k): v for k, v in sorted(Counter(xs).items())},
        "y_distribution": {str(k): v for k, v in sorted(Counter(ys).items())},
    }


def block(rows, x_c, y_c, x_k, y_k):
    return {"correctness": paired(rows, x_c, y_c), "completeness": paired(rows, x_k, y_k)}


def main():
    rows = [r for r in load() if r["performance_included"]]
    unseen = [r for r in rows if not r["seen"]]
    out = {
        "n_matched_performance_genes": len(rows),
        "n_truncated_inputs_in_matched_set": sum(r["input_quality"] != "FULL_LENGTH_MATCH" for r in rows),
        "n_first_rater_scores_seen_before_rescore": sum(r["seen"] for r in rows),
        "same_rater": {
            "note": "x = SFT (rater B), y = RL (rater B)",
            "all": block(rows, "sft_c", "rlB_c", "sft_k", "rlB_k"),
            "by_reference_status": {
                st: block([r for r in rows if r["reference_status"] == st], "sft_c", "rlB_c", "sft_k", "rlB_k")
                for st in sorted({r["reference_status"] for r in rows})
            },
        },
        "rater_calibration": {
            "note": "x = RL rater B re-score, y = RL rater A (first rater); same RL text",
            "all": block(rows, "rlB_c", "rlA_c", "rlB_k", "rlA_k"),
            "unseen_only": block(unseen, "rlB_c", "rlA_c", "rlB_k", "rlA_k"),
        },
        "cross_rater_confounded": {
            "note": "x = SFT (rater B), y = RL (rater A); rater and model are confounded",
            "all": block(rows, "sft_c", "rlA_c", "sft_k", "rlA_k"),
        },
    }
    (HERE / "sft-rl-matched-summary.json").write_text(json.dumps(out, indent=2) + "\n")

    def line(name, b):
        c, k = b["correctness"], b["completeness"]
        return (
            f"| {name} | {c['n']} | {c['mean_x']:.2f} | {c['mean_y']:.2f} | "
            f"{c['x_higher']}/{c['y_higher']}/{c['tied']} | {c['wilcoxon_p']} | "
            f"{k['mean_x']:.2f} | {k['mean_y']:.2f} | {k['x_higher']}/{k['y_higher']}/{k['tied']} | {k['wilcoxon_p']} |"
        )

    print("| Comparison (x vs y) | n | x corr | y corr | x>y / y>x / tie | p | x compl | y compl | x>y / y>x / tie | p |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    print(line("SFT(B) vs RL(B), all", out["same_rater"]["all"]))
    for st, b in out["same_rater"]["by_reference_status"].items():
        print(line(f"SFT(B) vs RL(B), reference {st}", b))
    print(line("RL(B) vs RL(A), all", out["rater_calibration"]["all"]))
    print(line("RL(B) vs RL(A), unseen", out["rater_calibration"]["unseen_only"]))
    print(line("SFT(B) vs RL(A) [confounded]", out["cross_rater_confounded"]["all"]))
    for name, blk in [("RL(B) vs RL(A)", out["rater_calibration"]["all"]),
                      ("RL(B) vs RL(A) unseen", out["rater_calibration"]["unseen_only"])]:
        for ax in ("correctness", "completeness"):
            s = blk[ax]
            print(f"{name} {ax}: exact {s['exact_agreement']}/{s['n']}, within-1 {s['within_one']}/{s['n']}, QWK {s['quadratic_weighted_kappa']}")
    print({k: out[k] for k in list(out)[:3]})


if __name__ == "__main__":
    main()
