"""Reconcile every ARFGEF1 GOA row against exactly one review entry.

Adapted from `genes/human/AGT/AGT-bioinformatics/check_goa_reconciliation.py`.
The `fetch-gene` stub is known to collapse GOA rows (distinct `GO:0005515`
partners, same-term rows from different assigners), so "review everything the
stub gave you" can silently under-review a gene. This enforces:

1. Every GOA row maps to exactly one `existing_annotations` entry, matched on
   (GO id, evidence code, reference, qualifier, normalised WITH/FROM).
2. Every review entry maps back to a GOA row, except entries whose action is NEW.
3. Where a GOA row has a WITH/FROM, the entry's `supporting_entities` is exactly
   the `|`-split token list, de-duplicated, in GOA order — built FROM the GOA
   field, not by hand. Hand-maintained source lists have drifted on every gene in
   this campaign that tried it.
4. No entry is left `PENDING`.
5. Every propagated row (IBA/ISS/ISO/IEA/IC) whose action is REMOVE, MODIFY or
   MARK_AS_OVER_ANNOTATED carries a `propagation_review`. Propagated rows that
   are ACCEPTed are reported but not required to have one.
6. **Raw-vs-parsed reconciliation.** The YAML is additionally loaded with a
   strict loader that rejects duplicate mapping keys. PyYAML silently keeps the
   last occurrence of a duplicated key and discards the earlier one, so a
   duplicated `supported_by:` deletes provenance before any quote checker runs;
   every gate in this repo walks the parsed document and is blind to it.

Exit status is non-zero if any check fails. Run from the repo root:
    uv run python genes/human/ARFGEF1/ARFGEF1-bioinformatics/check_goa_reconciliation.py
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).parent
GOA = HERE.parent / "ARFGEF1-goa.tsv"
REVIEW = HERE.parent / "ARFGEF1-ai-review.yaml"

PROPAGATION_CODES = {"IBA", "ISS", "ISO", "IEA", "IC"}
NEEDS_PROPAGATION_REVIEW = {"REMOVE", "MODIFY", "MARK_AS_OVER_ANNOTATED"}


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that raises on a duplicated mapping key instead of dropping one."""


def _no_duplicates(loader, node, deep=False):  # type: ignore[no-untyped-def]
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r}", key_node.start_mark
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)


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
    raw = REVIEW.read_text()
    failures: list[str] = []

    try:
        yaml.load(raw, Loader=StrictLoader)
    except yaml.constructor.ConstructorError as exc:
        failures.append(f"duplicate YAML key (data would be silently lost): {exc}")

    review = yaml.safe_load(raw)
    entries = review["existing_annotations"]

    # Raw-vs-parsed count: derive the expected number independently rather than
    # finding a story that makes a gap acceptable.
    raw_terms = len(re.findall(r"^- term:$", raw, re.M))
    if raw_terms != len(entries):
        failures.append(
            f"raw '- term:' lines ({raw_terms}) != parsed existing_annotations "
            f"({len(entries)}) -- a duplicate key or a stray block"
        )

    goa_keys = Counter(goa_key(r) for r in goa_rows)
    reviewed = [e for e in entries if (e.get("review") or {}).get("action") != "NEW"]
    new_entries = [e for e in entries if (e.get("review") or {}).get("action") == "NEW"]
    entry_keys = Counter(entry_key(e) for e in reviewed)

    print(f"GOA rows: {len(goa_rows)}   review entries: {len(entries)} "
          f"({len(reviewed)} from GOA, {len(new_entries)} NEW)")
    dupes = {k: n for k, n in goa_keys.items() if n > 1}
    print(f"distinct GOA keys: {len(goa_keys)}   duplicate GOA keys: {len(dupes)}")
    for k, n in dupes.items():
        print(f"  GOA row appears {n}x (collapses to one review entry): {k}")

    for k in goa_keys:
        if k not in entry_keys:
            failures.append(f"GOA row has no review entry: {k}")
    for k in entry_keys:
        if k not in goa_keys:
            failures.append(f"review entry matches no GOA row: {k}")
    for k, n in entry_keys.items():
        if n > 1:
            failures.append(f"review has {n} entries for one GOA key: {k}")

    by_key: dict[tuple[str, ...], dict] = {}
    for e in reviewed:
        by_key.setdefault(entry_key(e), e)
    for row in goa_rows:
        e = by_key.get(goa_key(row))
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

    need, have, not_required = [], [], []
    for row in goa_rows:
        if row["GO EVIDENCE CODE"] not in PROPAGATION_CODES:
            continue
        if not row["WITH/FROM"].strip():
            continue
        e = by_key.get(goa_key(row))
        if e is None:
            continue
        action = (e.get("review") or {}).get("action")
        has = bool((e.get("review") or {}).get("propagation_review"))
        label = f"{row['GO TERM']} {row['GO EVIDENCE CODE']} {row['REFERENCE']} [{action}]"
        if action in NEEDS_PROPAGATION_REVIEW and not has:
            need.append(label)
        elif has:
            have.append(label)
        else:
            not_required.append(label)
    for n in need:
        failures.append(f"propagated row needs a propagation_review: {n}")
    print(f"propagated rows with a WITH/FROM: {len(need) + len(have) + len(not_required)}"
          f"  (with propagation_review: {len(have)}; "
          f"not required: {len(not_required)}; missing: {len(need)})")

    pending = [e["term"]["id"] for e in entries
               if (e.get("review") or {}).get("action") in {None, "PENDING"}]
    if pending:
        failures.append(f"{len(pending)} entries still PENDING: {pending[:10]}")

    # Every reference cited by a supported_by must be declared in references:.
    declared = {r["id"] for r in review.get("references") or []}
    cited: set[str] = set()

    def walk(node: object) -> None:
        if isinstance(node, dict):
            if "reference_id" in node:
                cited.add(str(node["reference_id"]))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(review)
    undeclared = sorted(cited - declared)
    for u in undeclared:
        failures.append(f"reference cited in a supported_by but not declared: {u}")

    actions = Counter((e.get("review") or {}).get("action") for e in entries)
    print("actions: " + ", ".join(f"{k}={v}" for k, v in sorted(actions.items(), key=str)))

    if failures:
        print(f"\nFAILED ({len(failures)}):")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("\nOK: every GOA row maps to exactly one review entry; supporting_entities "
          "match the GOA WITH/FROM verbatim; no duplicate YAML keys; every cited "
          "reference is declared.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
