#!/usr/bin/env python3
"""Invariants that must hold between AEBP2's review YAML, its notes, and each other.

These are the failure classes that no repo gate covers, each selected on a **stable
entity** (a GO id, an action value, a row index) rather than on a conclusion's wording,
because the wording is exactly what gets reworded when a verdict changes.

Checks, and what each exists to catch:

A. **Summary opener vs action.** A verdict recalibrated late leaves the summary's first
   clause naming the old action, in the position a human reads first.
B. **Same term, same action.** The repo validator enforces this (exempting GO:0005515);
   duplicating it here means a violation is caught before validation runs.
C. **Hedge sweep.** For every term this review *declines* in prose, no structured slot
   may assert it. A reviewer reads the prose; a machine reads only the slot.
D. **Complex terms belong in `in_complex`, never in `locations`.**
E. **No curation or project commentary in `description`.**
F. **Every `NEW` row whose claim is isoform-specific carries an `isoform`.**
G. **The notes' verdict table agrees with the YAML**, term by term, both directions:
   every term in the YAML has a notes row naming its action, and every term named in the
   notes table exists in the YAML. Writing only the first direction is how a stale notes
   row survives.

    uv run --no-project python audit_review_consistency.py
    uv run --no-project python audit_review_consistency.py --self-test
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REVIEW = GENE_DIR / "AEBP2-ai-review.yaml"
NOTES = GENE_DIR / "AEBP2-notes.md"

# Openers are matched case-insensitively against the summary's first words. The list is
# deliberately permissive about phrasing and strict about *direction*: check A's real work
# is done by CONTRADICTING_PHRASES below, which fires on an opener naming another action.
ACCEPTABLE_OPENERS = {
    "ACCEPT": ("correct", "the term is correct", "sound", "direct", "part of",
               "the oldest", "a keyword", "the companion", "a reactome",
               "the same reactome", "the third reactome"),
    "KEEP_AS_NON_CORE": ("retained", "a complexportal", "the same complexportal"),
    "MARK_AS_OVER_ANNOTATED": ("over-annotated", "the same complex-level"),
    "NEW": ("proposed",),
}
# A phrase that names a DIFFERENT action than the row carries. An *attributed* mention of
# another row's action is legitimate cross-referencing and is not matched here, because
# these are tested only against the summary's opening sentence.
CONTRADICTING_PHRASES = {
    "ACCEPT": ("over-annotated", "removed", "not supported"),
    "KEEP_AS_NON_CORE": ("accepted.", "over-annotated", "removed"),
    "MARK_AS_OVER_ANNOTATED": ("accepted.", "correct and core"),
    "NEW": ("accepted.", "over-annotated"),
}

# Terms this review argues against in prose. Selected on the GO id, which does not get
# line-wrapped or reworded.
DECLINED_TERMS = {
    "GO:0042393": "histone binding - the structures show AEBP2 mimicking an H3 tail, "
                  "not binding a histone",
    "GO:0003677": "DNA binding - both measurements are on the mouse protein",
    "GO:0003712": "transcription coregulator activity - no human PRC2 subunit carries it, "
                  "and its definition requires binding a DNA-binding transcription factor",
    "GO:0008047": "enzyme activator activity - the direction of AEBP2's effect is disputed",
}

STRUCTURED_TERM_SLOTS = {
    "molecular_function", "contributes_to_molecular_function", "directly_involved_in",
    "locations", "anatomical_locations", "substrates", "in_complex",
}

FORBIDDEN_IN_DESCRIPTION = (
    "this review", "curation", "GOA", "should be annotated", "should not be annotated",
    "over-annotat", "PAINT", "affinage", "ACCEPT", "proposed",
)


def structured_terms(node, out: set[tuple[str, str]]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key in STRUCTURED_TERM_SLOTS:
                for term in (value if isinstance(value, list) else [value]):
                    if isinstance(term, dict) and "id" in term:
                        out.add((key, term["id"]))
            structured_terms(value, out)
    elif isinstance(node, list):
        for value in node:
            structured_terms(value, out)


def audit(review_path: Path = REVIEW, notes_path: Path = NOTES) -> list[str]:
    problems: list[str] = []
    doc = yaml.safe_load(review_path.read_text())
    notes = notes_path.read_text()

    annotations = doc.get("existing_annotations") or []
    # A block with no annotations must FAIL LOUDLY rather than pass vacuously.
    if not annotations:
        problems.append("existing_annotations is empty or missing - audit would pass vacuously")
        return problems

    # --- A. summary opener vs action -------------------------------------------------
    for i, ann in enumerate(annotations):
        review = ann.get("review") or {}
        action = review.get("action")
        summary = " ".join((review.get("summary") or "").split()).lower()
        if not action:
            problems.append(f"row {i} {ann['term']['id']}: no action - cannot be checked")
            continue
        if not summary:
            problems.append(f"row {i} {ann['term']['id']}: no summary - cannot be checked")
            continue
        if action not in ACCEPTABLE_OPENERS:
            problems.append(f"row {i} {ann['term']['id']}: action {action!r} not covered by this audit")
            continue
        if not any(summary.startswith(o) for o in ACCEPTABLE_OPENERS[action]):
            problems.append(
                f"row {i} {ann['term']['id']} action={action}: summary opener does not "
                f"match the action: {summary[:80]!r}"
            )
        first_sentence = summary.split(".")[0] + "."
        for bad in CONTRADICTING_PHRASES[action]:
            if bad in first_sentence:
                problems.append(
                    f"row {i} {ann['term']['id']} action={action}: opening sentence names a "
                    f"different action ({bad!r})"
                )

    # --- B. same term, same action ---------------------------------------------------
    by_term: dict[str, set[str]] = defaultdict(set)
    for ann in annotations:
        if (ann.get("review") or {}).get("action") != "NEW":
            by_term[ann["term"]["id"]].add(ann["review"]["action"])
    for term, actions in by_term.items():
        if len(actions) > 1:
            problems.append(f"{term}: conflicting actions across rows: {sorted(actions)}")

    # --- C. hedge sweep --------------------------------------------------------------
    asserted: set[tuple[str, str]] = set()
    structured_terms(doc.get("core_functions") or [], asserted)
    row_terms = {ann["term"]["id"] for ann in annotations}
    for go_id, why in DECLINED_TERMS.items():
        slots = sorted(slot for slot, term in asserted if term == go_id)
        if slots:
            problems.append(
                f"{go_id} is declined in prose but asserted in structured slot(s) {slots}: {why}"
            )
        if go_id in row_terms:
            problems.append(
                f"{go_id} is declined in prose but present as an annotation row: {why}"
            )

    # --- D. complex terms out of locations -------------------------------------------
    for i, cf in enumerate(doc.get("core_functions") or []):
        locations = {t["id"] for t in (cf.get("locations") or [])}
        complex_term = (cf.get("in_complex") or {}).get("id")
        if complex_term and complex_term in locations:
            problems.append(f"core_functions[{i}]: complex term {complex_term} also in locations")

    # --- E. description hygiene ------------------------------------------------------
    description = doc.get("description") or ""
    if not description or description.startswith("TODO"):
        problems.append("description is missing or still a TODO stub")
    for phrase in FORBIDDEN_IN_DESCRIPTION:
        if phrase.lower() in description.lower():
            problems.append(f"description contains curation/project commentary: {phrase!r}")

    # --- F. isoform scoping on NEW rows ---------------------------------------------
    for ann in annotations:
        if (ann.get("review") or {}).get("action") == "NEW" and not ann.get("isoform"):
            problems.append(
                f"NEW row {ann['term']['id']} has no isoform field; every proposal in this "
                "review is isoform-scoped, so an unscoped one is almost certainly an omission"
            )

    # --- G. notes verdict table, BOTH directions ------------------------------------
    notes_rows = dict(re.findall(r"^\| `(GO:\d+)`[^|]*\|[^|]*\|[^|]*\| ([A-Z_]+) \|$",
                                 notes, re.M))
    if not notes_rows:
        problems.append("no verdict table found in the notes - check G would pass vacuously")
    for term, actions in by_term.items():
        action = next(iter(actions))
        if term not in notes_rows:
            problems.append(f"notes verdict table has no row for {term}")
        elif notes_rows[term] != action:
            problems.append(
                f"notes verdict table gives {term} action {notes_rows[term]}, "
                f"YAML says {action}"
            )
    # the reverse direction: a notes row for a term the YAML no longer carries
    for term in notes_rows:
        if term not in by_term and term not in row_terms:
            problems.append(f"notes verdict table names {term}, which is absent from the YAML")

    expected = f"20 existing rows + 2 NEW = {len(annotations)}"
    if expected not in notes:
        problems.append(
            f"notes row-count sentence does not state {expected!r}; the YAML has "
            f"{len(annotations)} entries"
        )

    print(f"audited {len(annotations)} annotation rows, "
          f"{len(doc.get('core_functions') or [])} core functions, "
          f"{len(by_term)} distinct existing terms; {len(problems)} problem(s)")
    return problems


def self_test() -> int:
    """Break-test every check in the direction it exists to catch, and assert the
    failure MESSAGE. Also test the happy path, which is the one that goes untested."""
    import tempfile

    failures: list[str] = []
    raw = REVIEW.read_text()
    notes_raw = NOTES.read_text()

    def run(review_text: str, notes_text: str = notes_raw) -> list[str]:
        with tempfile.TemporaryDirectory() as td:
            r = Path(td) / "r.yaml"
            n = Path(td) / "n.md"
            r.write_text(review_text)
            n.write_text(notes_text)
            return audit(r, n)

    def expect(label: str, review_text: str, needle: str, notes_text: str = notes_raw) -> None:
        problems = run(review_text, notes_text)
        blob = " || ".join(problems)
        if not problems:
            failures.append(f"{label}: guard did not fire")
        elif needle not in blob:
            failures.append(f"{label}: fired but message lacks {needle!r}: {blob!r}")

    # happy path
    clean = audit(REVIEW, NOTES)
    if clean:
        failures.append(f"the real files are not clean: {clean}")

    # A: an opener naming the wrong action. Assert the anchor first so a drifted target
    # cannot turn the mutation into a silent no-op.
    anchor_a = "summary: >-\n      Over-annotated for this protein."
    if anchor_a not in raw:
        failures.append(f"check-A anchor absent: {anchor_a!r}")
    else:
        expect("A: opener names the wrong action",
               raw.replace(anchor_a, "summary: >-\n      Accepted. For this protein.", 1),
               "opener does not match the action")

    # B: two actions on one term.
    anchor_b = "      Complex-level in provenance, correct in substance, and independently supported on this gene\n      by the EXP row from PMID:29499137.\n    supported_by:"
    if anchor_b not in raw:
        failures.append("check-B anchor absent")
    else:
        expect("B: conflicting actions on one term",
               raw.replace("    action: ACCEPT\n    reason: >-\n      Complex-level in provenance",
                           "    action: REMOVE\n    reason: >-\n      Complex-level in provenance", 1),
               "conflicting actions across rows")

    # C: a declined term asserted in a structured slot.
    anchor_c = "  contributes_to_molecular_function:\n    id: GO:0031491\n    label: nucleosome binding"
    if anchor_c not in raw:
        failures.append("check-C anchor absent")
    else:
        expect("C: declined term asserted structurally",
               raw.replace(anchor_c,
                           "  contributes_to_molecular_function:\n    id: GO:0042393\n    label: histone binding", 1),
               "declined in prose but asserted in structured slot")

    # D: complex term placed in locations.
    anchor_d = "  locations:\n  - id: GO:0000785\n    label: chromatin"
    if anchor_d not in raw:
        failures.append("check-D anchor absent")
    else:
        expect("D: complex term in locations",
               raw.replace(anchor_d,
                           "  locations:\n  - id: GO:0035098\n    label: ESC/E(Z) complex", 1),
               "also in locations")

    # E: curation commentary in the description.
    expect("E: commentary in description",
           raw.replace("description: >-\n  AEBP2 is a nuclear",
                       "description: >-\n  In this review GOA is over-annotated. AEBP2 is a nuclear", 1),
           "curation/project commentary")

    # F: a NEW row with no isoform.
    anchor_f = "  qualifier: contributes_to\n  isoform: Q6ZN18-1"
    if anchor_f not in raw:
        failures.append("check-F anchor absent")
    else:
        expect("F: NEW row without isoform",
               raw.replace(anchor_f, "  qualifier: contributes_to", 1),
               "has no isoform field")

    # G forward: notes table disagrees with the YAML.
    expect("G: notes action disagrees",
           raw,
           "notes verdict table gives GO:0031507 action ACCEPT",
           notes_raw.replace("| `GO:0031507` heterochromatin formation | 2 | NAS ×2 | MARK_AS_OVER_ANNOTATED |",
                             "| `GO:0031507` heterochromatin formation | 2 | NAS ×2 | ACCEPT |", 1))
    # G reverse: a notes row for a term the YAML does not carry. Writing only the forward
    # direction is how a stale notes row survives, so both are exercised.
    expect("G: stale notes row",
           raw,
           "which is absent from the YAML",
           notes_raw.replace("| `GO:0031507` heterochromatin formation | 2 | NAS ×2 | MARK_AS_OVER_ANNOTATED |",
                             "| `GO:0031507` heterochromatin formation | 2 | NAS ×2 | MARK_AS_OVER_ANNOTATED |\n"
                             "| `GO:0099999` invented term | 1 | IEA | ACCEPT |", 1))
    # G vacuity: no table at all must fail, not pass.
    expect("G: no verdict table",
           raw, "would pass vacuously",
           re.sub(r"^\| `GO:.*$", "", notes_raw, flags=re.M))

    # vacuity: an empty annotation list must fail loudly.
    expect("vacuous review", "id: Q6ZN18\ndescription: x\n", "pass vacuously")

    for f in failures:
        print(f"SELF-TEST FAILURE: {f}", file=sys.stderr)
    print(f"self-test: {len(failures)} failure(s)")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    problems = audit()
    for p in problems:
        print("PROBLEM:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
