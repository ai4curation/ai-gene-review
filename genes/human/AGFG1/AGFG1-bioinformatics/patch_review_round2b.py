"""The round-2 fix landed in the reason and the description but not in the summary.

Classic "fixed in N places, landed in N-1", and in the worst position: the summary is
the first thing a reader sees. The summary still attributed a negative to
PMID:18809720 ("the family's own reference reports no GAP measurement for either human
AGFG protein") after the reason and the description had both been corrected to say
that the reference's sentence asserts a subfamily-level positive covering AGFG.

Also reflows two over-long folded lines in the reason that the previous patch created.

Usage: uv run python patch_review_round2b.py
"""

from __future__ import annotations

import pathlib

import yaml

HERE = pathlib.Path(__file__).parent
REVIEW = HERE.parent / "AGFG1-ai-review.yaml"
RETRACTED = "reference reports no GAP measurement"

EDITS: list[tuple[str, str]] = [
    (
        """      interactome - but the family's own reference reports no GAP measurement for either
      human AGFG protein, and it also supplies a counterexample showing that an intact motif
      does not imply activity.""",
        """      interactome - but no direct GAP measurement on either human AGFG protein has been
      located, and the family's own reference supplies a counterexample showing that an
      intact motif does not imply activity.""",
    ),
    (
        """      over-annotated - without supplying the measurement that would make it core. What is positive: the fly orthologue's
      GTPase-activating function is essential for border-cell detachment and acts against
      the class III Arf, and a human ARF-family proximity interactome places AGFG1 with
      ARF1, ARF3 and ARF6. What no source consulted here supplies is a GAP measurement on
      human AGFG1 or AGFG2, or an identified substrate: PMID:18809720's AGFG section reports
      neither, and a recorded Europe PMC query returned no such study. That is a statement
      about those sources and that query, not a proof that no assay exists. Note also that GO has merged the nine substrate-specific GAP
      terms into GO:0005096 (they are its secondaryIds), so this term is already maximal
      and no substrate-specific child should be proposed.""",
        """      over-annotated - without supplying the measurement that would make it core. What is
      positive: the fly orthologue's GTPase-activating function is essential for border-cell
      detachment and acts against the class III Arf, and a human ARF-family proximity
      interactome places AGFG1 with ARF1, ARF3 and ARF6. What no source consulted here
      supplies is a GAP measurement on human AGFG1 or AGFG2, or an identified substrate:
      PMID:18809720's AGFG section reports neither, and a recorded Europe PMC query returned
      no such study. That is a statement about those sources and that query, not a proof
      that no assay exists. Note also that GO has merged the nine substrate-specific GAP
      terms into GO:0005096 (they are its secondaryIds), so this term is already maximal
      and no substrate-specific child should be proposed.""",
    ),
]


def main() -> None:
    text = REVIEW.read_text()
    if RETRACTED not in text:
        print("already patched; nothing to do")
        return
    for old, new in EDITS:
        count = text.count(old)
        assert count == 1, f"anchor found {count} times:\n{old[:160]}"
        text = text.replace(old, new, 1)
        assert new in text, "replacement did not land"
    REVIEW.write_text(text)

    doc = yaml.safe_load(text)
    row = next(a for a in doc["existing_annotations"] if a["term"]["id"] == "GO:0005096")
    for field in ("summary", "reason"):
        assert RETRACTED not in row["review"][field], f"{field} still carries it"
    assert RETRACTED not in doc["description"]
    # And check it nowhere survives in the emitted YAML at all.
    assert RETRACTED not in text, "the retracted attribution survives somewhere"
    print("summary and reason reflowed; retracted attribution gone from the YAML")


if __name__ == "__main__":
    main()
