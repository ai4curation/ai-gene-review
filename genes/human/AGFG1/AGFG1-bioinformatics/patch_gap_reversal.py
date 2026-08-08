"""RETRACTION: GO:0005096 moves from KEEP_AS_NON_CORE to MARK_AS_OVER_ANNOTATED.

I tested ONE of the three residues the field says Arf GAP catalysis requires. The
concurrent AGFG2 review surfaced PMID:23433073, which names three - W451, R469 and
D484 in ASAP3 - and states that "Mutation of any one of these three residues leads to
severe loss in Arf GAP activity". I verified this independently for AGFG1 rather than
inheriting it (catalytic_residues.py, with all three controls passing): AGFG1 keeps the
arginine finger at R57 but has Tyr39 where W is required and Thr71 where D is required.
1 of 3. Every GAP-competent control recovers 3 of 3, so the absence is biological.

So the pseudoenzyme hypothesis IS confirmed for this gene, and my headline
non-confirmation was an artefact of testing only the residue the 2008 nomenclature
paper happens to name. The reversal also RESOLVES rather than creates a tension: the
same paper says the predicted catalytic loss "should not be confused with consequent
changes in the ability to bind Arf family GTPases", which is exactly why AGFG1 is
proximal to ARF1/ARF3/ARF6 in a human interactome while having no GAP activity - an
Arf effector, not an Arf GAP.

It also removes an inconsistency between two independently-produced reviews of the
identical GOA row: paint/AGFG2 had already reached MARK_AS_OVER_ANNOTATED on this row.

Anchors asserted; idempotent.

Usage: uv run python patch_gap_reversal.py
"""

from __future__ import annotations

import pathlib

import yaml

HERE = pathlib.Path(__file__).parent
REVIEW = HERE.parent / "AGFG1-ai-review.yaml"
DONE_MARKER = "Tyr39"

NEW_SUMMARY = """      Over-annotated. The zinc finger and the arginine finger are intact, but the field
      identifies three residues as catalytically required and AGFG1 retains only one:
      it has Tyr39 where a tryptophan is needed and Thr71 where the aspartate that
      contacts the Arf catalytic glutamine is needed. Every GAP-competent ArfGAP tested
      keeps all three. AGFG proteins are Arf effectors rather than Arf GAPs, which is why
      AGFG1 sits with ARF1, ARF3 and ARF6 in a human interactome while no GAP activity has
      ever been measured for the subfamily."""

NEW_REASON = """      This row reverses an earlier verdict in this same review, and the reversal is the
      finding. The first pass tested the one residue the consensus-nomenclature paper names
      - the arginine finger of CX2CX16CX2CX4R - found it intact at Arg57, and reported the
      pseudoenzyme hypothesis as NOT confirmed. That was an artefact of testing one residue.
      PMID:23433073 names three positions as catalytically required (W451, R469 and D484 in
      ASAP3, the subfamily with a solved Arf6 complex) and states that mutating any one of
      them severely impairs activity: R469 is the arginine finger, D484 contacts the Arf6
      catalytic glutamine Q67 and stabilises switch 2, and W451 sits in the Arf-ArfGAP
      interface. Measured by alignment to the ASAP3 domain, with every GAP-competent member
      of the panel required to recover all three before any absence is reported: ARFGAP1,
      ARFGAP3, ASAP1, ASAP3 and SMAP1 all score 3/3, while human AGFG1 scores 1/3 - Tyr39
      for the tryptophan, Arg57 for the arginine, Thr71 for the aspartate. Human AGFG2,
      mouse Agfg1 and Drosophila drongo are identical in pattern, and the same alignment
      independently reproduces the arginine position that the motif scan gives, so two
      methods agree. This is the subfamily-wide loss the source paper predicts from 40 AGFG
      sequences, of which only two retain the aspartate and none the tryptophan. Two things
      the reversal does NOT do. It does not contradict the ARF-proximity result: the same
      paper is explicit that predicted catalytic loss "should not be confused with
      consequent changes in the ability to bind Arf family GTPases", and it proposes that
      such proteins act as Arf effectors - so binding retained plus catalysis lost is one
      coherent picture rather than two conflicting ones. And it does not make the fly
      genetics irrelevant, but it does reinterpret it: drongo's "GTPase-activating function"
      was assayed genetically, drongo itself scores 1/3, and the same paper's alternative -
      an Arf effector that antagonises an Arf-GEF without hydrolysing GTP - fits that
      genetics as well. MARK_AS_OVER_ANNOTATED rather than REMOVE, because the domain is
      genuine, Arf binding is real, and no direct assay has been run on the human protein
      either way; the annotation route is also specific and filable, since of AGFG1's four
      InterPro signatures only IPR001164, the pan-ArfGAP catalytic-domain entry, maps to
      GO:0005096, while the AGFG-specific family entry IPR052248 maps to nothing - so
      InterPro2GO is capable of restraint here and the claim comes from the one entry that
      cannot discriminate subfamilies. Note also that GO has merged the nine
      substrate-specific GAP terms into GO:0005096 (they are its secondaryIds), so there is
      no more specific term to fall back to. The concurrent review of the paralogue AGFG2
      reached the same verdict on this identical row from the same primary source, which is
      recorded here because an inconsistency between two independently-produced reviews of
      one row would itself be a defect."""

