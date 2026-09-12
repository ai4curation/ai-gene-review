# TXNDC16 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9P2K2
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TXNDC16/TXNDC16-ai-review.yaml](TXNDC16-ai-review.yaml)
- AIGR review HTML: missing - genes/human/TXNDC16/TXNDC16-ai-review.html
- Gene notes: present - [genes/human/TXNDC16/TXNDC16-notes.md](TXNDC16-notes.md)
- GOA TSV: present - [genes/human/TXNDC16/TXNDC16-goa.tsv](TXNDC16-goa.tsv)
- UniProt record: present - [genes/human/TXNDC16/TXNDC16-uniprot.txt](TXNDC16-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TXNDC16.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TXNDC16.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TXNDC16.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TXNDC16.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/TXNDC16/TXNDC16-deep-research-falcon.md](TXNDC16-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: TXNDC16 (Thioredoxin domain-containing protein 16; also called ERp90 or KIAA1344) is a large (825 aa precursor) soluble glycoprotein of the protein disulfide isomerase (PDI) family resident in the endoplasmic reticulum lumen. After signal-peptide cleavage it comprises several (about five) thioredoxin (Trx)-like domains and is N-glycosylated, with at least some of its cysteines forming intramolecular disulfides. Notably, none of its Trx domains contains a canonical Cys-Xaa-Xaa-Cys redox active-site motif, so it is likely a redox-inactive or non-catalytic PDI-family member whose precise enzymatic activity remains uncharacterized. Its best-supported molecular role is as a direct interaction partner of the ER-associated degradation (ERAD) flavoprotein ERFAD (FOXRED2), suggesting a function in recruitment or delivery of substrates to the ERAD retrotranslocation machinery. TXNDC16 carries a masked, non-functional KDEL-type ER-retrieval motif and is therefore partly secreted into the extracellular space; it has been described as a meningioma-associated antigen against which patient autoantibodies arise.
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 4

## PN Consistency Summary

- **Consistency:** CONTRADICTION. The review and notes (and deep research) explicitly conclude TXNDC16/ERp90 is a **non-catalytic** PDI-family member: none of its ~five Trx-like domains carry a canonical CXXC redox motif (PMID:21359175; review PMID:32971745 corroborates non-canonical CX8C/CX9C/CX6C motifs). The review asserts no catalytic oxidoreductase MF, leaves `proposed_new_terms: []`, and frames the best-supported role as an ERFAD/FOXRED2 ERAD-substrate-recruitment partner. The PN projects GO:0003756 protein disulfide isomerase activity (verified real via OLS) onto this gene by virtue of family membership — directly at odds with the gene-level finding of redox inactivity.
- **PN story / NEW pressure:** PN asserts PDI activity NOT in GOA (GOA has only GO:0005515 + localizations). But this is an OVER-REACH: catalytic PDI activity is contradicted by the absence of a CXXC active site. No defensible catalytic NEW term; an ERAD substrate-recruitment/adapter MF is plausible but unproven (review keeps it a suggested question). Conclude: PN PDI-activity projection over-reaches for THIS gene.
- **Evidence alignment:** PN row carries no reference titles. Review evidence (PMID:21359175 HIGH/VERIFIED defining paper; PMID:25122923, 32971745, 19199708, 38673779) is far richer and all point to non-catalytic status. No shared citations to compare; no divergence beyond the PN's family-level inference lacking gene-specific support.
- **Verdict:** Inconsistent on the one substantive point — PN projects PDI catalytic activity that the review/literature refute (no CXXC). Review is correct; PN projection over-reaches.

## Full Consistency Review

- **UniProt:** Q9P2K2 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE (thorough; ER-luminal PDI-family glycoprotein, ERFAD/FOXRED2 partner)
- **PN placement:** 1 row — `ER proteostasis|Folding enzyme|Protein disulfide isomerases`. **PN-node mapping:** group→mapped GO:0003756 protein disulfide isomerase activity (ok_for_propagation_to_go, new_to_goa); class (Folding enzyme) and branch (ER proteostasis) no_mapping. Projected: GO:0003756 (new_to_goa).
- **Consistency:** CONTRADICTION. The review and notes (and deep research) explicitly conclude TXNDC16/ERp90 is a **non-catalytic** PDI-family member: none of its ~five Trx-like domains carry a canonical CXXC redox motif (PMID:21359175; review PMID:32971745 corroborates non-canonical CX8C/CX9C/CX6C motifs). The review asserts no catalytic oxidoreductase MF, leaves `proposed_new_terms: []`, and frames the best-supported role as an ERFAD/FOXRED2 ERAD-substrate-recruitment partner. The PN projects GO:0003756 protein disulfide isomerase activity (verified real via OLS) onto this gene by virtue of family membership — directly at odds with the gene-level finding of redox inactivity.
- **PN story / NEW pressure:** PN asserts PDI activity NOT in GOA (GOA has only GO:0005515 + localizations). But this is an OVER-REACH: catalytic PDI activity is contradicted by the absence of a CXXC active site. No defensible catalytic NEW term; an ERAD substrate-recruitment/adapter MF is plausible but unproven (review keeps it a suggested question). Conclude: PN PDI-activity projection over-reaches for THIS gene.
- **Mapping strategy:** The group→GO:0003756 mapping is reasonable for the *canonical catalytic* PDIs but should NOT propagate to TXNDC16, a redox-inactive family member (analogous to ERp27/ERp29 b-type pseudo-PDIs). This is a member-level exclusion, not a node-status change: the group mapping rationale already says "catalytically active family members," so TXNDC16 falls outside that scope.
- **Evidence alignment:** PN row carries no reference titles. Review evidence (PMID:21359175 HIGH/VERIFIED defining paper; PMID:25122923, 32971745, 19199708, 38673779) is far richer and all point to non-catalytic status. No shared citations to compare; no divergence beyond the PN's family-level inference lacking gene-specific support.
- **Verdict:** Inconsistent on the one substantive point — PN projects PDI catalytic activity that the review/literature refute (no CXXC). Review is correct; PN projection over-reaches.
- **Recommended edits:** [MAP] Exclude TXNDC16 (Q9P2K2) from the GO:0003756 protein disulfide isomerase activity projection (redox-inactive PDI-family member, no CXXC) — flag as member-level exception under the "Protein disulfide isomerases" group, do NOT project to GOA. [YAML] none required (review correctly omits a catalytic MF).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/TXNDC16/TXNDC16-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Folding enzyme | Protein disulfide isomerases
- UniProt: Q9P2K2
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
