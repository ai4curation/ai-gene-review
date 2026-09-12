# AARSD1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: priority-only PN rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BTE6
- AIGR review status: COMPLETE
- Priority category: isoform_context_exception
- Local AIGR project status: local_review_complete_not_phase1
- Related project: not_recorded

## Source Files Checked

- AIGR review YAML: present - [genes/human/AARSD1/AARSD1-ai-review.yaml](AARSD1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AARSD1/AARSD1-ai-review.html](AARSD1-ai-review.html)
- Gene notes: present - [genes/human/AARSD1/AARSD1-notes.md](AARSD1-notes.md)
- GOA TSV: present - [genes/human/AARSD1/AARSD1-goa.tsv](AARSD1-goa.tsv)
- UniProt record: present - [genes/human/AARSD1/AARSD1-uniprot.txt](AARSD1-uniprot.txt)
- PROTEOSTASIS priority table: [projects/PROTEOSTASIS/priority_genes.tsv](../../../projects/PROTEOSTASIS/priority_genes.tsv)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)
- PN mapping file: none from current projection rows.

### Deep Research Files

- [genes/human/AARSD1/AARSD1-deep-research-falcon.md](AARSD1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AARSD1 encodes a conserved AlaX-family trans-editing factor that functions in the cytoplasm to hydrolyze mischarged aminoacyl-tRNAs and preserve translational fidelity. The literature and UniProt support AARSD1 as a proofreading enzyme rather than an alanine-tRNA ligase. Recent direct work on human AlaX shows broad activity against Ser-mischarged tRNAs and links AARSD1 loss to Ala- and Thr-to-Ser mistranslation, supporting a translation-quality-control role as core biology. A proposed HSP90 cochaperone interpretation is not supported as a core gene-level assignment for canonical AARSD1; the relevant muscle-differentiation paper appears to map to non-canonical readthrough-derived PTGES3L-AARSD1 fusion isoforms noted by UniProt for isoforms 2 and 3. That HSP90-related role is best treated as contextual and isoform-associated rather than a general function of canonical AARSD1.
- Existing/core annotation action counts: ACCEPT: 6; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 1; REMOVE: 8

## PN Consistency Summary

- **Consistency:** Priority-only record; no phase-1 dossier section exists yet. Local review status is `local_review_complete_not_phase1`. PN placement: Cytonuclear proteostasis > HSP90 cochaperone; Translation > tRNA synthetase. Main issue: Review supports canonical AlaX translational proofreading as core and treats HSP90 cochaperone evidence as likely readthrough/fusion-isoform context
- **PN story / NEW pressure:** No current projected GO row; the value is exception/context tracking.
- **Mapping strategy:** Keep canonical gene biology separate from readthrough, fusion, or isoform-specific PN context before propagating family-level mappings.
- **Verdict:** Record HSP90-cochaperone exception and keep canonical proofreading as the GO bridge outcome

## Priority Review Context

- Category: isoform_context_exception
- PN annotations: Cytonuclear proteostasis > HSP90 cochaperone; Translation > tRNA synthetase
- Why interesting: Review supports canonical AlaX translational proofreading as core and treats HSP90 cochaperone evidence as likely readthrough/fusion-isoform context
- Suggested next step: Record HSP90-cochaperone exception and keep canonical proofreading as the GO bridge outcome
- Related project: not_recorded

## PN Projection Rows

- No current PN projected GO row for this gene. Treat this priority item as an exception, boundary, or context-tracking case rather than a direct GO propagation candidate.

## PN Dossier Context

No phase-1 dossier exists for this priority-only gene. This note preserves the current PROTEOSTASIS boundary or exception decision and should be superseded by a dossier section if the gene is promoted into a full phase-1 batch.

## Note

This file is generated from the current PROTEOSTASIS priority table, PN projection outputs, and local gene-review artifacts. Edit those source records rather than this generated note when correcting the underlying curation.
