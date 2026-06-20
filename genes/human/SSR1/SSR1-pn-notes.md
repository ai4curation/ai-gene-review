# SSR1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: priority-only PN rereview against local AIGR review and available deep-research artifacts
- UniProt: P43307
- AIGR review status: COMPLETE
- Priority category: positive_control
- Local AIGR project status: local_review_complete_not_phase1
- Related project: ER_PHAGY.md

## Source Files Checked

- AIGR review YAML: present - [genes/human/SSR1/SSR1-ai-review.yaml](SSR1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/SSR1/SSR1-ai-review.html](SSR1-ai-review.html)
- Gene notes: present - [genes/human/SSR1/SSR1-notes.md](SSR1-notes.md)
- GOA TSV: present - [genes/human/SSR1/SSR1-goa.tsv](SSR1-goa.tsv)
- UniProt record: present - [genes/human/SSR1/SSR1-uniprot.txt](SSR1-uniprot.txt)
- PROTEOSTASIS priority table: [projects/PROTEOSTASIS/priority_genes.tsv](../../../projects/PROTEOSTASIS/priority_genes.tsv)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)
- PN mapping file: [projects/PROTEOSTASIS/mappings/er_proteostasis.yaml](../../../projects/PROTEOSTASIS/mappings/er_proteostasis.yaml)

### Deep Research Files

- [genes/human/SSR1/SSR1-deep-research-falcon.md](SSR1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SSR1 encodes Translocon-associated protein subunit alpha (TRAP-alpha), a single-pass type I ER membrane glycoprotein that is a core component of the heterotetrameric TRAP complex (TRAP-alpha/beta/gamma/delta, encoded by SSR1-4). The TRAP complex stably associates with the Sec61 protein-conducting channel and ribosomes at the ER membrane, facilitating co-translational translocation of secretory and membrane proteins, particularly those with weak or atypical signal peptides. TRAP-alpha features a large N-terminal luminal domain positioned beneath the Sec61 channel exit site and a single long transmembrane helix that contacts Sec61. The complex coordinates with the oligosaccharyltransferase (OST) to couple translocation with N-glycosylation. TRAP-alpha also participates in ER quality control and ERAD pathways.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 5; NEW: 1

## PN Consistency Summary

- **Consistency:** Priority-only record; no phase-1 dossier section exists yet. Local review status is `local_review_complete_not_phase1`. PN placement: ER proteostasis > Protein transport > TRAP complex component. Main issue: Good example where PN context is compatible with existing ER targeting/translocation GO terms
- **PN story / NEW pressure:** Current projection rows: GO:0015031 protein transport (entailed_by_goa_closure).
- **Mapping strategy:** Use as a calibration case for PN-to-GO propagation: the PN placement should agree with an already well-supported local review rather than driving broad new ontology pressure.
- **Verdict:** Add to boundary/phase1 tracking as a mapping positive control

## Priority Review Context

- Category: positive_control
- PN annotations: ER proteostasis > Protein transport > TRAP complex component
- Why interesting: Good example where PN context is compatible with existing ER targeting/translocation GO terms
- Suggested next step: Add to boundary/phase1 tracking as a mapping positive control
- Related project: ER_PHAGY.md

## PN Projection Rows

- GO:0015031 protein transport - entailed_by_goa_closure; scope=ok_for_propagation_to_go; mapping=er_proteostasis.yaml; PN=ER proteostasis|Protein transport|TRAP complex component

## PN Dossier Context

No phase-1 dossier exists for this priority-only gene. This note preserves the current PROTEOSTASIS boundary or exception decision and should be superseded by a dossier section if the gene is promoted into a full phase-1 batch.

## Note

This file is generated from the current PROTEOSTASIS priority table, PN projection outputs, and local gene-review artifacts. Edit those source records rather than this generated note when correcting the underlying curation.
