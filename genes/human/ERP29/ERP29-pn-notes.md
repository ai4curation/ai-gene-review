# ERP29 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P30040
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ERP29/ERP29-ai-review.yaml](ERP29-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ERP29/ERP29-ai-review.html](ERP29-ai-review.html)
- Gene notes: present - [genes/human/ERP29/ERP29-notes.md](ERP29-notes.md)
- GOA TSV: present - [genes/human/ERP29/ERP29-goa.tsv](ERP29-goa.tsv)
- UniProt record: present - [genes/human/ERP29/ERP29-uniprot.txt](ERP29-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ERP29.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ERP29.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ERP29.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ERP29.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: ERP29 (endoplasmic reticulum resident protein 29; also called ERp28 and ERp31) is a soluble, ER-lumenal, homodimeric member of the protein disulfide isomerase (PDI) family that is catalytically redox-inactive - it has a thioredoxin-like fold but lacks the CXXC active-site motif and is not a disulfide isomerase. It functions as a non-catalytic escort/chaperone that assists the folding, processing and trafficking of secretory cargo in the ER, and is a component of a large ER chaperone multiprotein complex (containing BiP/HSPA5, GRP94/HSP90B1, PDI, the Hsp40 co-chaperone ERdj3/DNAJB11, cyclophilin B/PPIB, ERp72/PDIA4, UGGT1 and SDF2L1) that binds nascent, incompletely folded clients such as immunoglobulin heavy chains. It is retained in the ER lumen by a C-terminal KEEL retention signal and is broadly expressed, especially in secretory tissues; pools have also been detected at the cell surface, in melanosomes and secreted. Beyond its core chaperone role it has been implicated in handling of specific cargo (e.g. thyroglobulin, connexins) and in toxin/virus membrane penetration, and in cell-context-specific signaling (p38 MAPK, gene expression and secretion control in cancer models).
- Existing/core annotation action counts: ACCEPT: 9; KEEP_AS_NON_CORE: 19; MARK_AS_OVER_ANNOTATED: 1

## PN Consistency Summary

- **Consistency:** Review, notes, and UniProt agree that ERP29 is a non-catalytic, redox-inactive PDI-family escort/chaperone — it has a thioredoxin-like fold but LACKS the CXXC (CGHC) active-site motif and is NOT a disulfide isomerase. The PN-node mapping CONTRADICTS this: the "Protein disulfide isomerases" group projects GO:0003756 positively onto ERP29, but ERP29's only GOA annotation to GO:0003756 is `NOT|enables` (IKR, PMID:9738895) and the review ACCEPTs that negation. So the PN group rationale ("catalytically active family members") is correct only for the catalytic PDIs — ERP29 is the family exception, mis-swept into the group projection.
- **PN story / NEW pressure:** GO:0003756 (VERIFIED real via OLS) is a catalytic isomerase activity ERP29 demonstrably does not have. This is not a defensible NEW term for ERP29 — it directly opposes the negated experimental annotation and the no-CXXC biology. The review's true core MF is GO:0051087 protein-folding chaperone binding (ACCEPT), already captured. Conclude: OVER-REACHES (worse — actively contradicted), do NOT add.
- **Evidence alignment:** PN node carries no reference titles. Review well-anchored: PMID:9738895 (lacks CXXC; founding characterization, VERIFIED) and PMID:12475965 (ER chaperone multiprotein complex, VERIFIED). No shared evidence supports a disulfide-isomerase-activity claim; the cited PMID:9738895 in fact establishes the opposite.
- **Verdict:** OVER-REACHES / CONTRADICTED — reject projected GO:0003756 for ERP29; the gene is a non-catalytic PDI member whose function is already captured by GO:0051087. **Recommended edits:** [MAP] do not propagate GO:0003756 to ERP29 (it carries a curated NOT for this term); exclude non-catalytic PDI-family members from the group's isomerase projection or re-map ERP29 to GO:0051087 protein-folding chaperone binding.

## Full Consistency Review

- **UniProt:** P30040 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE (exhaustive; ~32 annotations, notes present, no provider deep-research file)
- **PN placement:** `ER proteostasis|Folding enzyme|Protein disulfide isomerases` ; **PN-node mapping:** group (Protein disulfide isomerases)→GO:0003756 protein disulfide isomerase activity (mapped/ok_for_propagation, goa_status=new_to_goa); class (Folding enzyme)→no_mapping; branch→no_mapping.
- **Consistency:** Review, notes, and UniProt agree that ERP29 is a non-catalytic, redox-inactive PDI-family escort/chaperone — it has a thioredoxin-like fold but LACKS the CXXC (CGHC) active-site motif and is NOT a disulfide isomerase. The PN-node mapping CONTRADICTS this: the "Protein disulfide isomerases" group projects GO:0003756 positively onto ERP29, but ERP29's only GOA annotation to GO:0003756 is `NOT|enables` (IKR, PMID:9738895) and the review ACCEPTs that negation. So the PN group rationale ("catalytically active family members") is correct only for the catalytic PDIs — ERP29 is the family exception, mis-swept into the group projection.
- **PN story / NEW pressure:** GO:0003756 (VERIFIED real via OLS) is a catalytic isomerase activity ERP29 demonstrably does not have. This is not a defensible NEW term for ERP29 — it directly opposes the negated experimental annotation and the no-CXXC biology. The review's true core MF is GO:0051087 protein-folding chaperone binding (ACCEPT), already captured. Conclude: OVER-REACHES (worse — actively contradicted), do NOT add.
- **Mapping strategy:** This gene SHOULD change the group projection. The catalytic-PDI mapping (GO:0003756) is the right target for active members (PDIA1, etc.) but must NOT propagate to the non-catalytic ERP29; the group node needs a per-member exclusion or ERP29 should map to a chaperone-binding/escort term (GO:0051087) instead.
- **Evidence alignment:** PN node carries no reference titles. Review well-anchored: PMID:9738895 (lacks CXXC; founding characterization, VERIFIED) and PMID:12475965 (ER chaperone multiprotein complex, VERIFIED). No shared evidence supports a disulfide-isomerase-activity claim; the cited PMID:9738895 in fact establishes the opposite.
- **Verdict:** OVER-REACHES / CONTRADICTED — reject projected GO:0003756 for ERP29; the gene is a non-catalytic PDI member whose function is already captured by GO:0051087. **Recommended edits:** [MAP] do not propagate GO:0003756 to ERP29 (it carries a curated NOT for this term); exclude non-catalytic PDI-family members from the group's isomerase projection or re-map ERP29 to GO:0051087 protein-folding chaperone binding.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/ERP29/ERP29-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Folding enzyme | Protein disulfide isomerases
- UniProt: P30040
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Folding enzyme|Protein disulfide isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003756 protein disulfide isomerase activity]
        rationale: This PN group captures the canonical ER protein-disulfide-isomerase folding enzymes. GO protein disulfide isomerase activity is the cleanest propagation target for the catalytically active family members.
    - [class] ER proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0003756 protein disulfide isomerase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Folding enzyme|Protein disulfide isomerases

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
