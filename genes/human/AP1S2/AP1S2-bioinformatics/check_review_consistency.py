"""Consistency checks between the AP1S2 GOA tsv and the AP1S2 review YAML.

Three checks, all of which must pass:

1. GOA-row <-> YAML-entry reconciliation. Every row of AP1S2-goa.tsv maps to exactly one
   existing_annotations entry with the same term id, evidence code, reference and an
   identical normalized supporting_entities list, and every non-NEW YAML entry maps back.
2. source_entities are drawn from the row's own supporting_entities. No source_id in a
   propagation_review may be absent from that row's supporting_entities list.
3. propagation_review coverage. Every IBA row, and every ISS/ISO/IEA/IC row that has
   supporting_entities, carries a propagation_review with a root_cause and at least one
   source entity.

Run from the repository root:
    uv run python genes/human/AP1S2/AP1S2-bioinformatics/check_review_consistency.py
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[4]
GOA = ROOT / "genes/human/AP1S2/AP1S2-goa.tsv"
REVIEW = ROOT / "genes/human/AP1S2/AP1S2-ai-review.yaml"
NEEDS_PROPAGATION = {"IBA", "ISS", "ISO", "IEA", "IC"}


def split_with_from(value: str) -> list[str]:
    """Reproduce the seeder's WITH/FROM normalization: split on '|', strip, dedupe, keep order."""
    seen: set[str] = set()
    out: list[str] = []
    for item in (x.strip() for x in value.split("|")) if value.strip() else []:
        if item and item not in seen:
            seen.add(item)
            out.append(item)
    return out


def goa_rows() -> list[tuple]:
    rows = []
    with GOA.open() as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            rows.append((
                r["GO TERM"],
                r["GO EVIDENCE CODE"],
                r["REFERENCE"],
                tuple(split_with_from(r["WITH/FROM"])),
            ))
    return rows


def main() -> int:
    review = yaml.safe_load(REVIEW.read_text())
    annotations = review["existing_annotations"]
    failures: list[str] = []

    # --- check 1: reconciliation -------------------------------------------------
    goa = Counter(goa_rows())
    yaml_keys = Counter()
    new_rows = []
    for a in annotations:
        key = (
            a["term"]["id"],
            a["evidence_type"],
            a["original_reference_id"],
            tuple(a.get("supporting_entities") or []),
        )
        if a["review"]["action"] == "NEW":
            new_rows.append(key)
        else:
            yaml_keys[key] += 1

    only_goa = goa - yaml_keys
    only_yaml = yaml_keys - goa
    for key, n in sorted(only_goa.items()):
        failures.append(f"GOA row with no matching YAML entry (x{n}): {key}")
    for key, n in sorted(only_yaml.items()):
        failures.append(f"YAML entry with no matching GOA row (x{n}): {key}")
    print(f"[1] GOA rows: {sum(goa.values())}; reviewed YAML entries: {sum(yaml_keys.values())}; "
          f"NEW entries: {len(new_rows)}")

    # --- check 2: source_entities are a subset of supporting_entities ------------
    checked = 0
    for a in annotations:
        pr = a["review"].get("propagation_review")
        if not pr:
            continue
        declared = set(a.get("supporting_entities") or [])
        for se in pr.get("source_entities") or []:
            checked += 1
            if se["source_id"] not in declared:
                failures.append(
                    f"{a['term']['id']} {a['evidence_type']} {a['original_reference_id']}: "
                    f"source_id {se['source_id']} is not in this row's supporting_entities"
                )
    print(f"[2] source_entities checked against their row's supporting_entities: {checked}")

    # --- check 3: propagation_review coverage ------------------------------------
    required = 0
    for a in annotations:
        ev = a["evidence_type"]
        ents = a.get("supporting_entities") or []
        if ev == "IBA" or (ev in NEEDS_PROPAGATION and ents):
            required += 1
            pr = a["review"].get("propagation_review")
            label = f"{a['term']['id']} {ev} {a['original_reference_id']}"
            if not pr:
                failures.append(f"{label}: missing propagation_review")
            elif not pr.get("root_cause"):
                failures.append(f"{label}: propagation_review has no root_cause")
            elif not pr.get("source_entities"):
                failures.append(f"{label}: propagation_review has no source_entities")
    print(f"[3] rows requiring a propagation_review: {required}")

    if failures:
        print(f"\nFAILURES ({len(failures)}):")
        for f in failures:
            print("  -", f)
        return 1
    print("\nall checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
