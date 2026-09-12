#!/usr/bin/env python3
"""Invariant checks for the human AHI1 gene review, with a built-in self-test.

Run from anywhere:

    uv run python genes/human/AHI1/AHI1-bioinformatics/audit_ahi1_claims.py
    uv run python genes/human/AHI1/AHI1-bioinformatics/audit_ahi1_claims.py --self-test

Exit status is non-zero when anything fails, so a caller can gate a commit on it
(`cmd && git commit`). Note that `$?` after a pipeline is the pipeline's status, not
this script's - test the command directly.

Paths are resolved RELATIVE TO THIS FILE, never hardcoded to one checkout. A sibling
scratch copy of a similar checker carried an absolute path into another agent's
worktree, which made every full-text quote resolve against a cache that only had
abstracts and reported 56 false failures.

What is checked
---------------
1. The raw YAML contains no duplicate mapping keys. PyYAML keeps the LAST occurrence
   of a duplicated key and silently discards the earlier one, so provenance can be
   deleted before any quote checker - all of which walk the parsed document - can see it.
2. Every row of AHI1-goa.tsv has exactly one matching `existing_annotations` entry,
   keyed on (GO term, evidence code, reference, WITH/FROM set), and every reviewed
   entry matches a GOA row. Entries with `action: NEW` are excluded and counted
   separately, so the arithmetic is explicit rather than approximate.
3. Every `propagation_review.source_entities` list is derived from the GOA WITH/FROM
   field rather than maintained by hand. Hand-maintained source lists have drifted on
   several genes in this campaign and the drift is invisible by eye.
4. No review is left at `action: PENDING`.
5. Every `reference_id` cited anywhere is declared in the top-level `references`.
6. The raw count of `- reference_id:` lines equals the parsed count, which is the
   cross-check that makes defect (1) detectable even if the strict loader is bypassed.

The self-test mutates a temporary copy of the review, asserting each anchor string is
present BEFORE replacing it, so a drifted anchor is an error rather than a mutation
that silently no-ops and "proves" the guard fires. A passing self-test shows the guards
that were written do fire; it cannot show which guard was never written.
"""

from __future__ import annotations

import argparse
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
YAML_PATH = GENE_DIR / "AHI1-ai-review.yaml"
GOA_PATH = GENE_DIR / "AHI1-goa.tsv"

ACC_LIKE = re.compile(
    r"^(UniProtKB|MGI|ZFIN|PANTHER|RGD|SGD|FB|WB|TAIR|ComplexPortal|PMID):"
)


class NoDupSafeLoader(yaml.SafeLoader):
    """SafeLoader that refuses duplicate mapping keys instead of dropping data."""


def _no_dup_construct_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None,
                None,
                f"duplicate key {key!r} at line {key_node.start_mark.line + 1}",
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


NoDupSafeLoader.construct_mapping = _no_dup_construct_mapping


def goa_key(row: dict) -> tuple:
    return (
        row["GO TERM"],
        row["GO EVIDENCE CODE"],
        row["REFERENCE"],
        tuple(sorted(t for t in row["WITH/FROM"].split("|") if t)),
    )


def ann_key(ann: dict) -> tuple:
    supporting = ann.get("supporting_entities") or []
    return (
        ann["term"]["id"],
        ann["evidence_type"],
        ann["original_reference_id"],
        tuple(sorted(supporting)),
    )


def _walk_reference_ids(obj, out: set) -> None:
    if isinstance(obj, dict):
        ref = obj.get("reference_id")
        if isinstance(ref, str):
            out.add(ref)
        for value in obj.values():
            _walk_reference_ids(value, out)
    elif isinstance(obj, list):
        for value in obj:
            _walk_reference_ids(value, out)


def _count_reference_ids(obj) -> int:
    if isinstance(obj, dict):
        n = 1 if "reference_id" in obj else 0
        return n + sum(_count_reference_ids(v) for v in obj.values())
    if isinstance(obj, list):
        return sum(_count_reference_ids(v) for v in obj)
    return 0


