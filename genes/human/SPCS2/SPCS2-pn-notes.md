# SPCS2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q15005
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SPCS2/SPCS2-ai-review.yaml](SPCS2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SPCS2/SPCS2-ai-review.html
- Gene notes: present - [genes/human/SPCS2/SPCS2-notes.md](SPCS2-notes.md)
- GOA TSV: present - [genes/human/SPCS2/SPCS2-goa.tsv](SPCS2-goa.tsv)
- UniProt record: present - [genes/human/SPCS2/SPCS2-uniprot.txt](SPCS2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SPCS2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SPCS2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SPCS2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SPCS2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/SPCS2/SPCS2-deep-research-falcon.md](SPCS2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SPCS2 (signal peptidase complex subunit 2, also SPC25, the microsomal signal peptidase 25 kDa subunit) is a 226 aa multi-pass endoplasmic reticulum membrane protein that is one of the three non-catalytic accessory subunits (with SPCS1 and SPCS3) of the eukaryotic ER signal peptidase complex (SPC). The SPC removes N-terminal signal sequences from secretory and membrane preproteins as they are translocated into the ER lumen; catalysis resides in the SEC11A or SEC11C subunits. SPCS2 spans the ER membrane twice with both termini facing the cytosol and is thought to enhance the enzymatic activity of the complex and to facilitate interactions between components of the translocation site. Together with the other subunits it helps form the transmembrane window that locally thins the ER bilayer, contributing to the complex's selectivity for signal-peptide hydrophobic regions shorter than about 18-20 residues.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 3; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Strong agreement. Deep research, review YAML, and PN all describe SPCS2 as a non-catalytic accessory SPC subunit that enhances complex activity and shapes substrate/cleavage-site selection (yeast Spc2 ortholog; membrane-thinning). PN node correctly captures complex membership without ascribing catalysis. No contradictions.
- **PN story / NEW pressure:** Same pattern as SPCS1. PN asserts CC membership (GO:0005787, already in review IBA/IEA/IPI) and the broad transport class (GO:0015031). The review deliberately MODIFIES IBA GO:0045047→GO:0006465 (signal peptide processing), arguing SPCS2 acts after targeting. So the PN GO:0015031 protein transport projection slightly over-reaches; GO:0006465 is the accurate BP. No new MF (non-catalytic; "enhances enzymatic activity" is a regulatory/architectural role, not a catalytic MF). Conclude: membership already captured; transport-class projection over-reaches.
- **Evidence alignment:** PN row carries no titles; review's structural/mechanistic evidence (PMID:34388369; PMID:39565596 yeast Spc2 substrate/cleavage-site selection, explicitly cross-referenced to human SPCS2) plus host-pathogen context (PMID:34232536, 36789796, 38230952) and falcon deep research (chung2024, kozono2023) all converge. Congruent.
- **Verdict:** CONSISTENT on membership; PN's protein-transport class projection over-reaches (review's GO:0006465 is more accurate). No gene-YAML edit needed.

## Full Consistency Review

- **UniProt:** Q15005 (SPC25) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|ER signal peptidase`; **PN-node mapping:** group mapped, ok_for_propagation_to_go, GO:0005787 (signal peptidase complex); class GO:0015031 (protein transport).
- **Consistency:** Strong agreement. Deep research, review YAML, and PN all describe SPCS2 as a non-catalytic accessory SPC subunit that enhances complex activity and shapes substrate/cleavage-site selection (yeast Spc2 ortholog; membrane-thinning). PN node correctly captures complex membership without ascribing catalysis. No contradictions.
- **PN story / NEW pressure:** Same pattern as SPCS1. PN asserts CC membership (GO:0005787, already in review IBA/IEA/IPI) and the broad transport class (GO:0015031). The review deliberately MODIFIES IBA GO:0045047→GO:0006465 (signal peptide processing), arguing SPCS2 acts after targeting. So the PN GO:0015031 protein transport projection slightly over-reaches; GO:0006465 is the accurate BP. No new MF (non-catalytic; "enhances enzymatic activity" is a regulatory/architectural role, not a catalytic MF). Conclude: membership already captured; transport-class projection over-reaches.
- **Mapping strategy:** GO:0005787 CC mapping correct. GO:0015031 protein transport is the questionable class projection for accessory subunits; review's GO:0006465 signal peptide processing is more defensible. Node should distinguish accessory (architecture/selectivity, GO:0006465) from catalytic (GO:0009003) members rather than flattening all four to one CC + protein-transport BP.
- **Evidence alignment:** PN row carries no titles; review's structural/mechanistic evidence (PMID:34388369; PMID:39565596 yeast Spc2 substrate/cleavage-site selection, explicitly cross-referenced to human SPCS2) plus host-pathogen context (PMID:34232536, 36789796, 38230952) and falcon deep research (chung2024, kozono2023) all converge. Congruent.
- **Verdict:** CONSISTENT on membership; PN's protein-transport class projection over-reaches (review's GO:0006465 is more accurate). No gene-YAML edit needed.
- **Recommended edits:** [MAP] At the "ER signal peptidase" class, prefer GO:0006465 signal peptide processing over GO:0015031 protein transport as the BP projection for accessory subunits (SPCS1/2). Optionally [REF] note PMID:39565596 (Spc2/SPCS2 substrate-selection) supports a substrate-selectivity contribution beyond bare membership.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SPCS2/SPCS2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | ER signal peptidase
- UniProt: Q15005
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
