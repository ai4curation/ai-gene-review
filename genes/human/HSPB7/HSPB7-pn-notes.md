# HSPB7 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UBY9
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07b
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/HSPB7/HSPB7-ai-review.yaml](HSPB7-ai-review.yaml)
- AIGR review HTML: present - [genes/human/HSPB7/HSPB7-ai-review.html](HSPB7-ai-review.html)
- Gene notes: present - [genes/human/HSPB7/HSPB7-notes.md](HSPB7-notes.md)
- GOA TSV: present - [genes/human/HSPB7/HSPB7-goa.tsv](HSPB7-goa.tsv)
- UniProt record: present - [genes/human/HSPB7/HSPB7-uniprot.txt](HSPB7-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/HSPB7.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/HSPB7.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HSPB7.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/HSPB7.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: HSPB7 (heat shock protein beta-7), also known as cardiovascular heat shock protein (cvHsp), is a member of the small heat shock protein (sHSP / HSP20, alpha-crystallin domain) family. It is selectively and highly expressed in cardiovascular and insulin-sensitive tissues, predominantly heart and skeletal muscle. HSPB7 binds the actin-crosslinking protein filamin (alpha-filamin / actin-binding protein 280) through its core alpha-crystallin domain and forms hetero-oligomeric complexes with other small heat shock proteins including HSPB8 (HSP22), HSPB2 (MKBP) and HSPB1 (HSP27). Unlike the canonical small HSPs HSPB1 and HSPB5, HSPB7 does not promote refolding of denatured substrates; instead it acts as a non-canonical chaperone/sequestrase that binds and sequesters aggregation-prone proteins (e.g. polyglutamine-expanded and filamin clients), suppressing their aggregation. HSPB7 localizes to the cytoplasm and nucleus and constitutively resides in SC35 nuclear splicing speckles via its N-terminal region. It is implicated in cardiac biology and cardiomyopathy risk.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 6; MODIFY: 3

## PN Consistency Summary

- **Consistency:** Notes ↔ review converge tightly — HSPB7/cvHsp is a NON-canonical sHSP that does NOT refold denatured substrate (PMID:19464326 "HSPB7 did not support refolding"); it sequesters aggregation-prone clients (polyQ, filamin) and binds alpha-filamin (PMID:10593960). Cardiac-enriched, SC35-speckle resident. This directly contradicts the PN GO:0044183 (foldase) projection.
- **PN story / NEW pressure:** GOA has no folding-chaperone MF for HSPB7 (has GO:0031005 filamin binding, GO:0006986 BP). PN projects GO:0044183 protein folding chaperone (verified real, but a FOLDASE per OLS — "binds an unfolded protein to fold it"). HSPB7 is explicitly a non-foldase sequestrase, so GO:0044183 is the most over-reaching projection of the six sHSPs here. The review's genuine MFs are GO:0031005 filamin binding (ACCEPT) and GO:0051082 unfolded protein binding (holdase/sequestrase, core). The defensible MF gap, if any, is GO:0140309 unfolded protein holdase activity / GO:0051082, NOT GO:0044183.
- **Evidence alignment:** PN row carries no reference titles; review PMIDs (19464326, 10593960, 14594798, plus interactome set) cover the non-refolding phenotype, filamin binding, and sHSP hetero-oligomers — no overlap to diverge, but the key review finding (no refolding) refutes the PN projection.
- **Verdict:** sHSP membership correct but the GO:0044183 foldase projection is contradicted by direct evidence; over-reaches. **Recommended edits:** [MAP] do not project GO:0044183 protein folding chaperone onto Q9UBY9 (HSPB7 demonstrably does not refold; PMID:19464326); if a shared sHSP MF is desired use GO:0140309 unfolded protein holdase activity / GO:0051082 unfolded protein binding, and mark HSPB7 a non-canonical exception.

## Full Consistency Review

- **UniProt:** Q9UBY9 · **batch:** proteostasis-batch-2026-06-07b · **review status:** COMPLETE
- **PN placement:** one row — `Cytonuclear proteostasis|Chaperone|small HSP system|small HSP` (type) ; **PN-node mapping:** sHSP type → mapped/ok_for_propagation_to_go GO:0044183 protein folding chaperone (new_to_goa); group/class/branch no_mapping.
- **Consistency:** Notes ↔ review converge tightly — HSPB7/cvHsp is a NON-canonical sHSP that does NOT refold denatured substrate (PMID:19464326 "HSPB7 did not support refolding"); it sequesters aggregation-prone clients (polyQ, filamin) and binds alpha-filamin (PMID:10593960). Cardiac-enriched, SC35-speckle resident. This directly contradicts the PN GO:0044183 (foldase) projection.
- **PN story / NEW pressure:** GOA has no folding-chaperone MF for HSPB7 (has GO:0031005 filamin binding, GO:0006986 BP). PN projects GO:0044183 protein folding chaperone (verified real, but a FOLDASE per OLS — "binds an unfolded protein to fold it"). HSPB7 is explicitly a non-foldase sequestrase, so GO:0044183 is the most over-reaching projection of the six sHSPs here. The review's genuine MFs are GO:0031005 filamin binding (ACCEPT) and GO:0051082 unfolded protein binding (holdase/sequestrase, core). The defensible MF gap, if any, is GO:0140309 unfolded protein holdase activity / GO:0051082, NOT GO:0044183.
- **Mapping strategy:** This gene is the exemplar where the sHSP-family GO:0044183 mapping is wrong: HSPB7 is a poor classical holdase and an outright non-foldase. GO:0044183 is broader-and-wrong (foldase activity HSPB7 lacks). Either re-scope the sHSP "small HSP" type away from a foldase term, or flag HSPB7 as an exception on Q9UBY9.
- **Evidence alignment:** PN row carries no reference titles; review PMIDs (19464326, 10593960, 14594798, plus interactome set) cover the non-refolding phenotype, filamin binding, and sHSP hetero-oligomers — no overlap to diverge, but the key review finding (no refolding) refutes the PN projection.
- **Verdict:** sHSP membership correct but the GO:0044183 foldase projection is contradicted by direct evidence; over-reaches. **Recommended edits:** [MAP] do not project GO:0044183 protein folding chaperone onto Q9UBY9 (HSPB7 demonstrably does not refold; PMID:19464326); if a shared sHSP MF is desired use GO:0140309 unfolded protein holdase activity / GO:0051082 unfolded protein binding, and mark HSPB7 a non-canonical exception.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07b
- review_yaml: genes/human/HSPB7/HSPB7-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | small HSP system | small HSP
- UniProt: Q9UBY9
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
