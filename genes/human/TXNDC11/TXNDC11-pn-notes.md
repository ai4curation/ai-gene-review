# TXNDC11 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q6PKC3
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TXNDC11/TXNDC11-ai-review.yaml](TXNDC11-ai-review.yaml)
- AIGR review HTML: missing - genes/human/TXNDC11/TXNDC11-ai-review.html
- Gene notes: present - [genes/human/TXNDC11/TXNDC11-notes.md](TXNDC11-notes.md)
- GOA TSV: present - [genes/human/TXNDC11/TXNDC11-goa.tsv](TXNDC11-goa.tsv)
- UniProt record: present - [genes/human/TXNDC11/TXNDC11-uniprot.txt](TXNDC11-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TXNDC11.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TXNDC11.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TXNDC11.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TXNDC11.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/TXNDC11/TXNDC11-deep-research-falcon.md](TXNDC11-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: TXNDC11 (Thioredoxin domain-containing protein 11; also called EFP1) is a large (985 aa) single-pass endoplasmic reticulum membrane glycoprotein of the protein disulfide isomerase (PDI) family. It contains a single N-terminal transmembrane helix and a luminal region with five thioredoxin (Trx)-like domains followed by a C-terminal coiled coil. Only one of its Trx domains carries a canonical redox-active CXXC motif; the other Trx folds are degenerate/redox-inactive, and biochemically the catalytic center behaves as a thiol-disulfide reductase rather than an oxidase. TXNDC11 forms a stable, disulfide-linked complex with the ER mannosidase-like protein EDEM2, and this covalent partnership is required for the initial mannose-trimming step (Man9 to Man8) that commits misfolded N-glycoproteins to ER-associated degradation (glycoprotein ERAD). TXNDC11 was originally identified through its interaction with the cytoplasmic regions of the dual oxidases DUOX1 and DUOX2 and with thyroid peroxidase, suggesting a redox-regulatory role linked to the thyroid hydrogen-peroxide-generating system, though TXNDC11 alone is not sufficient to support DUOX-mediated H2O2 generation. It is widely but weakly expressed, with higher expression in thyroid and prostate.
- Existing/core annotation action counts: ACCEPT: 1; KEEP_AS_NON_CORE: 12

## PN Consistency Summary

- **Consistency:** Partial mismatch on the catalytic activity. Review, notes, and deep research converge that TXNDC11 is a **disulfide reductase**, not an isomerase/oxidase: only Trx5 carries a bona fide CXXC (CGFC, C692/C695), the other four Trx folds are degenerate, and Trx5 has reduction-potential (~−234 mV) behaving "as a reductase rather than an oxidase" (PMID:32065582; Timms 2016). The review's core MF and proposed_new_terms use GO:0015035 protein-disulfide reductase activity. The PN node projects GO:0003756 (isomerase). Verified via OLS: GO:0003756 (isomerase, S-S rearrangement) and GO:0015035 (reductase) are **siblings under different parents**, not parent/child — so GO:0003756 does not subsume the reductase function and is an over-projection for this specific member.
- **PN story / NEW pressure:** Strong NEW pressure — TXNDC11 GOA has NO molecular-function term at all (only protein binding + localizations; verified goa.tsv). A catalytic MF should be added, but as GO:0015035 protein-disulfide reductase activity (verified real), not GO:0003756. The review also proposes a BP gap: glycoprotein ERAD (GO:0036503 ERAD pathway / GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway, both verified real) via the disulfide-linked EDEM2 mannose-trimming complex. Conclusion: ADD GO:0015035 (MF) + GO:0097466/GO:0036503 (BP).
- **Evidence alignment:** PN mapping-only. Review key refs: PMID:32065582 (EDEM2-TXNDC11 reductase, gpERAD), PMID:30374462, PMID:15561711 (legacy DUOX/EFP1). The reductase-not-isomerase evidence directly undercuts the PN isomerase projection.
- **Verdict:** Inconsistent on activity class — PN GO:0003756 (isomerase) over-projects; review-supported activity is GO:0015035 reductase. MF is genuinely missing from GOA.

## Full Consistency Review

- **UniProt:** Q6PKC3 (EFP1) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis | Folding enzyme | Protein disulfide isomerases` ; **PN-node mapping:** group=mapped, scope=ok_for_propagation_to_go, GO=GO:0003756 protein disulfide isomerase activity (class/branch=no_mapping). Projection goa_status=new_to_goa.
- **Consistency:** Partial mismatch on the catalytic activity. Review, notes, and deep research converge that TXNDC11 is a **disulfide reductase**, not an isomerase/oxidase: only Trx5 carries a bona fide CXXC (CGFC, C692/C695), the other four Trx folds are degenerate, and Trx5 has reduction-potential (~−234 mV) behaving "as a reductase rather than an oxidase" (PMID:32065582; Timms 2016). The review's core MF and proposed_new_terms use GO:0015035 protein-disulfide reductase activity. The PN node projects GO:0003756 (isomerase). Verified via OLS: GO:0003756 (isomerase, S-S rearrangement) and GO:0015035 (reductase) are **siblings under different parents**, not parent/child — so GO:0003756 does not subsume the reductase function and is an over-projection for this specific member.
- **PN story / NEW pressure:** Strong NEW pressure — TXNDC11 GOA has NO molecular-function term at all (only protein binding + localizations; verified goa.tsv). A catalytic MF should be added, but as GO:0015035 protein-disulfide reductase activity (verified real), not GO:0003756. The review also proposes a BP gap: glycoprotein ERAD (GO:0036503 ERAD pathway / GO:0097466 ubiquitin-dependent glycoprotein ERAD pathway, both verified real) via the disulfide-linked EDEM2 mannose-trimming complex. Conclusion: ADD GO:0015035 (MF) + GO:0097466/GO:0036503 (BP).
- **Mapping strategy:** The "Protein disulfide isomerases" group's GO:0003756 projection over-reaches for TXNDC11 specifically (it lacks canonical PDI isomerase activity). Group-level GO:0003756 may be right for canonical members but is the wrong activity class for this non-canonical reductase. The node mapping itself need not change, but TXNDC11 should be flagged as a group member whose projected isomerase term should NOT be propagated (scope exception), or projected as reductase.
- **Evidence alignment:** PN mapping-only. Review key refs: PMID:32065582 (EDEM2-TXNDC11 reductase, gpERAD), PMID:30374462, PMID:15561711 (legacy DUOX/EFP1). The reductase-not-isomerase evidence directly undercuts the PN isomerase projection.
- **Verdict:** Inconsistent on activity class — PN GO:0003756 (isomerase) over-projects; review-supported activity is GO:0015035 reductase. MF is genuinely missing from GOA.
- **Recommended edits:** [MAP] Flag TXNDC11 in the "Protein disulfide isomerases" group as a non-canonical reductase: do not propagate GO:0003756 to it; project GO:0015035 protein-disulfide reductase activity instead. [YAML] Optionally tighten the TXNDC11 proposed_new_terms to GO:0097466 (ubiquitin-dependent glycoprotein ERAD pathway) as the precise BP, and drop the GO:0003756 alternative wording in favor of GO:0015035.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/TXNDC11/TXNDC11-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Folding enzyme | Protein disulfide isomerases
- UniProt: Q6PKC3
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
