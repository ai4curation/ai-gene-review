#!/usr/bin/env python3
"""Lint: every phosphate-binding-loop-1 conservation claim must state WHICH sequence it holds for.

Why this exists. ACTL10's central result is that Swiss-Prot Q5JWF8 (245 aa) stops short of actin's
phosphate-binding loop 1, while the reading frame extended with the upstream genomic coding
sequence retains it. So "ACTL10 conserves phosphate-binding loop 1" is true of one sequence and
false of the other, and an unscoped statement of it is wrong about the entry that GO and UniProt
actually publish. The PR reviewer caught three such unscoped sites; this makes the invariant
mechanical instead of a hand-checked list, because "fixed in N places, landed in N-1" has recurred
throughout this campaign.

The invariant: for every occurrence of a P-loop-1 phrase in the review or the notes, a scoping
phrase must appear within WINDOW characters on either side.

Two bugs found while writing it, both by running it rather than reading it, and both worth
recording because they are the reason the first version passed nothing useful:

1. **YAML line-wrapping defeats literal matching.** A folded scalar breaks phrases across lines
   with indentation, so "does not reach" is stored as "does not\\n      reach". Matching the raw
   text missed legitimately-scoped sites and reported them as violations. All text is therefore
   whitespace-normalised before matching.
2. **A scope vocabulary that is too narrow inverts the check.** The notes scope one claim by
   saying the translation is of the transcript's *leader*, which no "extended ORF" synonym
   covers. A missing synonym makes a correct site look broken, which trains the reader to ignore
   the lint - the opposite of what it is for.

Run:  uv run python check_claim_scoping.py [--self-test]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE_DIR = HERE.parent
TARGETS = [GENE_DIR / "ACTL10-ai-review.yaml", GENE_DIR / "ACTL10-notes.md"]

WINDOW = 300

CLAIM = re.compile(r"phosphate-binding loop 1|P-loop 1", re.I)

# A claim is scoped if any of these appears nearby. Two families: phrases naming the extended
# sequence, and phrases naming the annotated sequence's failure to reach the loop. Either one
# disambiguates, because the reader then knows which of the two sequences is meant.
SCOPE = re.compile(
    r"extended reading frame|reading frame extended|extended ORF|extended frame|extended form"
    r"|extended human ORF|extended 412|upstream reading frame|upstream region|upstream ORF"
    r"|upstream genomic|leader in the CDS reading frame|555-nucleotide leader|5. leader"
    r"|annotated protein lacks|absent from the annotated|does not reach|do not reach"
    r"|fails to reach|stops short|not present to score|uninterrupted codons",
    re.I,
)


def normalise(text: str) -> str:
    """Collapse all whitespace runs to single spaces so YAML folding cannot hide a phrase."""
    return re.sub(r"\s+", " ", text)


def line_of(raw: str, norm_index: int) -> int:
    """Approximate source line for a normalised-text offset, for a usable error message."""
    count = 0
    for i, ch in enumerate(raw):
        if not (ch.isspace() and i and raw[i - 1].isspace()):
            if count == norm_index:
                return raw[:i].count("\n") + 1
            count += 1
    return raw.count("\n") + 1


def violations(raw_by_path: dict[Path, str]) -> list[str]:
    out: list[str] = []
    total = 0
    for path, raw in raw_by_path.items():
        norm = normalise(raw)
        for m in CLAIM.finditer(norm):
            total += 1
            lo = max(0, m.start() - WINDOW)
            window = norm[lo: m.end() + WINDOW]
            if not SCOPE.search(window):
                # Offset of the claim inside `window`, clamped: for a claim in the first 60
                # characters of a file an unclamped `rel - 60` is negative and Python slices from
                # the END, garbling the message exactly when a violation exists.
                rel = m.start() - lo
                excerpt = window[max(0, rel - 60):][:170]
                out.append(f"{path.name}:{line_of(raw, m.start())} unscoped claim: ...{excerpt}...")
    if total == 0:
        raise RuntimeError(
            "found zero P-loop-1 claims across the review and notes; either the wording changed "
            "or the wrong files are being linted - a lint that inspects nothing passes vacuously")
    print(f"  inspected {total} P-loop-1 claim(s) across {len(raw_by_path)} file(s)")
    return out


def load() -> dict[Path, str]:
    out = {}
    for p in TARGETS:
        if not p.exists():
            raise FileNotFoundError(f"missing {p}")
        out[p] = p.read_text()
    return out


def self_test(raw_by_path: dict[Path, str]) -> None:
    """Break it deliberately; each break must be caught.

    Every mutation asserts its target exists first, so a drifted anchor is an error rather than a
    no-op that "passes". An earlier version of this self-test used mutations that deleted ONE
    scoping phrase from a passage containing two; the lint correctly kept passing and the self-test
    correctly reported failure. That is worth recording: the mutations were inadequate, not the
    lint. A mutation must remove *all* scope from a claim's window, or add a claim that has none.
    """
    review = next(p for p in raw_by_path if p.name.endswith("ai-review.yaml"))
    notes = next(p for p in raw_by_path if p.name.endswith("notes.md"))
    cases = []

    # 1. Add a claim in a region with no scoping phrase anywhere near it.
    heading = "## 1. Where this gene starts from: a genuinely dark gene, and how dark\n"
    def add_unscoped(d):
        assert heading in d[notes], f"mutation target missing: {heading!r}"
        d[notes] = d[notes].replace(
            heading, heading + "\nACTL10 conserves phosphate-binding loop 1.\n")
    cases.append(("add an unscoped claim in a scope-free region", add_unscoped))

    # 2. Strip EVERY scoping phrase from the description block, leaving the claim bare.
    #
    # This mutation is the reason the note above exists. The first version substituted on the RAW
    # text while asserting on the NORMALISED text, so the wrapped phrases it meant to remove did
    # not match and the mutation silently did nothing - the very whitespace bug this lint guards
    # against, reproduced inside its own self-test. The mutation therefore works on normalised
    # text and asserts that the number of scope phrases it detected equals the number it removed.
    desc_claim = "including a well-conserved phosphate-binding loop 1"
    def strip_all_scope(d):
        norm = normalise(d[review])
        assert desc_claim in norm, f"mutation target missing: {desc_claim!r}"
        i = norm.index(desc_claim)
        lo, hi = max(0, i - 600), i + len(desc_claim) + 600
        region = norm[lo:hi]
        detected = len(SCOPE.findall(region))
        assert detected > 0, "mutation target missing: no scope phrase around the claim"
        cleaned, changed = SCOPE.subn("SEQUENCE", region)
        assert detected == changed, f"mutator/detector scope divergence: {detected} != {changed}"
        d[review] = norm[:lo] + cleaned + norm[hi:]
    cases.append(("strip every scoping phrase around the description claim", strip_all_scope))

    failures = []
    for name, mutate in cases:
        d = dict(raw_by_path)
        mutate(d)
        if violations(d):
            print(f"  caught: {name}")
        else:
            failures.append(name)

    # 3. The lint must not pass vacuously when there is nothing to inspect.
    d = {p: CLAIM.sub("REDACTED", t) for p, t in raw_by_path.items()}
    try:
        violations(d)
    except RuntimeError:
        print("  caught: a file set containing zero claims (vacuous pass rejected)")
    else:
        failures.append("zero-claim input was not rejected")

    if failures:
        raise SystemExit(f"SELF-TEST FAILED - not caught: {failures}")
    print(f"self-test: all {len(cases) + 1} mutations caught")
    print("NOTE: this proves the guards written here fire; it cannot show which guard was never "
          "written. In particular it checks that a scoping phrase is PRESENT, never that it is TRUE.")


def main() -> None:
    raw = load()
    print("linting P-loop-1 claim scoping")
    bad = violations(raw)
    if bad:
        for b in bad:
            print(f"  FAIL  {b}")
        raise SystemExit(f"{len(bad)} unscoped P-loop-1 claim(s)")
    print("every P-loop-1 claim states which sequence it holds for")
    if "--self-test" in sys.argv:
        print("\nrunning self-test")
        self_test(raw)


if __name__ == "__main__":
    main()
