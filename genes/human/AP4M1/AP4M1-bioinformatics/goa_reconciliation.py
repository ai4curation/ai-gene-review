"""Reconcile every row of AP4M1-goa.tsv against the entries of AP4M1-ai-review.yaml.

The review YAML's `existing_annotations` are seeded deterministically from the GOA tsv.
This script re-derives the seeding key from the tsv and checks, in both directions, that
GOA rows and YAML entries correspond, with identical normalised `supporting_entities`.

It also reports:
  * GOA rows that collapse onto one YAML entry (identical on every key field, differing
    only in a column the seeder does not key on, such as DATE);
  * YAML entries with `action: NEW`, which are reviewer additions and have no GOA row;
  * every review action, and the propagation_review coverage of rows that carry
    `supporting_entities`.

Exit status is non-zero if any GOA row is unmatched, any non-NEW YAML entry is
unmatched, or a matched pair disagrees on `supporting_entities`.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GOA = HERE.parent / "AP4M1-goa.tsv"
REVIEW = HERE.parent / "AP4M1-ai-review.yaml"

PROPAGATION_EVIDENCE = {"IBA", "ISS", "ISO", "IEA", "IC"}


def norm_withfrom(raw: str) -> tuple[str, ...]:
    if not raw or not raw.strip():
        return ()
    seen: list[str] = []
    for part in raw.split("|"):
        p = part.strip()
        if p and p not in seen:
            seen.append(p)
    return tuple(seen)


def goa_rows() -> list[dict]:
    with GOA.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def main() -> int:
    rows = goa_rows()
    review = yaml.safe_load(REVIEW.read_text())
    entries = review["existing_annotations"]

    goa_keys: Counter = Counter()
    for r in rows:
        goa_keys[
            (
                r["GO TERM"],
                r["GO EVIDENCE CODE"],
                r["REFERENCE"],
                norm_withfrom(r["WITH/FROM"]),
            )
        ] += 1

    yaml_keys: Counter = Counter()
    new_entries = 0
    by_key: dict[tuple, list[dict]] = defaultdict(list)
    for e in entries:
        if e.get("review", {}).get("action") == "NEW":
            new_entries += 1
            continue
        key = (
            e["term"]["id"],
            e["evidence_type"],
            e["original_reference_id"],
            norm_withfrom("|".join(e.get("supporting_entities") or [])),
        )
        yaml_keys[key] += 1
        by_key[key].append(e)

    print(f"GOA rows (excluding header): {len(rows)}")
    print(f"YAML existing_annotations:   {len(entries)}  "
          f"({len(entries) - new_entries} seeded from GOA, {new_entries} NEW)")

    errors = 0

    missing_in_yaml = [k for k in goa_keys if k not in yaml_keys]
    for k in missing_in_yaml:
        print(f"ERROR unmatched GOA row: {k}")
        errors += 1

    missing_in_goa = [k for k in yaml_keys if k not in goa_keys]
    for k in missing_in_goa:
        print(f"ERROR YAML entry with no GOA row: {k}")
        errors += 1

    for k in goa_keys:
        if k in yaml_keys and yaml_keys[k] != 1:
            print(f"ERROR YAML has {yaml_keys[k]} entries for one GOA key: {k}")
            errors += 1

    collapsed = {k: n for k, n in goa_keys.items() if n > 1}
    for k, n in collapsed.items():
        print(f"NOTE  {n} GOA rows collapse onto 1 YAML entry (identical on every "
              f"seeded field): {k[0]} {k[1]} {k[2]} {list(k[3])}")

    # supporting_entities equality is already enforced by the key, so a match implies it.
    print(f"\nsupporting_entities agree on all {len(goa_keys)} matched keys: "
          f"{errors == 0}")

    actions = Counter(
        e.get("review", {}).get("action", "MISSING") for e in entries
    )
    print("\naction counts:")
    for a, n in sorted(actions.items()):
        print(f"  {a:24s} {n}")

    need_prop = [
        e
        for e in entries
        if e.get("supporting_entities")
        and e["evidence_type"] in PROPAGATION_EVIDENCE
        and e.get("review", {}).get("action") != "NEW"
    ]
    have_prop = [e for e in need_prop if e.get("review", {}).get("propagation_review")]
    print(f"\nrows requiring propagation_review: {len(need_prop)}; "
          f"present on {len(have_prop)}")
    for e in need_prop:
        if not e.get("review", {}).get("propagation_review"):
            print(f"ERROR missing propagation_review: {e['term']['id']} "
                  f"{e['evidence_type']} {e['original_reference_id']}")
            errors += 1

    # every propagation_review source_id that is a row-level donor must come from the
    # row's own supporting_entities (node ids and GO_REF labels are allowed extras)
    for e in entries:
        pr = e.get("review", {}).get("propagation_review")
        if not pr:
            continue
        declared = set(e.get("supporting_entities") or [])
        for s in pr.get("source_entities") or []:
            sid = s["source_id"]
            if sid not in declared:
                print(f"ERROR source_id not in supporting_entities: {sid} on "
                      f"{e['term']['id']} {e['evidence_type']} "
                      f"{e['original_reference_id']}")
                errors += 1

    iba = [e for e in entries if e["evidence_type"] == "IBA"]
    print(f"\nIBA rows: {len(iba)}")
    for e in iba:
        pr = e.get("review", {}).get("propagation_review") or {}
        print(f"  {e['term']['id']:12s} {e['review']['action']:22s} "
              f"root_cause={pr.get('root_cause')}")

    print(f"\nERRORS: {errors}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
