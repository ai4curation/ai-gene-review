#!/usr/bin/env python3
"""Invariant checks on the ADCK2 review, run before every push.

Motivated by three recurring failures in this campaign:

* "fixed in N places, landed in N-1" -- so every claim is checked by counting, not by eye;
* `source_entities` silently drifting from the GOA WITH/FROM field on 3 of 3 genes that
  maintained the list by hand -- so it is rebuilt from the TSV and compared;
* a duplicate YAML key silently discarding data before any quote gate can see it -- so the
  file is loaded once with a strict loader that rejects repeated keys, and the raw text is
  counted independently of the parsed object.

Design rules learned the hard way: a check appends to `problems` and never raises, so one
failure cannot abort the rest of the harness; and `--self-test` mutates the document to
prove each guard actually fires, asserting the mutation target exists first so a drifted
target cannot "pass" by no-op.

Usage:
    uv run python audit_adck2_claims.py
    uv run python audit_adck2_claims.py --self-test
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REVIEW = GENE_DIR / "ADCK2-ai-review.yaml"
GOA = GENE_DIR / "ADCK2-goa.tsv"
NOTES = GENE_DIR / "ADCK2-notes.md"
RESULTS_JSON = HERE / "results.json"

SUBJECT = "Q7Z695"


class StrictLoader(yaml.SafeLoader):
    """SafeLoader that refuses duplicate mapping keys instead of silently keeping the last."""


def _no_duplicates(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                None, None, f"duplicate key {key!r} at line {key_node.start_mark.line + 1}"
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_duplicates
)


def load_goa(path: Path) -> list[dict]:
    with path.open() as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def check_row_coverage(doc: dict, goa: list[dict], problems: list[str]) -> None:
    """Every distinct GOA annotation must have a reviewed entry, and none may stay PENDING."""
    entries = doc.get("existing_annotations") or []
    distinct = {
        (r["GO TERM"], r["GO EVIDENCE CODE"], r["REFERENCE"], r["QUALIFIER"])
        for r in goa
    }
    if len(entries) != len(distinct):
        problems.append(
            f"coverage: {len(entries)} review entries vs {len(distinct)} distinct GOA "
            f"annotations ({len(goa)} raw rows). Reconcile explicitly; an unexplained "
            f"mismatch is either missing coverage or a silent collapse."
        )
    reviewed = {
        (e["term"]["id"], e["evidence_type"], e.get("original_reference_id"),
         e.get("qualifier"))
        for e in entries
    }
    for d in sorted(distinct - reviewed):
        problems.append(f"coverage: GOA annotation with no matching review entry: {d}")
    for i, e in enumerate(entries):
        action = ((e.get("review") or {}).get("action"))
        if action in (None, "PENDING"):
            problems.append(
                f"coverage: existing_annotations[{i}] ({e['term']['id']}) has action="
                f"{action!r}; every row must carry a decided verdict."
            )


def check_source_entities(doc: dict, goa: list[dict], problems: list[str]) -> None:
    """source_entities must be reconstructible from the GOA WITH/FROM column, not by hand."""
    for i, e in enumerate(doc.get("existing_annotations") or []):
        review = e.get("review") or {}
        prop = review.get("propagation_review")
        if not prop:
            continue
        listed = {s["source_id"] for s in (prop.get("source_entities") or [])}
        matching = [
            r for r in goa
            if r["GO TERM"] == e["term"]["id"]
            and r["GO EVIDENCE CODE"] == e["evidence_type"]
            and r["REFERENCE"] == e.get("original_reference_id")
        ]
        if not matching:
            problems.append(
                f"source_entities: existing_annotations[{i}] has a propagation_review but "
                f"no GOA row matches its (term, evidence, reference); cannot verify."
            )
            continue
        expected = {
            tok for r in matching for tok in (r["WITH/FROM"] or "").split("|") if tok
        }
        if listed != expected:
            problems.append(
                f"source_entities: existing_annotations[{i}] ({e['term']['id']}) lists "
                f"{sorted(listed)} but GOA WITH/FROM is {sorted(expected)}; "
                f"missing={sorted(expected - listed)} extra={sorted(listed - expected)}"
            )


def check_supporting_entities(doc: dict, goa: list[dict], problems: list[str]) -> None:
    """Same invariant for the top-level supporting_entities list on IBA rows."""
    for i, e in enumerate(doc.get("existing_annotations") or []):
        listed = e.get("supporting_entities")
        if listed is None:
            continue
        matching = [
            r for r in goa
            if r["GO TERM"] == e["term"]["id"]
            and r["GO EVIDENCE CODE"] == e["evidence_type"]
            and r["REFERENCE"] == e.get("original_reference_id")
        ]
        expected = {
            tok for r in matching for tok in (r["WITH/FROM"] or "").split("|") if tok
        }
        if set(listed) != expected:
            problems.append(
                f"supporting_entities: existing_annotations[{i}] lists {sorted(listed)} "
                f"but GOA WITH/FROM is {sorted(expected)}"
            )


def check_motif_claims(doc: dict, notes: str, results: dict, problems: list[str]) -> None:
    """Residue claims in prose must match the computed alignment, not a remembered number."""
    sites = {r["site"]: r["targets"][SUBJECT] for r in results["sites"]}
    for site, expected_aa, expected_pos in [
        ("KxGQ_K", "K", 147),
        ("KxGQ_Q", "Q", 150),
        ("beta3_K", "K", 311),
        ("cat_D", "D", 445),
        ("DFG_D", "D", 493),
        ("Arich_A1", "G", 207),
        ("Arich_A3", "G", 209),
    ]:
        got = sites.get(site)
        if got is None:
            problems.append(f"motif: results.json has no site {site}")
            continue
        if (got["aa"], got["pos"]) != (expected_aa, expected_pos):
            problems.append(
                f"motif: {site} computed as {got['aa']}{got['pos']} but this script "
                f"expects {expected_aa}{expected_pos}; prose citing the old value is stale."
            )
    blob = yaml.safe_dump(doc) + notes
    for token in ["K147", "K311", "D445", "D493", "G207", "G209"]:
        if token not in blob:
            problems.append(f"motif: residue {token} is computed but cited nowhere in prose")
    # The alignment must remain trustworthy, or every residue claim above is unfounded.
    cc = results["control_checks"]
    if cc["pka_kxgq_matches"] != 0:
        problems.append(
            f"motif: negative control now matches {cc['pka_kxgq_matches']} KxGQ positions, "
            f"so KxGQ is no longer UbiB-diagnostic and the prose claim is unfounded."
        )
    if cc["columns_in_register"] < 6:
        problems.append(
            f"motif: only {cc['columns_in_register']}/{cc['columns_total']} columns in "
            f"register; the review claims 6."
        )


def check_retracted_phrasings(raw_review: str, notes: str, problems: list[str]) -> None:
    """Claims considered and rejected during review must not survive anywhere.

    Scans the RAW review text, not the parsed document: the parsed form drops comments,
    so a detector built on it is blind to part of the file it is supposed to police.
    Whitespace is normalised first, because YAML block scalars wrap long sentences and an
    un-normalised regex would miss any claim that happens to straddle a line break.
    """
    blob = re.sub(r"\s+", " ", raw_review + "\n" + notes)
    # Each pattern encodes the AFFIRMATIVE form of a rejected claim, and every hit is then
    # tested for a preceding negator. Two earlier versions of this check fired on correct
    # statements -- first on the bare word "pseudokinase", then on "neither is a
    # pseudokinase" after mere anchoring. A guard that rejects the truth is worse than no
    # guard, so negation handling is explicit rather than encoded in ever-longer regexes.
    # The negator must be in the SAME CLAUSE as the claim, so the window stops at any
    # sentence or clause boundary. A window that only forbids a full stop is too permissive:
    # "ADCK2 has no measured activity, and ADCK2 is a serine/threonine kinase" would be
    # suppressed by an incidental "no" belonging to a different clause. Punctuation and
    # coordinating conjunctions both close the window.
    negator = re.compile(
        r"\b(?:not|never|neither|nor|no|cannot|rather than|instead of|without|"
        r"isn't|dis(?:proved|proven)|refut\w*)\b(?:(?!\band\b|\bbut\b|\bwhile\b|"
        r"\bwhereas\b|\bhowever\b)[^.;,:])" r"{0,30}$",
        re.I,
    )
    for pattern, why in [
        (r"ADCK2 is a (?:protein )?serine/threonine kinase", "never demonstrated"),
        (r"ADCK2 (?:is|acts as) an ATPase", "never measured for ADCK2"),
        (r"\bis a pseudokinase\b", "refuted: all four catalytic positions are intact"),
        (r"ADCK2 .{0,40}\bcatalys(?:es|is|ing) a step", "refuted by the labelling experiment"),
    ]:
        for m in re.finditer(pattern, blob, re.I):
            preceding = blob[max(0, m.start() - 60): m.start()]
            if negator.search(preceding):
                continue  # a negated mention is the correct statement, not a retracted one
            problems.append(f"retracted phrasing present ({why}): {m.group(0)!r}")


def check_raw_vs_parsed(problems: list[str]) -> None:
    """Guard against a duplicate YAML key deleting provenance before any gate can see it."""
    raw = REVIEW.read_text()
    raw_count = len(re.findall(r"^\s*- reference_id:", raw, re.M))
    doc = yaml.safe_load(raw)

    def walk(node):
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "supported_by" and isinstance(v, list):
                    yield from (e for e in v if isinstance(e, dict))
                else:
                    yield from walk(v)
        elif isinstance(node, list):
            for e in node:
                yield from walk(e)

    parsed_count = sum(1 for _ in walk(doc))
    if raw_count != parsed_count:
        problems.append(
            f"raw/parsed: {raw_count} '- reference_id:' lines in the file but "
            f"{parsed_count} parsed supported_by entries. Do not explain the gap away - a "
            f"duplicate mapping key silently discards the earlier value."
        )


def run(review_text: str | None = None) -> list[str]:
    problems: list[str] = []
    raw = review_text if review_text is not None else REVIEW.read_text()
    try:
        doc = yaml.load(raw, Loader=StrictLoader)
    except yaml.YAMLError as exc:
        return [f"YAML: {exc}"]
    goa = load_goa(GOA)
    notes = NOTES.read_text()
    results = json.loads(RESULTS_JSON.read_text())

    check_row_coverage(doc, goa, problems)
    check_source_entities(doc, goa, problems)
    check_supporting_entities(doc, goa, problems)
    check_motif_claims(doc, notes, results, problems)
    check_retracted_phrasings(raw, notes, problems)
    if review_text is None:
        check_raw_vs_parsed(problems)
    return problems


def self_test() -> int:
    """Each mutation must make the audit fail. Assert the target exists before mutating,
    so a drifted anchor is an error rather than a guard that silently proves nothing."""
    base = REVIEW.read_text()
    if run(base):
        print("SELF-TEST ABORTED: the unmutated document already fails")
        for p in run(base):
            print("  -", p)
        return 1

    mutations = [
        ("drop a source_entity", "      - source_id: SGD:S000006030", ""),
        ("relabel a source_id", "source_id: MGI:MGI:1889336", "source_id: MGI:MGI:9999999"),
        ("revert a verdict to PENDING", "    action: MARK_AS_OVER_ANNOTATED",
         "    action: PENDING"),
        ("delete a whole annotation entry", "- term:\n    id: GO:0010795", "- term:\n    id: GO:9999999"),
        ("assert a refuted claim", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: ADCK2 is a serine/threonine kinase"),
        ("assert the pseudokinase claim", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: the protein is a pseudokinase"),
        ("assert ADCK2 catalyses a pathway step", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: ADCK2 catalyses a step of CoQ synthesis"),
        # Decoy negator in a DIFFERENT clause: the guard must not be disarmed by an
        # incidental "no" that does not negate the claim itself.
        ("decoy negator before an asserted claim", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: there is no purified protein, and ADCK2 is"
         " a serine/threonine kinase"),
        ("decoy negator across a full stop", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: the assay was not run. ADCK2 is a"
         " serine/threonine kinase"),
    ]
    failures = 0

    # False-positive tests: these mutations are CORRECT statements and must NOT be
    # flagged. Two successive versions of the retracted-phrasing check failed exactly
    # here, so the "guard must stay quiet" case is tested as deliberately as the
    # "guard must fire" case.
    must_not_fire = [
        ("negated pseudokinase claim", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: neither gene is a pseudokinase"),
        ("negated kinase claim", "gene_symbol: ADCK2",
         "gene_symbol: ADCK2\ndescription_note: it is not the case that ADCK2 is a"
         " serine/threonine kinase"),
    ]
    for name, target, replacement in must_not_fire:
        if target not in base:
            print(f"  BROKEN GUARD: false-positive target for {name!r} not present")
            failures += 1
            continue
        if run(base.replace(target, replacement, 1)):
            print(f"  FALSE POSITIVE: {name} was flagged but is a correct statement")
            failures += 1
        else:
            print(f"  correctly ignored: {name}")

    for name, target, replacement in mutations:
        if target not in base:
            print(f"  BROKEN GUARD: mutation target for {name!r} not present in the file; "
                  f"this self-test proves nothing")
            failures += 1
            continue
        mutated = base.replace(target, replacement, 1)
        if mutated == base:
            print(f"  BROKEN GUARD: mutation {name!r} was a no-op")
            failures += 1
            continue
        if not run(mutated):
            print(f"  NOT CAUGHT: {name}")
            failures += 1
        else:
            print(f"  caught: {name}")
    print("self-test:", "PASS" if failures == 0 else f"FAIL ({failures})")
    return 1 if failures else 0


def main() -> int:
    if "--self-test" in sys.argv:
        return self_test()
    problems = run()
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print("  -", p)
        return 1
    print("audit: all invariants hold")
    return 0


if __name__ == "__main__":
    sys.exit(main())
