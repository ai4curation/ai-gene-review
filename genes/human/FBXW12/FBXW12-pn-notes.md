# FBXW12 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q6X9E4
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXW12/FBXW12-ai-review.yaml](FBXW12-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXW12/FBXW12-ai-review.html
- Gene notes: missing - genes/human/FBXW12/FBXW12-notes.md
- GOA TSV: present - [genes/human/FBXW12/FBXW12-goa.tsv](FBXW12-goa.tsv)
- UniProt record: present - [genes/human/FBXW12/FBXW12-uniprot.txt](FBXW12-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXW12.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXW12.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXW12.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXW12.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXW12/FBXW12-deep-research-falcon.md](FBXW12-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXW12 (F-box only protein 35; FBXO12/FBXO35) is a member of the F-box/WD40 (FBXW) family, with an N-terminal F-box motif and a C-terminal beta-propeller of WD40 repeats. F-box proteins are the interchangeable substrate-recognition subunits of SCF (SKP1-CUL1-F-box)-type cullin-RING E3 ubiquitin ligase complexes: the F-box motif binds SKP1 (which bridges to CUL1 and the RBX1-bound catalytic RING), while the WD40 propeller recognizes substrates and presents them for ubiquitination and proteasomal degradation. FBXW12 is ubiquitously expressed. It binds SKP1 and assembles into an SCF complex, and in human epithelial cells it functions as a substrate receptor that ubiquitinates the interleukin-22 receptor subunit IL22RA1: ectopic FBXW12 accelerates IL22RA1 degradation in resting and IL-22-stimulated cells, and FBXW12 reconstitutes IL22RA1 ubiquitination in a defined cell-free SCF system. Through this activity FBXW12 dampens IL-22/STAT3 signaling and acts as an epithelial cell-growth suppressor, with its knockdown enhancing proliferation, cell-cycle progression and JNK/ERK activation.
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 11

## PN Consistency Summary

- **Consistency:** Fully consistent. Deep research, review YAML, PN annotation and PN-node mapping all agree FBXW12 is an SCF F-box/WD40 substrate receptor. Better characterized than FBXW10: experimentally binds SKP1/CUL1 and reconstitutes IL22RA1 ubiquitination in a cell-free SCF system. Review proposes GO:1990756, matching the PN projection. No contradictions.
- **PN story / NEW pressure:** PN asserts GO:1990756 (substrate-adaptor MF), absent from GOA (goa.tsv has only generic GO:0016567 IEA, no MF adaptor term). GO:1990756 verified real (OLS). Verdict: ADD GO:1990756 — strongly supported (direct IL22RA1 substrate, in vitro SCF reconstitution) and already proposed in the review.
- **Evidence alignment:** Aligned. PN ref 15340381 (Jin et al. F-box family review) is generic family context. The review's load-bearing PMID is 26171402 (Franz et al., IL-22R / FBXW12 growth suppressor), full-text-available, relevance HIGH / VERIFIED — stronger and more specific than the PN's cited reference. Falcon corroborates; circ-FBXW12 correctly excluded as distinct gene product.
- **Verdict:** Consistent; PN GO:1990756 add well-supported and already mirrored in the review. No changes needed.

## Full Consistency Review

- **UniProt:** Q6X9E4 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|WD40` ; **PN-node mapping:** group=mapped, ok_for_propagation_to_go, GO:1990756; subtype/type=no_mapping; projected GO:1990756 goa_status=new_to_goa.
- **Consistency:** Fully consistent. Deep research, review YAML, PN annotation and PN-node mapping all agree FBXW12 is an SCF F-box/WD40 substrate receptor. Better characterized than FBXW10: experimentally binds SKP1/CUL1 and reconstitutes IL22RA1 ubiquitination in a cell-free SCF system. Review proposes GO:1990756, matching the PN projection. No contradictions.
- **PN story / NEW pressure:** PN asserts GO:1990756 (substrate-adaptor MF), absent from GOA (goa.tsv has only generic GO:0016567 IEA, no MF adaptor term). GO:1990756 verified real (OLS). Verdict: ADD GO:1990756 — strongly supported (direct IL22RA1 substrate, in vitro SCF reconstitution) and already proposed in the review.
- **Mapping strategy:** Correct. FBXW12 is a Cul1/SCF F-box receptor; GO:1990756 is the right MF category (receptor, not scaffold/catalytic). Scope ok_for_propagation. Class-level GO:0061630 correctly held context_only/too_broad.
- **Evidence alignment:** Aligned. PN ref 15340381 (Jin et al. F-box family review) is generic family context. The review's load-bearing PMID is 26171402 (Franz et al., IL-22R / FBXW12 growth suppressor), full-text-available, relevance HIGH / VERIFIED — stronger and more specific than the PN's cited reference. Falcon corroborates; circ-FBXW12 correctly excluded as distinct gene product.
- **Verdict:** Consistent; PN GO:1990756 add well-supported and already mirrored in the review. No changes needed.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXW12/FBXW12-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | WD40
- UniProt: Q6X9E4
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR001680
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|WD40
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [type] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower substrate-receptor, adaptor, domain, or family subdivision already covered by the curated parent adaptor/receptor mapping. No additional direct GO mapping is needed at this node.
    - [group] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:1990756 ubiquitin-like ligase-substrate adaptor activity]
        rationale: This PN group captures substrate receptors/adaptors for cullin/UBL ligase systems. The shared GO molecular-function target is ubiquitin-like ligase-substrate adaptor activity.
    - [class] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases
        status=context_only scope=too_broad_to_propagate GO=[GO:0061630 ubiquitin protein ligase activity]
        rationale: This class is a genuine E3-ligase context, but its descendants include catalytic ligases, cullin scaffolds, substrate receptors, adaptors, cofactors, regulators, and UBL modifier systems. A class-level propagation would over-annotate.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:1990756 ubiquitin-like ligase-substrate adaptor activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
