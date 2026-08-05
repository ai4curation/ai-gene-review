#!/usr/bin/env python3
"""Assert ADGRA2's review covers every GOA row exactly once, and that no data was lost
to a duplicate YAML key.

Two failures this exists to catch, both invisible to `just validate` and to the quote
checkers:

1. **Under-coverage from the seeder.** `GOAValidator.seed_missing_annotations` keys
   seeded entries on (GO id, evidence, reference, negated, qualifier) — **WITH/FROM is
   not in the key** — so rows differing only in the partner collapse into one stub. On
   ADGRA2 the GOA TSV has 59 distinct rows and the stub had 41: all 21 `GO:0005515`
   rows collapsed to 3. An agent reviewing every stub entry silently under-reviews the
   gene.

2. **Duplicate YAML keys.** PyYAML keeps the *last* occurrence of a duplicated mapping
   key and discards the earlier one, silently. Every other checker in this repo walks
   the *parsed* document, so data destroyed at parse time cannot fail them. Detection
   requires reading the raw text.

Run:  python3 check_coverage.py [--self-test]
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GOA = HERE.parent / "ADGRA2-goa.tsv"
REVIEW = HERE.parent / "ADGRA2-ai-review.yaml"

# Actions that mean "this entry is my own proposal, not a GOA row".
PROPOSAL_ACTIONS = {"NEW"}


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that REJECTS duplicate mapping keys instead of silently keeping the last."""


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None,
                f"duplicate key {key!r} at line {key_node.start_mark.line + 1} "
                "-- PyYAML would silently discard the earlier value",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates)


def goa_keys(path: Path) -> Counter:
    """(GO id, evidence, reference, qualifier, WITH/FROM) for every GOA data row."""
    keys = Counter()
    with path.open() as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            keys[(r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"],
                  r["QUALIFIER"], r["WITH/FROM"])] += 1
    assert keys, f"no rows parsed from {path} -- wrong delimiter or empty file"
    return keys


def review_keys(doc: dict) -> tuple[Counter, list]:
    covered, proposals = Counter(), []
    for a in doc["existing_annotations"]:
        action = (a.get("review") or {}).get("action")
        key = (a["term"]["id"], a["evidence_type"], a["original_reference_id"],
               a.get("qualifier", ""), "|".join(a.get("supporting_entities") or []))
        if action in PROPOSAL_ACTIONS:
            proposals.append(key)
        else:
            covered[key] += 1
    return covered, proposals


def raw_vs_parsed(path: Path, doc: dict) -> list[str]:
    """Reconcile a raw-text count against the parsed count.

    Anchored to `^\\s*(?:-\\s*)?reference_id:` because (a) a bare `in` test on
    "reference_id:" also matches `original_reference_id:`, and (b) PyYAML puts a YAML
    anchor on the list-item line and the key on the next, so `^\\s*- reference_id:`
    matches zero of an anchored file.
    """
    problems = []
    raw = len(re.findall(r"^\s*(?:-\s*)?reference_id:", path.read_text(), re.M))
    parsed = 0

    def walk(n):
        nonlocal parsed
        if isinstance(n, dict):
            if "reference_id" in n:
                parsed += 1
            for v in n.values():
                walk(v)
        elif isinstance(n, list):
            for v in n:
                walk(v)

    walk(doc)
    if raw != parsed:
        problems.append(
            f"reference_id count mismatch: {raw} in raw text, {parsed} parsed. "
            "Do NOT rationalise this gap -- derive the expected number independently."
        )
    return problems


def check(goa: Path = GOA, review: Path = REVIEW, verbose: bool = True) -> list[str]:
    problems: list[str] = []
    text = review.read_text()
    try:
        doc = yaml.load(text, Loader=StrictLoader)
    except yaml.constructor.ConstructorError as exc:
        return [f"DUPLICATE YAML KEY: {exc}"]

    if "&id" in text or re.search(r"\*id\d+", text):
        problems.append("YAML anchors/aliases present: rows may share one object, so a "
                        "single quote would verify N times as N successes.")

    want = goa_keys(goa)
    got, proposals = review_keys(doc)

    missing = want - got
    extra = got - want
    for k, n in sorted(missing.items()):
        problems.append(f"GOA row NOT reviewed (x{n}): {k}")
    for k, n in sorted(extra.items()):
        problems.append(f"review entry with no GOA row and action != NEW (x{n}): {k}")

    dup = {k: n for k, n in got.items() if n > 1}
    for k, n in sorted(dup.items()):
        problems.append(f"GOA row reviewed {n} times: {k}")

    pending = [a["term"]["id"] for a in doc["existing_annotations"]
               if (a.get("review") or {}).get("action") == "PENDING"]
    if pending:
        problems.append(f"{len(pending)} entries still PENDING: {sorted(set(pending))}")

    problems += raw_vs_parsed(review, doc)

    if verbose:
        print(f"GOA distinct rows          : {len(want)} (sum {sum(want.values())})")
        print(f"reviewed GOA-matched rows  : {len(got)} (sum {sum(got.values())})")
        print(f"own NEW proposals          : {len(proposals)}")
        for p in proposals:
            print(f"    NEW {p[0]} {p[1]} {p[2]}")
        print(f"total existing_annotations : {len(doc['existing_annotations'])}")
    return problems


