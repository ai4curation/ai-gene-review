"""Reconcile every GOA row for APOOL against exactly one reviewed YAML annotation.

Checks, in both directions:

* each GOA row (term id, evidence code, reference, qualifier, normalized WITH/FROM) matches
  exactly one ``existing_annotations`` entry, and vice versa;
* ``supporting_entities`` in the YAML is identical, as an ordered de-duplicated list, to
  the GOA WITH/FROM column split on ``|``;
* every non-NEW entry carries a review with an action that is not PENDING;
* every IBA row, and every ISS/ISO/IEA/IC row that has ``supporting_entities``, carries a
  ``propagation_review`` whose ``source_entities`` source_ids are exactly the row's
  ``supporting_entities`` (this is what stops the two lists drifting apart by hand-typing);
* counts of each action are printed, so no number in the review or PR body has to be
  asserted rather than counted.

Exits non-zero on any failure.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
GOA_TSV = GENE_DIR / "APOOL-goa.tsv"
REVIEW_YAML = GENE_DIR / "APOOL-ai-review.yaml"

PROPAGATION_REQUIRED_CODES = {"IBA", "ISS", "ISO", "IEA", "IC"}


def normalize_with_from(raw: str) -> list[str]:
    seen: list[str] = []
    for token in (raw or "").split("|"):
        token = token.strip()
        if token and token not in seen:
            seen.append(token)
    return seen


def goa_rows() -> list[tuple]:
    rows = []
    with GOA_TSV.open() as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            rows.append(
                (
                    row["GO TERM"],
                    row["GO EVIDENCE CODE"],
                    row["REFERENCE"],
                    row["QUALIFIER"],
                    tuple(normalize_with_from(row["WITH/FROM"])),
                )
            )
    return rows


def yaml_rows(doc: dict) -> list[tuple]:
    rows = []
    for entry in doc["existing_annotations"]:
        if entry["review"]["action"] == "NEW":
            continue
        rows.append(
            (
                entry["term"]["id"],
                entry["evidence_type"],
                entry["original_reference_id"],
                entry.get("qualifier"),
                tuple(entry.get("supporting_entities") or []),
            )
        )
    return rows


def main() -> None:
    doc = yaml.safe_load(REVIEW_YAML.read_text())
    goa = goa_rows()
    reviewed = yaml_rows(doc)
    failures: list[str] = []

    # Term labels must be GOA's, not the reviewer's.
    label_of = {}
    with GOA_TSV.open() as handle:
        for row in csv.DictReader(handle, delimiter="\t"):
            label_of[row["GO TERM"]] = row["GO NAME"]
    for entry in doc["existing_annotations"]:
        term = entry["term"]
        if term["id"] in label_of and term["label"] != label_of[term["id"]]:
            failures.append(
                f"{term['id']}: label {term['label']!r} != GOA label {label_of[term['id']]!r}"
            )

    goa_counts, yaml_counts = Counter(goa), Counter(reviewed)
    for key in sorted(set(goa_counts) | set(yaml_counts)):
        if goa_counts[key] != yaml_counts[key]:
            failures.append(
                f"multiplicity mismatch {key}: GOA={goa_counts[key]} YAML={yaml_counts[key]}"
            )

    actions = Counter()
    for entry in doc["existing_annotations"]:
        review = entry["review"]
        action = review["action"]
        actions[action] += 1
        term = entry["term"]["id"]
        code = entry["evidence_type"]
        if action == "PENDING":
            failures.append(f"{term}/{code}: action still PENDING")
        if action == "NEW":
            continue
        entities = entry.get("supporting_entities") or []
        needs = code == "IBA" or (code in PROPAGATION_REQUIRED_CODES and entities)
        propagation = review.get("propagation_review")
        if needs and not propagation:
            failures.append(f"{term}/{code}: propagation_review required but absent")
        if propagation:
            if not propagation.get("root_cause"):
                failures.append(f"{term}/{code}: propagation_review lacks root_cause")
            sources = [s["source_id"] for s in propagation.get("source_entities") or []]
            if sources != entities:
                failures.append(
                    f"{term}/{code}: source_entities {sources} != supporting_entities {entities}"
                )

    print(f"GOA rows: {len(goa)}")
    print(f"Reviewed existing (non-NEW) rows: {len(reviewed)}")
    print(f"NEW rows: {actions['NEW']}")
    print("Actions: " + ", ".join(f"{a}={n}" for a, n in sorted(actions.items())))
    iba = sum(
        1
        for e in doc["existing_annotations"]
        if e["evidence_type"] == "IBA" and e["review"]["action"] != "NEW"
    )
    blocks = sum(
        1
        for e in doc["existing_annotations"]
        if e["review"].get("propagation_review")
    )
    print(f"IBA rows: {iba}; propagation_review blocks: {blocks}")
    print(f"References: {len(doc['references'])}; "
          f"with reference_review: {sum(1 for r in doc['references'] if r.get('reference_review'))}")

    if failures:
        print()
        for failure in failures:
            print("FAIL " + failure)
        sys.exit(1)
    print("\nOK: GOA and YAML reconcile, no PENDING actions, propagation blocks consistent.")


if __name__ == "__main__":
    main()