EDITS: list[tuple[str, str]] = [
    # Description: the apparatus is NOT complete.
    (
        """  vesicles including clathrin-coated pits and vesicles. Its ArfGAP domain retains the
  complete catalytic apparatus of the family - the four zinc-coordinating cysteines and the
  conserved arginine - and the Drosophila orthologue's GTPase-activating function is
  genetically required for Arf-dependent actomyosin contractility, but no direct GAP
  measurement on either human AGFG protein has been located.""",
        """  vesicles including clathrin-coated pits and vesicles. Its ArfGAP domain is structurally
  genuine - the four zinc-coordinating cysteines hold a zinc ion in both solved structures
  and the arginine finger is present at Arg57 - but two of the three residues required for
  GTP hydrolysis are substituted, as they are throughout the AGFG subfamily, so the domain
  is thought to bind Arf GTPases without accelerating their hydrolysis; no GAP activity has
  been measured for any AGFG protein, and the family is better described as an Arf effector
  than an Arf GAP.""",
    ),
    # Action
    (
        """    action: KEEP_AS_NON_CORE
    reason: >-
      The pseudoenzyme hypothesis was tested and NOT confirmed, and the test used a""",
        """    action: MARK_AS_OVER_ANNOTATED
    reason: >-
      SUPERSEDED_MARKER
      The pseudoenzyme hypothesis was tested and NOT confirmed, and the test used a""",
    ),
]


