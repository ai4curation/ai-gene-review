# ABTB1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q969K4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1328)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ABTB1/ABTB1-ai-review.yaml](ABTB1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ABTB1/ABTB1-ai-review.html](ABTB1-ai-review.html)
- Gene notes: present - [genes/human/ABTB1/ABTB1-notes.md](ABTB1-notes.md)
- GOA TSV: present - [genes/human/ABTB1/ABTB1-goa.tsv](ABTB1-goa.tsv)
- UniProt record: present - [genes/human/ABTB1/ABTB1-uniprot.txt](ABTB1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ABTB1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ABTB1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ABTB1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ABTB1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ABTB1/ABTB1-deep-research-falcon.md](ABTB1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ABTB1 is a cytoplasmic ankyrin-repeat and BTB/POZ-domain protein with multiple splice isoforms. It was originally described as BPOZ/elongation factor 1A-binding protein and as a PTEN-responsive growth-suppressive factor in cancer cell assays. Its domain architecture and interaction with CUL3 support membership in a cullin-associated ubiquitin ligase complex, most plausibly a CRL3 context, but specific physiological substrates and direct ubiquitin-ligase substrate-adaptor activity remain poorly characterized.
- Existing/core annotation action counts: ACCEPT: 4; MARK_AS_OVER_ANNOTATED: 7; MODIFY: 2

## PN Consistency Summary

- **Consistency:** Consistent in evidence, divergent in conclusion (deliberately). Deep research/notes: ABTB1 = cytoplasmic ankyrin+BTB/POZ protein, CUL3 interactor (UniProt NbExp=5), BPOZ/PTEN-responsive growth suppressor; **no validated CRL3 substrate**. The review accepts cytoplasm/cytosol, MODIFIES generic ligase-complex→GO:0031463 Cul3-RING ubiquitin ligase complex and protein binding→GO:0097602 cullin family protein binding, and **declines** the PN-projected GO:1990756 substrate-adaptor activity because no substrate-bridging assay exists. PN (substrate-receptor activity) vs review (CUL3 binding + CRL3 membership, no adaptor activity) is an evidence-based divergence, not a contradiction — the review is the more conservative, better-justified position.
- **PN story / NEW pressure:** PN asserts substrate-adaptor (receptor) activity via GO:1990756 (verified real; def. "usually mediated by F-box/BTB/POZ proteins"). Architecturally plausible but unproven for ABTB1 (no substrate). The review instead adds two verified, better-supported terms — **GO:0031463** (Cul3-RING ubiquitin ligase complex; verified real) and **GO:0097602** (cullin family protein binding; verified real) — as proposed replacements. Conclusion: PN's adaptor-activity claim **over-reaches**; the defensible additions are GO:0031463/GO:0097602, **already captured** in the review as MODIFY replacements.
- **Evidence alignment:** PN reference titles: PMID:15071497/rev and PMID:23912815/rev (Cul3/BTB substrate-receptor reviews). The review instead anchors CUL3 evidence on PMID:21145461 (CRL-network proteomics) + UniProt IntAct (CUL3 NbExp=5); the two PN review-PMIDs are not in the review reference list. Mild divergence (different supporting reviews) but same CRL3 biology.
- **Verdict:** Consistent; PN substrate-adaptor activity correctly held back (no substrate), review adds verified CRL3 complex + cullin-binding terms. **Recommended edits:** [MAP] Keep GO:1990756 non-propagating for ABTB1 pending substrate evidence (review's GO:0031463/GO:0097602 are the correct landing terms). Optional [REF]: consider adding PMID:15071497 / PMID:23912815 (PN-cited Cul3 reviews) to the review references for completeness.

## Full Consistency Review

- **UniProt:** Q969K4 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul3 substrate receptor|BTB-BACK|ankyrin` ; **PN-node mapping:** subtype/type (`BTB-BACK`,`ankyrin`)=no_mapping; group `Cul3 substrate receptor`=mapped→**GO:1990756 ubiquitin-like ligase-substrate adaptor activity** (new_to_goa); class `E3...ligases`=context_only (GO:0061630 too_broad); branch UPS=no_mapping.
- **Consistency:** Consistent in evidence, divergent in conclusion (deliberately). Deep research/notes: ABTB1 = cytoplasmic ankyrin+BTB/POZ protein, CUL3 interactor (UniProt NbExp=5), BPOZ/PTEN-responsive growth suppressor; **no validated CRL3 substrate**. The review accepts cytoplasm/cytosol, MODIFIES generic ligase-complex→GO:0031463 Cul3-RING ubiquitin ligase complex and protein binding→GO:0097602 cullin family protein binding, and **declines** the PN-projected GO:1990756 substrate-adaptor activity because no substrate-bridging assay exists. PN (substrate-receptor activity) vs review (CUL3 binding + CRL3 membership, no adaptor activity) is an evidence-based divergence, not a contradiction — the review is the more conservative, better-justified position.
- **PN story / NEW pressure:** PN asserts substrate-adaptor (receptor) activity via GO:1990756 (verified real; def. "usually mediated by F-box/BTB/POZ proteins"). Architecturally plausible but unproven for ABTB1 (no substrate). The review instead adds two verified, better-supported terms — **GO:0031463** (Cul3-RING ubiquitin ligase complex; verified real) and **GO:0097602** (cullin family protein binding; verified real) — as proposed replacements. Conclusion: PN's adaptor-activity claim **over-reaches**; the defensible additions are GO:0031463/GO:0097602, **already captured** in the review as MODIFY replacements.
- **Mapping strategy:** Group node `Cul3 substrate receptor`→GO:1990756 should be treated as non-propagating for ABTB1 until a substrate-bridging assay exists; the review's CRL3-complex membership (GO:0031463) is the appropriate landing point instead. Class-node GO:0061630 correctly context_only. The PN MF projection is broader/stronger than evidence supports — analogous to the rejected-projection precedent.
- **Evidence alignment:** PN reference titles: PMID:15071497/rev and PMID:23912815/rev (Cul3/BTB substrate-receptor reviews). The review instead anchors CUL3 evidence on PMID:21145461 (CRL-network proteomics) + UniProt IntAct (CUL3 NbExp=5); the two PN review-PMIDs are not in the review reference list. Mild divergence (different supporting reviews) but same CRL3 biology.
- **Verdict:** Consistent; PN substrate-adaptor activity correctly held back (no substrate), review adds verified CRL3 complex + cullin-binding terms. **Recommended edits:** [MAP] Keep GO:1990756 non-propagating for ABTB1 pending substrate evidence (review's GO:0031463/GO:0097602 are the correct landing terms). Optional [REF]: consider adding PMID:15071497 / PMID:23912815 (PN-cited Cul3 reviews) to the review references for completeness.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ABTB1/ABTB1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul3 substrate receptor | BTB-BACK | ankyrin
- UniProt: Q969K4
- In branches: UPS
- Signature domains: IPR000210, cd18497
- Auxiliary domains: IPR002110
- PN references (titles):
    - 15071497 / rev
    - 23912815 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor|BTB-BACK|ankyrin
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor|BTB-BACK
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul3 substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
