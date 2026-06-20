# SH3GLB1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y371
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SH3GLB1/SH3GLB1-ai-review.yaml](SH3GLB1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/SH3GLB1/SH3GLB1-ai-review.html](SH3GLB1-ai-review.html)
- Gene notes: present - [genes/human/SH3GLB1/SH3GLB1-notes.md](SH3GLB1-notes.md)
- GOA TSV: present - [genes/human/SH3GLB1/SH3GLB1-goa.tsv](SH3GLB1-goa.tsv)
- UniProt record: present - [genes/human/SH3GLB1/SH3GLB1-uniprot.txt](SH3GLB1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SH3GLB1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SH3GLB1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SH3GLB1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SH3GLB1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: SH3GLB1 encodes endophilin B1/Bif-1, an N-BAR/SH3 membrane-curvature adaptor that links UVRAG/BECN1/PI3KC3-C2 autophagy signaling to ATG9-positive Golgi membrane fission and autophagosome assembly. Its core functions include PI3KC3 activation, adaptor-mediated association with UVRAG/Beclin 1, and membrane fission/tubulation at Golgi/autophagosome membranes. SH3GLB1 also has supported non-core roles in mitochondrial outer membrane dynamics, Bax/Bak-dependent apoptosis, receptor degradation, cytokinesis, and older lipid-binding/acyltransferase biochemistry.
- Existing/core annotation action counts: ACCEPT: 14; KEEP_AS_NON_CORE: 14; MARK_AS_OVER_ANNOTATED: 21; MODIFY: 12

## PN Consistency Summary

- **Consistency:** Consistent. Notes, review, and PN agree SH3GLB1/Bif-1/endophilin B1 is a POSITIVE N-BAR/SH3 adaptor that activates PI3KC3 via UVRAG (PMID:17891140) and drives ATG9/Golgi membrane fission (PMID:21068542). PN Notes ("binds to UVRAG and promotes activity") correctly state the positive direction — contrast with the RUBCNL row, which was mislabeled. No contradictions.
- **PN story / NEW pressure:** PN asserts GO:0034272 membership. GOA has only generic GO:0032991 (protein-containing complex, IDA+IEA), so GO:0034272 is `more_specific_than_existing_goa`. Review handles this via MODIFY of GO:0032991 → proposed_replacement GO:0034272 (rather than a standalone NEW row). GO:0034272 verified real. Review also adds membrane-fission (GO:0090148) and positive regulation of membrane tubulation (GO:1903527) as core — both verified real, non-obsolete, and beyond the PN story. Verdict: ADD/refine to GO:0034272 (review does via MODIFY) — aligned with PN.
- **Evidence alignment:** PN cites Annual Review, a cardiovascular review, and PMID:19270696. Review uses primary PMID:17891140 (Bif-1/UVRAG autophagy), 21068542 (ATG9/Golgi fission), 11604418 (endophilin membrane tubulation), 15452144/16227588 (mitochondria/Bax, non-core), 12456676 (LPAAT, non-core). PMID:19270696 is not cited in this review; the PN reference list is shared-branch boilerplate, only loosely SH3GLB1-specific.
- **Verdict:** Consistent; PN GO:0034272 refines the gene's generic GO:0032991 (more_specific) and the review captures it via MODIFY plus richer membrane-fission/tubulation MF/BP terms (all verified). No edits required.

## Full Consistency Review

- **UniProt:** Q9Y371 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Class 3 PI3K complex 2 component` ; **PN-node mapping:** `type` leaf mapped, `ok_for_propagation_to_go` → GO:0034272, goa_status `more_specific_than_existing_goa`; ancestors GO:0035032 / GO:0016236 context_only.
- **Consistency:** Consistent. Notes, review, and PN agree SH3GLB1/Bif-1/endophilin B1 is a POSITIVE N-BAR/SH3 adaptor that activates PI3KC3 via UVRAG (PMID:17891140) and drives ATG9/Golgi membrane fission (PMID:21068542). PN Notes ("binds to UVRAG and promotes activity") correctly state the positive direction — contrast with the RUBCNL row, which was mislabeled. No contradictions.
- **PN story / NEW pressure:** PN asserts GO:0034272 membership. GOA has only generic GO:0032991 (protein-containing complex, IDA+IEA), so GO:0034272 is `more_specific_than_existing_goa`. Review handles this via MODIFY of GO:0032991 → proposed_replacement GO:0034272 (rather than a standalone NEW row). GO:0034272 verified real. Review also adds membrane-fission (GO:0090148) and positive regulation of membrane tubulation (GO:1903527) as core — both verified real, non-obsolete, and beyond the PN story. Verdict: ADD/refine to GO:0034272 (review does via MODIFY) — aligned with PN.
- **Mapping strategy:** Supports the C2-component mapping; the PN-projected GO:0034272 is NARROWER than the gene's existing generic GO:0032991, which is exactly the intended refinement (not an over-broad projection). As with the other C2 binders, `part_of` for an associating membrane-fission adaptor is defensible but borderline vs. an associated/recruitment relation — review flags this in suggested_questions. Ancestors correctly held too_broad.
- **Evidence alignment:** PN cites Annual Review, a cardiovascular review, and PMID:19270696. Review uses primary PMID:17891140 (Bif-1/UVRAG autophagy), 21068542 (ATG9/Golgi fission), 11604418 (endophilin membrane tubulation), 15452144/16227588 (mitochondria/Bax, non-core), 12456676 (LPAAT, non-core). PMID:19270696 is not cited in this review; the PN reference list is shared-branch boilerplate, only loosely SH3GLB1-specific.
- **Verdict:** Consistent; PN GO:0034272 refines the gene's generic GO:0032991 (more_specific) and the review captures it via MODIFY plus richer membrane-fission/tubulation MF/BP terms (all verified). No edits required.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/SH3GLB1/SH3GLB1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Class 3 PI3K complex 2, direct | Class 3 PI3K complex 2 component
- UniProt: Q9Y371
- In branches: ALP
- Notes: Member of class III PI3K complex 2 that binds to UVRAG and promotes activity
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
- GO:0034272 phosphatidylinositol 3-kinase complex, class III, type II | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Class 3 PI3K complex 2 component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
