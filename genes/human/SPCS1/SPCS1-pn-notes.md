# SPCS1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y6A9
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/SPCS1/SPCS1-ai-review.yaml](SPCS1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/SPCS1/SPCS1-ai-review.html
- Gene notes: present - [genes/human/SPCS1/SPCS1-notes.md](SPCS1-notes.md)
- GOA TSV: present - [genes/human/SPCS1/SPCS1-goa.tsv](SPCS1-goa.tsv)
- UniProt record: present - [genes/human/SPCS1/SPCS1-uniprot.txt](SPCS1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/SPCS1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/SPCS1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SPCS1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/SPCS1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/SPCS1/SPCS1-deep-research-falcon.md](SPCS1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SPCS1 (signal peptidase complex subunit 1, also SPC12, the microsomal signal peptidase 12 kDa subunit) is a small (169 aa) multi-pass endoplasmic reticulum membrane protein that is one of the three non-catalytic accessory subunits (with SPCS2 and SPCS3) of the eukaryotic ER signal peptidase complex (SPC). The SPC removes N-terminal signal sequences from secretory and membrane preproteins as they are translocated into the ER lumen; its catalytic activity resides in the SEC11A or SEC11C subunits, and SPCS1 is dispensable for enzymatic cleavage. SPCS1 spans the ER membrane twice with both termini facing the cytosol and only minimal lumenal exposure, and together with the other subunits it shapes a transmembrane "window" that locally thins the lipid bilayer, contributing to substrate selectivity for signal-peptide hydrophobic regions shorter than about 18-20 residues. Beyond its housekeeping role in signal peptide processing, SPCS1 acts as a host factor exploited by flaviviruses (West Nile, Dengue, Zika, yellow fever, Japanese encephalitis viruses) and hepatitis C virus, where it promotes post-translational processing of viral structural proteins and assembly of infectious virions through interactions with viral membrane proteins such as HCV NS2/E2 and flaviviral NS2B.
- Existing/core annotation action counts: ACCEPT: 12; KEEP_AS_NON_CORE: 8; MODIFY: 1

## PN Consistency Summary

- **Consistency:** Strong agreement. Deep research, review YAML, and PN all describe SPCS1 as a non-catalytic accessory SPC subunit (multi-pass, cytosol-facing termini, dispensable for catalysis; contributes to membrane-thinning window/selectivity) plus a flavivirus/HCV host factor. PN node correctly captures complex membership without ascribing catalysis. No contradictions.
- **PN story / NEW pressure:** PN asserts only CC membership (GO:0005787) and broad transport (GO:0015031). GO:0005787 already in review (IBA/IEA/IPI/TAS). The transport class GO:0015031 is broader than the review, which deliberately MODIFIES the IBA GO:0045047 (protein targeting to ER) to GO:0006465 signal peptide processing — i.e. the review argues SPCS1 acts downstream of targeting, not in transport. So PN's GO:0015031 (protein transport) projection slightly over-reaches for an accessory peptidase subunit. The accurate process is GO:0006465. No new MF justified (non-catalytic). Conclude: membership already captured; PN transport-class projection over-reaches vs review's signal-peptide-processing framing.
- **Evidence alignment:** PN row carries no titles; review's accessory/topology evidence (PMID:8632014, PMID:34388369) and viral host-factor evidence (PMID:24009510, 27383988, 29593046, 35130329, 33577859) plus falcon deep research (liaci2021, chung2024) all converge. Congruent.
- **Verdict:** CONSISTENT on membership; PN's protein-transport class projection over-reaches (review's GO:0006465 signal peptide processing is more accurate). No gene-YAML edit needed.

## Full Consistency Review

- **UniProt:** Q9Y6A9 (SPC12) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|ER signal peptidase`; **PN-node mapping:** group mapped, ok_for_propagation_to_go, GO:0005787 (signal peptidase complex); class GO:0015031 (protein transport).
- **Consistency:** Strong agreement. Deep research, review YAML, and PN all describe SPCS1 as a non-catalytic accessory SPC subunit (multi-pass, cytosol-facing termini, dispensable for catalysis; contributes to membrane-thinning window/selectivity) plus a flavivirus/HCV host factor. PN node correctly captures complex membership without ascribing catalysis. No contradictions.
- **PN story / NEW pressure:** PN asserts only CC membership (GO:0005787) and broad transport (GO:0015031). GO:0005787 already in review (IBA/IEA/IPI/TAS). The transport class GO:0015031 is broader than the review, which deliberately MODIFIES the IBA GO:0045047 (protein targeting to ER) to GO:0006465 signal peptide processing — i.e. the review argues SPCS1 acts downstream of targeting, not in transport. So PN's GO:0015031 (protein transport) projection slightly over-reaches for an accessory peptidase subunit. The accurate process is GO:0006465. No new MF justified (non-catalytic). Conclude: membership already captured; PN transport-class projection over-reaches vs review's signal-peptide-processing framing.
- **Mapping strategy:** GO:0005787 CC mapping is correct. The class-level GO:0015031 protein transport is the questionable projection: for accessory SPC subunits the review's signal peptide processing (GO:0006465) is the defensible BP, and protein transport over-states an upstream-transport role SPCS1 does not have (parallels the broader-than-warranted precedent). Suggest the node distinguish accessory (membership/selectivity, GO:0006465) from catalytic members.
- **Evidence alignment:** PN row carries no titles; review's accessory/topology evidence (PMID:8632014, PMID:34388369) and viral host-factor evidence (PMID:24009510, 27383988, 29593046, 35130329, 33577859) plus falcon deep research (liaci2021, chung2024) all converge. Congruent.
- **Verdict:** CONSISTENT on membership; PN's protein-transport class projection over-reaches (review's GO:0006465 signal peptide processing is more accurate). No gene-YAML edit needed.
- **Recommended edits:** [MAP] At the "ER signal peptidase" class, prefer GO:0006465 signal peptide processing over GO:0015031 protein transport as the BP projection for accessory subunits (SPCS1/2), reflecting that SPCS1 acts downstream of ER targeting (matches review MODIFY of GO:0045047→GO:0006465).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/SPCS1/SPCS1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | ER signal peptidase
- UniProt: Q9Y6A9
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
