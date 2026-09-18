"""Assert the review covers every GOA row exactly once, and name the extras.

CLAUDE.md requires an `existing_annotations` entry for every line in the GOA
TSV, and the `fetch-gene` stub is known not to satisfy its own rule: it collapses
distinct `GO:0005515` partners and same-term rows from different assigners. So
the count has to be reconciled against the **TSV**, never against what the stub
produced.

The key is `(GO id, evidence code, reference, WITH/FROM)` rather than just the GO
id, so the two `GO:0005515` IPI rows on the same paper with different partners
stay distinct - exactly the pair most at risk of being merged.

This found a real defect on this gene: a `GO:0005886` IEA row silently lost its
`ARBA:ARBA00027801` token during a file rewrite. Reading the file did not catch
it; only the row-by-row key comparison did.

Run: uv run python reconcile_goa.py
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).parent
GENE_DIR = HERE.parent
GOA = GENE_DIR / "AHNAK2-goa.tsv"
REVIEW = GENE_DIR / "AHNAK2-ai-review.yaml"


def main() -> int:
    for p in (GOA, REVIEW):
        if not p.exists():
            raise SystemExit(f"missing {p}; run `just fetch-gene human AHNAK2` first")

    with GOA.open() as fh:
        goa = list(csv.DictReader(fh, delimiter="\t"))
    doc = yaml.safe_load(REVIEW.read_text())
    anns = doc["existing_annotations"]

    goa_keys = Counter(
        (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"],
         tuple(sorted(t for t in r["WITH/FROM"].split("|") if t)))
        for r in goa
    )
    reviewed = [a for a in anns if (a.get("review") or {}).get("action") != "NEW"]
    new_rows = [a for a in anns if (a.get("review") or {}).get("action") == "NEW"]
    rev_keys = Counter(
        (a["term"]["id"], a["evidence_type"], a["original_reference_id"],
         tuple(sorted(a.get("supporting_entities") or [])))
        for a in reviewed
    )

    print(f"GOA data rows       : {len(goa)}")
    print(f"review entries      : {len(anns)}")
    print(f"  reviewed GOA rows : {len(reviewed)}")
    print(f"  NEW proposals     : {len(new_rows)}")
    print()

    problems = []
    for k, n in (goa_keys - rev_keys).items():
        problems.append(f"GOA row NOT covered ({n}x): {k}")
    for k, n in (rev_keys - goa_keys).items():
        problems.append(f"review entry not in GOA ({n}x): {k}")
    if len(anns) != len(goa) + len(new_rows):
        problems.append(
            f"arithmetic: {len(anns)} entries != {len(goa)} GOA rows + "
            f"{len(new_rows)} NEW - derive the expected number independently "
            "rather than finding a story that makes the gap acceptable"
        )

    for a in new_rows:
        print(f"NEW: {a['term']['id']} {a['term']['label']} "
              f"[{a['evidence_type']}] {a['original_reference_id']}")
    print()
    for p in problems:
        print("  PROBLEM:", p)
    print("RECONCILES EXACTLY" if not problems else f"{len(problems)} problem(s)")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
