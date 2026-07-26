#!/usr/bin/env python3
"""Invariant lint for the ACTMAP review's cross-cutting numeric claims.

Why this exists: the review's argument turns on how many gene products a single
ontology fix would correct, and that number is asserted at several independent
sites with no generation relationship between them (a review `reason`, a
`knowledge_gap.resolution`, a `suggested_question`, the notes, and the PR body).
The first pass said "4 in 4 species" from a taxon-restricted census that cannot
see the bovine and Xenopus family members; the true family-wide figure is 6 of 6.
A hand-checked list is not enough to keep five sites in step, so the invariant is
committed instead.

Usage:
    python3 audit_actmap_claims.py [extra_file ...]   # e.g. a PR-body markdown file
    python3 audit_actmap_claims.py --self-test        # prove each check can fire

Exit status is non-zero if any invariant is violated.
"""

from __future__ import annotations

import sys
import tempfile

import yaml
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
REVIEW = GENE_DIR / "ACTMAP-ai-review.yaml"
NOTES = GENE_DIR / "ACTMAP-notes.md"

# Phrasings withdrawn during review. They must not appear anywhere EXCEPT inside a
# line that also marks itself as a retraction, which is how the notes are allowed to
# quote what they are retracting.
RETRACTED = [
    # Round 1: the taxon-restricted census read as a family-wide count.
    "4 gene products in 4 species",
    "four gene products in four species",
    "four ACTMAP-family gene products",
    "the mouse, zebrafish and Drosophila orthologs",
    "human, mouse, zebrafish and Drosophila ACTMAP",
    # Round 2: GO:0030047 was proposed as a NEW annotation, then withdrawn because GO
    # keeps proteolysis and protein modification in disjoint branches. Any text that
    # still proposes it, or still leans on the NAA80 precedent, is stale.
    "an additional GO:0030047 actin modification annotation is proposed",
    "actin modification annotation is proposed below",
    "Proposed new annotation. GOA records that ACTMAP processes a protein",
]
RETRACTION_MARKERS = ("My first pass wrote", "Correction to my own first pass")

# Claims that must be present, with the exact number of occurrences expected in each
# file. Stating the count (not merely "present") is what catches an edit that lands in
# N-1 of N places.
REQUIRED: dict[Path, list[tuple[str, int]]] = {
    REVIEW: [
        # review.reason + knowledge_gap.resolution + suggested_question. Counts were
        # derived by grepping the file, not guessed: guessing gave 2 and the check
        # failed on a real third site, which is the behaviour wanted.
        ("six reviewed", 3),
        ("all six reviewed members of PTHR28631", 1),
        # The taxon-restricted figure is still quoted, but only where its scope is stated.
        ("74 gene products", 3),
    ],
    NOTES: [
        ("6 gene products in 6 species", 1),
        ("6 of 6 carrying `GO:0004239`", 1),
        # Round 2: the disjoint-branch finding is what justifies withdrawing GO:0030047,
        # so it must remain stated in the notes.
        ("disjoint", 3),  # count derived by grepping, not guessed
    ],
}

# Structural invariants on the review YAML itself, checked after parsing so that prose
# discussing a withdrawn term is allowed while an actual annotation row is not.
STRUCTURAL = {
    "no GO:0030047 annotation row": lambda d: all(
        a["term"]["id"] != "GO:0030047" for a in d["existing_annotations"]
    ),
    "no GO:0030047 in core_functions.directly_involved_in": lambda d: all(
        t["id"] != "GO:0030047"
        for cf in d["core_functions"]
        for t in cf.get("directly_involved_in", [])
    ),
    "has_input ACTB+ACTG1 on both accepted GO:0070005 and GO:0016485 IDA rows": lambda d: all(
        [e["term"]["id"] for e in (a.get("extensions") or [])]
        == ["UniProtKB:P60709", "UniProtKB:P63261"]
        for a in d["existing_annotations"]
        if a["evidence_type"] == "IDA" and a["term"]["id"] in ("GO:0070005", "GO:0016485")
    ),
    "substrates list only the two demonstrated actins": lambda d: all(
        [t["id"] for t in cf.get("substrates", [])]
        == ["UniProtKB:P60709", "UniProtKB:P63261"]
        for cf in d["core_functions"]
    ),
}

# Claims that must appear in any extra file supplied on the command line (the PR body).
REQUIRED_EXTRA: list[tuple[str, int]] = [("six reviewed", 1)]


def check_retracted(path: Path, text: str) -> list[str]:
    problems = []
    for phrase in RETRACTED:
        for i, line in enumerate(text.splitlines(), 1):
            if phrase in line and not any(m in line for m in RETRACTION_MARKERS):
                problems.append(
                    f"{path.name}:{i}: retracted phrasing {phrase!r} outside a retraction line"
                )
    return problems


def check_required(path: Path, text: str, required: list[tuple[str, int]]) -> list[str]:
    problems = []
    for phrase, expected in required:
        got = text.count(phrase)
        if got != expected:
            problems.append(
                f"{path.name}: expected {expected} occurrence(s) of {phrase!r}, found {got}"
            )
    return problems


