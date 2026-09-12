# FBXL15 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H469
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-13
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/FBXL15/FBXL15-ai-review.yaml](FBXL15-ai-review.yaml)
- AIGR review HTML: missing - genes/human/FBXL15/FBXL15-ai-review.html
- Gene notes: missing - genes/human/FBXL15/FBXL15-notes.md
- GOA TSV: present - [genes/human/FBXL15/FBXL15-goa.tsv](FBXL15-goa.tsv)
- UniProt record: present - [genes/human/FBXL15/FBXL15-uniprot.txt](FBXL15-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL15.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/FBXL15.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL15.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/FBXL15.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/FBXL15/FBXL15-deep-research-falcon.md](FBXL15-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: FBXL15 (F-box/LRR-repeat protein 15; F-box only protein 37, FBXO37) is a substrate-recognition subunit of an SCF (SKP1-CUL1-RBX1) E3 ubiquitin ligase complex. Its F-box motif binds SKP1 to dock it onto the CUL1-RBX1 catalytic scaffold, while its leucine-rich repeat domain provides substrate selectivity. SCF(FBXL15) targets the HECT-type E3 ubiquitin ligase SMURF1 for ubiquitination and proteasomal degradation; by lowering SMURF1 levels it acts as a positive regulator of bone morphogenetic protein (BMP) signaling. FBXL15 recognizes the large subdomain within the N-lobe of the SMURF1 HECT domain and promotes SMURF1 ubiquitination on lysines in the WW-HECT linker (Lys357 primary, Lys355 secondary), and it can also ubiquitinate the related HECT ligases SMURF2 and WWP2. Because SMURF1 is an inhibitor of BMP signaling, SCF(FBXL15)-driven SMURF1 turnover relieves this inhibition and enhances BMP/SMAD transcriptional output, including induction of canonical BMP target genes such as ID1 and SMAD6. Through this control of SMURF1 stability, FBXL15 contributes to dorsal/ventral pattern formation during embryonic development and to bone mass maintenance. It acts in the cytoplasm.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 16; NEW: 1; UNDECIDED: 1

## PN Consistency Summary

- **Consistency:** Strong. Falcon, review YAML, and PN mapping agree FBXL15 (FBXO37) is the SCF(FBXL15) substrate receptor that degrades the HECT ligase SMURF1 (also SMURF2/WWP2), positively regulating BMP signaling (PMID:21572392, IDA-rich). Falcon refines the SMURF1 degron (K357/K355) and BMP readout (ID1/SMAD6) — consistent. One internal caveat handled well: the IMP G2/M annotation (GO:0000086) is left UNDECIDED because the abstract foregrounds BMP, not cell cycle — correct per "don't overrule curators" guidance.
- **PN story / NEW pressure:** PN asserts generic adaptor MF (GO:1990756, verified real). GOA carries only `protein binding` (IPI) as MF. The review adds GO:1990756 as a NEW IDA annotation; bare protein binding kept non-core. Correct call. Downstream BP roles (BMP regulation, bone mineralization, D/V patterning) are already annotated and kept non-core — no UPS NEW-term gap.
- **Evidence alignment:** PN reference only "15340381/rev" (placeholder); review does not cite it. Review centers on PMID:21572392 (primary, full text) + falcon. Benign divergence.
- **Verdict:** CONSISTENT / ACCEPT mapping. No edits required; NEW(GO:1990756) pattern correctly applied; substrate validated; G2/M UNDECIDED appropriately conservative.

## Full Consistency Review

- **UniProt:** Q9H469 · **batch:** proteostasis-batch-2026-06-13 · **review status:** COMPLETE
- **PN placement:** `UPS|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR` ; **PN-node mapping:** group-level `mapped / ok_for_propagation_to_go / GO:1990756`; F-box+LRR subtype/type `no_mapping`; class `context_only / too_broad / GO:0061630`; branch `no_mapping`.
- **Consistency:** Strong. Falcon, review YAML, and PN mapping agree FBXL15 (FBXO37) is the SCF(FBXL15) substrate receptor that degrades the HECT ligase SMURF1 (also SMURF2/WWP2), positively regulating BMP signaling (PMID:21572392, IDA-rich). Falcon refines the SMURF1 degron (K357/K355) and BMP readout (ID1/SMAD6) — consistent. One internal caveat handled well: the IMP G2/M annotation (GO:0000086) is left UNDECIDED because the abstract foregrounds BMP, not cell cycle — correct per "don't overrule curators" guidance.
- **PN story / NEW pressure:** PN asserts generic adaptor MF (GO:1990756, verified real). GOA carries only `protein binding` (IPI) as MF. The review adds GO:1990756 as a NEW IDA annotation; bare protein binding kept non-core. Correct call. Downstream BP roles (BMP regulation, bone mineralization, D/V patterning) are already annotated and kept non-core — no UPS NEW-term gap.
- **Mapping strategy:** Gene does not change the node. Catalysis correctly excluded from sub-nodes (RBX1 RING). SMURF1 is a validated substrate (LRR recognizes HECT N-lobe) → adaptor MF grounded, not orphan. PN-projected GO:1990756 matches review core_functions MF exactly. Note: substrate is itself a HECT E3, so this is an E3-degrades-E3 node — does not change mapping.
- **Evidence alignment:** PN reference only "15340381/rev" (placeholder); review does not cite it. Review centers on PMID:21572392 (primary, full text) + falcon. Benign divergence.
- **Verdict:** CONSISTENT / ACCEPT mapping. No edits required; NEW(GO:1990756) pattern correctly applied; substrate validated; G2/M UNDECIDED appropriately conservative.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-13
- review_yaml: genes/human/FBXL15/FBXL15-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Ubiquitin Proteasome System | E3 ubiquitin and UBL ligases | Cul1 substrate receptor | F-box | LRR
- UniProt: Q9H469
- In branches: UPS
- Signature domains: IPR001810
- Auxiliary domains: IPR001611, IPR032675
- PN references (titles):
    - 15340381 / rev
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|E3 ubiquitin and UBL ligases|Cul1 substrate receptor|F-box|LRR
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
