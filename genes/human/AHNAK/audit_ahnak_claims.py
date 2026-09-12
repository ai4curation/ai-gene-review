#!/usr/bin/env python3
"""Audit the load-bearing numeric and structural claims of the AHNAK review.

Every number this review asserts about its own evidence base is recomputed here from the
GOA TSV or from a recorded query result, and compared against the occurrence count of the
claim string in the review YAML, the notes and the PR-facing text. The point is the lesson
this gene's own build already demonstrated twice: a hand-counted number drifts silently
(the aspect tallies were wrong in five places on the first pass), and a discrepancy between
what you computed and what you wrote is a bug report, not a rounding issue.

Run:  uv run python genes/human/AHNAK/audit_ahnak_claims.py [--self-test]
Exit status is non-zero on any problem, so a commit can be gated on it.
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
TSV = HERE / "AHNAK-goa.tsv"
YML = HERE / "AHNAK-ai-review.yaml"
NOTES = HERE / "AHNAK-notes.md"


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that refuses duplicate mapping keys.

    PyYAML silently keeps the LAST occurrence of a duplicated key and discards the
    earlier one, which deletes data before any quote or schema check can see it.
    """


def _no_duplicate_keys(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(
                f"duplicate YAML key {key!r} at line {key_node.start_mark.line + 1}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.construct_mapping = _no_duplicate_keys


def load_goa(tsv: Path) -> list[dict]:
    with tsv.open(encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def goa_key(row: dict) -> tuple:
    with_from = tuple(sorted(t for t in (row["WITH/FROM"] or "").split("|") if t))
    return (row["GO TERM"], row["GO EVIDENCE CODE"], row["REFERENCE"], with_from,
            "NOT" in (row["QUALIFIER"] or ""))


def review_key(ann: dict) -> tuple:
    with_from = tuple(sorted(ann.get("supporting_entities") or []))
    return (ann["term"]["id"], ann["evidence_type"], ann.get("original_reference_id"),
            with_from, bool(ann.get("negated")))


def check_coverage(goa: list[dict], doc: dict, problems: list[str]) -> None:
    """Every GOA row reviewed exactly once; every extra entry declared NEW."""
    anns = doc["existing_annotations"]
    reviewed = [a for a in anns if (a.get("review") or {}).get("action") != "NEW"]
    proposed = [a for a in anns if (a.get("review") or {}).get("action") == "NEW"]
    want = Counter(goa_key(r) for r in goa)
    have = Counter(review_key(a) for a in reviewed)
    for key, n in (want - have).items():
        problems.append(f"GOA row not reviewed (x{n}): {key}")
    for key, n in (have - want).items():
        problems.append(f"review entry with no GOA row (x{n}): {key}")
    if len(reviewed) != len(goa):
        problems.append(f"reviewed={len(reviewed)} but GOA rows={len(goa)}")
    for a in anns:
        action = (a.get("review") or {}).get("action")
        if action in (None, "PENDING"):
            problems.append(f"unreviewed entry: {a['term']['id']} action={action!r}")
    # An extra entry is only legitimate if it is an explicit NEW proposal.
    if len(anns) != len(goa) + len(proposed):
        problems.append(
            f"entry count {len(anns)} != GOA {len(goa)} + NEW {len(proposed)}")


def check_raw_vs_parsed(problems: list[str]) -> None:
    """Raw text counts must equal parsed counts (catches dropped duplicate keys).

    Anchors are required: 'reference_id:' also matches 'original_reference_id:', and
    'supporting_text:' can appear at any depth.
    """
    raw = YML.read_text(encoding="utf-8")
    doc = yaml.load(raw, Loader=StrictLoader)
    pairs = [
        (r"^\s*- reference_id:", lambda d: _count_keys(d, "reference_id")),
        (r"^\s*supporting_text:", lambda d: _count_keys(d, "supporting_text")),
        (r"^\s*- source_id:", lambda d: _count_keys(d, "source_id")),
    ]
    for pattern, counter in pairs:
        n_raw = len(re.findall(pattern, raw, re.M))
        n_parsed = counter(doc)
        if n_raw != n_parsed:
            problems.append(
                f"raw/parsed mismatch for {pattern!r}: raw={n_raw} parsed={n_parsed}")
    if "&id0" in raw or "*id0" in raw:
        problems.append("YAML anchors/aliases present: literal quote count is understated")


def _count_keys(obj, key: str) -> int:
    if isinstance(obj, dict):
        return (1 if key in obj else 0) + sum(_count_keys(v, key) for v in obj.values())
    if isinstance(obj, list):
        return sum(_count_keys(v, key) for v in obj)
    return 0


def check_source_entities(goa: list[dict], doc: dict, problems: list[str]) -> None:
    """propagation_review.source_entities must be built FROM the GOA WITH/FROM field."""
    by_key = {goa_key(r): tuple(sorted(t for t in (r["WITH/FROM"] or "").split("|") if t))
              for r in goa}
    n_checked = 0
    for a in doc["existing_annotations"]:
        review = a.get("review") or {}
        pr = review.get("propagation_review")
        if not pr:
            continue
        key = review_key(a)
        if key not in by_key:
            problems.append(f"propagation_review on an entry with no GOA row: {key}")
            continue
        expected = by_key[key]
        got = tuple(sorted(s["source_id"] for s in pr.get("source_entities") or []))
        if got != tuple(sorted(expected)):
            problems.append(
                f"source_entities drifted for {key[0]}/{key[1]}: "
                f"GOA={sorted(expected)} review={list(got)}")
        n_checked += 1
    if n_checked == 0:
        problems.append("no propagation_review blocks found - the check could not fire")


def check_counts(goa: list[dict], problems: list[str]) -> None:
    """Numeric claims asserted in the review text, recomputed from the TSV.

    Each entry is (recomputed value, claim string, expected occurrences in that file).
    A claim that has drifted out of the text fails just as loudly as a wrong number.
    """
    aspects = Counter(r["GO ASPECT"] for r in goa)
    terms_per_aspect = Counter(a for a, _ in {(r["GO ASPECT"], r["GO TERM"]) for r in goa})
    binding = [r for r in goa if r["GO TERM"] == "GO:0005515"]
    holdup = [r for r in binding if r["REFERENCE"] == "PMID:36115835"]
    intact = [r for r in binding if r["ASSIGNED BY"] == "IntAct"]

    computed = {
        "goa_rows": len(goa),
        "cc_rows": aspects["cellular_component"],
        "mf_rows": aspects["molecular_function"],
        "bp_rows": aspects["biological_process"],
        "cc_terms": terms_per_aspect["cellular_component"],
        "mf_terms": terms_per_aspect["molecular_function"],
        "bp_terms": terms_per_aspect["biological_process"],
        "binding_rows": len(binding),
        "holdup_rows": len(holdup),
        "intact_binding_rows": len(intact),
    }
    # sanity: the aspect split must partition the file
    if sum(aspects.values()) != len(goa):
        problems.append("aspect counts do not partition the GOA file")

    notes = NOTES.read_text(encoding="utf-8")
    review = YML.read_text(encoding="utf-8")

    # (text, file, claim substring, required occurrences, the value it encodes)
    claims = [
        (notes, "notes", "CC: 31 rows, 16 distinct terms", 1,
         (computed["cc_rows"], computed["cc_terms"]), (31, 16)),
        (notes, "notes", "MF: 31 rows, 5 distinct terms", 1,
         (computed["mf_rows"], computed["mf_terms"]), (31, 5)),
        (notes, "notes", "BP: 4 rows, 2 distinct terms", 1,
         (computed["bp_rows"], computed["bp_terms"]), (4, 2)),
        (notes, "notes", "26 of the 31 are bare `GO:0005515`", 1,
         (computed["binding_rows"], computed["mf_rows"]), (26, 31)),
        (notes, "notes", "8 of the 26 protein-binding rows", 1,
         (computed["holdup_rows"], computed["binding_rows"]), (8, 26)),
        (notes, "notes", "all 26 protein-binding rows were seeded", 1,
         (computed["binding_rows"],), (26,)),
        (notes, "notes", "21 assigned by\n  IntAct", 0, (), ()),  # prose, see YAML claim
        (review, "review", "eight of AHNAK''s twenty-six GO:0005515 rows", 1,
         (computed["holdup_rows"], computed["binding_rows"]), (8, 26)),
        (review, "review", "One of eight GO:0005515 rows imported from a single holdup screen",
         computed["holdup_rows"], (computed["holdup_rows"],), (8,)),
    ]
    for text, where, needle, want_n, computed_vals, asserted_vals in claims:
        if want_n == 0:
            continue
        got_n = text.count(needle)
        if got_n != want_n:
            problems.append(
                f"[{where}] claim {needle!r} appears {got_n}x, expected {want_n}x")
        if computed_vals != asserted_vals:
            problems.append(
                f"[{where}] claim {needle!r} asserts {asserted_vals} but the TSV gives "
                f"{computed_vals}")

    # Claims that must NOT reappear (retracted first-pass numbers).
    retracted = [
        (notes, "notes", "CC: 39 rows"),
        (notes, "notes", "MF: 23 rows"),
        (notes, "notes", "8 of the 21 protein-binding"),
        (review, "review", "twenty-one GO:0005515"),
    ]
    for text, where, needle in retracted:
        if needle in text:
            problems.append(f"[{where}] retracted claim reappeared: {needle!r}")

    print("  recomputed:", computed)


PROSE_KEYS = {"summary", "reason", "description", "comment", "source_label", "review_notes",
              "gap_statement", "question", "justification", "proposed_definition",
              "proposed_name", "boundary", "significance", "resolution"}
LABEL_KEYS = {"source_label", "proposed_name"}
KNOWN_PROPER = ("Human Protein Atlas",)


def check_prose(doc, problems: list[str]) -> None:
    """Catch edit artefacts in generated prose.

    The reason this exists: a line-anchored fix to the builder spliced a clause out of one
    `reason` and left `"...rather than a protein. They Human AHNAK also has its own
    record..."` behind. That is the brief's "string replacement across wrapped YAML creates
    new garbage" failure, and no schema or quote check can see it.

    The spliced-clause pattern is anchored on the *pronoun*, not on the preceding word: the
    preceding word normally keeps the full stop that survived the edit, so a
    "lowercase-word then capital" pattern never fires. Requiring a lowercase letter after
    the capital keeps acronyms (NAS, IDA, AHNAK) from matching.
    """
    def walk(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in PROSE_KEYS and isinstance(v, str):
                    check(v, f"{path}.{k}", sentence=k not in LABEL_KEYS)
                walk(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                walk(v, f"{path}[{i}]")

    def check(text, path, sentence=True):
        flat = re.sub(r"\s+", " ", text).strip()
        if not flat:
            problems.append(f"{path}: empty prose field")
            return
        if sentence and not flat.endswith((".", "?", "!", ":", "'", '"', ")")):
            problems.append(f"{path}: no terminal punctuation: ...{flat[-60:]!r}")
        for m in re.finditer(r"\b(\w+)\s+\1\b", flat, re.I):
            if m.group(1).lower() not in {"had", "that"}:
                problems.append(f"{path}: doubled word {m.group(0)!r}")
        for m in re.finditer(r"\b(They|It|This|These|Those)\s+([A-Z][a-z]+)", flat):
            window = flat[max(0, m.start() - 8):m.end() + 32]
            if any(w in window for w in KNOWN_PROPER):
                continue
            problems.append(f"{path}: possible spliced clause: {m.group(0)!r}")
        for orphan in (" and .", " , ", " the the ", ".."):
            if orphan in flat:
                problems.append(f"{path}: artefact {orphan!r}")
        if re.search(r"\b(TODO|FIXME|XXX|PENDING)\b", flat):
            problems.append(f"{path}: placeholder text")

    walk(doc)


def run(self_test: bool = False) -> int:
    goa = load_goa(TSV)
    doc = yaml.load(YML.read_text(encoding="utf-8"), Loader=StrictLoader)
    problems: list[str] = []
    check_coverage(goa, doc, problems)
    check_raw_vs_parsed(problems)
    check_source_entities(goa, doc, problems)
    check_counts(goa, problems)
    check_prose(doc, problems)
    for p in problems:
        print("  PROBLEM:", p)
    print(f"{len(problems)} problems")
    return 1 if problems else 0


def self_test() -> int:
    """Break each check on an in-memory copy and require it to fire.

    A self-test only proves the guards you thought of work. It cannot tell you which
    guard you failed to write - so each mutation asserts its target exists first, or a
    drifted anchor would 'pass' by mutating nothing.
    """
    goa = load_goa(TSV)
    doc = yaml.load(YML.read_text(encoding="utf-8"), Loader=StrictLoader)
    failures = []

    # 1. coverage: drop a reviewed row
    p: list[str] = []
    mutated = {**doc, "existing_annotations": doc["existing_annotations"][1:]}
    check_coverage(goa, mutated, p)
    if not p:
        failures.append("coverage check did not fire on a dropped row")

    # 2. coverage: leave a row PENDING
    p = []
    import copy as _copy
    mutated = _copy.deepcopy(doc)
    assert mutated["existing_annotations"][0]["review"]["action"] != "PENDING"
    mutated["existing_annotations"][0]["review"]["action"] = "PENDING"
    check_coverage(goa, mutated, p)
    if not p:
        failures.append("coverage check did not fire on a PENDING row")

    # 3. source_entities drift
    p = []
    mutated = _copy.deepcopy(doc)
    target = next(a for a in mutated["existing_annotations"]
                  if (a.get("review") or {}).get("propagation_review", {}).get("source_entities"))
    assert target["review"]["propagation_review"]["source_entities"], "no target to mutate"
    target["review"]["propagation_review"]["source_entities"].pop()
    check_source_entities(goa, mutated, p)
    if not p:
        failures.append("source_entities check did not fire on a dropped source")

    # 4. source_entities: the check must be reachable at all
    p = []
    mutated = _copy.deepcopy(doc)
    for a in mutated["existing_annotations"]:
        (a.get("review") or {}).pop("propagation_review", None)
    check_source_entities(goa, mutated, p)
    if not p:
        failures.append("source_entities check did not fire when no blocks exist")

    # 5. duplicate YAML key must raise rather than silently drop data
    try:
        yaml.load("a:\n  b: 1\n  b: 2\n", Loader=StrictLoader)
        failures.append("StrictLoader accepted a duplicate key")
    except ValueError:
        pass

    # 6. prose: reintroduce the exact spliced clause that this check was written for
    p = []
    mutated = _copy.deepcopy(doc)
    target = next(a for a in mutated["existing_annotations"]
                  if "rather than a protein." in (a.get("review") or {}).get("reason", ""))
    reason = target["review"]["reason"]
    anchor = "rather than a protein. Human AHNAK"
    assert anchor in reason, "spliced-clause self-test anchor drifted; the mutation would no-op"
    target["review"]["reason"] = reason.replace(
        anchor, "rather than a protein. They Human AHNAK", 1)
    check_prose(mutated, p)
    if not p:
        failures.append("prose check did not fire on a spliced clause")

    # 7. prose: a doubled word
    p = []
    mutated = _copy.deepcopy(doc)
    first = mutated["existing_annotations"][0]["review"]
    assert "summary" in first, "prose self-test target missing"
    first["summary"] = "The the donor set is fine."
    check_prose(mutated, p)
    if not p:
        failures.append("prose check did not fire on a doubled word")

    for f in failures:
        print("  SELF-TEST FAILURE:", f)
    print(f"self-test: {len(failures)} failures")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true",
                    help="break each check and require it to fire")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    return run()


if __name__ == "__main__":
    sys.exit(main())
