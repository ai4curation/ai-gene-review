#!/usr/bin/env python3
"""Keep AADACL2, AADACL3 and AADACL4 in agreement about the PTN009058710 hydrolase row.

Why this exists rather than a resolution to be more careful: five items on the PR that produced
this file (9, 13, 17, 18, 22) were the *same* defect — a claim corrected in one file and left
standing in another — twice inside the very journal that recorded the lesson. A hand-checked list
did not work five times, so the checks are code.

Two things are enforced, over the reviews, the notes files and the shared audit prose:

  1. the agreement invariant. The three paralogs carry one identical `GO:0016787` IBA row
     (GO_REF:0000033, PANTHER:PTN009058710, the same 17 WITH/FROM tokens), so their treatment of it
     must not diverge again: MODIFY -> GO:0052689, root_cause EVIDENCE_CIRCULAR_OR_REDUNDANT, no
     GRANULARITY_MISMATCH failure mode, supporting_entities equal to that gene's own GOA WITH/FROM
     column, core_functions molecular function GO:0052689, and the shared node audit cited.

     Also the assessment of InterPro:IPR013094, the fold-level signature that is the sole source of
     all three IEA rows. That field was missed twice: once by the harmonisation, and again by the
     three-line follow-up written to remove this exact class of divergence - because it sits one
     line below the field being fixed, so re-reading the edited block could not reveal it.

  2. the stale-claim greps. Statements that were true before the harmonisation are false after it,
     and they hid in notes files and in generated prose, not only in the YAML.

     Curator-facing text (the reviews, the shared audit prose, RESULTS.md) must contain no stale
     phrase at all, except in the audit's motivation section, which carries an explicit historical
     marker - and the marker's presence is itself checked, so the exemption cannot be used to
     smuggle a live claim through.

     Notes files are journals: a journal that records "X was wrong, now fixed" necessarily contains
     X, so a blanket grep would be unusable there. The rule instead distinguishes an *assertion*
     from a *quotation*: a stale phrase is allowed in a notes paragraph only if that paragraph, or
     the heading it sits under, carries a retrospective cue (superseded, no longer, corrected, "as
     merged", a Round-N heading, and so on). An unqualified stale sentence in running prose fails -
     which is exactly the shape of the AADACL3 notes section that survived four rounds.

Run:
    uv run --no-project python check_paralog_agreement.py            # check the tree
    uv run --no-project python check_paralog_agreement.py --self-test  # prove each guard fires

`--self-test` copies the tree to a temporary directory, breaks one guard at a time, and requires
each mutation to be caught. A check that has never failed is not known to work.

Exit status 0 = agreement holds. Non-zero prints every violation, not just the first.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import tempfile
from pathlib import Path

import yaml

GENES = ["AADACL2", "AADACL3", "AADACL4"]
TERM = "GO:0016787"
REF = "GO_REF:0000033"
REPLACEMENT = "GO:0052689"
ROOT_CAUSE = "EVIDENCE_CIRCULAR_OR_REDUNDANT"
CORE_MF = "GO:0052689"
AUDIT = "NODE_PTN009058710.md"
HISTORICAL_MARKER = "Historical: this section records the state that motivated the audit"

# The fold-level signature that every one of these three IEA rows cites as its only source. Its
# assessment has to agree too: a divergence here was missed by the harmonisation PR and then again
# by the three-line PR written to remove exactly this kind of divergence, because the field sits one
# line below the one being fixed.
FOLD_SOURCE = "InterPro:IPR013094"
FOLD_SOURCE_STATUS = "CIRCULAR_OR_REDUNDANT"
# Values retracted for this row: the root cause recorded on it is redundancy, which says nothing
# about source strength, and the fold-3 signature is not a weak source. They live in DIFFERENT
# enums, and a first version of this guard rejected both in source_status - where SOURCE_EVIDENCE_WEAK
# is not a permissible value at all, so that half was unreachable and read as coverage while the
# field it can legally occupy went unguarded.
RETRACTED_SOURCE_STATUS = "SOURCE_WEAK_OR_INFERRED"   # PropagationSourceStatusEnum
RETRACTED_FAILURE_MODE = "SOURCE_EVIDENCE_WEAK"       # PropagationFailureModeEnum

# Phrasings that were true before the three reviews were harmonised and are false after it.
# Each is (regex, why it is stale). Applied to reviews, notes and the audit prose alike.
STALE = [
    (r"TERM_SCOPING_PROBLEM",
     "the row is not a term-scoping problem; all three genes record EVIDENCE_CIRCULAR_OR_REDUNDANT"),
    (r"[Bb]oth cannot be right",
     "the three reviews no longer disagree about this row"),
    (r"needs a follow-up",
     "no follow-up is outstanding on this row"),
    (r"while keeping the mode on the literal reading",
     "no paralog keeps GRANULARITY_MISMATCH any more"),
    (r"IDA[^.]{0,70}?two of them",
     "all three family-node donors carry GO:0017171 by IDA, not two"),
    (r"two of them[^.]{0,70}?IDA",
     "all three family-node donors carry GO:0017171 by IDA, not two"),
    (r"IDA-supported by two",
     "all three family-node donors carry GO:0017171 by IDA, not two"),
    (r"held by IDA in two of them",
     "all three family-node donors carry GO:0017171 by IDA, not two"),
    (r"every donor at the family node",
     "the measured set is the donors PAINT cites at that node; membership is not enumerated"),
    (r"every donor at `PTN009058713`",
     "the measured set is the donors PAINT cites at that node; membership is not enumerated"),
    (r"catalytic serine on (?:AADACL2 )?position 189",
     "15 of 15 align their catalytic nucleophile there; 14 of 15 have a serine"),
    (r"not yet in the tree",
     "all three gene folders are present"),
    (r"folder is not in this tree",
     "all three gene folders are present"),
    (r"no folder in this tree",
     "all three gene folders are present"),
    (r"is not a hydrolase at all but a dehydratase",
     "HIDH is a bifunctional carboxylesterase/dehydratase with a GO:0106435 IDA"),
    (r"conflicts with the merged AADACL2 review",
     "the conflict was resolved; AADACL2 now carries AADACL3's verdict"),
    (r"gets contradictory advice",
     "the three reviews agree about this row"),
]

# A serine count that is superseded must carry its pointer in the same passage, not elsewhere
# in the file. Item 20 on the PR was exactly this placement failure.
SUPERSEDED_COUNTS = [
    (r"13[- ]of[- ]14", r"15 of 16", "the 13-of-14 serine count must point at the audit's 15 of 16"),
    (r"\*\*13 are serine\*\*", r"15 of 16|superseded",
     "the 13-are-serine table quote must sit near its supersession"),
]


def repo_root(start: Path) -> Path:
    p = start.resolve()
    while p != p.parent and not (p / "genes").is_dir():
        p = p.parent
    if not (p / "genes").is_dir():
        sys.exit("ERROR: could not find the repository root (no genes/ directory above this file)")
    return p


def gene_files(root: Path, gene: str) -> dict[str, Path]:
    d = root / "genes" / "human" / gene
    return {"review": d / f"{gene}-ai-review.yaml",
            "notes": d / f"{gene}-notes.md",
            "goa": d / f"{gene}-goa.tsv"}


def goa_with_from(path: Path, problems: list[str]) -> list[str] | None:
    if not path.exists():
        problems.append(f"{path}: missing; run `just fetch-gene human {path.parent.name}`")
        return None
    rows = [l for l in path.read_text().splitlines()
            if f"\t{TERM}\t" in l and "\tIBA\t" in l and f"\t{REF}\t" in l]
    if len(rows) != 1:
        problems.append(f"{path}: expected exactly one {TERM} IBA/{REF} row, found {len(rows)}")
        return None
    return rows[0].split("\t")[10].split("|")


def check_invariant(root: Path, problems: list[str]) -> None:
    """The six rows across three genes must say the same thing, and match GOA by construction."""
    token_sets: dict[str, list[str]] = {}
    for gene in GENES:
        f = gene_files(root, gene)
        if not f["review"].exists():
            problems.append(f"{f['review']}: missing")
            continue
        tokens = goa_with_from(f["goa"], problems)
        if tokens is not None:
            token_sets[gene] = tokens
        doc = yaml.safe_load(f["review"].read_text())
        anns = doc.get("existing_annotations") or []
        rows = [a for a in anns if a["term"]["id"] == TERM]
        if len(rows) != 2:
            problems.append(f"{gene}: expected 2 {TERM} rows (IBA + IEA), found {len(rows)}")
        for a in rows:
            ev = a.get("evidence_type")
            rv = a.get("review") or {}
            where = f"{gene} {TERM}/{ev}"
            if rv.get("action") != "MODIFY":
                problems.append(f"{where}: action is {rv.get('action')!r}, expected MODIFY")
            got = [t["id"] for t in (rv.get("proposed_replacement_terms") or [])]
            if got != [REPLACEMENT]:
                problems.append(f"{where}: replacement terms {got}, expected [{REPLACEMENT}]")
            pr = rv.get("propagation_review") or {}
            if pr.get("root_cause") != ROOT_CAUSE:
                problems.append(f"{where}: root_cause {pr.get('root_cause')!r}, expected {ROOT_CAUSE}")
            if RETRACTED_FAILURE_MODE in (pr.get("failure_modes") or []):
                problems.append(f"{where}: {RETRACTED_FAILURE_MODE} is recorded; every protein "
                                f"donor on this node carries its own experimental evidence, so the "
                                f"sources are not weak - the defect is that the term should not "
                                f"propagate, which root_cause already states")
            if "GRANULARITY_MISMATCH" in (pr.get("failure_modes") or []):
                problems.append(f"{where}: GRANULARITY_MISMATCH is recorded; the donors are "
                                f"heterogeneous, so the parent is their LCA and there is no "
                                f"granularity defect")
            if ev == "IBA" and tokens is not None:
                if a.get("supporting_entities") != tokens:
                    problems.append(f"{where}: supporting_entities do not equal this gene's GOA "
                                    f"WITH/FROM column ({len(a.get('supporting_entities') or [])} "
                                    f"vs {len(tokens)} tokens)")
            seen_fold = False
            for entity in pr.get("source_entities") or []:
                if entity.get("source_id") != FOLD_SOURCE:
                    continue
                seen_fold = True
                status = entity.get("source_status")
                if status == RETRACTED_SOURCE_STATUS:
                    problems.append(f"{where}: {FOLD_SOURCE} source_status is {status!r}, which was "
                                    f"retracted for this row - the root cause is redundancy, which "
                                    f"says nothing about source strength, and the fold-3 signature "
                                    f"is not a weak source; expected {FOLD_SOURCE_STATUS}")
                elif status != FOLD_SOURCE_STATUS:
                    problems.append(f"{where}: {FOLD_SOURCE} source_status is {status!r}, expected "
                                    f"{FOLD_SOURCE_STATUS} to match the sibling paralogs")
            # Presence is asserted, not assumed. A continue-on-mismatch loop passes silently when the
            # entity is deleted, the source_entities list is dropped, or source_id is relabelled -
            # i.e. the guard could be defeated by removing the thing it guards, which is the same
            # shape of hole this check was added to close.
            if ev == "IEA" and not seen_fold:
                problems.append(f"{where}: no {FOLD_SOURCE} source entity; it is the sole source of "
                                f"this row in all three paralogs, so its absence is a divergence, "
                                f"not an exemption")

        cf = doc.get("core_functions") or []
        if not cf or (cf[0].get("molecular_function") or {}).get("id") != CORE_MF:
            problems.append(f"{gene}: core_functions molecular_function is not {CORE_MF}")
        if not any(str(r.get("id", "")).endswith(AUDIT) for r in (doc.get("references") or [])):
            problems.append(f"{gene}: does not cite the shared node audit {AUDIT}")

    if len(token_sets) == len(GENES):
        distinct = {tuple(v) for v in token_sets.values()}
        if len(distinct) != 1:
            problems.append("the three genes' WITH/FROM sets are no longer identical: "
                            + str({g: len(v) for g, v in token_sets.items()}))
        elif len(next(iter(distinct))) != 17:
            problems.append(f"expected 17 WITH/FROM tokens, found {len(next(iter(distinct)))}")


def checked_files(root: Path) -> list[Path]:
    out: list[Path] = []
    for gene in GENES:
        f = gene_files(root, gene)
        out += [f["review"], f["notes"]]
    bio = root / "genes" / "human" / "AADACL2" / "AADACL2-bioinformatics"
    out += [bio / AUDIT, bio / "RESULTS.md", bio / "audit_node_PTN009058710.py"]
    return [p for p in out if p.exists()]


# A notes paragraph may quote a stale claim while recording its correction. These cues mark a
# passage as retrospective; without one, a stale phrase in a journal reads as a live assertion.
RETROSPECTIVE_CUES = [
    r"superseded", r"no longer", r"since resolved", r"since fixed", r"was resolved",
    r"were?\s+(?:wrong|corrected|conceded|fixed|removed|dropped)", r"corrected",
    r"still (?:said|says|read|reads|carried|carries|carry|presents)", r"as merged",
    r"verdict as merged", r"had (?:kept|reached|relied)", r"could not (?:both )?be right",
    r"this whole section is superseded", r"written when", r"which is how they survived",
    r"none of that survives", r"invalidated", r"does not contain", r"did not contain",
]
RETROSPECTIVE_HEADING = re.compile(
    r"^#{2,6}\s+.*(round-\d|adjudication|corrections|superseded|since resolved|automation)",
    re.IGNORECASE)

# A section may be marked retrospective once, at the top, and cover its paragraphs - that is how a
# reader takes it. The section-level marker must be one of these strong cues, not merely any past
# tense, so that appending a new live claim to an old section does not get laundered by its header.
SECTION_MARKERS = [r"superseded", r"historical", r"since resolved", r"since fixed",
                   r"written when", r"no longer exists", r"kept for its reasoning"]


def _notes_paragraph_is_retrospective(paragraph: str, heading: str, section_marked: bool) -> bool:
    if section_marked or RETROSPECTIVE_HEADING.match(heading.strip()):
        return True
    return any(re.search(c, paragraph.lower()) for c in RETROSPECTIVE_CUES)


def _inside_supporting_text(flat: str, pos: int) -> bool:
    """True if pos falls in a `supporting_text:` value.

    Those are required to be verbatim substrings of their source, so they cannot carry an inline
    correction; the requirement falls on the surrounding prose instead.
    """
    before = flat[max(0, pos - 400):pos]
    last_key = max((before.rfind(k) for k in ("supporting_text:", "statement:", "comment:",
                                              "reason:", "summary:", "review_notes:")),
                   default=-1)
    return before.rfind("supporting_text:") == last_key and last_key != -1


def _scan(path: Path, root: Path, flat: str, allow_historical: bool, problems: list[str],
          context: str = "") -> None:
    for pattern, why in STALE:
        for m in re.finditer(pattern, flat):
            if allow_historical and pattern == r"TERM_SCOPING_PROBLEM":
                continue  # the audit's motivation section, explicitly marked
            problems.append(f"{path.relative_to(root)}{context}: stale claim /{pattern}/: {why}\n"
                            f"    ...{flat[max(0, m.start() - 80):m.end() + 60]}...")
    for pattern, pointer, why in SUPERSEDED_COUNTS:
        for m in re.finditer(pattern, flat):
            # look both ways: the supersession reads naturally either before or after the count
            window = flat[max(0, m.start() - 420):m.end() + 420]
            if _inside_supporting_text(flat, m.start()):
                continue  # a verbatim quote cannot be annotated; the row's prose carries it
            if not re.search(pointer, window):
                problems.append(f"{path.relative_to(root)}{context}: /{pattern}/ with no "
                                f"superseding pointer in the same passage: {why}\n"
                                f"    ...{flat[max(0, m.start() - 60):m.end() + 120]}...")


def check_stale(root: Path, problems: list[str]) -> None:
    """No file may *assert* something the harmonisation made false.

    Notes files are in scope deliberately - item 22 on the PR was a false claim in a journal, which
    a YAML-only guard could not have caught - but they are scanned paragraph by paragraph so that a
    quotation inside a retrospective passage is allowed and a bare assertion is not.
    """
    for path in checked_files(root):
        text = path.read_text()
        flat = " ".join(text.split())
        if path.name.endswith("-notes.md"):
            heading, section_marked, first_after_heading = "", False, False
            for block in re.split(r"\n\s*\n", text):
                stripped = block.strip()
                if stripped.startswith("#"):
                    heading = stripped.splitlines()[0]
                    section_marked = False
                    first_after_heading = True
                    rest = "\n".join(stripped.splitlines()[1:]).lower()
                    if any(re.search(mk, rest) for mk in SECTION_MARKERS):
                        section_marked = True
                        first_after_heading = False
                elif first_after_heading:
                    first_after_heading = False
                    if any(re.search(mk, stripped.lower()) for mk in SECTION_MARKERS):
                        section_marked = True
                if _notes_paragraph_is_retrospective(stripped, heading, section_marked):
                    continue
                _scan(path, root, " ".join(block.split()), False, problems,
                      context=f" (under {heading[:60]!r})" if heading else "")
        else:
            _scan(path, root, flat, HISTORICAL_MARKER in flat, problems)


def check_historical_marker(root: Path, problems: list[str]) -> None:
    """The exemption must be earned: the audit file has to actually carry the marker."""
    audit = root / "genes" / "human" / "AADACL2" / "AADACL2-bioinformatics" / AUDIT
    if not audit.exists():
        problems.append(f"{AUDIT} is missing")
        return
    flat = " ".join(audit.read_text().split())
    if "TERM_SCOPING_PROBLEM" in flat and HISTORICAL_MARKER not in flat:
        problems.append(f"{AUDIT}: mentions TERM_SCOPING_PROBLEM without the historical marker, so "
                        f"the exemption in check_stale is not earned")


def run(root: Path) -> list[str]:
    problems: list[str] = []
    check_invariant(root, problems)
    check_stale(root, problems)
    check_historical_marker(root, problems)
    return problems


# --------------------------------------------------------------------------- self-test

def _break_invariant_root_cause(root: Path) -> None:
    p = gene_files(root, "AADACL4")["review"]
    p.write_text(p.read_text().replace(
        f"      root_cause: {ROOT_CAUSE}", "      root_cause: TERM_SCOPING_PROBLEM", 1))

def _break_invariant_failure_mode(root: Path) -> None:
    p = gene_files(root, "AADACL3")["review"]
    p.write_text(p.read_text().replace(
        f"      root_cause: {ROOT_CAUSE}\n      source_entities:",
        f"      root_cause: {ROOT_CAUSE}\n      failure_modes:\n      - GRANULARITY_MISMATCH\n"
        "      source_entities:", 1))

def _break_invariant_replacement(root: Path) -> None:
    p = gene_files(root, "AADACL2")["review"]
    p.write_text(p.read_text().replace(
        "    - id: GO:0052689\n      label: carboxylic ester hydrolase activity",
        "    - id: GO:0017171\n      label: serine hydrolase activity", 1))

def _break_invariant_supporting_entities(root: Path) -> None:
    p = gene_files(root, "AADACL4")["review"]
    p.write_text(p.read_text().replace("  - UniProtKB:Q9HTI0\n  review:", "  review:", 1))

def _break_invariant_fold_source_status(root: Path) -> None:
    """Reinstate the retracted assessment on the fold signature, one field below failure_modes."""
    f = gene_files(root, "AADACL3")["review"]
    text = f.read_text()
    target = f"source_status: {FOLD_SOURCE_STATUS}"
    assert target in text, f"mutation target drifted: {target!r} not found in {f}"
    f.write_text(text.replace(target, f"source_status: {RETRACTED_SOURCE_STATUS}", 1))


def _break_invariant_fold_entity_deleted(root: Path) -> None:
    """Delete the fold source entity, which a continue-on-mismatch check would not notice."""
    f = gene_files(root, "AADACL3")["review"]
    lines = f.read_text().splitlines(keepends=True)
    out, dropping = [], False
    for line in lines:
        if f"source_id: {FOLD_SOURCE}" in line:
            dropping = True
            continue
        if dropping:
            # Drop the entity's remaining keys, i.e. until the next list item or a dedent.
            if line.lstrip().startswith("- ") or not line.startswith(" " * 8):
                dropping = False
            else:
                continue
        out.append(line)
    assert len(out) < len(lines), f"mutation target drifted: no {FOLD_SOURCE} entity found in {f}"
    f.write_text("".join(out))


def _break_invariant_retracted_failure_mode(root: Path) -> None:
    """Reinstate SOURCE_EVIDENCE_WEAK in failure_modes, where it is a legal enum value."""
    f = gene_files(root, "AADACL3")["review"]
    text = f.read_text()
    target = f"      root_cause: {ROOT_CAUSE}\n"
    assert target in text, f"mutation target drifted: {target!r} not found in {f}"
    f.write_text(
        text.replace(
            target,
            f"      root_cause: {ROOT_CAUSE}\n      failure_modes:\n"
            f"      - {RETRACTED_FAILURE_MODE}\n",
            1,
        )
    )


def _break_invariant_core_mf(root: Path) -> None:
    p = gene_files(root, "AADACL3")["review"]
    t = p.read_text()
    i = t.index("core_functions:")
    p.write_text(t[:i] + t[i:].replace("    id: GO:0052689", "    id: GO:0017171", 1))

def _break_stale_in_notes(root: Path) -> None:
    """A live assertion in a journal, under a heading with no retrospective cue."""
    p = gene_files(root, "AADACL4")["notes"]
    p.write_text(p.read_text() + "\n## Current status\n\n"
                 "A curator reading both files today gets contradictory advice about this row.\n")

def _break_stale_in_review(root: Path) -> None:
    p = gene_files(root, "AADACL3")["review"]
    p.write_text(p.read_text().replace("suggested_questions:",
                                       "suggested_questions:\n- question: PR #2266 needs a follow-up.\n"
                                       "  experts: []", 1))

def _break_stale_two_of_them(root: Path) -> None:
    """The same phrasing that survived three rounds, asserted rather than quoted."""
    p = gene_files(root, "AADACL2")["notes"]
    p.write_text(p.read_text() + "\n## Family node\n\n"
                 "The term is true of all three donors and held by IDA in two of them.\n")

def _break_superseded_pointer(root: Path) -> None:
    """Revert the count to its pre-harmonisation form: the whole superseding clause removed.

    The first version of this mutation only reworded the lead-in and left "15 of 16" inside the
    window, so it broke nothing and the guard correctly stayed silent - which is why the self-test
    reported a failure until the mutation itself was fixed. Deleting the clause is the regression
    that actually matters.
    """
    p = gene_files(root, "AADACL3")["review"]
    t = p.read_text()
    clause = """ That count is superseded by the shared node audit in
      genes/human/AADACL2/AADACL2-bioinformatics/, which resolves BNA7 directly through
      xref:sgd-S000002836 to Q04066 rather than through the Alliance record and so reports 15 of 16
      donors with a serine nucleophile; the sole non-serine donor is HIDH either way."""
    if clause not in t:
        raise AssertionError("mutation target text has moved; update _break_superseded_pointer "
                             "rather than letting the self-test silently pass")
    p.write_text(t.replace(clause, "", 1))

def _break_historical_marker(root: Path) -> None:
    p = root / "genes" / "human" / "AADACL2" / "AADACL2-bioinformatics" / AUDIT
    p.write_text(p.read_text().replace(HISTORICAL_MARKER, "This section explains why", 1))

def _break_stale_pseudo_retrospective(root: Path) -> None:
    """A heading that merely looks like prose history must not launder a live claim."""
    p = gene_files(root, "AADACL3")["notes"]
    p.write_text(p.read_text() + "\n## Notes on the family node\n\n"
                 "This review conflicts with the merged AADACL2 review.\n")


MUTATIONS = [
    ("invariant: root_cause reverted", _break_invariant_root_cause),
    ("invariant: GRANULARITY_MISMATCH re-added", _break_invariant_failure_mode),
    ("invariant: retracted source_status on the fold signature", _break_invariant_fold_source_status),
    ("invariant: fold source entity deleted outright", _break_invariant_fold_entity_deleted),
    ("invariant: retracted SOURCE_EVIDENCE_WEAK failure mode", _break_invariant_retracted_failure_mode),
    ("invariant: replacement term reverted to GO:0017171", _break_invariant_replacement),
    ("invariant: a supporting_entities token dropped", _break_invariant_supporting_entities),
    ("invariant: core_functions MF changed", _break_invariant_core_mf),
    ("stale claim added to a notes file", _break_stale_in_notes),
    ("stale claim added to a review", _break_stale_in_review),
    ("'IDA in two of them' added to a notes file", _break_stale_two_of_them),
    ("superseding pointer removed from a count", _break_superseded_pointer),
    ("historical marker removed while the claim stays", _break_historical_marker),
    ("stale claim smuggled into a retrospective-looking section without a cue",
     _break_stale_pseudo_retrospective),
]


def self_test(root: Path) -> int:
    if run(root):
        print("SELF-TEST ABORTED: the tree does not currently pass, so a mutation proving nothing "
              "cannot be distinguished from one proving something. Fix the tree first.")
        return 2
    failures = 0
    for name, mutate in MUTATIONS:
        with tempfile.TemporaryDirectory() as tmp:
            copy = Path(tmp) / "repo"
            shutil.copytree(root / "genes", copy / "genes",
                            ignore=shutil.ignore_patterns(".venv", "*.html"))
            before = run(copy)
            if before:
                print(f"  ?? {name}: the copy already fails before mutation; guard untestable")
                failures += 1
                continue
            mutate(copy)
            after = run(copy)
            if after:
                print(f"  ok {name}: caught ({len(after)} problem(s))")
            else:
                print(f"  FAIL {name}: NOT caught - this guard does not work")
                failures += 1
    print(f"\nself-test: {len(MUTATIONS) - failures}/{len(MUTATIONS)} guards demonstrably fire")
    return 1 if failures else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true",
                    help="break each guard in a temporary copy and require it to fire")
    args = ap.parse_args()
    root = repo_root(Path(__file__).parent)
    if args.self_test:
        return self_test(root)
    problems = run(root)
    if problems:
        print(f"{len(problems)} problem(s):\n")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"AADACL2/AADACL3/AADACL4 agree on the {TERM} row, and no stale claim remains in the "
          f"{len(checked_files(root))} files checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
