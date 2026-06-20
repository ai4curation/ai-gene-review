# AGR2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O95994
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1341)
- Batch change status: modified

## Source Files Checked

- AIGR review YAML: present - [genes/human/AGR2/AGR2-ai-review.yaml](AGR2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AGR2/AGR2-ai-review.html](AGR2-ai-review.html)
- Gene notes: present - [genes/human/AGR2/AGR2-notes.md](AGR2-notes.md)
- GOA TSV: present - [genes/human/AGR2/AGR2-goa.tsv](AGR2-goa.tsv)
- UniProt record: present - [genes/human/AGR2/AGR2-uniprot.txt](AGR2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AGR2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AGR2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AGR2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AGR2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AGR2/AGR2-deep-research-falcon.md](AGR2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AGR2 is a secretory-pathway, ER-retained anterior gradient/thioredoxin-fold protein expressed most prominently in mucus-producing epithelial cells. Its best-supported physiological role is as an ER foldase/protein disulfide-isomerase-family factor for gel-forming mucins, especially MUC2: AGR2 forms mixed disulfide-linked complexes with MUC2, is required for intestinal mucus production, and human AGR2 deficiency causes goblet-cell depletion, loss of gel-forming mucins, ER stress, mucus barrier failure, and infantile inflammatory bowel disease. AGR2 can also be detected extracellularly and has reported cancer-associated interactions with dystroglycan, LYPD3/C4.4a, EGFR, and cell-adhesion/inflammatory pathways, but these are best treated as context-dependent or non-core relative to its conserved ER mucin-processing function.
- Existing/core annotation action counts: ACCEPT: 11; KEEP_AS_NON_CORE: 15; MARK_AS_OVER_ANNOTATED: 13; MODIFY: 6; NEW: 3; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Deep research (Falcon), notes, review YAML, and the PN PDI mapping are consistent. All frame AGR2 as a secretory/ER-retained (KTEL) **PDI-family/thioredoxin-fold foldase** that forms mixed disulfides with MUC2 and is required for gel-forming mucin production (PMID:19359471, 34237462). The review honestly tracks the literature conflict (PMID:25666625 argued EGFR, not MUC2, is the major mixed-disulfide substrate) but defensibly weights the MUC2/mucin model as core. No internal contradiction.
- **PN story / NEW pressure:** GO:0003756 (OLS-verified real) is **not** in AGR2's GOA (GOA MF = dystroglycan/EGFR/identical-protein/homodimerization binding only), confirming PN's new_to_goa. The review **adds** it as a MODIFY proposed_replacement for two generic protein-binding rows (PMID:19359471, 34237462), alongside GO:0034975 protein folding in ER. This matches the PN projection. Caveat: AGR2 is a non-canonical "pseudo-PDI" (CXXS, single active-site Cys), so true isomerase catalysis is debated; the review's mixed-disulfide/foldase framing is the safest support. Conclusion: legitimate ADD, executed; mild over-reach risk on the term name only.
- **Evidence alignment:** PN dossier lists no reference titles for AGR2. Review evidence (PMID:19359471, 22184114, 23274113, 25666625, 31040128, 34237462, 38177498/501) is reviewer-supplied; alignment is by biology (PDI/mucin), not shared citation list.
- **Verdict:** Consistent; PN GO:0003756 projection validated and added via MODIFY; only nuance is the pseudo-PDI catalysis debate (review mitigates via mixed-disulfide evidence). **Recommended edits:** none required; [REF] optionally note in review that AGR2 is a non-canonical CXXS PDI-family member (catalytic isomerase activity debated) to pre-empt over-reading GO:0003756.

## Full Consistency Review

- **UniProt:** O95994 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Folding enzyme|Protein disulfide isomerases` ; **PN-node mapping:** group `Protein disulfide isomerases`=mapped→**GO:0003756 protein disulfide isomerase activity** (new_to_goa); class `Folding enzyme`=no_mapping; branch `ER proteostasis`=no_mapping.
- **Consistency:** Deep research (Falcon), notes, review YAML, and the PN PDI mapping are consistent. All frame AGR2 as a secretory/ER-retained (KTEL) **PDI-family/thioredoxin-fold foldase** that forms mixed disulfides with MUC2 and is required for gel-forming mucin production (PMID:19359471, 34237462). The review honestly tracks the literature conflict (PMID:25666625 argued EGFR, not MUC2, is the major mixed-disulfide substrate) but defensibly weights the MUC2/mucin model as core. No internal contradiction.
- **PN story / NEW pressure:** GO:0003756 (OLS-verified real) is **not** in AGR2's GOA (GOA MF = dystroglycan/EGFR/identical-protein/homodimerization binding only), confirming PN's new_to_goa. The review **adds** it as a MODIFY proposed_replacement for two generic protein-binding rows (PMID:19359471, 34237462), alongside GO:0034975 protein folding in ER. This matches the PN projection. Caveat: AGR2 is a non-canonical "pseudo-PDI" (CXXS, single active-site Cys), so true isomerase catalysis is debated; the review's mixed-disulfide/foldase framing is the safest support. Conclusion: legitimate ADD, executed; mild over-reach risk on the term name only.
- **Mapping strategy:** Group-level GO:0003756 is the cleanest catalytic-family target and is correctly scoped (review does not extend to broad ER proteostasis or generic UPR). The review separately adds a narrow IRE1beta-repression UPR role (PMID:38177498/38177501) the PN node does not surface — enrichment, not conflict. No mapping change needed.
- **Evidence alignment:** PN dossier lists no reference titles for AGR2. Review evidence (PMID:19359471, 22184114, 23274113, 25666625, 31040128, 34237462, 38177498/501) is reviewer-supplied; alignment is by biology (PDI/mucin), not shared citation list.
- **Verdict:** Consistent; PN GO:0003756 projection validated and added via MODIFY; only nuance is the pseudo-PDI catalysis debate (review mitigates via mixed-disulfide evidence). **Recommended edits:** none required; [REF] optionally note in review that AGR2 is a non-canonical CXXS PDI-family member (catalytic isomerase activity debated) to pre-empt over-reading GO:0003756.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AGR2/AGR2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Folding enzyme | Protein disulfide isomerases
- UniProt: O95994
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
