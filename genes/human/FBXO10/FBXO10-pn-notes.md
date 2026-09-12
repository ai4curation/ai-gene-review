# FBXO10 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9UK96
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXO10/FBXO10-ai-review.yaml](FBXO10-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXO10/FBXO10-ai-review.html
- Gene notes: missing - genes/human/FBXO10/FBXO10-notes.md
- GOA TSV: present - [genes/human/FBXO10/FBXO10-goa.tsv](FBXO10-goa.tsv)
- UniProt record: present - [genes/human/FBXO10/FBXO10-uniprot.txt](FBXO10-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO10.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXO10.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO10.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXO10.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXO10/FBXO10-deep-research-falcon.md](FBXO10-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXO10 (F-box only protein 10) is a large (956 aa) F-box protein that serves as the substrate-recognition subunit of an SCF (SKP1-CUL1-F-box)-type E3 ubiquitin ligase complex. Through an N-terminal F-box motif it binds SKP1, docking onto the CUL1-RBX1 catalytic core (the SCF(FBXO10) complex consists of CUL1, SKP1 and FBXO10), while its extensive C-terminal beta-helix/PbH1 repeat region provides the substrate-binding surface. As the adaptor it does not itself catalyze ubiquitin transfer; rather it selects substrates that the CUL1-RBX1-E2 machinery polyubiquitinates for degradation. Its best-characterized substrate is the antiapoptotic protein BCL2: FBXO10 binds BCL2 and promotes its ubiquitination and degradation, thereby promoting apoptosis, a role conserved with the C. elegans F-box protein DRE-1, which inactivates the BCL2 ortholog CED-9. Loss-of-function mutations or reduced FBXO10 expression occur in diffuse large B-cell lymphoma, where they permit BCL2 accumulation. FBXO10 also targets the germinal-center protein HGAL/GCSAM for ubiquitination and degradation; upon B-cell receptor stimulation FBXO10 is palmitoylated and relocates to the plasma membrane, where HGAL degradation forms a negative-feedback loop that dampens BCR signaling. An additional reported substrate is the receptor for advanced glycation end products (RAGE/ AGER), which FBXO10 targets for ubiquitination and lysosomal degradation (recognized via cytoplasmic residues K374 and the phosphorylation-sensitive S391). A distinct, lipidation-controlled pool of FBXO10 is geranylgeranylated at a C-terminal CaaX motif (Cys953) and delivered to the outer mitochondrial membrane via a PDE6delta/HSP90/TOM70 route, where it assembles a mitochondrial SCF(FBXO10) that polyubiquitinates and degrades the mitochondrial phosphatase PGAM5 to control outer-mitochondrial-membrane proteostasis, mitochondrial morphology/bioenergetics, and myogenic differentiation. In colorectal cancer, an upstream CYP1B1/20-HETE/PKC axis induces FBXO10, which polyubiquitinates ACSL4 to suppress ferroptosis. FBXO10 is widely expressed and predominantly cytoplasmic, with regulated pools at the plasma membrane and outer mitochondrial membrane. Notably, engineered Fbxo10 loss-of-function mice show no increase in BCL2 or B-cell accumulation, suggesting species-dependent regulation or functional redundancy with other ligases.
- Existing/core annotation action counts: ACCEPT: 9; KEEP_AS_NON_CORE: 16; MODIFY: 2

## PN Consistency Summary

- **Consistency:** Consistent and well-aligned. Review explicitly executes the canonical F-box pattern: two NAS GO:0004842 ubiquitin-protein transferase annotations MODIFY → GO:1990756 (verified real), exactly matching the PN projection. DR ↔ YAML agree on BCL2/HGAL/PGAM5/RAGE substrates and SCF(FBXO10) membership.
- **PN story / NEW pressure:** PN asserts the adaptor MF; review supplies it via MODIFY of the wrong catalytic-transferase terms — already captured/improved, not over-reach. Beyond the PN family story, the review carries substantial extra biology (apoptosis via BCL2 IMP PMID:23431138; mitochondrial OMM PGAM5 degradation; species caveat from Fbxo10 KO mice) that PN does not assert. No additional NEW GO pressure beyond GO:1990756. Validated substrates present (not a substrate-less F-box).
- **Evidence alignment:** PN cites only 15340381. Review uses PMID:23431138 (BCL2), 31570756 (HGAL), 34445249 (SCF), 10531035/10531037 (family cloning, source of the transferase NAS terms), plus Falcon PGAM5/RAGE leads. Expansion, no conflict.
- **Verdict:** Consistent; review already implements the PN adaptor-MF mapping via MODIFY GO:0004842→GO:1990756.

## Full Consistency Review

- **UniProt:** Q9UK96 · **batch:** proteostasis-batch-2026-06-13 (Falcon DR) · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|CASH` (aux domain IPR006633) ; **PN-node mapping:** subtype/type `no_mapping`; group `Cul1 substrate receptor`=`mapped` / `ok_for_propagation_to_go` → GO:1990756 (new_to_goa); class `context_only`/`too_broad` (GO:0061630).
- **Consistency:** Consistent and well-aligned. Review explicitly executes the canonical F-box pattern: two NAS GO:0004842 ubiquitin-protein transferase annotations MODIFY → GO:1990756 (verified real), exactly matching the PN projection. DR ↔ YAML agree on BCL2/HGAL/PGAM5/RAGE substrates and SCF(FBXO10) membership.
- **PN story / NEW pressure:** PN asserts the adaptor MF; review supplies it via MODIFY of the wrong catalytic-transferase terms — already captured/improved, not over-reach. Beyond the PN family story, the review carries substantial extra biology (apoptosis via BCL2 IMP PMID:23431138; mitochondrial OMM PGAM5 degradation; species caveat from Fbxo10 KO mice) that PN does not assert. No additional NEW GO pressure beyond GO:1990756. Validated substrates present (not a substrate-less F-box).
- **Mapping strategy:** Gene does not change the node; status/scope correct. PN-projected GO:1990756 is at correct altitude (matches the review's MODIFY replacement target). Class GO:0061630 correctly too_broad.
- **Evidence alignment:** PN cites only 15340381. Review uses PMID:23431138 (BCL2), 31570756 (HGAL), 34445249 (SCF), 10531035/10531037 (family cloning, source of the transferase NAS terms), plus Falcon PGAM5/RAGE leads. Expansion, no conflict.
- **Verdict:** Consistent; review already implements the PN adaptor-MF mapping via MODIFY GO:0004842→GO:1990756.
- **Recommended edits:** none to FBXO10-ai-review.yaml. [MAP] none — node mapping and review concur.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXO10/FBXO10-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | CASH
- UniProt: Q9UK96
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR006633
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|CASH
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
