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
J. **A DNA-binding suppression claim names its arm.** Five variants of one sentence shipped on
   this gene saying the long isoform "suppresses PRC2 DNA binding" without saying which
   measurement. The arms differ: below baseline for the methyltransferase and for chromatin
   occupancy in cells, but merely *at* baseline on a naked-DNA probe. A literal phrase pin caught
   four and missed the fifth, so this check anchors on the claim's **shape** - suppression verb +
   DNA-binding marker + long-isoform subject, minus any arm qualifier - which survives rewording.
G. **The notes' verdict table agrees with the YAML**, term by term, both directions:
   every term in the YAML has a notes row naming its action, and every term named in the
   notes table exists in the YAML. Writing only the first direction is how a stale notes
   row survives.
I. **An isoform scope is single-sourced.** The blocking defect on this gene was a
   `core_functions` description excluding isoform 2 from an activity the cited paper shows it
   has, while the annotation row's own reason had it right. Two surfaces could express the
   scope, so correcting one left the other. Rather than adding a third assertion, the scope is
   now one canonical clause required verbatim in both surfaces, so editing one without the
   other fires.
H. **Prose numbers are tied to ``results.json``.** A hand-written count drifts the moment
   the underlying query changes, and it drifted here: the PRC2 census covers 12 proteins and
   two surfaces said "eleven". Each claim below names the JSON key it comes from, so a
   changed measurement breaks the check instead of quietly falsifying the sentence.

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

# Check J. The structural trigger, replacing what a literal phrase pin could not close.
# The recurring defect is a sentence that says the long isoform DECREASES something about DNA
# binding without naming which arm - and the two arms differ: below baseline for the
# methyltransferase and for chromatin occupancy in cells, but merely AT baseline on a naked-DNA
# probe in vitro. So any sentence pairing a suppression verb with "DNA binding" must also carry
# an arm qualifier. This fires on paraphrase because it matches the claim's shape, not its
# wording. Five variants of this sentence shipped on this gene before it existed.
SUPPRESSION_VERBS = ("suppress", "inhibit", "impair", "reduce", "lower", "decreas", "restrain")
DNA_BINDING_MARKERS = ("dna binding", "dna-binding", "binding to dna", "affinity for dna",
                       "bind the dna", "binds dna")
ARM_QUALIFIERS = (
    "in cells", "chromatin occupancy", "on chromatin", "at baseline", "naked", "in vitro probe",
    "the short form confers", "the short isoform confers", "no better than",
    "target genes in cells", "no-rescue",
)

STRUCTURED_TERM_SLOTS = {
    "molecular_function", "contributes_to_molecular_function", "directly_involved_in",
    "locations", "anatomical_locations", "substrates", "in_complex",
}

RESULTS_JSON = HERE / "results.json"

# Check H. Each entry is (label, key path into results.json, a function turning the measured
# value into the exact substring the prose must contain, and the surfaces it must appear in).
# Selecting on the measured NUMBER means a changed measurement breaks the check; selecting on
# the sentence would not, because the sentence is what gets reworded.
NUMERIC_CLAIMS = [
    (
        "size of the PRC2 molecular-function census",
        lambda r: len(r["prc2_mf_census"]["subunits"]),
        lambda v: f"the {v} PRC2-associated proteins surveyed",
        ("review",),
    ),
    (
        "size of the PRC2 census, second surface",
        lambda r: len(r["prc2_mf_census"]["subunits"]),
        lambda v: f"one of the {v} PRC2-associated human proteins surveyed",
        ("review",),
    ),
    (
        "GO:0031507 NAS-only count",
        lambda r: len(r["prc2_mf_census"]["GO_0031507_NAS_only_subunits"]),
        lambda v: f"{v} of those 11 hold it by NAS alone",
        ("review",),
    ),
    (
        "TFClass recipients denominator",
        lambda r: r["tfclass_dbtf"]["n_recipients"],
        lambda v: f"GO_REF:0000113 covers {v} human",
        ("review",),
    ),
    (
        "TFClass DbTF numerator",
        lambda r: r["tfclass_dbtf"]["n_with_GO_0000981_dbtf_activity"],
        lambda v: f"{v} of which (97.5%) receive GO:0000981",
        ("review",),
    ),
    (
        "TFClass withheld-set size",
        lambda r: r["tfclass_dbtf"]["n_without_GO_0000981"],
        lambda v: f"AEBP2 is one of {v} given",
        ("review",),
    ),
    (
        "PANTHER node recipient count",
        lambda r: r["panther_node"]["n_recipients"],
        lambda v: f"the node reaches {v}",
        ("review",),
    ),
    (
        "PANTHER node GO:0035098 recipients",
        lambda r: r["panther_node"]["n_with_both_terms"],
        lambda v: f"gives GO:0035098 to only {v} of them",
        ("review",),
    ),
    (
        "ARBA condition-set count",
        lambda r: r["funfam_match"]["n_condition_sets"],
        lambda v: f"from {v} alternative condition sets",
        ("review",),
    ),
    (
        "PDB entries with an AEBP2 chain",
        lambda r: r["pdb_constructs"]["n_pdb_entries_with_an_AEBP2_chain"],
        lambda v: f"of {v} PDB entries resolving",
        ("review",),
    ),
    (
        "N-terminally truncated PDB constructs",
        lambda r: r["pdb_constructs"]["n_n_terminally_truncated"],
        lambda v: f"{v} declare an N-terminally truncated construct",
        ("review", "notes"),
    ),
    (
        "GO:0180000 annotation count in GOA",
        lambda r: r["go0180000"]["n_annotations_in_goa"],
        lambda v: f"GO:0180000 has {v} annotations in GOA",
        ("review",),
    ),
    (
        "isoform-2 overlap with the nucleosome-binding region",
        lambda r: r["isoform_mapping"]["overlap_residues"],
        lambda v: f"removes {v} of the 23 residues",
        ("review",),
    ),
]

