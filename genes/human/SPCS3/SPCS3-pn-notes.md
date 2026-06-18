# SPCS3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P61009
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SPCS3/SPCS3-ai-review.yaml](SPCS3-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SPCS3/SPCS3-ai-review.html
- Gene notes: present - [genes/human/SPCS3/SPCS3-notes.md](SPCS3-notes.md)
- GOA TSV: present - [genes/human/SPCS3/SPCS3-goa.tsv](SPCS3-goa.tsv)
- UniProt record: present - [genes/human/SPCS3/SPCS3-uniprot.txt](SPCS3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SPCS3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SPCS3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SPCS3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SPCS3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/SPCS3/SPCS3-deep-research-falcon.md](SPCS3-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SPCS3 (signal peptidase complex subunit 3, also SPC22/23, the microsomal signal peptidase 22/23 kDa subunit) is a 180 aa single-pass type II endoplasmic reticulum membrane protein that is one of the three non-catalytic accessory subunits (with SPCS1 and SPCS2) of the eukaryotic ER signal peptidase complex (SPC). The SPC removes N-terminal signal sequences from secretory and membrane preproteins as they are translocated into the ER lumen; catalysis resides in the SEC11A or SEC11C subunits. SPCS3 has a single N-terminal transmembrane helix and a large lumenal domain, and although not catalytic itself it is essential for SPC catalytic activity, thought to stabilize and position the catalytic center near the lumenal surface of the membrane. Together with the other subunits it contributes to the transmembrane window that locally thins the ER bilayer and sets the complex's selectivity for short signal-peptide hydrophobic regions. SPCS3 also acts as a host factor required for efficient production of flaviviruses (West Nile, Japanese encephalitis, Dengue type 2, and yellow fever viruses).
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 9; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Deep research (notes + falcon) ↔ review YAML ↔ PN annotation are consistent. All four describe SPCS3 as a non-catalytic accessory subunit of the ER signal peptidase complex (SPC-A/SPC-C), essential for SEC11 catalytic activity, single-pass type II ER membrane protein, plus a secondary flavivirus host-factor role. No contradictions. The PN "ER signal peptidase" group→GO:0005787 matches the review's CORE annotation exactly.
- **PN story / NEW pressure:** The PN group mapping (signal peptidase complex, GO:0005787) is already a CORE GOA/review annotation — already captured, no NEW pressure. The review's preferred process term GO:0006465 signal peptide processing (proposed replacement for the IBA GO:0045047) is already a standard term, also no NEW term needed.
- **Evidence alignment:** Strong overlap. PN reference titles (cryo-EM SPC structure; flavivirus CRISPR screen) match review PMID:34388369 and PMID:27383988. Review adds breadth (CHIKV PMID:39261662, HCV PMID:38230952, ComplexPortal/Reactome) beyond the PN row.
- **Verdict:** Internally consistent and well-curated. Recommend NOT propagating the class-level GO:0015031 protein transport to SPCS3 (over-reach); GO:0005787 is correctly captured.

## Full Consistency Review

- **UniProt:** P61009 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|ER signal peptidase` ; **PN-node mapping:** group=mapped/ok_for_propagation_to_go GO:0005787 signal peptidase complex; parent class "Protein transport"=mapped/ok GO:0015031 protein transport; branch=no_mapping.
- **Consistency:** Deep research (notes + falcon) ↔ review YAML ↔ PN annotation are consistent. All four describe SPCS3 as a non-catalytic accessory subunit of the ER signal peptidase complex (SPC-A/SPC-C), essential for SEC11 catalytic activity, single-pass type II ER membrane protein, plus a secondary flavivirus host-factor role. No contradictions. The PN "ER signal peptidase" group→GO:0005787 matches the review's CORE annotation exactly.
- **PN story / NEW pressure:** The PN group mapping (signal peptidase complex, GO:0005787) is already a CORE GOA/review annotation — already captured, no NEW pressure. The review's preferred process term GO:0006465 signal peptide processing (proposed replacement for the IBA GO:0045047) is already a standard term, also no NEW term needed.
- **Mapping strategy:** Concern — the parent **class** node "ER proteostasis|Protein transport" projects **GO:0015031 protein transport** as `new_to_goa` to SPCS3. SPCS3 does NOT mediate protein transport; it is a signal peptidase accessory subunit acting downstream of translocation (the review explicitly MODIFIES the IBA "protein targeting to ER" to "signal peptide processing"). GO:0015031 over-reaches here, analogous to the TOMM20/HSPA8/RAB7A "broader" rejections. The group-level GO:0005787 mapping is correct; the class-level GO:0015031 projection should not be propagated to SPCS3.
- **Evidence alignment:** Strong overlap. PN reference titles (cryo-EM SPC structure; flavivirus CRISPR screen) match review PMID:34388369 and PMID:27383988. Review adds breadth (CHIKV PMID:39261662, HCV PMID:38230952, ComplexPortal/Reactome) beyond the PN row.
- **Verdict:** Internally consistent and well-curated. Recommend NOT propagating the class-level GO:0015031 protein transport to SPCS3 (over-reach); GO:0005787 is correctly captured.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SPCS3/SPCS3-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | ER signal peptidase
- UniProt: P61009
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Protein transport|ER signal peptidase
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0005787 signal peptidase complex]
        rationale: This PN group denotes ER signal peptidase complex components. The matching GO cellular-component term is the direct propagation target.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (2)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport
- GO:0005787 signal peptidase complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Protein transport|ER signal peptidase

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
