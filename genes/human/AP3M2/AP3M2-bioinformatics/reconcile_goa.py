"""Reconcile the GOA tsv against the review YAML, row for row.

Asserts that every GOA line maps to exactly one `existing_annotations` entry with the
same term, evidence code, reference and WITH/FROM set (normalised the same way the
seeder does: split on '|', strip, dedupe, keep order), and that the only YAML entries
without a GOA line are the ones whose review action is NEW. Also asserts that every
row carrying supporting_entities carries a propagation_review whose source_entities
are exactly those supporting_entities, in the same order.

Run:  uv run python reconcile_goa.py
Exits non-zero on any mismatch.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).parent
GENE_DIR = HERE.parent
TSV = GENE_DIR / "AP3M2-goa.tsv"
YML = GENE_DIR / "AP3M2-ai-review.yaml"

NEEDS_PROP = {"IBA", "ISS", "ISO", "IEA", "IC"}


def norm(withfrom: str) -> tuple[str, ...]:
    seen: list[str] = []
    for part in withfrom.split("|"):
        part = part.strip()
        if part and part not in seen:
            seen.append(part)
    return tuple(seen)


def main() -> int:
    with TSV.open() as fh:
        goa = list(csv.DictReader(fh, delimiter="\t"))
    doc = yaml.safe_load(YML.read_text())
    rows = doc["existing_annotations"]

    goa_keys = Counter(
        (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], norm(r["WITH/FROM"]))
        for r in goa
    )
    yaml_keys = Counter(
        (
            r["term"]["id"],
            r["evidence_type"],
            r["original_reference_id"],
            tuple(r.get("supporting_entities") or ()),
        )
        for r in rows
        if r["review"]["action"] != "NEW"
    )

    problems: list[str] = []
    for key, n in goa_keys.items():
        if yaml_keys.get(key, 0) != n:
            problems.append(f"GOA key {key} appears {n}x in tsv, {yaml_keys.get(key, 0)}x in YAML")
    for key, n in yaml_keys.items():
        if goa_keys.get(key, 0) != n:
            problems.append(f"YAML key {key} appears {n}x in YAML, {goa_keys.get(key, 0)}x in tsv")

    new_rows = [r for r in rows if r["review"]["action"] == "NEW"]
    reviewed = len(rows) - len(new_rows)

    for r in rows:
        ents = tuple(r.get("supporting_entities") or ())
        pr = r["review"].get("propagation_review")
        tid, ev = r["term"]["id"], r["evidence_type"]
        if ents and pr is None:
            problems.append(f"{tid}/{ev}: supporting_entities but no propagation_review")
            continue
        if pr is None:
            if ev in NEEDS_PROP and ents:
                problems.append(f"{tid}/{ev}: {ev} row with WITH/FROM lacks propagation_review")
            continue
        got = tuple(s["source_id"] for s in pr.get("source_entities", []))
        if got != ents:
            problems.append(
                f"{tid}/{ev}: source_entities {got} != supporting_entities {ents}"
            )
        if not pr.get("root_cause"):
            problems.append(f"{tid}/{ev}: propagation_review without root_cause")
        for s in pr.get("source_entities", []):
            if not s.get("comment"):
                problems.append(f"{tid}/{ev}: source {s['source_id']} has no comment")

    pending = [r["term"]["id"] for r in rows if r["review"]["action"] == "PENDING"]
    if pending:
        problems.append(f"rows still PENDING: {pending}")

    print(f"GOA tsv rows            : {len(goa)}")
    print(f"YAML reviewed rows      : {reviewed}")
    print(f"YAML NEW rows           : {len(new_rows)}")
    print(f"rows with propagation_review: "
          f"{sum(1 for r in rows if r['review'].get('propagation_review'))}")
    print(f"rows with supporting_entities: "
          f"{sum(1 for r in rows if r.get('supporting_entities'))}")
    print(f"action counts           : "
          f"{dict(Counter(r['review']['action'] for r in rows))}")
    if problems:
        for p in problems:
            print(f"MISMATCH: {p}")
        return 1
    print("OK: GOA and review reconcile exactly")
    return 0


if __name__ == "__main__":
    sys.exit(main())
