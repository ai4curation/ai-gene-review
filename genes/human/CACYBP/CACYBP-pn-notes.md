# CACYBP PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9HB71
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CACYBP/CACYBP-ai-review.yaml](CACYBP-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CACYBP/CACYBP-ai-review.html](CACYBP-ai-review.html)
- Gene notes: present - [genes/human/CACYBP/CACYBP-notes.md](CACYBP-notes.md)
- GOA TSV: present - [genes/human/CACYBP/CACYBP-goa.tsv](CACYBP-goa.tsv)
- UniProt record: present - [genes/human/CACYBP/CACYBP-uniprot.txt](CACYBP-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CACYBP.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CACYBP.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CACYBP.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CACYBP.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/CACYBP/CACYBP-deep-research-falcon.md](CACYBP-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: CACYBP (Calcyclin-Binding Protein; also known as SIP, Siah-Interacting Protein, and S100A6-binding protein) is a small nucleocytoplasmic adaptor protein that acts as a molecular bridge in a Siah1/Siah2-based, SKP1-containing E3 ubiquitin ligase complex. Through an N-terminal dimerization domain that binds Siah1 and a C-terminal domain that binds SKP1, it scaffolds substrate and the E2 enzyme into apposition, enabling ubiquitination and proteasomal degradation of target proteins, most notably beta-catenin (CTNNB1) in a p53-responsive pathway. CACYBP binds proteins of the S100 family (calcyclin/S100A6, S100A1, S100B, S100P, S100A12) in a calcium-dependent manner, linking calcium signaling to this ubiquitination machinery, and it forms homodimers. It is found in the cytoplasm at low calcium and redistributes between cytoplasm and nucleus upon calcium increase and certain stimuli.
- Existing/core annotation action counts: ACCEPT: 11; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 18

## PN Consistency Summary

- **Consistency:** Major divergence. PN classifies CACYBP as an **HSP90 cochaperone** (CS/p23-like domain) and projects GO:0051879 Hsp90 protein binding. The review, the notes, and the Falcon deep research instead establish CACYBP/SIP as a **Ca2+-regulated adaptor in a Siah1-based (non-cullin) E3 ubiquitin ligase** that degrades beta-catenin, and as an **S100A6/calcyclin-binding** protein (PMID:16085652, 18803400, 22295074). The review has NO Hsp90-binding annotation and does not mention HSP90 cochaperone function. The CS/p23-like (HSP20-like, IPR007052/IPR037893) domain is the only basis for the HSP90-cochaperone call; CS-domain presence does not establish Hsp90 binding for this protein.
- **PN story / NEW pressure:** PN asserts an Hsp90-cochaperone role NOT in existing GO annotations and NOT supported by the review/literature. GO:0051879 is a real term (verified) but is unsupported for CACYBP — the deep research found no primary Hsp90-binding data (the only Hsp90 link is review-level mention of radicicol-induced abundance changes, not binding). Conclusion: over-reaches — projecting Hsp90 binding onto CACYBP is a domain-similarity over-transfer. The protein's real shared MF is molecular adaptor activity (GO:0060090, already ACCEPT) and S100/ubiquitin-ligase binding.
- **Evidence alignment:** PN cites no references. Review/deep-research PMIDs (16085652 Siah1 assembly; 18803400 S100A6 structure; 22295074 gastric-cancer beta-catenin) are entirely about E3-adaptor/S100 biology — zero overlap with any Hsp90-cochaperone literature.
- **Verdict:** Domain-based misclassification — CACYBP is a Siah1 E3-ligase adaptor / S100A6-binding protein, not a demonstrated HSP90 cochaperone; Hsp90-binding projection is unsupported. **Recommended edits:** [MAP] remove/flag GO:0051879 projection onto Q9HB71 and reconsider the HSP90-cochaperone placement; the gene's shared MF is better represented by molecular adaptor activity (GO:0060090) / ubiquitin protein ligase binding, already in the review.

## Full Consistency Review

- **UniProt:** Q9HB71 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE
- **PN placement:** `Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone|CS domain containing` ; **PN-node mapping:** cochaperone type → mapped/ok_for_propagation GO:0051879 Hsp90 protein binding (goa_status=more_specific_than_existing_goa); subtype/group/class/branch → no_mapping.
- **Consistency:** Major divergence. PN classifies CACYBP as an **HSP90 cochaperone** (CS/p23-like domain) and projects GO:0051879 Hsp90 protein binding. The review, the notes, and the Falcon deep research instead establish CACYBP/SIP as a **Ca2+-regulated adaptor in a Siah1-based (non-cullin) E3 ubiquitin ligase** that degrades beta-catenin, and as an **S100A6/calcyclin-binding** protein (PMID:16085652, 18803400, 22295074). The review has NO Hsp90-binding annotation and does not mention HSP90 cochaperone function. The CS/p23-like (HSP20-like, IPR007052/IPR037893) domain is the only basis for the HSP90-cochaperone call; CS-domain presence does not establish Hsp90 binding for this protein.
- **PN story / NEW pressure:** PN asserts an Hsp90-cochaperone role NOT in existing GO annotations and NOT supported by the review/literature. GO:0051879 is a real term (verified) but is unsupported for CACYBP — the deep research found no primary Hsp90-binding data (the only Hsp90 link is review-level mention of radicicol-induced abundance changes, not binding). Conclusion: over-reaches — projecting Hsp90 binding onto CACYBP is a domain-similarity over-transfer. The protein's real shared MF is molecular adaptor activity (GO:0060090, already ACCEPT) and S100/ubiquitin-ligase binding.
- **Mapping strategy:** This gene argues the HSP90-cochaperone node should not project GO:0051879 onto CACYBP. CS-domain membership alone is too broad to assert Hsp90 binding (CS domains occur in non-Hsp90 contexts, as here). Treat as a node where this member is mis-bucketed.
- **Evidence alignment:** PN cites no references. Review/deep-research PMIDs (16085652 Siah1 assembly; 18803400 S100A6 structure; 22295074 gastric-cancer beta-catenin) are entirely about E3-adaptor/S100 biology — zero overlap with any Hsp90-cochaperone literature.
- **Verdict:** Domain-based misclassification — CACYBP is a Siah1 E3-ligase adaptor / S100A6-binding protein, not a demonstrated HSP90 cochaperone; Hsp90-binding projection is unsupported. **Recommended edits:** [MAP] remove/flag GO:0051879 projection onto Q9HB71 and reconsider the HSP90-cochaperone placement; the gene's shared MF is better represented by molecular adaptor activity (GO:0060090) / ubiquitin protein ligase binding, already in the review.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/CACYBP/CACYBP-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Cytonuclear proteostasis | Chaperone | HSP90 system | HSP90 cochaperone | CS domain containing
- UniProt: Q9HB71
- In branches: CY
- PN-node mapping records (path + ancestors):
    - [subtype] Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone|CS domain containing
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a family/domain/subtype label. It classifies PN members but is not itself a GO annotation target; any functional assertion should come from a parent role mapping or gene-specific review.
    - [type] Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0051879 Hsp90 protein binding]
        rationale: This PN type groups HSP90 cochaperones. Hsp90 protein binding is the most defensible shared GO molecular-function target for propagation.
    - [group] Cytonuclear proteostasis|Chaperone|HSP90 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [class] Cytonuclear proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a specific GO class. The member genes span multiple activities, complexes, or contexts, so propagation from this node would overstate the shared biology; use narrower child or gene-level curations.
    - [branch] Cytonuclear proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0051879 Hsp90 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Cytonuclear proteostasis|Chaperone|HSP90 system|HSP90 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
