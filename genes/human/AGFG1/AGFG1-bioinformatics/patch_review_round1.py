"""Round-1 reviewer response: four YAML edits plus one new annotation row.

Applied by script, with every anchor asserted present before replacement and every
replacement asserted to have landed, because "fixed in N places, landed in N-1" is
this campaign's most-recurring defect. Idempotent - refuses to run twice.

Reviewer items addressed here (item 1, the empty zinc_site.json, was fixed in
zinc_site.py; item 5 was already fixed in commit ee64a787 before the review landed):

  2. GO:0035615 entails the coat-bridging that GO:0030276 was withheld for. The
     entailment is acknowledged, and the reviewer's premise that GO:0140312 "does
     not commit to clathrin" is corrected - its own definition names the coat's
     scaffolding elements explicitly, so retreating to the parent does not avoid
     the entailment and adds a cargo-receptor clause that is wrong here.
  3. GO:0008270's IDA-with-file:-reference. Answered with a fact rather than a
     convention: neither structure has a primary publication (PDBe reports both as
     "To be published", null PubMed id, null DOI), so no PMID exists to carry it.
  4. Whether the HIV-1 Rev role belongs in core_functions. Kept, deliberately, with
     the reasoning stated and a knowledge gap added for the nuclear pool's host
     function.
  6. The acrosome CC decision. GO:0001669 is declined on its definition (it denotes
     the mature acrosome, which never forms in the null) and on the absence of human
     evidence - but the search for it turned up GO:0120211 proacrosomal vesicle
     fusion, whose definition matches the mouse phenotype exactly and which is a
     verified descendant of the accepted GO:0001675. That is proposed as a NEW ISS
     row, which is a better answer than the CC the reviewer asked about.

Usage: uv run python patch_review_round1.py
"""

from __future__ import annotations

import pathlib

import yaml

HERE = pathlib.Path(__file__).parent
REVIEW = HERE.parent / "AGFG1-ai-review.yaml"
DONE_MARKER = "GO:0120211"

