"""Reconcile AP5M1-goa.tsv against existing_annotations in AP5M1-ai-review.yaml.

Every GOA row must map to exactly one review entry with the same term id,
evidence code, reference and normalised supporting_entities (WITH/FROM split on
"|", stripped, deduped, order kept).  Every non-NEW review entry must map back to
a GOA row.  Also reports the action histogram and checks no entry is left PENDING.

Exits non-zero if anything fails.
"""

from __future__ import annotations

import collections
import csv
import pathlib
import sys

import yaml

GENE_DIR = pathlib.Path(__file__).resolve().parent.parent
GOA = GENE_DIR / "AP5M1-goa.tsv"
REVIEW = GENE_DIR / "AP5M1-ai-review.yaml"


def normalise_withfrom(value: str) -> tuple[str, ...]:
    seen: list[str] = []
    for part in (value or "").split("|"):
        part = part.strip()
        if part and part not in seen:
            seen.append(part)
    return tuple(seen)


def main() -> int:
    with GOA.open() as fh:
        goa_rows = list(csv.DictReader(fh, delimiter="\t"))
    review = yaml.safe_load(REVIEW.read_text())
    entries = review["existing_annotations"]

    goa_keys = collections.Counter(
        (
            r["GO TERM"],
            r["GO EVIDENCE CODE"],
            r["REFERENCE"],
            normalise_withfrom(r["WITH/FROM"]),
        )
        for r in goa_rows
    )

    review_keys: collections.Counter = collections.Counter()
    new_rows = []
    pending = []
    actions: collections.Counter = collections.Counter()
    for e in entries:
        action = (e.get("review") or {}).get("action")
        actions[action] += 1
        if action == "PENDING":
            pending.append(e["term"]["id"])
        if action == "NEW":
            new_rows.append(e)
            continue
        review_keys[
            (
                e["term"]["id"],
                e["evidence_type"],
                e["original_reference_id"],
                tuple(e.get("supporting_entities") or ()),
            )
        ] += 1

    ok = True
    print(f"GOA rows: {len(goa_rows)}")
    print(f"review existing_annotations: {len(entries)}  (NEW: {len(new_rows)}, "
          f"reviewed-from-GOA: {len(entries) - len(new_rows)})")

    missing = goa_keys - review_keys
    extra = review_keys - goa_keys
    if missing:
        ok = False
        print(f"\nFAIL: {sum(missing.values())} GOA row(s) with no matching review entry:")
        for k, n in missing.items():
            print(f"  x{n} {k}")
    if extra:
        ok = False
        print(f"\nFAIL: {sum(extra.values())} non-NEW review entr(ies) with no matching GOA row:")
        for k, n in extra.items():
            print(f"  x{n} {k}")
    if pending:
        ok = False
        print(f"\nFAIL: {len(pending)} entr(ies) still PENDING: {pending}")

    withfrom_goa = sum(1 for r in goa_rows if normalise_withfrom(r["WITH/FROM"]))
    withfrom_yaml = sum(
        1 for e in entries
        if (e.get("review") or {}).get("action") != "NEW" and e.get("supporting_entities")
    )
    print(f"\nrows carrying WITH/FROM: GOA {withfrom_goa}, review {withfrom_yaml}")
    if withfrom_goa != withfrom_yaml:
        ok = False
        print("FAIL: supporting_entities present on a different number of rows than GOA WITH/FROM")

    # propagation_review coverage: required on every IBA row and on every
    # ISS/ISO/IEA/IC row that carries supporting_entities.
    need_prop = [
        e for e in entries
        if (e.get("review") or {}).get("action") != "NEW"
        and (e["evidence_type"] == "IBA"
             or (e["evidence_type"] in {"ISS", "ISO", "IEA", "IC"} and e.get("supporting_entities")))
    ]
    no_prop = [e for e in need_prop if not (e.get("review") or {}).get("propagation_review")]
    bare = [
        e for e in need_prop
        if ((e.get("review") or {}).get("propagation_review") or {}).get("source_entities") in (None, [])
    ]
    print(f"rows requiring propagation_review: {len(need_prop)}; "
          f"missing: {len(no_prop)}; without source_entities: {len(bare)}")
    if no_prop or bare:
        ok = False
        for e in no_prop:
            print(f"  FAIL missing propagation_review: {e['term']['id']} {e['evidence_type']}")
        for e in bare:
            print(f"  FAIL bare propagation_review: {e['term']['id']} {e['evidence_type']}")

    # source_entities must be drawn from the row's own supporting_entities,
    # optionally plus donors resolved to a UniProtKB accession.
    for e in need_prop:
        prop = (e.get("review") or {}).get("propagation_review") or {}
        supporting = set(e.get("supporting_entities") or ())
        for src in prop.get("source_entities", []):
            if src["source_id"] not in supporting:
                ok = False
                print(f"  FAIL source_id {src['source_id']} not in supporting_entities of "
                      f"{e['term']['id']} {e['evidence_type']} {sorted(supporting)}")

    print("\naction histogram:")
    for action, n in sorted(actions.items(), key=lambda kv: (-kv[1], kv[0] or "")):
        print(f"  {action:<24} {n}")

    # reference_review coverage
    refs = review.get("references") or []
    unreviewed = [r["id"] for r in refs if not r.get("reference_review")]
    print(f"\nreferences: {len(refs)}; without reference_review: {len(unreviewed)} {unreviewed}")
    if unreviewed:
        ok = False

    # every reference_id used anywhere must be declared in references:
    declared = {r["id"] for r in refs}
    used: set[str] = set()
    for e in entries:
        rid = e.get("original_reference_id")
        if rid:
            used.add(rid)
        rv = e.get("review") or {}
        for s in rv.get("supported_by") or []:
            used.add(s["reference_id"])
        for rid in rv.get("additional_reference_ids") or []:
            used.add(rid)
    for cf in review.get("core_functions") or []:
        for s in cf.get("supported_by") or []:
            used.add(s["reference_id"])
    undeclared = sorted(used - declared)
    print(f"reference ids used: {len(used)}; undeclared: {undeclared}")
    if undeclared:
        ok = False

    print("\nRECONCILIATION " + ("PASSED" if ok else "FAILED"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