def self_test() -> None:
    """Break-test in both directions: the guard must fire on damage AND pass when clean."""
    import tempfile

    base = REVIEW.read_text()
    doc = yaml.load(base, Loader=StrictLoader)

    # Happy path first -- an agreement check that fails on *perfect* agreement is a real
    # and previously-observed defect, so the clean case is exercised explicitly.
    assert check(verbose=False) == [], "guard reports problems on the committed, clean file"

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)

        # 1. Deleting a reviewed row must be detected.
        d1 = yaml.safe_load(base)
        removed = None
        for i, a in enumerate(d1["existing_annotations"]):
            if a["term"]["id"] == "GO:0005515":
                removed = d1["existing_annotations"].pop(i)
                break
        assert removed is not None, "self-test mutation target absent -- has the file drifted?"
        p1 = td / "drop.yaml"
        p1.write_text(yaml.safe_dump(d1, sort_keys=False))
        probs = check(review=p1, verbose=False)
        assert any(p.startswith("GOA row NOT reviewed") for p in probs), probs

        # 2. An invented row (not marked NEW) must be detected.
        d2 = yaml.safe_load(base)
        d2["existing_annotations"].append({
            "term": {"id": "GO:9999999", "label": "invented"},
            "evidence_type": "IDA", "original_reference_id": "PMID:1", "qualifier": "enables",
            "review": {"summary": "x", "action": "ACCEPT", "reason": "x"},
        })
        p2 = td / "extra.yaml"
        p2.write_text(yaml.safe_dump(d2, sort_keys=False))
        probs = check(review=p2, verbose=False)
        assert any(p.startswith("review entry with no GOA row") for p in probs), probs

        # 3. The SAME invented row, marked NEW, must NOT be flagged -- otherwise the
        #    guard would forbid legitimate proposals.
        d3 = yaml.safe_load(base)
        row = dict(d2["existing_annotations"][-1])
        row["review"] = {"summary": "x", "action": "NEW", "reason": "x"}
        d3["existing_annotations"].append(row)
        p3 = td / "new.yaml"
        p3.write_text(yaml.safe_dump(d3, sort_keys=False))
        assert check(review=p3, verbose=False) == [], check(review=p3, verbose=False)

        # 4. A duplicate YAML key must be rejected by the strict loader.
        p4 = td / "dup.yaml"
        p4.write_text(base.replace("gene_symbol: ADGRA2",
                                   "gene_symbol: ADGRA2\ngene_symbol: WRONG", 1))
        probs = check(review=p4, verbose=False)
        assert probs and probs[0].startswith("DUPLICATE YAML KEY"), probs

        # 5. A PENDING action must be caught (the "complete-looking but unreviewed" case).
        d5 = yaml.safe_load(base)
        d5["existing_annotations"][0]["review"]["action"] = "PENDING"
        p5 = td / "pending.yaml"
        p5.write_text(yaml.safe_dump(d5, sort_keys=False))
        probs = check(review=p5, verbose=False)
        assert any("still PENDING" in p for p in probs), probs

        # 6. Truncating the GOA input must fail loudly, not degrade to "0 problems".
        p6 = td / "empty.tsv"
        p6.write_text(GOA.read_text().splitlines()[0] + "\n")
        try:
            check(goa=p6, verbose=False)
        except AssertionError:
            pass
        else:
            raise AssertionError("empty GOA file did not raise -- silent degradation")

    print("self-test OK: 6 directions exercised "
          "(clean file passes; dropped row, invented row, legitimate NEW, duplicate key, "
          "PENDING action, empty GOA input)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        self_test()
        sys.exit(0)
    found = check()
    print()
    if found:
        for p in found:
            print("PROBLEM:", p)
        sys.exit(1)
    print("OK: every GOA row reviewed exactly once, no duplicate keys, no anchors, nothing PENDING")