EDITS: list[tuple[str, str]] = [
    # Item 2
    (
        """      review - so GO:0030276 clathrin binding is deliberately NOT proposed. The functional
      term rests on cargo binding, coated-pit colocalisation and the depletion phenotype,
      not on a measured clathrin contact.""",
        """      review - so GO:0030276 clathrin binding is deliberately NOT proposed. The functional
      term rests on cargo binding, coated-pit colocalisation and the depletion phenotype,
      not on a measured clathrin contact. The entailment between the two runs one way and
      is worth stating rather than eliding: because GO:0035615 sits under GO:0140312,
      asserting it does commit to bridging cargo to the coat. Retreating to that parent
      would not avoid the commitment - GO:0140312's own definition reads "Binding directly
      to the structural scaffolding elements of a vesicle coat (such as clathrin or COPII),
      and bridging the membrane, cargo receptor, and membrane deformation machinery", so it
      names the coat too and adds a cargo-receptor clause that is wrong here, since VAMP7
      is the cargo and not a receptor. What discharges the commitment is measurement rather
      than the motif argument: concentration-dependent binding to the FCHO1 mu-homology
      domain with controls excluding an indirect route, direct colocalisation with clathrin
      and AP-2 in coated pits and vesicles, and a depletion phenotype that phenocopies
      clathrin depletion for this cargo. GO:0030276 remains withheld because it would
      assert something narrower and stronger - a directly assayed AGFG1-clathrin contact -
      which no experiment provides.""",
    ),
    # Item 3
    (
        """      GOA, so the term is absent from all 35 GOA rows. This is the mirror of the DNA-binding
      keyword on the same entry, which is not supported and is filed as a UniProt
      correction request instead.""",
        """      GOA, so the term is absent from all 35 GOA rows. This is the mirror of the DNA-binding
      keyword on the same entry, which is not supported and is filed as a UniProt
      correction request instead. On the choice of reference: neither structure has a
      primary publication. PDBe reports 2OLM as "ArfGap domain of HIV-1 Rev binding
      protein" and 2D9L as "Solution structure of the ArfGap domain of human RIP", both
      "To be published" with a null PubMed id and a null DOI, and UniProt records 2D9L
      only as submitted to the PDB. So no PMID exists to carry original_reference_id. The
      evidence code stays IDA because the assay is the two deposited structures
      themselves; the file: reference points at the committed computation over their
      coordinates, which is the only citable record of the coordination shell.""",
    ),
    # Item 4
    (
        """    RNA rather than to nuclear export generally. The contact with Rev is indirect, bridged by
    CRM1 through AGFG1's FG repeats, so no direct molecular function is asserted for this
    role.""",
        """    RNA rather than to nuclear export generally. The contact with Rev is indirect, bridged by
    CRM1 through AGFG1's FG repeats, so no direct molecular function is asserted for this
    role. This is host machinery appropriated by a virus rather than an evolved function of
    AGFG1, and it is kept here as a deliberate judgement rather than by default: GO annotates
    host gene products to viral-process terms as a matter of course, and this is the only
    characterised activity of AGFG1's nuclear pool, so dropping the block would leave the
    four accepted nucleus rows with no functional account at all. That absence is itself the
    finding, and it is recorded as a knowledge gap below.""",
    ),
    (
        """  knowledge_gaps:
  - gap_statement: >-
      GO has no term for Rev-dependent export of intron-retaining viral RNA, so this role
      can only be recorded with a general viral-transport parent.""",
        """  knowledge_gaps:
  - gap_statement: >-
      The host function of AGFG1's nuclear pool is undetermined. Every characterised
      activity of the nuclear fraction is the appropriated HIV-1 Rev role; no endogenous
      nuclear substrate, cargo or process has been identified.
    boundary: >-
      Established: AGFG1 is in the nucleus by two independent immunofluorescence studies,
      its FG repeats bind CRM1, and it is required for Rev-directed viral RNA to leave the
      nuclear periphery. Excluded: a general host mRNA-export role, since bulk poly(A)+
      mRNA, nuclear proteins and NES-containing proteins are all unaffected when AGFG1 is
      ablated. What is missing is any endogenous counterpart of the viral cargo.
    gap_kind:
    - BIOLOGY
    resolution: >-
      Identify the endogenous RNAs or proteins whose nuclear-periphery-to-cytoplasm
      movement requires AGFG1, if any - for example by CRM1-dependent export profiling in
      AGFG1-depleted cells.
    provenance:
    - reference_id: PMID:14701878
      supporting_text: 'We further show that the RNA mislocalization pattern resulting from
        loss of hRIP activity is highly specific to Rev function: the intracellular distribution
        of cellular poly(A)(+) mRNA, nuclear proteins, and, most important, NES-containing
        proteins, are unaffected.'
  - gap_statement: >-
      GO has no term for Rev-dependent export of intron-retaining viral RNA, so this role
      can only be recorded with a general viral-transport parent.""",
    ),
    # Item 6: the new row, inserted after the GO:0008270 NEW row (the last entry
    # before core_functions).
    (
        """core_functions:
- description: >-
    Cargo-selective clathrin adaptor (CLASP) for the R-SNARE VAMP7.""",
        """- term:
    id: GO:0120211
    label: proacrosomal vesicle fusion
  evidence_type: ISS
  original_reference_id: PMID:11711676
  qualifier: involved_in
  supporting_entities:
  - UniProtKB:Q8K2K6
  review:
    summary: >-
      Proposed as the specific process the mouse experiments actually measured. The accepted
      GO:0001675 acrosome assembly IBA is correct but general; what the null blocks is
      precisely the fusion step, and GO has a term for it.
    action: NEW
    reason: >-
      GO:0120211's definition is "Fusion of the membrane of proacrosomal vesicle with the
      membrane of another proacrosomal vesicle to form the acrosome", which is the mouse
      phenotype verbatim: the vesicles form, coat with AGFG1, and cannot fuse. It was
      verified to be a descendant of GO:0001675 over is_a/part_of, so this row is additive
      and asserts strictly more than - not something different from - the IBA it sits under.
      Evidence code ISS with the mouse orthologue in supporting_entities, because the
      measurement is on mouse Agfg1 (Q8K2K6) and human AGFG1's support is orthology; ISS
      takes the sequence-similar entity, not the interactor. This row also records the
      decision on the acrosome-associated cellular component, which was raised in review:
      GO:0001669 acrosomal vesicle is NOT proposed, on two grounds. Its definition denotes
      the mature organelle - "A structure in the head of a spermatozoon that contains acid
      hydrolases ... derived from the lysosome" - whereas AGFG1 is documented on the
      cytosolic surface of the precursor vesicles, and in the null the mature acrosome never
      forms at all; and the evidence is mouse-only, so a human CC row would rest on
      orthology for a compartment whose human counterpart has not been imaged. Searching
      for that CC is what surfaced GO:0120211, which is the better annotation.
    supported_by:
    - reference_id: PMID:11711676
      supporting_text: Although proacrosomic vesicles form in spermatids that lack Hrb, the
        vesicles are unable to fuse, blocking acrosome development at step 2.
    - reference_id: PMID:11711676
      supporting_text: We conclude that Hrb is required for docking and/or fusion of proacrosomic
        vesicles during acrosome biogenesis.
core_functions:
- description: >-
    Cargo-selective clathrin adaptor (CLASP) for the R-SNARE VAMP7.""",
    ),
    # ... and add it to the acrosome core function's process list.
    (
        """  directly_involved_in:
  - id: GO:0001675
    label: acrosome assembly
  locations:
  - id: GO:0031410
    label: cytoplasmic vesicle
  supported_by:
  - reference_id: PMID:11711676
    supporting_text: In wild-type spermatids, Hrb is associated with the cytosolic surface""",
        """  directly_involved_in:
  - id: GO:0001675
    label: acrosome assembly
  - id: GO:0120211
    label: proacrosomal vesicle fusion
  locations:
  - id: GO:0031410
    label: cytoplasmic vesicle
  supported_by:
  - reference_id: PMID:11711676
    supporting_text: In wild-type spermatids, Hrb is associated with the cytosolic surface""",
    ),
]


def main() -> None:
    text = REVIEW.read_text()
    if DONE_MARKER in text:
        print("already patched; nothing to do")
        return

    for old, new in EDITS:
        count = text.count(old)
        assert count == 1, f"anchor found {count} times:\n{old[:200]}"
        text = text.replace(old, new, 1)
        assert new in text, "replacement did not land"
    REVIEW.write_text(text)

    doc = yaml.safe_load(text)
    anns = doc["existing_annotations"]
    new_rows = [a for a in anns if a["review"]["action"] == "NEW"]
    assert len(new_rows) == 6, f"expected 6 NEW rows, found {len(new_rows)}"
    assert any(a["term"]["id"] == "GO:0120211" for a in new_rows)
    cf2 = doc["core_functions"][1]
    assert [t["id"] for t in cf2["directly_involved_in"]] == ["GO:0001675", "GO:0120211"]
    assert "molecular_function" not in cf2, "the hedged MF came back"
    cf3 = doc["core_functions"][2]
    assert len(cf3["knowledge_gaps"]) == 2, cf3["knowledge_gaps"]
    print(f"{len(EDITS)} edits applied; 6 NEW rows; core_functions verified")


if __name__ == "__main__":
    main()
