#!/usr/bin/env python3
"""Print the headline numbers of the snapshot-derived benchmark reports, one per line.

``just refresh-benchmark-snapshot`` prints this before and after regenerating, and
diffs the two, so a snapshot bump shows exactly which reported numbers moved.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import typer

REPO_ROOT = Path(__file__).resolve().parents[1]
REPORTS = {
    "bioreason": "projects/BIOREASON_COMPARISON/benchmark-metrics.json",
    "protnlm": "projects/PROTNLM_EVALUATION/benchmark-summary.json",
}
SKIPPED_KEYS = {"review_snapshot", "narrative_reviews", "zero_go_prediction_reviews"}


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


def headlines(repo_root: Path) -> list[str]:
    """Headline lines for every snapshot-derived report under ``repo_root``."""
    lines: list[str] = []
    for name, path in REPORTS.items():
        lines += flatten(json.loads((repo_root / path).read_text(encoding="utf-8")), name)
    return lines


def main(repo_root: Path = typer.Option(REPO_ROOT, help="Repository root")) -> None:
    """Print the headline numbers."""
    for line in headlines(repo_root):
        typer.echo(line)


if __name__ == "__main__":
    typer.run(main)
