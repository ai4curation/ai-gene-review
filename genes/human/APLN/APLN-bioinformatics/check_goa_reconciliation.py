"""Reconcile every GOA row for APLN against exactly one entry in the review YAML.

The review's ``existing_annotations`` are seeded deterministically from ``APLN-goa.tsv``,
so any drift introduced while editing (a dropped row, a duplicated row, a hand-edited
``supporting_entities`` list) is a silent defect. This script re-derives the join key
from both sides and fails loudly on any mismatch.

Join key: (GO id, evidence code, reference, normalized WITH/FROM tuple). WITH/FROM is
part of the key because GOA emits rows that differ only in that column, and the seeder
keeps them as separate YAML entries.

    uv run python check_goa_reconciliation.py
"""

from __future__ import annotations

import collections
import csv
import pathlib
import sys

import yaml

GENE_DIR = pathlib.Path(__file__).resolve().parent.parent
GOA = GENE_DIR / "APLN-goa.tsv"
REVIEW = GENE_DIR / "APLN-ai-review.yaml"


def norm_with(raw: str) -> tuple[str, ...]:
    """Split WITH/FROM on '|', strip, drop empties, dedupe, keep order."""
    seen: list[str] = []
    for tok in (raw or "").split("|"):
        tok = tok.strip()
        if tok and tok not in seen:
            seen.append(tok)
    return tuple(seen)


def goa_keys() -> list[tuple]:
    keys = []
    with GOA.open(newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            keys.append(
                (
                    row["GO TERM"],
                    row["GO EVIDENCE CODE"],
                    row["REFERENCE"],
                    norm_with(row["WITH/FROM"]),
                )
            )
    return keys


def yaml_keys() -> tuple[list[tuple], list[dict]]:
    doc = yaml.safe_load(REVIEW.read_text())
    keys, new_rows = [], []
    for ann in doc["existing_annotations"]:
        if ann.get("review", {}).get("action") == "NEW":
            new_rows.append(ann)
            continue
        keys.append(
            (
                ann["term"]["id"],
                ann["evidence_type"],
                ann["original_reference_id"],
                tuple(ann.get("supporting_entities") or []),
            )
        )
    return keys, new_rows


def main() -> int:
    g = goa_keys()
    y, new_rows = yaml_keys()
    gc, yc = collections.Counter(g), collections.Counter(y)

    problems = []
    for key, n in (gc - yc).items():
        problems.append(f"  GOA row absent from (or under-represented in) YAML x{n}: {key}")
    for key, n in (yc - gc).items():
        problems.append(f"  YAML entry with no matching GOA row x{n}: {key}")
    for key, n in yc.items():
        if n > 1 and gc[key] == n:
            # legitimate only if GOA really does carry the row n times
            continue

    print(f"GOA rows                 : {len(g)}")
    print(f"YAML reviewed entries    : {len(y)}")
    print(f"YAML NEW entries (extra) : {len(new_rows)}")
    for ann in new_rows:
        print(f"    NEW {ann['term']['id']} {ann['term']['label']} ({ann['evidence_type']}, {ann['original_reference_id']})")
    print()
    if problems:
        print("RECONCILIATION FAILED")
        print("\n".join(problems))
        return 1
    print("RECONCILIATION OK: every GOA row maps to exactly one YAML entry, "
          "including identical normalized supporting_entities.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
