# SSR2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: priority-only PN rereview against local AIGR review and available deep-research artifacts
- UniProt: P43308
- AIGR review status: COMPLETE
- Priority category: positive_control
- Local AIGR project status: local_review_complete_not_phase1
- Related project: ER_PHAGY.md

## Source Files Checked

- AIGR review YAML: present - [genes/human/SSR2/SSR2-ai-review.yaml](SSR2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/SSR2/SSR2-ai-review.html](SSR2-ai-review.html)
- Gene notes: present - [genes/human/SSR2/SSR2-notes.md](SSR2-notes.md)
- GOA TSV: present - [genes/human/SSR2/SSR2-goa.tsv](SSR2-goa.tsv)
- UniProt record: present - [genes/human/SSR2/SSR2-uniprot.txt](SSR2-uniprot.txt)
- PROTEOSTASIS priority table: [projects/PROTEOSTASIS/priority_genes.tsv](../../../projects/PROTEOSTASIS/priority_genes.tsv)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)
- PN mapping file: [projects/PROTEOSTASIS/mappings/er_proteostasis.yaml](../../../projects/PROTEOSTASIS/mappings/er_proteostasis.yaml)

### Deep Research Files

- [genes/human/SSR2/SSR2-deep-research-falcon.md](SSR2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: SSR2 encodes the beta subunit of the translocon-associated protein (TRAP) complex, also known as signal sequence receptor subunit beta (SSR-beta/TRAP-beta). TRAP is a heterotetrameric complex (SSR1/alpha, SSR2/beta, SSR3/gamma, SSR4/delta) that associates with the Sec61 translocon at the endoplasmic reticulum membrane. The complex assists in co-translational protein translocation, particularly for nascent polypeptides with weak or suboptimal signal peptides. SSR2/TRAP-beta is a type I single-pass membrane glycoprotein with its N-terminus facing the ER lumen, where it contributes to the lumenal crescent structure that contacts nascent chains exiting the Sec61 pore. The TRAP complex also coordinates with the oligosaccharyltransferase (OST) complex to facilitate N-glycosylation of nascent proteins. SSR2 was identified as a STING1 interactor in a yeast-two-hybrid screen (PMID:18724357), but the biological significance of this interaction is uncertain; it likely reflects proximity at the ER membrane rather than a dedicated immune-signaling function.
- Existing/core annotation action counts: ACCEPT: 5; MARK_AS_OVER_ANNOTATED: 3; NEW: 1; REMOVE: 1

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
