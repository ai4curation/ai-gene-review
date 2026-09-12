# BTF3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: priority-only PN rereview against local AIGR review and available deep-research artifacts
- UniProt: P20290
- AIGR review status: COMPLETE
- Priority category: positive_control
- Local AIGR project status: local_review_complete_not_phase1
- Related project: RIBOSOME_QUALITY_CONTROL.md

## Source Files Checked

- AIGR review YAML: present - [genes/human/BTF3/BTF3-ai-review.yaml](BTF3-ai-review.yaml)
- AIGR review HTML: present - [genes/human/BTF3/BTF3-ai-review.html](BTF3-ai-review.html)
- Gene notes: present - [genes/human/BTF3/BTF3-notes.md](BTF3-notes.md)
- GOA TSV: present - [genes/human/BTF3/BTF3-goa.tsv](BTF3-goa.tsv)
- UniProt record: present - [genes/human/BTF3/BTF3-uniprot.txt](BTF3-uniprot.txt)
- PROTEOSTASIS priority table: [projects/PROTEOSTASIS/priority_genes.tsv](../../../projects/PROTEOSTASIS/priority_genes.tsv)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)
- PN mapping file: [projects/PROTEOSTASIS/mappings/translation.yaml](../../../projects/PROTEOSTASIS/mappings/translation.yaml)

### Deep Research Files

- [genes/human/BTF3/BTF3-deep-research-falcon.md](BTF3-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: BTF3 encodes the beta subunit of the nascent polypeptide-associated complex (NAC), a conserved ribosome-associated factor that helps sort emerging nascent chains and prevents inappropriate SRP-dependent delivery of non-secretory proteins to the ER. Human BTF3 is also reported in the nucleus and retains legacy transcription-factor literature, but its best-supported core role is cytoplasmic cotranslational nascent-peptide handling rather than broad transcriptional regulation.
- Existing/core annotation action counts: ACCEPT: 6; KEEP_AS_NON_CORE: 2; MARK_AS_OVER_ANNOTATED: 6; NEW: 1

## PN Consistency Summary

- **Consistency:** Priority-only record; no phase-1 dossier section exists yet. Local review status is `local_review_complete_not_phase1`. PN placement: Translation > Cytosolic translation > Nascent peptide husbandry > Nascent peptide sorting > NAC component. Main issue: True human BTF3 (P20290) is a reviewed PN translation factor; BTN3A3 synonym confusion was the original tracking concern
- **PN story / NEW pressure:** Current projection rows: GO:0005854 nascent polypeptide-associated complex (already_in_goa_exact).
- **Mapping strategy:** Use as a calibration case for PN-to-GO propagation: the PN placement should agree with an already well-supported local review rather than driving broad new ontology pressure.
- **Verdict:** Add to boundary/phase1 tracking and use as NAC-component positive control

## Priority Review Context

- Category: positive_control
- PN annotations: Translation > Cytosolic translation > Nascent peptide husbandry > Nascent peptide sorting > NAC component
- Why interesting: True human BTF3 (P20290) is a reviewed PN translation factor; BTN3A3 synonym confusion was the original tracking concern
- Suggested next step: Add to boundary/phase1 tracking and use as NAC-component positive control
- Related project: RIBOSOME_QUALITY_CONTROL.md

## PN Projection Rows

- GO:0005854 nascent polypeptide-associated complex - already_in_goa_exact; scope=ok_for_propagation_to_go; mapping=translation.yaml; PN=Translation|Cytosolic translation|Nascent peptide husbandry|Nascent peptide sorting|NAC component

## PN Dossier Context

No phase-1 dossier exists for this priority-only gene. This note preserves the current PROTEOSTASIS boundary or exception decision and should be superseded by a dossier section if the gene is promoted into a full phase-1 batch.

## Note

This file is generated from the current PROTEOSTASIS priority table, PN projection outputs, and local gene-review artifacts. Edit those source records rather than this generated note when correcting the underlying curation.
