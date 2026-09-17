#!/usr/bin/env python3
"""Repo-wide report on `file:` supporting_text quotes.

The per-gene check runs inside `ai-gene-review validate`; this script is the
whole-corpus view, for triaging the backlog. It uses the same matching logic
(`ai_gene_review.validation.file_supporting_text`), so its verdicts and the
validator's always agree.

    uv run --no-dev python scripts/check_file_supporting_text.py

Writes reports/file_supporting_text_report.tsv and prints a summary.

Two kinds of finding:
  narration     -- the "quote" describes the source instead of quoting it
                   ("Falcon report summarizes ..."). Cannot be verbatim by
                   construction; an ERROR in the validator.
  not_verbatim  -- the words are not in the cited file. Usually real paraphrase,
                   sometimes a quote that elides non-contiguous text without
                   marking it with an ellipsis. A WARNING in the validator.
"""

from __future__ import annotations

import csv
import glob
import sys
from collections import Counter
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ai_gene_review.validation.file_supporting_text import (  # noqa: E402
    check_file_supporting_text,
)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    out_dir = root / "reports"
    out_dir.mkdir(exist_ok=True)
    report = out_dir / "file_supporting_text_report.tsv"

    checked = 0
    kinds: Counter[str] = Counter()
    per_gene: Counter[str] = Counter()
    rows = []

    files = sorted(glob.glob(str(root / "genes" / "*" / "*" / "*-ai-review.yaml")))
    for f in files:
        path = Path(f)
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        res = check_file_supporting_text(data, root)
        checked += res.checked
        for issue in res.issues:
            kinds[issue.kind] += 1
            per_gene[path.parent.name] += 1
            rows.append(
                {
                    "organism": path.parent.parent.name,
                    "gene": path.parent.name,
                    "kind": issue.kind,
                    "reference_id": issue.reference_id,
                    "path": issue.path,
                    "supporting_text": " ".join(issue.supporting_text.split())[:300],
                }
            )

    with report.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(
            fh,
            fieldnames=[
                "organism", "gene", "kind", "reference_id", "path", "supporting_text",
            ],
            delimiter="\t",
        )
        w.writeheader()
        w.writerows(rows)

    total_issues = sum(kinds.values())
    clean = 100 * (checked - total_issues) / checked if checked else 100.0
    print(f"review files scanned   : {len(files)}")
    print(f"file: quotes checked   : {checked}")
    print(f"clean                  : {clean:.1f}%")
    print(f"issues by kind         : {dict(kinds)}")
    print(f"genes affected         : {len(per_gene)}")
    print(f"report                 : {report.relative_to(root)}")
    if per_gene:
        worst = ", ".join(f"{g} ({n})" for g, n in per_gene.most_common(5))
        print(f"most affected genes    : {worst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