def audit(extra: list[Path]) -> list[str]:
    problems: list[str] = []
    targets = list(REQUIRED) + extra
    for path in targets:
        # Assert presence: a guard that skips a missing file can be defeated by
        # deleting the file it guards.
        if not path.exists():
            problems.append(f"{path}: MISSING - nothing to audit, which is itself a failure")
            continue
        text = path.read_text()
        problems += check_retracted(path, text)
        problems += check_required(
            path, text, REQUIRED.get(path, REQUIRED_EXTRA if path in extra else [])
        )
    problems += check_structural()
    return problems


def check_structural() -> list[str]:
    """Structural invariants on the review YAML. Asserts the file is loadable rather
    than skipping silently, so deleting it cannot defeat the check."""
    review = next((p for p in REQUIRED if p.name.endswith("-ai-review.yaml")), None)
    if review is None or not review.exists():
        return ["review YAML: MISSING - structural invariants could not be checked"]
    try:
        doc = yaml.safe_load(review.read_text())
    except Exception as exc:  # a malformed review must be loud, not skipped
        return [f"{review.name}: unparseable ({exc})"]
    out = []
    for name, predicate in STRUCTURAL.items():
        if not predicate(doc):
            out.append(f"{review.name}: structural invariant violated - {name}")
    return out


# --------------------------------------------------------------------------- #
def self_test() -> int:
    """Prove every check can actually fire, by breaking the files in a copy.

    Each mutation asserts its target string is present first, so a drifted target
    is an error rather than a mutation that silently does nothing (and therefore a
    self-test that "passes" without exercising anything).
    """
    global REQUIRED, NOTES, REVIEW
    failures = 0
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        for src in (REVIEW, NOTES):
            (tmp / src.name).write_text(src.read_text())
        review_c, notes_c = tmp / REVIEW.name, tmp / NOTES.name
        orig_required = REQUIRED
        REQUIRED = {review_c: orig_required[REVIEW], notes_c: orig_required[NOTES]}
        real_review, real_notes = REVIEW, NOTES
        REVIEW, NOTES = review_c, notes_c

        cases = []

        # 1. clean baseline must pass
        cases.append(("clean baseline", lambda: None, False))

        # 2. reintroduce a retracted phrasing on a non-retraction line
        def reintroduce():
            t = notes_c.read_text()
            anchor = "The right fix is a **new term**"
            assert anchor in t, f"self-test target drifted: {anchor!r}"
            notes_c.write_text(t.replace(anchor, "It would correct 4 gene products in 4 species. " + anchor, 1))

        cases.append(("retracted phrasing reintroduced", reintroduce, True))

        # 3. delete a required claim from the review (the N-1 landing failure)
        def drop_required():
            t = review_c.read_text()
            anchor = "all six reviewed members of PTHR28631"
            assert anchor in t, f"self-test target drifted: {anchor!r}"
            review_c.write_text(t.replace(anchor, "all of the members of PTHR28631", 1))

        cases.append(("required claim dropped from review", drop_required, True))

        # 4. delete a guarded file entirely
        def delete_file():
            assert notes_c.exists(), "self-test target drifted: notes copy missing"
            notes_c.unlink()

        cases.append(("guarded file deleted", delete_file, True))

        # 5. reintroduce the withdrawn GO:0030047 annotation row (structural invariant)
        def readd_row():
            t = review_c.read_text()
            anchor_row = "- term:\n    id: GO:0005522\n"
            assert anchor_row in t, "self-test target drifted: GO:0005522 row"
            row = (
                "- term:\n    id: GO:0030047\n    label: actin modification\n"
                "  evidence_type: IMP\n  original_reference_id: PMID:42159598\n"
                "  qualifier: involved_in\n  review:\n    summary: reintroduced by self-test\n"
                "    action: NEW\n"
            )
            review_c.write_text(t.replace(anchor_row, row + anchor_row, 1))

        cases.append(("withdrawn GO:0030047 row reintroduced", readd_row, True))

        # 6. strip the has_input extensions from the GO:0016485 IDA row
        def strip_extensions():
            t = review_c.read_text()
            block = (
                "  extensions:\n  - predicate: RO:0002233\n    term:\n"
                "      id: UniProtKB:P60709\n      label: ACTB\n"
                "  - predicate: RO:0002233\n    term:\n"
                "      id: UniProtKB:P63261\n      label: ACTG1\n"
            )
            assert t.count(block) == 2, (
                f"self-test target drifted: expected 2 extension blocks, found {t.count(block)}"
            )
            review_c.write_text(t.replace(block, "", 1))

        cases.append(("has_input extensions stripped", strip_extensions, True))

        pristine = {p: p.read_text() for p in (review_c, notes_c)}
        for name, mutate, should_fail in cases:
            for p, t in pristine.items():
                p.write_text(t)
            mutate()
            problems = audit([])
            fired = bool(problems)
            ok = fired == should_fail
            print(f"  [{'ok' if ok else 'FAIL'}] {name}: "
                  f"{'reported' if fired else 'silent'} ({len(problems)} problem(s))")
            if not ok:
                failures += 1

        REQUIRED, REVIEW, NOTES = orig_required, real_review, real_notes
    print("self-test:", "all checks can fire" if not failures else f"{failures} broken check(s)")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        return self_test()
    extra = [Path(a) for a in argv if not a.startswith("-")]
    problems = audit(extra)
    for p in problems:
        print("PROBLEM:", p)
    n_files = len(REQUIRED) + len(extra)
    print(f"audited {n_files} file(s), {len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