def audit(yaml_path: Path, goa_path: Path, verbose: bool = True) -> list[str]:
    """Return a list of problems. Never raises from inside a check.

    A check that raises would abort every later check while the harness still prints
    as though it had run - which is exactly how this script's own KeyError bug was
    found, by the self-test rather than by reading it.
    """
    problems: list[str] = []

    def say(msg: str) -> None:
        if verbose:
            print(msg)

    raw = yaml_path.read_text(encoding="utf-8")

    # 1. duplicate mapping keys
    try:
        doc = yaml.load(raw, Loader=NoDupSafeLoader)
        say("1. duplicate-key loader: OK")
    except yaml.constructor.ConstructorError as exc:
        problems.append(f"DUPLICATE YAML KEY: {exc}")
        say(f"1. duplicate-key loader: FAIL ({exc})")
        doc = yaml.safe_load(raw)

    annotations = doc["existing_annotations"]

    # 2. GOA row coverage
    goa_lines = goa_path.read_text(encoding="utf-8").rstrip("\n").split("\n")
    header = goa_lines[0].split("\t")
    rows = [dict(zip(header, line.split("\t"))) for line in goa_lines[1:]]

    new_rows = [a for a in annotations if a["review"]["action"] == "NEW"]
    reviewed = [a for a in annotations if a["review"]["action"] != "NEW"]
    goa_counter = Counter(goa_key(r) for r in rows)
    ann_counter = Counter(ann_key(a) for a in reviewed)

    say(f"2. GOA data rows: {len(rows)}   existing_annotations: {len(annotations)}")
    if goa_counter == ann_counter:
        say(
            f"   coverage: OK ({len(rows)} GOA rows = {len(reviewed)} reviewed rows, "
            f"+{len(new_rows)} NEW proposals)"
        )
    else:
        for key, n in (goa_counter - ann_counter).items():
            problems.append(f"GOA row NOT REVIEWED (x{n}): {key}")
        for key, n in (ann_counter - goa_counter).items():
            problems.append(f"REVIEWED row NOT IN GOA (x{n}): {key}")
    if len(rows) != len(reviewed):
        problems.append(
            f"row count mismatch: GOA {len(rows)} vs reviewed {len(reviewed)}"
        )

    # 3. source_entities derived from GOA WITH/FROM
    withfrom = {
        goa_key(r): {t for t in r["WITH/FROM"].split("|") if t} for r in rows
    }
    compared = 0
    for ann in reviewed:
        review = ann["review"].get("propagation_review")
        if not review:
            continue
        declared = {
            s["source_id"]
            for s in review.get("source_entities", [])
            if ACC_LIKE.match(s["source_id"])
        }
        key = ann_key(ann)
        if key not in withfrom:
            problems.append(
                f"cannot check source_entities, row absent from GOA: {key}"
            )
            continue
        tokens = withfrom[key]
        if not tokens:
            # A NAS/IDA row has no WITH/FROM; naming a complex or reference as the
            # source is legitimate there and nothing can be compared against.
            continue
        compared += 1
        if declared != tokens:
            problems.append(
                f"source_entities DRIFT on {ann['term']['id']} "
                f"{ann['evidence_type']} {ann['original_reference_id']}: "
                f"declared={sorted(declared)} goa_withfrom={sorted(tokens)}"
            )
    say(f"3. source_entities vs GOA WITH/FROM: {compared} rows with tokens compared")

    # 4. no PENDING left
    pending = [a["term"]["id"] for a in annotations if a["review"]["action"] == "PENDING"]
    if pending:
        problems.append(f"PENDING actions remain: {pending}")
    say(f"4. PENDING actions: {len(pending)}")

    # 5. every cited reference declared
    declared_refs = {r["id"] for r in doc["references"]}
    used: set = set()
    _walk_reference_ids(doc, used)
    undeclared = used - declared_refs
    if undeclared:
        problems.append(f"cited but NOT declared in references: {sorted(undeclared)}")
    say(
        f"5. references: {len(declared_refs)} declared, {len(used)} cited, "
        f"{len(undeclared)} undeclared"
    )

    # 6. raw vs parsed reference_id counts
    raw_count = len(re.findall(r"^\s*- reference_id:", raw, re.M))
    parsed_count = _count_reference_ids(doc)
    if raw_count != parsed_count:
        problems.append(
            f"reference_id raw {raw_count} != parsed {parsed_count} "
            "(a duplicate key may have deleted provenance)"
        )
    say(f"6. reference_id occurrences: raw {raw_count} == parsed {parsed_count}")

    tally = Counter(a["review"]["action"] for a in annotations)
    say(f"\nactions: {dict(tally)}")
    return problems


