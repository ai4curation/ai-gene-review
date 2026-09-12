# BAG6 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: priority-only PN rereview against local AIGR review and available deep-research artifacts
- UniProt: P46379
- AIGR review status: COMPLETE
- Priority category: multibranch_boundary_case
- Local AIGR project status: local_review_complete_not_phase1
- Related project: ER_PHAGY.md

## Source Files Checked

- AIGR review YAML: present - [genes/human/BAG6/BAG6-ai-review.yaml](BAG6-ai-review.yaml)
- AIGR review HTML: present - [genes/human/BAG6/BAG6-ai-review.html](BAG6-ai-review.html)
- Gene notes: present - [genes/human/BAG6/BAG6-notes.md](BAG6-notes.md)
- GOA TSV: present - [genes/human/BAG6/BAG6-goa.tsv](BAG6-goa.tsv)
- UniProt record: present - [genes/human/BAG6/BAG6-uniprot.txt](BAG6-uniprot.txt)
- PROTEOSTASIS priority table: [projects/PROTEOSTASIS/priority_genes.tsv](../../../projects/PROTEOSTASIS/priority_genes.tsv)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)
- PN mapping file: [projects/PROTEOSTASIS/mappings/er_proteostasis.yaml](../../../projects/PROTEOSTASIS/mappings/er_proteostasis.yaml)

### Deep Research Files

- [genes/human/BAG6/BAG6-deep-research-falcon.md](BAG6-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: BAG6 is a multifunctional nucleo-cytoplasmic proteostasis factor that sits at the boundary between the GET pathway and ubiquitin-proteasome-associated quality control. In the cytosol, the BAG6/UBL4A/GET4 (BAT3) complex captures hydrophobic tail-anchored or otherwise mislocalized secretory proteins, promotes their handoff to TRC40/ASNA1 for post-translational delivery to the endoplasmic reticulum, and routes failed clients toward ubiquitin-proteasome degradation. BAG6 also acts as a holdase for retrotranslocated ERAD substrates and contributes to ER stress-induced pre-emptive quality control. Additional nuclear and extracellular roles, including p53 acetylation after DNA damage and exosomal NKp30 ligand activity, are supported in specific contexts but are not the core conserved proteostasis functions.
- Existing/core annotation action counts: ACCEPT: 30; KEEP_AS_NON_CORE: 32; MARK_AS_OVER_ANNOTATED: 4; MODIFY: 9; REMOVE: 29

## PN Consistency Summary

- **Consistency:** Priority-only record; no phase-1 dossier section exists yet. Local review status is `local_review_complete_not_phase1`. PN placement: ER proteostasis > GET pathway component; UPS > associated non-Ub enzyme chaperone; UPS > UBL domain > chaperones and related. Main issue: Review supports specific GET, ERAD, and holdase roles but not broad parent protein-transport propagation
- **PN story / NEW pressure:** Current projection rows: GO:0006620 post-translational protein targeting to endoplasmic reticulum membrane (already_in_goa_exact).
- **Mapping strategy:** Use narrow, evidence-aligned PN mappings, but preserve exceptions against broad parent propagation across mixed proteostasis branches.
- **Verdict:** Add to boundary/phase1 tracking; keep broad protein-transport exception and positive GET/ERAD bridge outcomes

## Priority Review Context

- Category: multibranch_boundary_case
- PN annotations: ER proteostasis > GET pathway component; UPS > associated non-Ub enzyme chaperone; UPS > UBL domain > chaperones and related
- Why interesting: Review supports specific GET, ERAD, and holdase roles but not broad parent protein-transport propagation
- Suggested next step: Add to boundary/phase1 tracking; keep broad protein-transport exception and positive GET/ERAD bridge outcomes
- Related project: ER_PHAGY.md

## PN Projection Rows

- GO:0006620 post-translational protein targeting to endoplasmic reticulum membrane - already_in_goa_exact; scope=ok_for_propagation_to_go; mapping=er_proteostasis.yaml; PN=ER proteostasis|Protein transport|GET pathway component

## PN Dossier Context

No phase-1 dossier exists for this priority-only gene. This note preserves the current PROTEOSTASIS boundary or exception decision and should be superseded by a dossier section if the gene is promoted into a full phase-1 batch.

## Note

This file is generated from the current PROTEOSTASIS priority table, PN projection outputs, and local gene-review artifacts. Edit those source records rather than this generated note when correcting the underlying curation.
