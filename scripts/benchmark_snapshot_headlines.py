#!/usr/bin/env python3
"""Print the headline numbers of the snapshot-derived benchmark reports, one per line.

``just refresh-benchmark-snapshot`` prints this before and after regenerating, and
diffs the two, so a snapshot bump shows exactly which reported numbers moved.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

import typer

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS = {
    "bioreason": "projects/BIOREASON_COMPARISON/benchmark-metrics.json",
    "protnlm": "projects/PROTNLM_EVALUATION/benchmark-summary.json",
    "second_review": "projects/BIOREASON_COMPARISON/second-review-agreement.json",
}
CAFA_DIR = "projects/BIOREASON_COMPARISON/cafa-style"
INCORRECT = {"NPI", "PLI", "REP"}
SKIPPED_KEYS = {
    "review_snapshot",
    "narrative_reviews",
    "zero_go_prediction_reviews",
    # second-review-agreement.json provenance strings, not numbers
    "blinding",
    "sampling",
    "sample_salt",
}


def flatten(value: Any, prefix: str) -> list[str]:
    """Flatten nested numbers into sorted ``dotted.key: value`` lines.

    >>> flatten({"b": {"n": 2}, "a": 1, "review_snapshot": {"commit": "x"}}, "r")
    ['r.a: 1', 'r.b.n: 2']
    >>> flatten([{"cohort": "fly", "records": 3}], "c")
    ['c.fly.records: 3']
    >>> flatten([{"n": 1}, 7], "x")
    ['x.0.n: 1', 'x.1: 7']
    """
    if isinstance(value, dict):
        return sorted(
            line
            for key, item in value.items()
            if key not in SKIPPED_KEYS
            for line in flatten(item, f"{prefix}.{key}")
        )
    if isinstance(value, list):
        return sorted(
            line
            for index, item in enumerate(value)
            for line in (
                flatten(
                    {k: v for k, v in item.items() if k != "cohort"},
                    f"{prefix}.{item['cohort']}",
                )
                if isinstance(item, dict) and "cohort" in item
                else flatten(item, f"{prefix}.{index}")
            )
        )
    return [f"{prefix}: {value}"]


def _read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def cafa_headlines(repo_root: Path) -> list[str]:
    """CAFA-style numbers quoted in the manuscript and supplement Table S7.

    Only the rows that are published are listed: the HF-catalogue NPI/PLI/REP
    GOA-overlap counts and the propagated all-aspect scores against all GOA.
    """
    cafa = repo_root / CAFA_DIR
    incorrect = [
        row
        for row in _read_csv(cafa / "argo139_prediction_goa_overlap.csv")
        if row["source_group"] == "hf_catalogue" and row["assessment"] in INCORRECT
    ]
    lines = [
        f"cafa.hf_incorrect.n: {len(incorrect)}",
        f"cafa.hf_incorrect.exact_in_goa: {sum(r['exact_in_goa_all'] == 'True' for r in incorrect)}",
        "cafa.hf_incorrect.propagated_overlap: "
        f"{sum(r['closure_intersects_goa_all'] == 'True' for r in incorrect)}",
    ]
    for row in _read_csv(cafa / "argo139_cafa_style_summary.csv"):
        if (row["reference_set"], row["term_mode"], row["aspect"]) != (
            "goa_all",
            "raw",
            "all_aspects",
        ):
            continue
        prefix = f"cafa.{row['source_group']}"
        lines += [
            f"{prefix}.n_ref_direct: {row['n_ref_direct']}",
            f"{prefix}.closure_precision: {float(row['closure_precision']):.3f}",
            f"{prefix}.closure_recall: {float(row['closure_recall']):.3f}",
            f"{prefix}.closure_f1: {float(row['closure_f1']):.3f}",
        ]
    return sorted(lines)


def headlines(repo_root: Path) -> list[str]:
    """Headline lines for every snapshot-derived report under ``repo_root``."""
    lines: list[str] = []
    for name, path in REPORTS.items():
        lines += flatten(json.loads((repo_root / path).read_text(encoding="utf-8")), name)
    return lines + cafa_headlines(repo_root)


def main(repo_root: Path = typer.Option(REPO_ROOT, help="Repository root")) -> None:
    """Print the headline numbers."""
    for line in headlines(repo_root):
        typer.echo(line)


if __name__ == "__main__":
    typer.run(main)
