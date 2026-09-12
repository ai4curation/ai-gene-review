"""Reconcile every GOA row for AP3D1 with exactly one entry in the review YAML.

The review's ``existing_annotations`` are seeded deterministically from the GOA
tsv, but they are then hand-edited, so drift is possible: a dropped row, a
duplicated row, or a ``supporting_entities`` list that no longer matches the
WITH/FROM column it came from.

Matching key: (GO id, evidence code, reference, normalized WITH/FROM set).
Both sides are reduced to a multiset of those keys and compared. Exit 1 on any
mismatch. Also prints the counts the review prose quotes, so no number in the
notes or the PR body is asserted rather than counted.
"""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).parent
GOA = HERE.parent / "AP3D1-goa.tsv"
REVIEW = HERE.parent / "AP3D1-ai-review.yaml"
ROOT = HERE.parents[3]


def _norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def strict_quote_check(doc) -> int:
    """Every supporting_text must be a LITERAL substring of its source.

    Deliberately stricter than the repo/CI reference validator and than
    checkquotes.py, both of which normalise before matching. That normalisation
    silently accepts a quote that transliterates a character the paper actually
    prints -- 'delta-adaptin' where PMID:22521722 has 'δ-adaptin' -- so the
    sentence stops being findable in the paper while still passing. Only
    whitespace is normalised here, and numeric citation markers are stripped from
    the SOURCE (not the quote) exactly as the validator does.
    """
    cache: dict[str, str | None] = {}

    def source(ref: str) -> str | None:
        if ref not in cache:
            if ref.startswith("PMID:"):
                path = ROOT / "publications" / f"PMID_{ref.split(':', 1)[1]}.md"
            elif ref.startswith("file:"):
                path = ROOT / "genes" / ref.split(":", 1)[1]
            else:
                cache[ref] = None
                return None
            raw = path.read_text(errors="replace")
            cache[ref] = _norm(re.sub(r"\[\d[\d,\s\-\u2013]*\]", " ", raw))
        return cache[ref]

    checked = bad = 0

    def walk(node, path=""):
        nonlocal checked, bad
        if isinstance(node, dict):
            if "supporting_text" in node and "reference_id" in node:
                src = source(node["reference_id"])
                if src is not None:
                    checked += 1
                    if _norm(node["supporting_text"]) not in src:
                        bad += 1
                        print(f"NOT LITERALLY VERBATIM: {path} {node['reference_id']}")
                        print(f"    {node['supporting_text'][:150]}")
            for k, v in node.items():
                walk(v, f"{path}.{k}")
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{path}[{i}]")

    walk(doc)
    print(f"strict verbatim check: {checked} quotes, {bad} not literally verbatim")
    return bad


def norm_entities(values) -> tuple[str, ...]:
    return tuple(sorted(v.strip() for v in values if v and v.strip()))


def goa_keys() -> Counter:
    keys = Counter()
    with GOA.open() as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            keys[(
                row["GO TERM"],
                row["GO EVIDENCE CODE"],
                row["REFERENCE"],
                norm_entities(row["WITH/FROM"].split("|")),
            )] += 1
    return keys


def yaml_keys(doc) -> Counter:
    keys = Counter()
    for a in doc["existing_annotations"]:
        if a["review"].get("action") == "NEW":
            continue
        keys[(
            a["term"]["id"],
            a["evidence_type"],
            a["original_reference_id"],
            norm_entities(a.get("supporting_entities") or []),
        )] += 1
    return keys


def main() -> None:
    doc = yaml.safe_load(REVIEW.read_text())
    g, y = goa_keys(), yaml_keys(doc)

    missing = g - y
    extra = y - g
    for k, n in sorted(missing.items()):
        print(f"IN GOA, NOT IN YAML (x{n}): {k}")
    for k, n in sorted(extra.items()):
        print(f"IN YAML, NOT IN GOA (x{n}): {k}")

    anns = doc["existing_annotations"]
    new_rows = [a for a in anns if a["review"].get("action") == "NEW"]
    print(f"\nGOA rows: {sum(g.values())}")
    print(f"YAML existing_annotations: {len(anns)} ({len(anns) - len(new_rows)} GOA-derived + {len(new_rows)} NEW)")

    ev = Counter(a["evidence_type"] for a in anns if a["review"].get("action") != "NEW")
    print("evidence codes (GOA-derived):", dict(sorted(ev.items())))
    act = Counter(a["review"]["action"] for a in anns)
    print("actions:", dict(sorted(act.items())))

    need_prop = [
        a for a in anns
        if a["review"].get("action") != "NEW"
        and (a["evidence_type"] == "IBA" or (a.get("supporting_entities") and a["evidence_type"] in {"ISS", "ISO", "IEA", "IC"}))
    ]
    without = [a["term"]["id"] for a in need_prop if "propagation_review" not in a["review"]]
    print(f"rows requiring propagation_review: {len(need_prop)}; missing: {without or 'none'}")

    # every propagation_review source_entity must come from that row's supporting_entities
    drift = []
    for a in anns:
        pr = a["review"].get("propagation_review")
        if not pr:
            continue
        declared = set(a.get("supporting_entities") or [])
        for se in pr.get("source_entities") or []:
            if se["source_id"] not in declared:
                drift.append((a["term"]["id"], a["evidence_type"], se["source_id"]))
    for d in drift:
        print(f"SOURCE NOT IN supporting_entities: {d}")

    refs = {r["id"] for r in doc.get("references", [])}
    cited = set()

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in {"reference_id", "original_reference_id"} and isinstance(v, str):
                    cited.add(v)
                if k == "additional_reference_ids" and isinstance(v, list):
                    cited.update(v)
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(doc)
    uncited = sorted(refs - cited)
    undeclared = sorted(cited - refs)
    print(f"references declared: {len(refs)}; cited but undeclared: {undeclared or 'none'}")
    if uncited:
        print(f"declared but not cited anywhere: {uncited}")
    reviewed = sum(1 for r in doc.get("references", []) if r.get("reference_review"))
    print(f"references with reference_review: {reviewed}/{len(refs)}")

    quote_failures = strict_quote_check(doc)

    bad = bool(missing or extra or without or drift or undeclared or quote_failures)
    print("\nRECONCILIATION:", "FAIL" if bad else "PASS")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
