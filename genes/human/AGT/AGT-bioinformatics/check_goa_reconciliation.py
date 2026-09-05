"""Reconcile every GOA row against exactly one entry in the AGT review YAML.

AGT has 114 GOA rows, which is too many to keep aligned by hand. This check
enforces three things:

1. Every GOA row maps to exactly one `existing_annotations` entry, matched on
   (GO id, evidence code, reference, qualifier, normalised WITH/FROM).
2. Every review entry maps back to a GOA row (no invented entries), except
   entries whose action is NEW.
3. Where a GOA row has a WITH/FROM, the entry's `supporting_entities` is exactly
   the `|`-split token list, de-duplicated, in GOA order.

It also reports GOA rows that are exact duplicates of one another, since those
legitimately collapse to a single review entry, and reports which IBA/ISS/IEA/IC
rows still lack a `propagation_review`.

Exit status is non-zero if any check fails.

Run: uv run python check_goa_reconciliation.py
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).parent
GOA = HERE.parent / "AGT-goa.tsv"
REVIEW = HERE.parent / "AGT-ai-review.yaml"

# Evidence codes for which the brief requires propagation_review when the row
# carries a WITH/FROM.
PROPAGATION_CODES = {"IBA", "ISS", "ISO", "IEA", "IC"}


def norm_entities(raw: str) -> tuple[str, ...]:
    out: list[str] = []
    for tok in raw.split("|"):
        tok = tok.strip()
        if tok and tok not in out:
            out.append(tok)
    return tuple(out)


def goa_key(row: dict[str, str]) -> tuple[str, ...]:
    return (
        row["GO TERM"],
        row["GO EVIDENCE CODE"],
        row["REFERENCE"],
        row["QUALIFIER"],
        "|".join(norm_entities(row["WITH/FROM"])),
    )


def entry_key(e: dict) -> tuple[str, ...]:
    qualifier = e.get("qualifier", "") or ""
    if e.get("negated"):
        qualifier = f"NOT|{qualifier}"
    return (
        e["term"]["id"],
        e.get("evidence_type", ""),
        e.get("original_reference_id", ""),
        qualifier,
        "|".join(norm_entities("|".join(e.get("supporting_entities") or []))),
    )


def main() -> int:
    with GOA.open() as fh:
        goa_rows = list(csv.DictReader(fh, delimiter="\t"))
    review = yaml.safe_load(REVIEW.read_text())
    entries = review["existing_annotations"]

    goa_keys = Counter(goa_key(r) for r in goa_rows)
    reviewed = [e for e in entries if (e.get("review") or {}).get("action") != "NEW"]
    new_entries = [e for e in entries if (e.get("review") or {}).get("action") == "NEW"]
    entry_keys = Counter(entry_key(e) for e in reviewed)

    failures: list[str] = []

    dupes = {k: n for k, n in goa_keys.items() if n > 1}
    print(f"GOA rows: {len(goa_rows)}   review entries: {len(entries)} "
          f"({len(reviewed)} from GOA, {len(new_entries)} NEW)")
    print(f"distinct GOA keys: {len(goa_keys)}   duplicate GOA keys: {len(dupes)}")
    for k, n in dupes.items():
        print(f"  GOA row appears {n}x (collapses to one review entry): {k}")

    missing = [k for k in goa_keys if k not in entry_keys]
    for k in missing:
        failures.append(f"GOA row has no review entry: {k}")

    extra = [k for k in entry_keys if k not in goa_keys]
    for k in extra:
        failures.append(f"review entry matches no GOA row: {k}")

    overcounted = [(k, entry_keys[k]) for k in entry_keys if entry_keys[k] > 1]
    for k, n in overcounted:
        failures.append(f"review has {n} entries for one GOA key: {k}")

    # supporting_entities fidelity, checked directly against the GOA field.
    by_key: dict[tuple[str, ...], dict] = {}
    for e in reviewed:
        by_key.setdefault(entry_key(e), e)
    for row in goa_rows:
        k = goa_key(row)
        e = by_key.get(k)
        if e is None:
            continue
        want = list(norm_entities(row["WITH/FROM"])) if row["WITH/FROM"].strip() else []
        got = list(e.get("supporting_entities") or [])
        if want != got:
            failures.append(
                f"supporting_entities mismatch for {row['GO TERM']} "
                f"{row['GO EVIDENCE CODE']} {row['REFERENCE']}:\n"
                f"      GOA:    {want}\n      review: {got}"
            )

    # propagation_review coverage on propagated rows that carry a WITH/FROM.
    need_prop = []
    for row in goa_rows:
        if row["GO EVIDENCE CODE"] not in PROPAGATION_CODES:
            continue
        if not row["WITH/FROM"].strip():
            continue
        e = by_key.get(goa_key(row))
        if e is None:
            continue
        if not (e.get("review") or {}).get("propagation_review"):
            need_prop.append(f"{row['GO TERM']} {row['GO EVIDENCE CODE']} {row['REFERENCE']}")
    for n in need_prop:
        failures.append(f"propagated row with WITH/FROM lacks propagation_review: {n}")

    n_prop_rows = sum(
        1 for r in goa_rows
        if r["GO EVIDENCE CODE"] in PROPAGATION_CODES and r["WITH/FROM"].strip()
    )
    print(f"rows requiring propagation_review: {n_prop_rows}; "
          f"missing: {len(need_prop)}")

    pending = [e["term"]["id"] for e in entries
               if (e.get("review") or {}).get("action") in {None, "PENDING"}]
    if pending:
        failures.append(f"{len(pending)} entries still PENDING: {pending[:10]}")

    if failures:
        print(f"\nFAILED ({len(failures)}):")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("\nOK: every GOA row maps to exactly one review entry, supporting_entities "
          "match the GOA WITH/FROM field verbatim, and every propagated row with a "
          "WITH/FROM carries a propagation_review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
