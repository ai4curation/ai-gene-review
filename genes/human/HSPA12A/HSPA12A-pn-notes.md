# HSPA12A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: priority-only PN rereview against local AIGR review and available deep-research artifacts
- UniProt: O43301
- AIGR review status: COMPLETE
- Priority category: domain_exception
- Local AIGR project status: local_review_complete_not_phase1
- Related project: UNFOLDED_PROTEIN_BINDING.md

## Source Files Checked

- AIGR review YAML: present - [genes/human/HSPA12A/HSPA12A-ai-review.yaml](HSPA12A-ai-review.yaml)
- AIGR review HTML: present - [genes/human/HSPA12A/HSPA12A-ai-review.html](HSPA12A-ai-review.html)
- Gene notes: present - [genes/human/HSPA12A/HSPA12A-notes.md](HSPA12A-notes.md)
- GOA TSV: present - [genes/human/HSPA12A/HSPA12A-goa.tsv](HSPA12A-goa.tsv)
- UniProt record: present - [genes/human/HSPA12A/HSPA12A-uniprot.txt](HSPA12A-uniprot.txt)
- PROTEOSTASIS priority table: [projects/PROTEOSTASIS/priority_genes.tsv](../../../projects/PROTEOSTASIS/priority_genes.tsv)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)
- PN mapping file: none from current projection rows.

### Deep Research Files

- [genes/human/HSPA12A/HSPA12A-deep-research-falcon.md](HSPA12A-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: HSPA12A is an atypical and still poorly characterized HSP70-family protein. The strongest direct mechanistic evidence supports ATP/ADP-sensitive binding to the cytosolic tail of SORL1/SorLA and modulation of SorLA trafficking, while later disease- and tissue-specific studies suggest context-dependent signaling or scaffold-like roles rather than a conserved GO-ready core activity. Current evidence supports a narrow SorLA/SORL1-selective adaptor-like trafficking role and does not establish canonical ATP-dependent protein folding chaperone activity or another broad core proteostasis function for HSPA12A.
- Existing/core annotation action counts: KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 3; MODIFY: 1; NEW: 1

## PN Consistency Summary

- **Consistency:** Priority-only record; no phase-1 dossier section exists yet. Local review status is `local_review_complete_not_phase1`. PN placement: Cytonuclear proteostasis > Chaperone > HSP70 system > HSP70. Main issue: MS1 inclusion is based on HSP70 architecture, but review supports SorLA/SORL1-tail adaptor trafficking rather than canonical HSP70 folding activity
- **PN story / NEW pressure:** No current projected GO row; the value is exception/context tracking.
- **Mapping strategy:** Keep as an explicit exception to family/domain propagation. The PN family placement is informative, but the local review should decide whether canonical chaperone activity is actually supported.
- **Verdict:** Record as HSP70 GO:0140662 gene exception and sync the domain-only caveat to PN

## Priority Review Context

- Category: domain_exception
- PN annotations: Cytonuclear proteostasis > Chaperone > HSP70 system > HSP70
- Why interesting: MS1 inclusion is based on HSP70 architecture, but review supports SorLA/SORL1-tail adaptor trafficking rather than canonical HSP70 folding activity
- Suggested next step: Record as HSP70 GO:0140662 gene exception and sync the domain-only caveat to PN
- Related project: UNFOLDED_PROTEIN_BINDING.md

## PN Projection Rows

- No current PN projected GO row for this gene. Treat this priority item as an exception, boundary, or context-tracking case rather than a direct GO propagation candidate.

## PN Dossier Context

No phase-1 dossier exists for this priority-only gene. This note preserves the current PROTEOSTASIS boundary or exception decision and should be superseded by a dossier section if the gene is promoted into a full phase-1 batch.

## Note

This file is generated from the current PROTEOSTASIS priority table, PN projection outputs, and local gene-review artifacts. Edit those source records rather than this generated note when correcting the underlying curation.
