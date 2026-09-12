# TTC28 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: priority-only PN rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96AY4
- AIGR review status: COMPLETE
- Priority category: cc_tpr_exception
- Local AIGR project status: local_review_complete_not_phase1
- Related project: not_recorded

## Source Files Checked

- AIGR review YAML: present - [genes/human/TTC28/TTC28-ai-review.yaml](TTC28-ai-review.yaml)
- AIGR review HTML: present - [genes/human/TTC28/TTC28-ai-review.html](TTC28-ai-review.html)
- Gene notes: present - [genes/human/TTC28/TTC28-notes.md](TTC28-notes.md)
- GOA TSV: present - [genes/human/TTC28/TTC28-goa.tsv](TTC28-goa.tsv)
- UniProt record: present - [genes/human/TTC28/TTC28-uniprot.txt](TTC28-uniprot.txt)
- PROTEOSTASIS priority table: [projects/PROTEOSTASIS/priority_genes.tsv](../../../projects/PROTEOSTASIS/priority_genes.tsv)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)
- PN mapping file: none from current projection rows.

### Deep Research Files

- [genes/human/TTC28/TTC28-deep-research-falcon.md](TTC28-deep-research-falcon.md)
- [genes/human/TTC28/TTC28-deep-research-openai.md](TTC28-deep-research-openai.md)
- [genes/human/TTC28/TTC28-deep-research-perplexity-lite.md](TTC28-deep-research-perplexity-lite.md)
- [genes/human/TTC28/TTC28-deep-research-perplexity.md](TTC28-deep-research-perplexity.md)

## AIGR Review Snapshot

- Description: Tetratricopeptide repeat protein 28 (TTC28/TPRBK), a very large (~271 kDa, ~2365-2481 AA) protein built from ~25-28 tetratricopeptide repeat (TPR) motifs. TPR domains are helical repeat motifs that mediate protein-protein interactions, and TTC28 acts as a scaffold/adaptor rather than an enzyme. Mechanistic work (Zhang et al. 2024, PNAS) establishes that TTC28 is a substrate of HSPA8/HSC70 chaperone-mediated autophagy (CMA)/microautophagy: its TPR domains bind the C-terminal PTIEEVD motif of HSPA8, and it carries multiple KFERQ-like motifs, leading to LAMP2A-dependent lysosomal turnover. Functionally, TTC28 is required for the maintenance of chromosomal stability, acting through regulation of mitosis and cytokinesis. It is mainly cytoplasmic with perinuclear enrichment and localizes to mitotic structures including the midbody and spindle apparatus, where it colocalizes with beta-tubulin (TUBB) and partially overlaps Aurora B (AURKB). Loss of TTC28 increases micronuclei frequency and DNA-damage markers (gamma-H2AX, comet assay), and TTC28 is frequently mutated/down-regulated in cancers where its loss may contribute to chromosomal instability (CIN).
- Existing/core annotation action counts: ACCEPT: 7; KEEP_AS_NON_CORE: 2; NEW: 4

## PN Consistency Summary

- **Consistency:** Priority-only record; no phase-1 dossier section exists yet. Local review status is `local_review_complete_not_phase1`. PN placement: Cytonuclear proteostasis > Chaperone > HSP70-HSP90 system integration > HSP70-HSP90 joint cochaperone > TPR domain containing. Main issue: Review supports HSPA8-mediated CMA/microautophagy substrate biology and mitotic scaffold function, not HSP90 cochaperone propagation
- **PN story / NEW pressure:** No current projected GO row; the value is exception/context tracking.
- **Mapping strategy:** Do not propagate generic HSP90-cochaperone semantics from a TPR-domain placement when the reviewed biology points to a different mechanism.
- **Verdict:** Record HSP90-cochaperone exception and preserve CMA-substrate versus core-mitosis distinction

## Priority Review Context

- Category: cc_tpr_exception
- PN annotations: Cytonuclear proteostasis > Chaperone > HSP70-HSP90 system integration > HSP70-HSP90 joint cochaperone > TPR domain containing
- Why interesting: Review supports HSPA8-mediated CMA/microautophagy substrate biology and mitotic scaffold function, not HSP90 cochaperone propagation
- Suggested next step: Record HSP90-cochaperone exception and preserve CMA-substrate versus core-mitosis distinction
- Related project: not_recorded

## PN Projection Rows

- No current PN projected GO row for this gene. Treat this priority item as an exception, boundary, or context-tracking case rather than a direct GO propagation candidate.

## PN Dossier Context

No phase-1 dossier exists for this priority-only gene. This note preserves the current PROTEOSTASIS boundary or exception decision and should be superseded by a dossier section if the gene is promoted into a full phase-1 batch.

## Note

This file is generated from the current PROTEOSTASIS priority table, PN projection outputs, and local gene-review artifacts. Edit those source records rather than this generated note when correcting the underlying curation.
