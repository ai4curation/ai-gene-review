# RUBCNL PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H714
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/RUBCNL/RUBCNL-ai-review.yaml](RUBCNL-ai-review.yaml)
- AIGR review HTML: present - [genes/human/RUBCNL/RUBCNL-ai-review.html](RUBCNL-ai-review.html)
- Gene notes: present - [genes/human/RUBCNL/RUBCNL-notes.md](RUBCNL-notes.md)
- GOA TSV: present - [genes/human/RUBCNL/RUBCNL-goa.tsv](RUBCNL-goa.tsv)
- UniProt record: present - [genes/human/RUBCNL/RUBCNL-uniprot.txt](RUBCNL-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/RUBCNL.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/RUBCNL.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RUBCNL.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/RUBCNL.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: RUBCNL encodes PACER, a Rubicon-like autophagy enhancer that acts at late autophagosome maturation. It is recruited to STX17-positive autophagosome membranes, interacts with UVRAG/STX17, promotes recruitment of PI3K/PI3KC3 and HOPS complexes, stimulates Vps34/PI3KC3-dependent PtdIns(3)P production, and supports autophagosome-endosome/lysosome fusion. RUBCNL functions as an autophagosome-maturation adaptor/recruitment factor associated with PI3KC3-C2 and HOPS.
- Existing/core annotation action counts: ACCEPT: 13; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 2; MODIFY: 1; NEW: 2

## PN Consistency Summary

- **Consistency:** A directionality mismatch in the shared PN Notes. The PN Notes string is "Member of class III PI3K complex 2 that binds to UVRAG and inhibits activity" — copied from the Rubicon row — but RUBCNL/PACER is a POSITIVE late-autophagy regulator that stimulates Vps34 activity and recruits PI3KC3/HOPS (PMID:28306502, 30704899; UniProt). Review and notes are correct (positive); the PN workbook Notes field is wrong for this gene. Flag.
- **PN story / NEW pressure:** PN asserts GO:0034272 membership absent from GOA (`new_to_goa`). Review adds GO:0034272 part_of as action NEW (PMID:28306502), plus GO:0030674 protein-macromolecule adaptor activity (NEW) replacing generic protein binding. GO:0034272 verified real. Verdict: ADD GO:0034272 (review already did) + adaptor MF — aligned with and richer than PN.
- **Evidence alignment:** Divergence. PN cites Annual Review, a cardiovascular review, and PMID:19270696 (the Atg14L/Rubicon paper) — none of which is PACER-specific; PMID:19270696 is not cited in the RUBCNL review (and is not PACER-relevant). Review uses the correct primary literature: PMID:28306502 (PACER discovery), 30704899 (mTORC1/TIP60). PN reference set is essentially a shared-branch boilerplate, weakly matched to this gene.
- **Verdict:** Consistent on biology, but the PN workbook Notes mis-state PACER as inhibitory ("inhibits activity") — it is a positive regulator. NEW GO:0034272 matches PN projection (verified). **Recommended edits:** none to the gene YAML (correct); upstream PN-workbook Notes for RUBCNL should be corrected from "inhibits activity" to a positive/recruitment role, and the PN reference list (PMID:19270696) is not PACER-specific.

## Full Consistency Review

- **UniProt:** Q9H714 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Class 3 PI3K complex 2 component` ; **PN-node mapping:** `type` leaf mapped, `ok_for_propagation_to_go` → GO:0034272, goa_status `new_to_goa`; ancestors GO:0035032 / GO:0016236 context_only.
- **Consistency:** A directionality mismatch in the shared PN Notes. The PN Notes string is "Member of class III PI3K complex 2 that binds to UVRAG and inhibits activity" — copied from the Rubicon row — but RUBCNL/PACER is a POSITIVE late-autophagy regulator that stimulates Vps34 activity and recruits PI3KC3/HOPS (PMID:28306502, 30704899; UniProt). Review and notes are correct (positive); the PN workbook Notes field is wrong for this gene. Flag.
- **PN story / NEW pressure:** PN asserts GO:0034272 membership absent from GOA (`new_to_goa`). Review adds GO:0034272 part_of as action NEW (PMID:28306502), plus GO:0030674 protein-macromolecule adaptor activity (NEW) replacing generic protein binding. GO:0034272 verified real. Verdict: ADD GO:0034272 (review already did) + adaptor MF — aligned with and richer than PN.
- **Mapping strategy:** Supports (does not change) the C2-component → GO:0034272 mapping. As with RUBCN, PACER recruits/associates with PI3KC3-C2 rather than being a defined stoichiometric subunit, so `part_of` is defensible but borderline (review flags this in suggested_questions). PN-projected term coincides with the review's NEW term.
- **Evidence alignment:** Divergence. PN cites Annual Review, a cardiovascular review, and PMID:19270696 (the Atg14L/Rubicon paper) — none of which is PACER-specific; PMID:19270696 is not cited in the RUBCNL review (and is not PACER-relevant). Review uses the correct primary literature: PMID:28306502 (PACER discovery), 30704899 (mTORC1/TIP60). PN reference set is essentially a shared-branch boilerplate, weakly matched to this gene.
- **Verdict:** Consistent on biology, but the PN workbook Notes mis-state PACER as inhibitory ("inhibits activity") — it is a positive regulator. NEW GO:0034272 matches PN projection (verified). **Recommended edits:** none to the gene YAML (correct); upstream PN-workbook Notes for RUBCNL should be corrected from "inhibits activity" to a positive/recruitment role, and the PN reference list (PMID:19270696) is not PACER-specific.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/RUBCNL/RUBCNL-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Class 3 PI3K complex 2, direct | Class 3 PI3K complex 2 component
- UniProt: Q9H714
- In branches: ALP
- Notes: Member of class III PI3K complex 2 that binds to UVRAG and inhibits activity
- PN references (titles):
    - Mammalian Autophagy: How Does It Work? | Annual Review of Biochemistry (annualreviews.org)
    - role of autophagy in cardiovascular pathology | Cardiovascular Research | Oxford Academic (oup.com)
    - Two Beclin 1-binding proteins, Atg14L and Rubicon, reciprocally regulate autophagy at different stages | Nature Cell Biology
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Class 3 PI3K complex 2 component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0034272 phosphatidylinositol 3-kinase complex, class III, type II]
        rationale: This PN type denotes component membership in the direct class III PI3K complex 2 module used during autophagosome maturation and lysosome fusion. The corresponding GO complex term is the right propagation target.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0034272 phosphatidylinositol 3-kinase complex, class III, type II | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Class 3 PI3K complex 2 component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