# Check I. The isoform scope of GO:0031491 is expressible on two surfaces - the
# core_functions description and the annotation row's reason - so it is single-sourced as one
# canonical clause required verbatim on both. Selecting on the clause rather than on either
# sentence means a reworded surface fires instead of silently diverging.
CANONICAL_ISOFORM_CLAUSE = (
    "it is strongest in the isoforms that retain the full C-terminus, isoforms 1 and "
    "3, and isoform 2 supports the activity but roughly twofold less well"
)
CANONICAL_CLAUSE_SURFACES = 2
# Wordings retracted on this gene. A literal pin CANNOT catch a paraphrase, and this list is
# kept only for the exact sentences that were wrong. The reviewer found a fifth variant that
# none of these match, which is why check J below anchors on the CLAIM'S SHAPE instead.
RETRACTED_PHRASES = (
    "scoped to the isoforms that retain the full C-terminus",
    "the form assayed with the full C-terminus",
    "suppresses PRC2 DNA binding and methyltransferase",
)

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

    # --- H. prose numbers tied to results.json --------------------------------------
    if not RESULTS_JSON.exists():
        problems.append(
            f"{RESULTS_JSON.name} missing - run analyze_aebp2.py; check H cannot run and "
            "would otherwise pass vacuously"
        )
    else:
        import json as _json
        measured = _json.loads(RESULTS_JSON.read_text())
        surfaces = {"review": review_path.read_text(), "notes": notes}
        if not NUMERIC_CLAIMS:
            problems.append("NUMERIC_CLAIMS is empty - check H would pass vacuously")
        for label, extract, phrase_of, where in NUMERIC_CLAIMS:
            try:
                value = extract(measured)
            except (KeyError, TypeError) as exc:
                problems.append(f"check H: cannot read {label} from results.json: {exc}")
                continue
            phrase = phrase_of(value)
            for surface in where:
                text = " ".join(surfaces[surface].split())
                if " ".join(phrase.split()) not in text:
                    problems.append(
                        f"check H: {surface} does not state the measured {label} "
                        f"({value}); expected the phrase {phrase!r}"
                    )

    # --- I. single-sourced isoform scope, and no retracted wording ------------------
    normalised = " ".join(review_path.read_text().split())
    canonical = " ".join(CANONICAL_ISOFORM_CLAUSE.split())
    occurrences = normalised.count(canonical)
    if occurrences != CANONICAL_CLAUSE_SURFACES:
        problems.append(
            f"the canonical isoform-scope clause appears {occurrences} time(s), expected "
            f"{CANONICAL_CLAUSE_SURFACES} (core_functions description and the GO:0031491 row "
            "reason). A scope stated on one surface and not the other is how the blocking "
            "defect on this gene arose"
        )
    for phrase in RETRACTED_PHRASES:
        if " ".join(phrase.split()) in normalised:
            problems.append(f"retracted wording has reappeared: {phrase!r}")

    # --- J. a DNA-binding suppression claim must name its arm ------------------------
    # Sentence-splitting the whole file produces chunks that span unrelated fields - the first
    # version of this check fired on a run-together of a supporting_text quote and a term label.
    # So it walks the PARSED document's prose fields and splits within each one. supporting_text
    # is excluded on purpose: it is someone else's sentence, not a claim this review makes.
    PROSE_FIELDS = ("description", "summary", "reason", "review_notes", "justification",
                    "gap_statement", "boundary", "significance", "question", "comment",
                    "proposed_definition", "hypothesis")
    def prose_strings(node, out):
        if isinstance(node, dict):
            for k, v in node.items():
                if k in PROSE_FIELDS and isinstance(v, str):
                    out.append(v)
                else:
                    prose_strings(v, out)
        elif isinstance(node, list):
            for v in node:
                prose_strings(v, out)
    blocks: list[str] = []
    prose_strings(doc, blocks)
    if not blocks:
        problems.append("check J collected no prose fields - it would pass vacuously")
    sentences = [s for block in blocks
                 for s in re.split(r"(?<=[.;])\s+", " ".join(block.split()))]
    flagged = 0
    for sentence in sentences:
        low = sentence.lower()
        if not any(v in low for v in SUPPRESSION_VERBS):
            continue
        if not any(m in low for m in DNA_BINDING_MARKERS):
            continue
        # A sentence reporting what the SHORT form does is not the defect; the defect is an
        # unqualified claim about the long form.
        if not any(x in low for x in ("aebp2l", "long isoform", "long form", "long protein form",
                                      "dominant isoform", "isoforms 1 and 2")):
            continue
        if not any(q in low for q in ARM_QUALIFIERS):
            problems.append(
                "check J: a DNA-binding suppression claim about the long isoform does not name "
                "its arm (below baseline for HMTase and for chromatin occupancy in cells, but "
                f"only AT baseline on the in vitro probe): {sentence[:170]!r}"
            )
        else:
            flagged += 1
    # Vacuity guard. The first version required at least one *qualified* suppression claim,
    # which a correctly-written file need not contain at all - it failed on perfect agreement,
    # the classic guard-defeat mode. The precondition that a correct file CAN satisfy is that
    # the matcher reaches DNA-binding prose at all.
    reachable = sum(1 for s in sentences
                    if any(m in s.lower() for m in DNA_BINDING_MARKERS))
    if reachable == 0:
        problems.append(
            "check J found no sentence mentioning DNA binding anywhere in the review's prose "
            "fields - the matcher is not reaching the prose and a clean result is meaningless"
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
    anchor_f = "  qualifier: contributes_to\n  isoform: Q6ZN18-2"
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

    # H forward: a prose number that no longer matches the measurement must fire. The
    # mutation is exactly the distinction claimed - one digit - not a blanked surface that
    # a much weaker implementation would also catch.
    anchor_h = "one of the 12 PRC2-associated human proteins surveyed"
    if anchor_h not in raw:
        failures.append(f"check-H anchor absent: {anchor_h!r}")
    else:
        expect("H: prose number drifted from the measurement",
               raw.replace(anchor_h, "one of the 11 PRC2-associated human proteins surveyed", 1),
               "does not state the measured size of the PRC2 census")
    # H second direction: a number written as a WORD is invisible to the check, which is the
    # defect that produced this guard. Spelling it out must fire, not pass.
    anchor_h2 = "from 8 alternative condition sets"
    if anchor_h2 not in raw:
        failures.append(f"check-H word-form anchor absent: {anchor_h2!r}")
    else:
        expect("H: number spelled as a word",
               raw.replace(anchor_h2, "from eight alternative condition sets", 1),
               "does not state the measured ARBA condition-set count")

    # I forward: dropping the clause from ONE surface must fire. This is the exact defect
    # that shipped, not a coarser mutation that a weaker implementation would also catch.
    # The clause is line-wrapped differently on its two surfaces, so the mutation targets a
    # short fragment that survives wrapping and appears exactly twice.
    frag = "and isoform 2 supports the activity but"
    if raw.count(frag) != 2:
        failures.append(
            f"check-I fragment appears {raw.count(frag)} times, expected 2; the break-test "
            "cannot discriminate one surface from two"
        )
    else:
        one_removed = raw.replace(frag, "and isoform 2 does not have the activity, since it", 1)
        expect("I: scope dropped from one surface", one_removed,
               "canonical isoform-scope clause appears 1 time(s)")
    # I reverse: the retracted wording reappearing must fire, even alongside a correct clause.
    expect("I: retracted wording reappears",
           raw.replace("in_complex:", "in_complex:  # scoped to the isoforms that retain the full C-terminus\n", 1),
           "retracted wording has reappeared")

    # J: the paraphrase the literal pin could not catch must now fire. The mutation is exactly
    # the distinction claimed - an arm qualifier removed - not a blanked surface.
    # Run the check against the sentence that ACTUALLY SHIPPED and was flagged in review -
    # a stronger claim than any mutation I would have invented. Reproduced verbatim from
    # commit 80c1459c9, where it sat at AEBP2-ai-review.yaml:1056-1058.
    shipped_defect = (
        "N-terminal region present in isoforms 1 and 2 - the forms found in essentially all human\n"
        "    tissues - suppresses the complex's DNA binding and takes its histone methyltransferase\n"
        "    activity below the level of the core complex alone."
    )
    current = (
        "N-terminal region present in isoforms 1 and 2 - the forms found in essentially all human\n"
        "    tissues - takes the complex's histone methyltransferase activity below the level of the core\n"
        "    complex alone,"
    )
    if current not in raw:
        failures.append("check-J anchor absent; the corrected sentence has drifted")
    else:
        expect("J: the sentence that actually shipped and was flagged in review",
               raw.replace(current, shipped_defect, 1),
               "does not name its arm")
    # J vacuity direction: a document whose prose never mentions DNA binding must FAIL, because
    # a clean result from a matcher that reaches nothing is meaningless.
    expect("J: vacuity when the matcher reaches no DNA-binding prose",
           "id: Q6ZN18\ndescription: A nuclear protein.\nexisting_annotations:\n- term:\n    id: GO:1\n"
           "    label: x\n  evidence_type: IDA\n  isoform: Q6ZN18-1\n  review:\n"
           "    summary: Proposed x.\n    action: NEW\n",
           "no sentence mentioning DNA binding")

    # vacuity: an empty annotation list must fail loudly.
    expect("vacuous review", "id: Q6ZN18\ndescription: x\n", "pass vacuously")

    for f in failures:
        print(f"SELF-TEST FAILURE: {f}", file=sys.stderr)
    print(f"self-test: {len(failures)} failure(s)")
    return 1 if failures else 0


def history() -> int:
    """Run check J against every version of the review this branch has pushed.

    A self-test proves the guards you thought of fire. Running the guard against the defects
    that actually shipped is the stronger claim, and it demonstrates coverage of the *class*
    rather than of one instance. Expected, and asserted: the count decreases monotonically to
    zero, and the version the reviewer flagged shows exactly the one variant the earlier
    literal-phrase pin could not match.
    """
    import subprocess

    shas = ["a50319089", "c58380583", "80c1459c9"]
    subjects = ("aebp2l", "long isoform", "long form", "long protein form",
                "dominant isoform", "isoforms 1 and 2")

    def flags(text: str) -> list[str]:
        doc = yaml.safe_load(text)
        blocks: list[str] = []
        fields = ("description", "summary", "reason", "review_notes", "justification",
                  "gap_statement", "boundary", "significance", "question", "comment",
                  "proposed_definition", "hypothesis")

        def walk(node):
            if isinstance(node, dict):
                for k, v in node.items():
                    if k in fields and isinstance(v, str):
                        blocks.append(v)
                    else:
                        walk(v)
            elif isinstance(node, list):
                for v in node:
                    walk(v)

        walk(doc)
        sentences = [s for b in blocks
                     for s in re.split(r"(?<=[.;])\s+", " ".join(b.split()))]
        out = []
        for s in sentences:
            low = s.lower()
            if (any(v in low for v in SUPPRESSION_VERBS)
                    and any(m in low for m in DNA_BINDING_MARKERS)
                    and any(x in low for x in subjects)
                    and not any(q in low for q in ARM_QUALIFIERS)):
                out.append(s)
        return out

    counts = []
    for sha in shas:
        proc = subprocess.run(
            ["git", "show", f"{sha}:genes/human/AEBP2/AEBP2-ai-review.yaml"],
            capture_output=True, text=True, cwd=REPO_ROOT if (REPO_ROOT := HERE.parents[3]) else None,
        )
        if proc.returncode != 0 or len(proc.stdout.splitlines()) < 500:
            print(f"{sha}: could not extract a plausible review file "
                  f"({len(proc.stdout.splitlines())} lines) - a zero here would be meaningless",
                  file=sys.stderr)
            return 1
        hits = flags(proc.stdout)
        counts.append(len(hits))
        print(f"{sha}: check J flags {len(hits)}")
        for h in hits:
            print(f"    {h[:130]}")
    current = len(flags(REVIEW.read_text()))
    counts.append(current)
    print(f"current: check J flags {current}")

    problems = []
    if counts != sorted(counts, reverse=True):
        problems.append(f"counts are not monotonically decreasing: {counts}")
    if current != 0:
        problems.append(f"the current file still has {current} unqualified claim(s)")
    if counts[0] < 2:
        problems.append(
            f"the first pushed version flags only {counts[0]}; the check is not demonstrating "
            "coverage of the class"
        )
    if counts[-2] != 1:
        problems.append(
            f"the reviewer-flagged version flags {counts[-2]}, expected exactly 1 - the variant "
            "the literal-phrase pin could not match"
        )
    for p_ in problems:
        print("PROBLEM:", p_, file=sys.stderr)
    print(f"history: {len(problems)} problem(s)")
    return 1 if problems else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--history", action="store_true",
                    help="run check J against every version this branch pushed")
    args = ap.parse_args()
    if args.self_test:
        return self_test()
    if args.history:
        return history()
    problems = audit()
    for p in problems:
        print("PROBLEM:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
