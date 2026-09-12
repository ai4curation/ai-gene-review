# AHR PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P35869
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1353)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/AHR/AHR-ai-review.yaml](AHR-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AHR/AHR-ai-review.html](AHR-ai-review.html)
- Gene notes: present - [genes/human/AHR/AHR-notes.md](AHR-notes.md)
- GOA TSV: present - [genes/human/AHR/AHR-goa.tsv](AHR-goa.tsv)
- UniProt record: present - [genes/human/AHR/AHR-uniprot.txt](AHR-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AHR.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AHR.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AHR.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AHR.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AHR/AHR-deep-research-falcon.md](AHR-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AHR encodes the aryl hydrocarbon receptor, a ligand-activated bHLH-PAS transcription factor that senses xenobiotic, dietary, microbiome-derived, and endogenous metabolites. In unstimulated cells AHR is mainly cytoplasmic in a chaperone-associated receptor complex; ligand binding promotes nuclear accumulation, heterodimerization with ARNT, binding to AHR/xenobiotic response elements, and regulation of RNA polymerase II target genes. AHR controls detoxification and xenobiotic-response programs such as CYP1A1 induction and also has context-dependent roles in immune regulation, intestinal epithelial responses, tumor immune escape, circadian cross-talk, development, and retinal biology.
- Existing/core annotation action counts: ACCEPT: 73; KEEP_AS_NON_CORE: 10; MARK_AS_OVER_ANNOTATED: 4; MODIFY: 15

## PN Consistency Summary

- **Consistency:** Large but well-managed divergence. PN frames AHR as a CUL4 substrate adaptor in the UPS branch. Deep research (falcon) and review establish AHR's canonical identity as a ligand-activated bHLH-PAS nuclear receptor / RNA Pol II transcription factor (HSP90/XAP2/p23 cytosolic complex → ARNT heterodimer → XRE binding). The review/notes explicitly did NOT accept the PN GO:1990756 projection: AHR's own subtype/type are `no_mapping`, and the parent group is flagged `manual_gene_level_review_required_before_gene_review_change`. Notes acknowledge CUL4B^AHR E3 activity from the literature (Xie 2024 review; ER-α/AR/β-catenin targets) but retain it as an open question, not an annotation. Internally consistent; PN UPS role deliberately not propagated.
- **PN story / NEW pressure:** PN asserts an MF (GO:1990756, verified real/non-obsolete) absent from GOA. AHR-as-CUL4-adaptor is supported only by a subset of (largely review/secondary) literature and is mechanistically contested vs. AHR being itself a CUL4 substrate. Verdict: **over-reaches** as a gene-level GO assertion now — correctly deferred (suggested_question + suggested_experiment to test direct substrate-bridging vs AHR turnover). The genuine AHR core functions (nuclear receptor activity, heterodimerization, sequence-specific DNA binding, Hsp90 binding) are already richly annotated.
- **Evidence alignment:** No overlap between PN refs (PMID:17392787, 28416634 — uncached, not used) and the review's evidence base (PMID:34521881, 28602820, 7961644, 11259606, 15641800, 32818467, etc.). The review builds the canonical TF case independently; the PN UPS citations are neither verified nor relied upon. Divergent reference sets, reconciled by treating the UPS role as unverified.
- **Verdict:** PN UPS/CUL4-adaptor projection (GO:1990756) over-reaches; correctly NOT propagated to AHR (left as open question). Core TF/nuclear-receptor function fully captured. **Recommended edits:** none to YAML. [MAP]: keep AHR/ARNT/TBL3 and PAS subtypes `no_mapping`; gate the Cul4A/Cul4B substrate-adaptor group GO:1990756 behind per-gene review (AHR is the cautionary case). [REF]: optionally fetch/verify PN PMID:17392787 & 28416634 to substantiate or retire the AHR UPS placement.

## Full Consistency Review

- **UniProt:** P35869 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor|AHR / ARNT / TBL3 complex|PAS` ; **PN-node mapping:** subtype(PAS)/type(AHR/ARNT/TBL3) `no_mapping`; group (Cul4A/Cul4B substrate adaptor) `mapped` GO:1990756 ubiquitin-like ligase-substrate adaptor activity (new_to_goa); class (E3 ligases) `context_only` too_broad GO:0061630; branch `no_mapping`. PN references: PMID:17392787, 28416634 (titles not in dossier; not cached locally).
- **Consistency:** Large but well-managed divergence. PN frames AHR as a CUL4 substrate adaptor in the UPS branch. Deep research (falcon) and review establish AHR's canonical identity as a ligand-activated bHLH-PAS nuclear receptor / RNA Pol II transcription factor (HSP90/XAP2/p23 cytosolic complex → ARNT heterodimer → XRE binding). The review/notes explicitly did NOT accept the PN GO:1990756 projection: AHR's own subtype/type are `no_mapping`, and the parent group is flagged `manual_gene_level_review_required_before_gene_review_change`. Notes acknowledge CUL4B^AHR E3 activity from the literature (Xie 2024 review; ER-α/AR/β-catenin targets) but retain it as an open question, not an annotation. Internally consistent; PN UPS role deliberately not propagated.
- **PN story / NEW pressure:** PN asserts an MF (GO:1990756, verified real/non-obsolete) absent from GOA. AHR-as-CUL4-adaptor is supported only by a subset of (largely review/secondary) literature and is mechanistically contested vs. AHR being itself a CUL4 substrate. Verdict: **over-reaches** as a gene-level GO assertion now — correctly deferred (suggested_question + suggested_experiment to test direct substrate-bridging vs AHR turnover). The genuine AHR core functions (nuclear receptor activity, heterodimerization, sequence-specific DNA binding, Hsp90 binding) are already richly annotated.
- **Mapping strategy:** Gene does not change the node. The Cul4A/Cul4B substrate-adaptor group→GO:1990756 mapping is too liberal for AHR; AHR's leaf nodes are appropriately `no_mapping`, and the review upholds that. This is a stronger "do not propagate" case than broader-term rejections (TOMM20/HSPA8/RAB7A) because the asserted MF is a different biological role from AHR's primary function.
- **Evidence alignment:** No overlap between PN refs (PMID:17392787, 28416634 — uncached, not used) and the review's evidence base (PMID:34521881, 28602820, 7961644, 11259606, 15641800, 32818467, etc.). The review builds the canonical TF case independently; the PN UPS citations are neither verified nor relied upon. Divergent reference sets, reconciled by treating the UPS role as unverified.
- **Verdict:** PN UPS/CUL4-adaptor projection (GO:1990756) over-reaches; correctly NOT propagated to AHR (left as open question). Core TF/nuclear-receptor function fully captured. **Recommended edits:** none to YAML. [MAP]: keep AHR/ARNT/TBL3 and PAS subtypes `no_mapping`; gate the Cul4A/Cul4B substrate-adaptor group GO:1990756 behind per-gene review (AHR is the cautionary case). [REF]: optionally fetch/verify PN PMID:17392787 & 28416634 to substantiate or retire the AHR UPS placement.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AHR/AHR-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul4A/Cul4B substrate adaptor | AHR / ARNT / TBL3 complex | PAS
- UniProt: P35869
- In branches: UPS
- Signature domains: (none)
- Auxiliary domains: IPR000014
- PN references (titles):
    - 17392787
    - 28416634
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor|AHR / ARNT / TBL3 complex|PAS
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor|AHR / ARNT / TBL3 complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul4A/Cul4B substrate adaptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
