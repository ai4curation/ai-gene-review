# HSPB9 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BQS6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/HSPB9/HSPB9-ai-review.yaml](HSPB9-ai-review.yaml)
- AIGR review HTML: present - [genes/human/HSPB9/HSPB9-ai-review.html](HSPB9-ai-review.html)
- Gene notes: present - [genes/human/HSPB9/HSPB9-notes.md](HSPB9-notes.md)
- GOA TSV: present - [genes/human/HSPB9/HSPB9-goa.tsv](HSPB9-goa.tsv)
- UniProt record: present - [genes/human/HSPB9/HSPB9-uniprot.txt](HSPB9-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/HSPB9.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/HSPB9.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HSPB9.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HSPB9.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: HSPB9 (heat shock protein beta-9, also called cancer/testis antigen 51, CT51) is a poorly characterized member of the small heat shock protein (sHSP / HSP20, alpha-crystallin domain) family. It contains the conserved alpha-crystallin domain but is one of the most divergent and rapidly evolving small HSPs (mouse and human orthologs differ by ~38%). Its expression is essentially restricted to the testis, specifically in spermatogenic cells from the late pachytene spermatocyte to elongate spermatid stages, and it is also detected in tumors, classifying it as a cancer/testis antigen. HSPB9 interacts with the dynein light chain TCTEL1 (DYNLT1), a component of cytoplasmic and flagellar dynein with which it is co-expressed in testis, suggesting a role linked to dynein-based transport during spermatogenesis. Like other small HSPs it localizes to the cytoplasm and nucleus and translocates to nuclear foci during heat shock, though direct chaperone (holdase) activity has not been experimentally demonstrated for HSPB9.
- Existing/core annotation action counts: ACCEPT: 7; KEEP_AS_NON_CORE: 1; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Notes ↔ review consistent — HSPB9/CT51 is a poorly characterized, rapidly evolving, testis-restricted sHSP; its only experimental molecular interaction is with the dynein light chain TCTEL1/DYNLT1 (PMID:15503857, "potentially interacts"), and direct chaperone/holdase activity has NEVER been demonstrated for this paralog (PMID:11470154). The review explicitly declines to assert a confident holdase MF, making GO:0045503 dynein light chain binding the core MF and flagging chaperone activity as inferred-only.
- **PN story / NEW pressure:** GOA has no chaperone MF (only GO:0005515 protein binding). PN projects GO:0044183 protein folding chaperone (verified real, foldase per OLS) purely by family membership. This double-over-reaches: (1) foldase vs holdase term mismatch shared with the other sHSPs, AND (2) HSPB9 has no demonstrated chaperone activity of any kind, so even a holdase term (GO:0140309 / GO:0051082) would be inference-only, not evidence-backed. The review's defensible MF is GO:0045503 dynein light chain binding (verified real, from PMID:15503857).
- **Evidence alignment:** PN row has no reference titles; review PMIDs (11470154 identity/testis; 15503857 DYNLT1 interaction/CT antigen; 19464326 localization) — no overlap to diverge, but none supports folding-chaperone activity, undercutting the PN projection.
- **Verdict:** sHSP placement defensible by homology but the GO:0044183 foldase projection over-reaches (wrong activity class + no demonstrated chaperone activity). **Recommended edits:** [MAP] do not project GO:0044183 (foldase) onto Q9BQS6; if the sHSP node propagates an MF use GO:0140309 / GO:0051082 as inference, and note HSPB9's only experimental MF is GO:0045503 dynein light chain binding.

## Full Consistency Review

- **UniProt:** Q9BQS6 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** one row — `Cytonuclear proteostasis|Chaperone|small HSP system|small HSP` (type) ; **PN-node mapping:** sHSP type → mapped/ok_for_propagation_to_go GO:0044183 protein folding chaperone (new_to_goa); group/class/branch no_mapping.
- **Consistency:** Notes ↔ review consistent — HSPB9/CT51 is a poorly characterized, rapidly evolving, testis-restricted sHSP; its only experimental molecular interaction is with the dynein light chain TCTEL1/DYNLT1 (PMID:15503857, "potentially interacts"), and direct chaperone/holdase activity has NEVER been demonstrated for this paralog (PMID:11470154). The review explicitly declines to assert a confident holdase MF, making GO:0045503 dynein light chain binding the core MF and flagging chaperone activity as inferred-only.
- **PN story / NEW pressure:** GOA has no chaperone MF (only GO:0005515 protein binding). PN projects GO:0044183 protein folding chaperone (verified real, foldase per OLS) purely by family membership. This double-over-reaches: (1) foldase vs holdase term mismatch shared with the other sHSPs, AND (2) HSPB9 has no demonstrated chaperone activity of any kind, so even a holdase term (GO:0140309 / GO:0051082) would be inference-only, not evidence-backed. The review's defensible MF is GO:0045503 dynein light chain binding (verified real, from PMID:15503857).
- **Mapping strategy:** HSPB9 is the weakest member for the sHSP-family GO:0044183 mapping — both the wrong activity class (foldase) and unproven for this paralog. If the family node propagates any MF, it should be a holdase term carried as inference (IBA-grade), not a foldase; better to treat HSPB9 as an under-characterized exception.
- **Evidence alignment:** PN row has no reference titles; review PMIDs (11470154 identity/testis; 15503857 DYNLT1 interaction/CT antigen; 19464326 localization) — no overlap to diverge, but none supports folding-chaperone activity, undercutting the PN projection.
- **Verdict:** sHSP placement defensible by homology but the GO:0044183 foldase projection over-reaches (wrong activity class + no demonstrated chaperone activity). **Recommended edits:** [MAP] do not project GO:0044183 (foldase) onto Q9BQS6; if the sHSP node propagates an MF use GO:0140309 / GO:0051082 as inference, and note HSPB9's only experimental MF is GO:0045503 dynein light chain binding.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/HSPB9/HSPB9-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | small HSP system | small HSP
- UniProt: Q9BQS6
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [type] Cytonuclear proteostasis|Chaperone|small HSP system|small HSP
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0044183 protein folding chaperone]
        rationale: This PN type denotes small heat-shock chaperones. Protein folding chaperone is the appropriate shared molecular-function term.
    - [group] Cytonuclear proteostasis|Chaperone|small HSP system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket that is already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0044183 protein folding chaperone | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Cytonuclear proteostasis|Chaperone|small HSP system|small HSP

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
