"""Add the affinage deep-research record as a reference and cite its corpus-level
negative on the GO:0005096 row.

Written as a script rather than by hand because every anchor is asserted present
before replacement and re-checked afterwards: "fixed in N places, landed in N-1"
has recurred repeatedly in this campaign. Idempotent - refuses to run twice.

Usage: uv run python patch_affinage_ref.py
"""

from __future__ import annotations

import pathlib

HERE = pathlib.Path(__file__).parent
REVIEW = HERE.parent / "AGFG1-ai-review.yaml"
AFFINAGE = HERE.parent / "AGFG1-deep-research-affinage.md"

QUOTE = (
    "Beyond these endocytic and Rev-export roles, no further mechanistic detail has "
    "been characterized in the available corpus."
)

REF_ANCHOR = """- id: file:human/AGFG1/AGFG1-bioinformatics/RESULTS.md
  title: AGFG1 computational analyses supporting the GO review
"""

REF_BLOCK = """- id: file:human/AGFG1/AGFG1-deep-research-affinage.md
  title: Affinage mechanistic annotation for AGFG1 (human)
  reference_review:
    relevance: LOW
    correctness: VERIFIED
    review_notes: >-
      Machine-generated provider record, gates_passed True, and its two citations
      (PMID:10613896 and PMID:18819912) are real and correctly quoted - so its precision
      is fine. Its recall is not, and that was measured rather than asserted: it returned
      neither of the two papers that decide this review (PMID:18775314, the VAMP7 structure
      and depletion phenotype, and PMID:11711676, the mouse null with no acrosome), nor
      PMID:18809720, the family reference supplying the catalytic-motif anchor, nor
      PMID:38606629, the only human dataset placing AGFG1 with ARF1/ARF3/ARF6. It also
      states the general clathrin-mediated-endocytosis requirement as settled when
      PMID:18775314 contradicts it for EGF. Cited here for exactly one thing: its explicit
      statement about the extent of its own corpus, used as a statement about that corpus
      and corroborated independently.
"""

QUOTE_ANCHOR = """    - reference_id: file:human/AGFG1/AGFG1-bioinformatics/RESULTS.md
      supporting_text: '**12/12 panel members retain CX2CX16CX2CX4R.**'
"""

QUOTE_BLOCK = f"""    - reference_id: file:human/AGFG1/AGFG1-deep-research-affinage.md
      supporting_text: {QUOTE}
"""


def main() -> None:
    text = REVIEW.read_text()
    assert QUOTE in AFFINAGE.read_text(), "the quoted sentence is not in the affinage record"

    if "AGFG1-deep-research-affinage.md" in text:
        print("already patched; nothing to do")
        return

    assert text.count(REF_ANCHOR) == 1, f"reference anchor found {text.count(REF_ANCHOR)} times"
    assert text.count(QUOTE_ANCHOR) == 1, f"quote anchor found {text.count(QUOTE_ANCHOR)} times"

    out = text.replace(REF_ANCHOR, REF_ANCHOR + REF_BLOCK, 1)
    out = out.replace(QUOTE_ANCHOR, QUOTE_ANCHOR + QUOTE_BLOCK, 1)

    # Post-conditions: both insertions landed exactly once, and nothing else moved.
    assert out.count("- id: file:human/AGFG1/AGFG1-deep-research-affinage.md") == 1
    assert out.count("    - reference_id: file:human/AGFG1/AGFG1-deep-research-affinage.md") == 1
    assert len(out) > len(text)
    assert out.replace(REF_BLOCK, "").replace(QUOTE_BLOCK, "") == text, (
        "the patch changed something other than the two inserted blocks"
    )

    REVIEW.write_text(out)
    print("patched: 1 reference entry + 1 supporting_by quote on the GO:0005096 row")


if __name__ == "__main__":
    main()
