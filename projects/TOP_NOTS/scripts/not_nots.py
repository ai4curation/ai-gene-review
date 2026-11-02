#!/usr/bin/env python3
"""List existing NOT (negated) GO annotations in gene reviews and how reviewers judged them.

The "NOT_NOTs" view of TOP_NOTS: TOP_NOTS mines REMOVE decisions for candidate new NOT
annotations; this script goes the other way and finds existing NOT annotations that
reviewers overturned (REMOVE, MARK_AS_OVER_ANNOTATED) or could not settle (UNDECIDED).

Usage (from repo root):
    uv run python projects/TOP_NOTS/scripts/not_nots.py

Outputs:
    projects/TOP_NOTS/not_nots.tsv     one row per negated annotation
    stdout                             action counts
"""

import csv
import subprocess
from collections import Counter
from pathlib import Path

import yaml

OUT = Path("projects/TOP_NOTS/not_nots.tsv")


def files_with_negations():
    # Pre-filter with grep: parsing every review YAML is slow.
    res = subprocess.run(
        ["grep", "-rl", "--include=*-ai-review.yaml", "negated: true", "genes"],
        capture_output=True, text=True,
    )
    return sorted(Path(p) for p in res.stdout.split())


def main():
    rows = []
    for f in files_with_negations():
        doc = yaml.safe_load(f.read_text())
        if not isinstance(doc, dict):
            continue
        for ann in doc.get("existing_annotations") or []:
            if not ann.get("negated"):
                continue
            term = ann.get("term") or {}
            review = ann.get("review") or {}
            rows.append({
                "organism": f.parts[1],
                "gene": f.parts[2],
                "go_id": term.get("id", ""),
                "go_label": term.get("label", ""),
                "evidence_type": ann.get("evidence_type", ""),
                "reference": ann.get("original_reference_id", ""),
                "action": review.get("action", "") or "",
                "summary": " ".join(str(review.get("summary", "")).split()),
            })
    with OUT.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    counts = Counter(r["action"] for r in rows)
    print(f"{len(rows)} negated annotations in {len({(r['organism'], r['gene']) for r in rows})} reviews")
    for action, n in counts.most_common():
        print(f"  {action or '(none)'}: {n}")


if __name__ == "__main__":
    main()