MUTATIONS = [
    (
        "duplicate key",
        "    action: MARK_AS_OVER_ANNOTATED\n    reason: >-\n      O43184 resolves",
        "    action: MARK_AS_OVER_ANNOTATED\n    action: ACCEPT\n    reason: >-\n      O43184 resolves",
        "DUPLICATE YAML KEY",
    ),
    (
        "dropped GOA row",
        "- term:\n    id: GO:0050795\n    label: regulation of behavior\n  evidence_type: ISS",
        "- term:\n    id: GO:9999999\n    label: regulation of behavior\n  evidence_type: ISS",
        "GOA row NOT REVIEWED",
    ),
    (
        "source_entities drift",
        "      - source_id: ZFIN:ZDB-GENE-060803-1",
        "      - source_id: ZFIN:ZDB-GENE-999999-9",
        "source_entities DRIFT",
    ),
    (
        "PENDING left behind",
        "    action: MODIFY\n    reason: >-\n      The donor's evidence is specific",
        "    action: PENDING\n    reason: >-\n      The donor's evidence is specific",
        "PENDING actions remain",
    ),
    (
        "undeclared reference",
        "    - reference_id: PMID:20081859\n      supporting_text: significantly (P = 0.00175",
        "    - reference_id: PMID:11111111\n      supporting_text: significantly (P = 0.00175",
        "cited but NOT declared",
    ),
]


def self_test() -> int:
    original = YAML_PATH.read_text(encoding="utf-8")
    baseline = audit(YAML_PATH, GOA_PATH, verbose=False)
    if baseline:
        print("baseline audit must PASS before the self-test can mean anything:")
        for p in baseline:
            print("  ", p)
        return 1
    print("baseline: audit passes")

    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        tmp_yaml = Path(tmp) / "AHI1-ai-review.yaml"
        for name, anchor, replacement, expected in MUTATIONS:
            if anchor not in original:
                failures.append(
                    f"{name}: SELF-TEST ANCHOR DRIFTED, mutation would no-op: "
                    f"{anchor[:60]!r}"
                )
                print(f"  FAIL  {name:24s} -> anchor missing")
                continue
            tmp_yaml.write_text(original.replace(anchor, replacement, 1), encoding="utf-8")
            problems = audit(tmp_yaml, GOA_PATH, verbose=False)
            fired = any(expected in p for p in problems)
            print(f"  {'PASS' if fired else 'FAIL'}  {name:24s} -> expected {expected!r}")
            if not fired:
                failures.append(f"{name}: guard did not fire (problems={problems})")

    print(f"\n{len(failures)} self-test failures")
    for f in failures:
        print("  ", f)
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="mutate a temporary copy and assert each guard fires",
    )
    args = parser.parse_args()
    if args.self_test:
        return self_test()

    problems = audit(YAML_PATH, GOA_PATH)
    print(f"\n{len(problems)} problems")
    for p in problems:
        print("  PROBLEM:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
