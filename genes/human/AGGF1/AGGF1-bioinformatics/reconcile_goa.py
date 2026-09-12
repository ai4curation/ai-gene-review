"""Every GOA row must have exactly one existing_annotations entry, and vice versa.

The `fetch-gene` stub is known to collapse rows that share a term, evidence code
and reference but differ in WITH/FROM, so the counts are reconciled here on the
full key (term, evidence, reference, with/from) rather than on the row count
alone. Entries in the review that have no GOA row must all be `action: NEW`, and
that is asserted rather than assumed.

Run: uv run python reconcile_goa.py
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).parent
GOA = HERE.parent / "AGGF1-goa.tsv"
REVIEW = HERE.parent / "AGGF1-ai-review.yaml"


def goa_keys() -> Counter[tuple[str, str, str, str]]:
    if not GOA.exists():
        raise SystemExit(f"missing {GOA}; run `just fetch-gene human AGGF1` first")
    with GOA.open() as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if not rows:
        raise SystemExit(f"{GOA} has no data rows; run `just fetch-gene human AGGF1` first")
    return Counter(
        (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], r["WITH/FROM"].strip())
        for r in rows
    ), len(rows)


def review_keys() -> tuple[Counter, list[dict]]:
    doc = yaml.safe_load(REVIEW.read_text())
    anns = doc["existing_annotations"]
    keys: Counter[tuple[str, str, str, str]] = Counter()
    for a in anns:
        wf = "|".join(a.get("supporting_entities") or [])
        keys[(a["term"]["id"], a["evidence_type"], a["original_reference_id"], wf)] += 1
    return keys, anns


def main() -> None:
    goa, n_goa = goa_keys()
    rev, anns = review_keys()

    print(f"GOA data rows              : {n_goa}")
    print(f"existing_annotations entries: {len(anns)}")
    actions = Counter(a["review"]["action"] for a in anns)
    print(f"actions                    : {dict(sorted(actions.items()))}")
    print()

    missing = goa - rev          # GOA rows with no review entry
    extra = rev - goa            # review entries with no GOA row
    print(f"GOA rows with no review entry : {sum(missing.values())}")
    for k, n in missing.items():
        print(f"    x{n} {k}")
    print(f"review entries with no GOA row: {sum(extra.values())}")

    new_rows = [a for a in anns if a["review"]["action"] == "NEW"]
    new_keys = Counter()
    for a in new_rows:
        wf = "|".join(a.get("supporting_entities") or [])
        new_keys[(a["term"]["id"], a["evidence_type"], a["original_reference_id"], wf)] += 1
    for k, n in extra.items():
        tag = "NEW proposal" if new_keys.get(k) else "UNEXPLAINED"
        print(f"    x{n} [{tag}] {k[0]} {k[1]} {k[2]}")

    print()
    assert sum(missing.values()) == 0, (
        f"{sum(missing.values())} GOA row(s) have no review entry -- the review "
        "under-covers the gene"
    )
    assert extra == new_keys, (
        "every review entry without a GOA row must be action: NEW; "
        f"unexplained extras: {sorted((extra - new_keys).elements())}"
    )
    assert len(anns) == n_goa + len(new_rows), (
        f"count mismatch: {len(anns)} entries != {n_goa} GOA rows + {len(new_rows)} NEW"
    )
    print(f"RECONCILED: {n_goa} GOA rows each have exactly one entry; "
          f"{len(new_rows)} further entries are all action: NEW; "
          f"{n_goa} + {len(new_rows)} = {len(anns)}.")


if __name__ == "__main__":
    main()
