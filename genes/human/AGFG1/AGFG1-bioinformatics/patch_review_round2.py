"""Round-2 reviewer response: the other half of the PMID:18809720 sentence.

The reviewer caught a selectively-bounded quotation. The sentence used as the
disconfirming control -

    "Arf GAP activity has been demonstrated in vitro for at least one member of
    each subfamily, with the exception of the ADAPs, which appear to lack in vitro
    GAP activity."

- has two clauses, and only the ADAP clause was argued from. The first clause is a
blanket POSITIVE that covers the AGFG subfamily, since AGFG is one of the paper's
ten subfamilies and is not among the exceptions. The verdict is unaffected, but the
asymmetry had to be fixed: this is the campaign's "a verbatim quote can be TRUE and
selectively bounded" defect, and no gate can see it because the quote is verbatim.

Two edits:
  * the GO:0005096 reason now states the blanket claim and gives four checkable
    grounds for discounting its AGFG instance;
  * the top-level description no longer attributes a negative to that reference; it
    is scoped to what was located.

Anchors asserted present before replacement; idempotent.

Usage: uv run python patch_review_round2.py
"""

from __future__ import annotations

import pathlib

import yaml

HERE = pathlib.Path(__file__).parent
REVIEW = HERE.parent / "AGFG1-ai-review.yaml"
DONE_MARKER = "blanket clause"

EDITS: list[tuple[str, str]] = [
    # Description: stop attributing a negative to the reference.
    (
        """  genetically required for Arf-dependent actomyosin contractility, while the family's
  consensus nomenclature reference reports no GAP measurement for either human AGFG
  protein.""",
        """  genetically required for Arf-dependent actomyosin contractility, but no direct GAP
  measurement on either human AGFG protein has been located.""",
    ),
    # GO:0005096 reason: use the whole sentence, not half of it.
    (
        """      ADAP1's motif is complete - 12 of 12 panel members retain the motif - so retention is
      necessary and demonstrably not sufficient.""",
        """      ADAP1's motif is complete - 12 of 12 panel members retain the motif - so retention is
      necessary and demonstrably not sufficient. That sentence has two clauses and both are
      used here, because leaning on one and passing over the other would be a selectively
      bounded quotation: its first clause is a blanket positive that covers this subfamily,
      since the paper classifies the 31 human ArfGAPs into ten subfamilies, AGFG is one of
      them, and only the ADAPs are excepted. Four checkable grounds for discounting its
      AGFG instance rather than treating it as the measurement: the clause carries no
      citation, while the sentences on either side of it do cite specific papers; it is
      stated at subfamily level and names no species, protein or assay; the paper's own
      AGFG section, where a specific claim would live, says nothing about GAP activity for
      either paralogue and only that much less information is available on AGFG2; and the
      same paragraph warns that "some ArfGAPs use their GAP domain to bind Arf without
      promoting GTP hydrolysis", which is precisely the distinction a subfamily-level
      summary cannot settle. So the blanket clause raises the prior that an AGFG member is
      catalytically active - which is part of why this row is kept rather than marked
      over-annotated - without supplying the measurement that would make it core.""",
    ),
    # Two more quotes so the reader can check both clauses and the caveat.
    (
        """    - reference_id: PMID:31533044
      supporting_text: Notably, we found that the ArfGAP Drongo and its GTPase-activating
        function are essential for the initial detachment of the border cell cluster from
        the basal lamina.""",
        """    - reference_id: PMID:18809720
      supporting_text: The 31 predicted human ArfGAPs have been classified into 10 subfamilies,
        based on sequence similarities of their ArfGAP domains
    - reference_id: PMID:18809720
      supporting_text: some ArfGAPs use their GAP domain to bind Arf without promoting GTP
        hydrolysis
    - reference_id: PMID:31533044
      supporting_text: Notably, we found that the ArfGAP Drongo and its GTPase-activating
        function are essential for the initial detachment of the border cell cluster from
        the basal lamina.""",
    ),
    # And record the same nuance in the reference_review, which is where a
    # citation-quality judgement belongs.
    (
        """      control, since it reports that the ADAP subfamily lacks in vitro GAP activity
      although ADAP1's motif is complete. Its AGFG section reports no GAP activity for
      either paralogue.""",
        """      control, since it reports that the ADAP subfamily lacks in vitro GAP activity
      although ADAP1's motif is complete. Both clauses of that sentence are used: the same
      sentence also asserts, at subfamily level and without a citation, that at least one
      member of every non-ADAP subfamily - which includes AGFG - has demonstrated in vitro
      GAP activity. Its AGFG section names no such measurement for either paralogue, so the
      blanket clause is treated as raising the prior rather than as the evidence.""",
    ),
]


def main() -> None:
    text = REVIEW.read_text()
    if DONE_MARKER in text:
        print("already patched; nothing to do")
        return
    for old, new in EDITS:
        count = text.count(old)
        assert count == 1, f"anchor found {count} times:\n{old[:160]}"
        text = text.replace(old, new, 1)
        assert new in text, "replacement did not land"
    REVIEW.write_text(text)

    doc = yaml.safe_load(text)
    # The description must no longer attribute a negative to the reference.
    desc = doc["description"]
    assert "reference reports no GAP measurement" not in desc, desc[-300:]
    assert "has been located" in desc
    # The GO:0005096 row must now carry both PMID:18809720 clauses plus the caveat.
    row = next(
        a for a in doc["existing_annotations"] if a["term"]["id"] == "GO:0005096"
    )
    quotes = [s["supporting_text"] for s in row["review"]["supported_by"]]
    assert any("10 subfamilies" in q for q in quotes), quotes
    assert any("without promoting GTP" in q for q in quotes), quotes
    assert any("with the exception of the ADAPs" in q for q in quotes), quotes
    print(f"{len(EDITS)} edits applied; GO:0005096 row now carries {len(quotes)} quotes")


if __name__ == "__main__":
    main()