def main() -> None:
    text = REVIEW.read_text()
    if DONE_MARKER in text:
        print("already patched; nothing to do")
        return

    # 1. description
    old, new = EDITS[0]
    assert text.count(old) == 1, f"description anchor found {text.count(old)} times"
    text = text.replace(old, new, 1)

    # 2. replace the whole GO:0005096 review block's summary + action + reason, by
    #    locating the row and rewriting it through the raw text between known anchors.
    start = text.index("    id: GO:0005096")
    sb_anchor = text.index("    supported_by:", start)
    block = text[start:sb_anchor]
    assert "action: KEEP_AS_NON_CORE" in block, "GO:0005096 row is not where expected"
    head = block[: block.index("    summary: >-") + len("    summary: >-")]
    rebuilt = (
        head
        + "\n"
        + NEW_SUMMARY
        + "\n    action: MARK_AS_OVER_ANNOTATED\n    reason: >-\n"
        + NEW_REASON
        + "\n"
    )
    text = text[:start] + rebuilt + text[sb_anchor:]

    # 3. add the decisive quotes and a propagation_review to that row.
    quote_anchor = """    - reference_id: file:human/AGFG1/AGFG1-bioinformatics/RESULTS.md
      supporting_text: '**12/12 panel members retain CX2CX16CX2CX4R.**'"""
    assert text.count(quote_anchor) == 1
    text = text.replace(
        quote_anchor,
        quote_anchor
        + """
    - reference_id: PMID:23433073
      supporting_text: Mutation of any one of these three residues leads to severe loss in
        Arf GAP activity
    - reference_id: PMID:23433073
      supporting_text: Only two of the 40 AGFG sequences contain an aspartate at the position
        homologous to D47 in the other subfamilies
    - reference_id: PMID:23433073
      supporting_text: The AGFG consensus also uniquely lacks W14, which we predict to play
        a role in hydrophobic interactions with Arfs.
    - reference_id: PMID:23433073
      supporting_text: the ArfGAP is a very highly conserved structural domain that is predicted
        to have lost substantial levels of GAP activity in at least one subfamily (AGFG)
    - reference_id: PMID:23433073
      supporting_text: These predicted changes (including complete loss, potentially) in GAP
        activity or its regulation should not be confused with consequent changes in the
        ability to bind Arf family GTPases.
    - reference_id: file:human/AGFG1/AGFG1-bioinformatics/RESULTS.md
      supporting_text: '| **AGFG1 human (SUBJECT)** | Y39 | R57 | T71 | **1/3** |'""",
        1,
    )

    # 4. the propagation_review must now record a real failure.
    old_pr = """    propagation_review:
      root_cause: NO_FAILURE_NON_CORE
      source_entities:
      - source_id: InterPro:IPR001164
        source_label: Arf GTPase activating protein domain - the catalytic domain signature
          itself, not a bare fold
        source_status: SUPPORTS_TRANSFER
        comment: AGFG1 matches it over residues 11-135 and retains every determinant the
          signature's own description names. The signature cannot distinguish an active
          from an inactive family member, which is why the row is non-core rather than core."""
    assert text.count(old_pr) == 1, "propagation_review anchor not found"
    text = text.replace(
        old_pr,
        """    propagation_review:
      root_cause: PROPAGATION_BAD
      failure_modes:
      - PSEUDO_OR_SUBACTIVITY_LOSS
      - FUNCTIONAL_DIVERGENCE
      source_entities:
      - source_id: InterPro:IPR001164
        source_label: Arf GTPase activating protein domain - the pan-ArfGAP catalytic-domain
          signature, spanning 60678 proteins
        source_status: SUPPORTS_SOURCE_BUT_NOT_TARGET
        comment: >-
          The signature is sound and AGFG1 genuinely matches it over residues 11-135, but
          it cannot discriminate subfamilies. It maps to GO:0005096 while the AGFG-specific
          family entry IPR052248 maps to nothing, so the claim arrives from the one entry
          that cannot see the subfamily-wide loss of two of the three catalytically
          required residues.""",
        1,
    )

    # Parse BEFORE writing. The first run of this script wrote the file and then
    # failed to parse it, leaving broken YAML on disk that had to be restored from
    # git - and, worse, containing the DONE_MARKER, so a re-run would have reported
    # "already patched". Validate, then write.
    doc = yaml.safe_load(text)
    row = next(a for a in doc["existing_annotations"] if a["term"]["id"] == "GO:0005096")
    assert row["review"]["action"] == "MARK_AS_OVER_ANNOTATED", row["review"]["action"]
    assert "SUPERSEDED_MARKER" not in row["review"]["reason"]
    assert "Tyr39" in row["review"]["summary"]
    assert "Tyr39" in row["review"]["reason"] or "Thr71" in row["review"]["reason"]
    assert row["review"]["propagation_review"]["root_cause"] == "PROPAGATION_BAD"
    assert "PSEUDO_OR_SUBACTIVITY_LOSS" in row["review"]["propagation_review"]["failure_modes"]
    quotes = [s["supporting_text"] for s in row["review"]["supported_by"]]
    assert sum(1 for q in quotes if "AGFG" in q) >= 3, quotes
    assert "complete catalytic apparatus" not in doc["description"]
    # GO:0005096 must not be in core_functions (it never was, but assert it).
    cf_mfs = [cf.get("molecular_function", {}).get("id") for cf in doc["core_functions"]]
    assert "GO:0005096" not in cf_mfs
    REVIEW.write_text(text)
    assert yaml.safe_load(REVIEW.read_text()), "wrote an unparseable file"
    print(f"GO:0005096 -> MARK_AS_OVER_ANNOTATED; row now carries {len(quotes)} quotes")


if __name__ == "__main__":
    main()
