"""Reconcile the GOA tsv against the reviewed YAML, row for row.

Checks, all of which must pass:

1. Every GOA row maps to exactly one YAML entry with the same
   (GO term, evidence code, reference, normalized supporting_entities), and vice
   versa. Exact-duplicate GOA lines (same tuple, different ASSIGNED BY) collapse to
   one YAML entry by design, so the comparison is on multisets of distinct tuples.
2. Every GOA row's WITH/FROM is reproduced verbatim, in order, as that entry's
   `supporting_entities`.
3. Every YAML row carries a completed review (no PENDING, no TODO).
4. Every IBA/ISS/ISO/IEA/IC row with supporting_entities carries a
   `propagation_review`, and each block's `source_entities` list exactly matches
   that row's `supporting_entities` - same ids, same order.
5. Every `supported_by.reference_id` used anywhere appears in `references`, and
   every reference carries a `reference_review`.

Run from the repo root:
    uv run python genes/human/APPL2/APPL2-bioinformatics/check_goa_reconciliation.py
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[4]
GOA = REPO / "genes" / "human" / "APPL2" / "APPL2-goa.tsv"
REVIEW = REPO / "genes" / "human" / "APPL2" / "APPL2-ai-review.yaml"

PROPAGATED = {"IBA", "ISS", "ISO", "IEA", "IC"}


def norm_withfrom(raw: str) -> tuple[str, ...]:
    return tuple(p.strip() for p in raw.split("|") if p.strip())


def main() -> int:
    failures: list[str] = []

    goa_rows = list(csv.DictReader(GOA.open(), delimiter="\t"))
    goa_keys = Counter(
        (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], norm_withfrom(r["WITH/FROM"]))
        for r in goa_rows
    )

    doc = yaml.safe_load(REVIEW.read_text())
    rows = doc["existing_annotations"]
    seeded = [r for r in rows if (r.get("review") or {}).get("action") != "NEW"]
    new_rows = [r for r in rows if (r.get("review") or {}).get("action") == "NEW"]

    yaml_keys = Counter(
        (r["term"]["id"], r["evidence_type"], r["original_reference_id"],
         tuple(r.get("supporting_entities") or []))
        for r in seeded
    )

    print(f"GOA lines: {len(goa_rows)}  distinct GOA tuples: {len(goa_keys)}")
    print(f"YAML rows: {len(rows)}  (seeded {len(seeded)}, NEW {len(new_rows)})")

    only_goa = set(goa_keys) - set(yaml_keys)
    only_yaml = set(yaml_keys) - set(goa_keys)
    for k in sorted(only_goa):
        failures.append(f"GOA tuple with no YAML entry: {k}")
    for k in sorted(only_yaml):
        failures.append(f"YAML entry with no GOA tuple: {k}")
    dupes = [k for k, n in yaml_keys.items() if n > 1]
    for k in dupes:
        failures.append(f"YAML has {yaml_keys[k]} entries for one tuple: {k}")

    collapsed = sum(n - 1 for n in goa_keys.values() if n > 1)
    print(f"exact-duplicate GOA lines collapsed into one YAML entry each: {collapsed}")

    # 3/4: review completeness and propagation_review integrity
    n_prop = 0
    for i, r in enumerate(rows):
        rev = r.get("review") or {}
        action = rev.get("action")
        if action in (None, "PENDING"):
            failures.append(f"row {i} ({r['term']['id']}) has action {action!r}")
        for field in ("summary", "reason"):
            val = rev.get(field) or ""
            if not val or "TODO" in val:
                failures.append(f"row {i} ({r['term']['id']}) has empty/TODO {field}")
        if not rev.get("supported_by"):
            failures.append(f"row {i} ({r['term']['id']}) has no supported_by")
        ents = r.get("supporting_entities") or []
        prop = rev.get("propagation_review")
        if r["evidence_type"] in PROPAGATED and ents:
            if not prop:
                failures.append(f"row {i} ({r['term']['id']}, {r['evidence_type']}) lacks propagation_review")
            else:
                n_prop += 1
                src = [s["source_id"] for s in prop.get("source_entities") or []]
                if src != ents:
                    failures.append(
                        f"row {i} ({r['term']['id']}) source_entities {src} != supporting_entities {ents}")
                if not prop.get("root_cause"):
                    failures.append(f"row {i} ({r['term']['id']}) propagation_review has no root_cause")
                for s in prop.get("source_entities") or []:
                    if not s.get("comment"):
                        failures.append(f"row {i} ({r['term']['id']}) source {s['source_id']} has no comment")
        elif prop and not ents:
            failures.append(f"row {i} ({r['term']['id']}) has propagation_review but no supporting_entities")
    print(f"propagation_review blocks on seeded/NEW rows with supporting_entities: {n_prop}")

    # 5: references
    refs = {r["id"]: r for r in doc["references"]}
    cited: set[str] = set()

    def walk(node):
        if isinstance(node, dict):
            if "reference_id" in node and "supporting_text" in node:
                cited.add(node["reference_id"])
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(doc)
    for rid in sorted(cited - set(refs)):
        failures.append(f"cited but not in references: {rid}")
    for rid, entry in refs.items():
        if not entry.get("reference_review"):
            failures.append(f"reference {rid} has no reference_review")
        if not entry.get("title"):
            failures.append(f"reference {rid} has no title")
    print(f"references: {len(refs)}, distinct ids cited in supported_by/provenance: {len(cited)}")

    # action census, for the PR body
    census = Counter((r.get("review") or {}).get("action") for r in rows)
    print("actions: " + ", ".join(f"{k}={v}" for k, v in sorted(census.items())))
    ev = Counter(r["evidence_type"] for r in rows)
    print("evidence: " + ", ".join(f"{k}={v}" for k, v in sorted(ev.items())))

    if failures:
        print(f"\nFAILED ({len(failures)}):")
        for f in failures:
            print("  " + f)
        return 1
    print("\nreconciliation OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
