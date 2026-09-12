"""Analyze blinded second-rater agreement for the ARGO139 RL score audit."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any


PROJECT_DIR = Path(__file__).resolve().parent
REPO_ROOT = PROJECT_DIR.parents[1]
SAMPLE_SALT = "argo-audit-2026-07-11"
SCORE_RE = {
    "correctness": re.compile(r"Correctness\*\*:\s*([1-5])\s*/\s*5", re.I),
    "completeness": re.compile(r"Completeness\*\*:\s*([1-5])\s*/\s*5", re.I),
}


def average_ranks(values: list[int]) -> list[float]:
    order = sorted(range(len(values)), key=values.__getitem__)
    ranks = [0.0] * len(values)
    start = 0
    while start < len(order):
        end = start + 1
        while end < len(order) and values[order[end]] == values[order[start]]:
            end += 1
        rank = (start + 1 + end) / 2
        for index in order[start:end]:
            ranks[index] = rank
        start = end
    return ranks


def pearson(values_x: list[float], values_y: list[float]) -> float:
    mean_x = sum(values_x) / len(values_x)
    mean_y = sum(values_y) / len(values_y)
    numerator = sum(
        (value_x - mean_x) * (value_y - mean_y)
        for value_x, value_y in zip(values_x, values_y)
    )
    denominator = math.sqrt(
        sum((value - mean_x) ** 2 for value in values_x)
        * sum((value - mean_y) ** 2 for value in values_y)
    )
    return numerator / denominator if denominator else 0.0


def quadratic_weighted_kappa(first: list[int], second: list[int]) -> float:
    n = len(first)
    first_counts = Counter(first)
    second_counts = Counter(second)
    scale = 16.0
    observed = sum((a - b) ** 2 / scale for a, b in zip(first, second)) / n
    expected = sum(
        first_counts[a] * second_counts[b] * ((a - b) ** 2 / scale)
        for a in range(1, 6)
        for b in range(1, 6)
    ) / (n * n)
    return 1.0 - observed / expected if expected else 1.0


def read_first_ratings(repo_root: Path) -> list[dict[str, Any]]:
    quality_path = (
        repo_root / "projects" / "BIOREASON_COMPARISON" / "benchmark-quality.csv"
    )
    with quality_path.open(newline="", encoding="utf-8") as handle:
        included = {
            (row["organism"], row["gene"])
            for row in csv.DictReader(handle)
            if row["performance_included"].lower() == "true"
        }

    rows: list[dict[str, Any]] = []
    for organism, gene in sorted(included):
        path = repo_root / "genes" / organism / gene / f"{gene}-bioreason-rl-review.md"
        text = path.read_text(encoding="utf-8")
        rows.append(
            {
                "species": organism,
                "gene": gene,
                "correctness": int(SCORE_RE["correctness"].search(text).group(1)),
                "completeness": int(SCORE_RE["completeness"].search(text).group(1)),
            }
        )
    return rows


def expected_sample(first_ratings: list[dict[str, Any]]) -> list[tuple[str, str]]:
    selected: list[tuple[str, str]] = []
    for score in range(1, 6):
        stratum = [row for row in first_ratings if row["correctness"] == score]
        stratum.sort(
            key=lambda row: hashlib.sha256(
                f"{SAMPLE_SALT}:{row['species']}/{row['gene']}".encode()
            ).hexdigest()
        )
        selected.extend((row["species"], row["gene"]) for row in stratum[:4])
    return selected


def axis_summary(first: list[int], second: list[int]) -> dict[str, Any]:
    return {
        "exact_agreement": round(sum(a == b for a, b in zip(first, second)) / len(first), 6),
        "within_one_agreement": round(
            sum(abs(a - b) <= 1 for a, b in zip(first, second)) / len(first), 6
        ),
        "mean_absolute_error": round(
            sum(abs(a - b) for a, b in zip(first, second)) / len(first), 6
        ),
        "quadratic_weighted_kappa": round(quadratic_weighted_kappa(first, second), 6),
        "pearson": round(pearson(first, second), 6),
        "spearman": round(
            pearson(average_ranks(first), average_ranks(second)), 6
        ),
        "first_mean": round(sum(first) / len(first), 6),
        "second_mean": round(sum(second) / len(second), 6),
        "first_distribution": dict(sorted(Counter(first).items())),
        "second_distribution": dict(sorted(Counter(second).items())),
    }


def analyze(
    repo_root: Path = REPO_ROOT,
    ratings_path: Path | None = None,
) -> dict[str, Any]:
    ratings_path = ratings_path or (
        repo_root
        / "projects"
        / "BIOREASON_COMPARISON"
        / "second-review-ratings.csv"
    )
    with ratings_path.open(newline="", encoding="utf-8") as handle:
        second = list(csv.DictReader(handle))

    first = read_first_ratings(repo_root)
    expected = expected_sample(first)
    observed = [(row["species"], row["gene"]) for row in second]
    if observed != expected:
        raise ValueError(
            "Second-review sample no longer matches the deterministic stratified sample"
        )

    first_by_key = {(row["species"], row["gene"]): row for row in first}
    result: dict[str, Any] = {
        "n": len(second),
        "sample_salt": SAMPLE_SALT,
        "sampling": "four SHA-256-selected genes per first-rater correctness stratum",
        "blinding": "second rater saw raw RL export and local AIGR reference only",
    }
    for axis in ("correctness", "completeness"):
        first_values = [int(first_by_key[key][axis]) for key in observed]
        second_values = [int(row[axis]) for row in second]
        result[axis] = axis_summary(first_values, second_values)
    result["both_axes_exact_agreement"] = round(
        sum(
            int(first_by_key[key]["correctness"]) == int(row["correctness"])
            and int(first_by_key[key]["completeness"]) == int(row["completeness"])
            for key, row in zip(observed, second)
        )
        / len(second),
        6,
    )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path, default=PROJECT_DIR / "second-review-agreement.json"
    )
    args = parser.parse_args()
    result = analyze()
    args.output.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
