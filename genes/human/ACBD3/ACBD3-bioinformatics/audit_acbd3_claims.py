#!/usr/bin/env python3
"""Regression test over every claim this review has retracted across 13 rounds.

The lesson of rounds 10-13: a fix to a claim needs a grep for the CLAIM, across
all five sites that can assert it (description, row summary, row reason,
findings.statement, notes), not an edit at the flagged location. This encodes each
retraction as a forbidden phrasing plus, where useful, the required replacement,
so a later edit cannot silently reintroduce one.

Usage: uv run python genes/human/ACBD3/ACBD3-bioinformatics/audit_acbd3_claims.py
       (run from the repository root)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve()
while REPO != REPO.parent and not (REPO / "genes").is_dir():
    REPO = REPO.parent
GENE = REPO / "genes/human/ACBD3"
# Deliberately TWO files. ACBD3-deep-research-affinage.md is excluded because it is a
# machine-fetched provider record that must not be edited - and FORBIDDEN[0] is still live
# in it, correctly so. The audit governs what this review asserts, not what the provider said.
FILES = [GENE / "ACBD3-ai-review.yaml", GENE / "ACBD3-notes.md"]

# (round, retracted phrasing, why it is wrong)
FORBIDDEN: list[tuple[int, str, str]] = [
    (3, "recruitment of the lipid kinase PI4KB to membranes through its GOLD domain",
        "PI4KB binds the Q domain (241-308), not GOLD"),
    (4, "short MWT motif that binds the golgins",
        "MWT374-376 sits in the UR upstream of GOLD; cite PMID:38134218"),
    (4, "targeted there through an MWT motif",
        "same, and the requirement is SCFD1-dependent"),
    (5, "genuinely contested, and the two sources disagree",
        "PMID:37044218 reconciles the RI/RII split itself"),
    (5, "interacts with RII but NOT RI", "the paper allows RI below detection limit"),
    (5, "The isoform is contested", "compartment-specific, not contested"),
    (5, "engage the separate GOLD domain", "3A is IN the UR; UR+GOLD is one surface"),
    (5, "it is also the surface that picornaviral 3A proteins engage",
        "implies a private site; 3A shares the surface"),
    (6, "RIIalpha docking maps to K381", "K381P is a helix-breaking proline"),
    (6, "with K381 also required for RII binding", "same"),
    (7, "overlap at a single residue", "I380P had almost no effect; state the helix"),
    (7, "The RIIalpha contact residue is I380", "same"),
    (8, "converging on residues 380-381", "SEC22B and RII have no residue-level mapping"),
    (9, "no acyl-CoA ligand", "ACBD3 binds C18:1-CoA/C16:0-CoA (PMID:26290611)"),
    (9, "never mentions acyl-CoA once", "a silent record is not evidence of absence"),
    (9, "Does ACBD3 bind acyl-CoA at all", "it does; the open question is the consequence"),
    (9, "establish that the domain is vestigial", "same"),
    (10, "separable arms of the same protein", "the ACB domain also recruits FAPP2"),
    (10, "map to the Q domain and the UR/GOLD surface",
         "omits the ACB domain, which has functions"),
    (11, "rests on gain-of-function evidence", "the knockdown result is in the cached text"),
    (11, "All assays are overexpression-based", "same"),
    (11, "rests on the gain-of-function direction alone", "same"),
    (12, "it binds SREBP1 and restrains its maturation",
         "subject resolves to the ACB domain; the co-IP was full-length"),
    (13, "maps that effect to", "the source says 'plays an important role'; ~50% residual"),
    (14, "the effect maps to", "same claim, GO:2000639 row and notes - source says 'important role'"),
    (13, "additionally carries a gene-specific", "contribution, not location of the function"),
    # process history belongs in notes / reference_review, not rows or findings
    (12, "because I read the Figure 3 legend", "first-person history in a row summary"),
    (13, "earlier versions of this review asserted did not exist",
         "a findings entry should be a finding of the paper"),
    # string-splice damage
    (13, "oligomerises on ligand; binds", "dangling verb from a mid-clause splice"),
]

# Claims that must be positively present, so a later edit cannot quietly drop them.
# (phrase, minimum occurrences across the gene folder, why)
# The count matters: an "appears anywhere" check cannot see a claim removed from ONE of
# several sites, which is exactly how the c1ba137 scope qualifier was lost. Found by the
# self-test below, which is the whole reason the self-test exists.
REQUIRED: list[tuple[str, int, str]] = [
    ("binds long-chain fatty acyl-CoAs", 2, "the corrected GO:0000062 call"),
    ("Separately, ACBD3 restrains SREBP1 maturation", 1, "SREBP1 attributed to the protein"),
    ("only been assayed with full-length ACBD3", 1, "co-IP caveat in the description"),
    ("contributes to the effect rather than carrying it", 1, "partial N-terminal contribution"),
    ("overlap as surfaces", 3, "helix-level, not residue-level, RII/3A claim"),
    ("an SCFD1-dependent step", 8, "SEC22B requirement is confounded; 1 description + 7 rows"),
    ("inferred by similarity rather than localised directly in human cells", 1,
     "mitochondrial pool hedge"),
    # a missing QUALIFIER cannot be caught by a forbidden string - only by requiring the scoped form.
    # This one was written in c1ba137, removed by 81f46c582, and flagged in round 15.
    ("3A-mediated PI4KB recruitment", 8,
     "the PMID:30755512 dispensability result is the VIRAL assay; host recruitment was not tested"),
    ("enteroviral setting, but scoring the Q-domain", 2,
     "the bridge from the viral assay to the host claim must stay attached"),
]


def norm(s: str) -> str:
    """Collapse whitespace and drop markdown emphasis.

    Both matter: a phrase broken across a line wrap is invisible to plain grep, and
    `dispensable for **3A-mediated** PI4KB recruitment` in the notes was invisible to the
    literal phrase - so the notes' most explicit statement of that scope counted for nothing.
    """
    return re.sub(r"[*`_]", "", re.sub(r"\s+", " ", s))


def main() -> int:
    text = {f: f.read_text() for f in FILES}
    flat = {f: norm(t) for f, t in text.items()}
    # a retracted phrasing may legitimately be QUOTED inside its own retraction
    RETRACTION = re.compile(
        r"that was (wrong|false)|was over-dramatised|earlier versions? of|a (later|round-\d+) version|"
        r"retracted|over-read|misuse of the source|was quoted as|coverage gap|asserted that",
        re.I,
    )
    bad = 0
    for rnd, phrase, why in FORBIDDEN:
        needle = norm(phrase)
        for f, t in flat.items():
            for m in re.finditer(re.escape(needle), t, re.I):
                # A retraction introduces the phrasing it is retracting, so weight the window
                # backwards - but some retractions put the marker just after the quote, hence the
                # smaller forward allowance. Keep both tight: a wide symmetric window silently
                # hides real regressions (it did, on the first version of this script).
                window = t[max(0, m.start() - 170) : m.end() + 140]
                if RETRACTION.search(window):
                    continue  # quoted inside its own retraction; that is the point
                print(f"REGRESSION (round {rnd})  {f.name}: {phrase!r}\n    -> {why}")
                bad += 1
    for phrase, want, why in REQUIRED:
        needle = norm(phrase).lower()
        got = sum(t.lower().count(needle) for t in flat.values())
        if got < want:
            print(f"MISSING  {phrase!r}: {got} occurrence(s), expected >= {want}\n    -> {why}")
            bad += 1
    print(
        f"\n{len(FORBIDDEN)} retracted phrasings checked, {len(REQUIRED)} required claims checked, "
        f"{bad} problem(s)"
    )
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
