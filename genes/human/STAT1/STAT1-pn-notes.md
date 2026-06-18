# STAT1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: priority-only PN rereview against local AIGR review and available deep-research artifacts
- UniProt: P42224
- AIGR review status: COMPLETE
- Priority category: context_specific_ALP
- Local AIGR project status: local_review_complete_not_phase1
- Related project: INTEGRATED_STRESS_RESPONSE.md

## Source Files Checked

- AIGR review YAML: present - [genes/human/STAT1/STAT1-ai-review.yaml](STAT1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/STAT1/STAT1-ai-review.html](STAT1-ai-review.html)
- Gene notes: present - [genes/human/STAT1/STAT1-notes.md](STAT1-notes.md)
- GOA TSV: present - [genes/human/STAT1/STAT1-goa.tsv](STAT1-goa.tsv)
- UniProt record: present - [genes/human/STAT1/STAT1-uniprot.txt](STAT1-uniprot.txt)
- PROTEOSTASIS priority table: [projects/PROTEOSTASIS/priority_genes.tsv](../../../projects/PROTEOSTASIS/priority_genes.tsv)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)
- PN mapping file: none from current projection rows.

### Deep Research Files

- [genes/human/STAT1/STAT1-deep-research-falcon.md](STAT1-deep-research-falcon.md)
- [genes/human/STAT1/STAT1-deep-research.md](STAT1-deep-research.md)

## AIGR Review Snapshot

- Description: STAT1 is a latent cytoplasmic transcription factor that serves as a central mediator of cytokine signaling, particularly interferon responses. Upon cytokine stimulation, STAT1 becomes phosphorylated on Y701 by JAK kinases, forms homodimers or heterodimers (e.g., with STAT2), and translocates to the nucleus where it binds specific DNA elements to regulate gene expression. STAT1 is essential for antiviral and antimicrobial immunity, mediating both type I (IFN-α/β, forming ISGF3 complex) and type II (IFN-γ, forming GAF complex) interferon responses. Knockout studies demonstrate STAT1's non-redundant role in host defense against viruses, bacteria, and fungi.
- Existing/core annotation action counts: ACCEPT: 205; KEEP_AS_NON_CORE: 38; MARK_AS_OVER_ANNOTATED: 43; MODIFY: 1; NEW: 1; REMOVE: 5; UNDECIDED: 1

## PN Consistency Summary

- **Consistency:** Priority-only record; no phase-1 dossier section exists yet. Local review status is `local_review_complete_not_phase1`. PN placement: ALP > Autophagy gene expression > Transcriptional repressor. Main issue: Workbook has an explicit ULK1-promoter note, but this likely remains a contextual non-core role
- **PN story / NEW pressure:** No current projected GO row; the value is exception/context tracking.
- **Mapping strategy:** Treat the PN ALP placement as context-specific regulatory biology. A non-core GO annotation may be warranted only if the gene-specific evidence supports it.
- **Verdict:** Create boundary/phase1 dossier and decide whether a non-core ALP regulatory annotation is warranted

## Priority Review Context

- Category: context_specific_ALP
- PN annotations: ALP > Autophagy gene expression > Transcriptional repressor
- Why interesting: Workbook has an explicit ULK1-promoter note, but this likely remains a contextual non-core role
- Suggested next step: Create boundary/phase1 dossier and decide whether a non-core ALP regulatory annotation is warranted
- Related project: INTEGRATED_STRESS_RESPONSE.md

## PN Projection Rows

- No current PN projected GO row for this gene. Treat this priority item as an exception, boundary, or context-tracking case rather than a direct GO propagation candidate.

## PN Dossier Context

No phase-1 dossier exists for this priority-only gene. This note preserves the current PROTEOSTASIS boundary or exception decision and should be superseded by a dossier section if the gene is promoted into a full phase-1 batch.

## Note

This file is generated from the current PROTEOSTASIS priority table, PN projection outputs, and local gene-review artifacts. Edit those source records rather than this generated note when correcting the underlying curation.
