# CRYAA PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: priority-only PN rereview against local AIGR review and available deep-research artifacts
- UniProt: P02489
- AIGR review status: COMPLETE
- Priority category: ontology_gap_bridge
- Local AIGR project status: local_review_complete_not_phase1
- Related project: UNFOLDED_PROTEIN_BINDING.md

## Source Files Checked

- AIGR review YAML: present - [genes/human/CRYAA/CRYAA-ai-review.yaml](CRYAA-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CRYAA/CRYAA-ai-review.html](CRYAA-ai-review.html)
- Gene notes: present - [genes/human/CRYAA/CRYAA-notes.md](CRYAA-notes.md)
- GOA TSV: present - [genes/human/CRYAA/CRYAA-goa.tsv](CRYAA-goa.tsv)
- UniProt record: present - [genes/human/CRYAA/CRYAA-uniprot.txt](CRYAA-uniprot.txt)
- PROTEOSTASIS priority table: [projects/PROTEOSTASIS/priority_genes.tsv](../../../projects/PROTEOSTASIS/priority_genes.tsv)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)
- PN mapping file: [projects/PROTEOSTASIS/mappings/chaperone_systems.yaml](../../../projects/PROTEOSTASIS/mappings/chaperone_systems.yaml)

### Deep Research Files

- [genes/human/CRYAA/CRYAA-deep-research-falcon.md](CRYAA-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: Alpha-crystallin A chain (CRYAA/HSPB4) is a member of the small heat shock protein (sHSP) family that serves dual roles as a major structural component of the ocular lens and as a molecular chaperone with holdase activity. CRYAA forms large oligomeric complexes (approximately 540 kDa) that suppress nonspecific aggregation of destabilized proteins under stress conditions including heat, UV irradiation, and chemical modification (PMID:8943244). Critically, CRYAA acts as a holdase rather than a foldase -- it prevents aggregation of partially unfolded proteins but does NOT actively refold them (as documented by the NOT annotation to GO:0042026 protein refolding, ISS from bovine ortholog). CRYAA hetero-oligomerizes with CRYAB (HSPB5) and contributes to lens transparency and refractive index. Post-translational modifications including phosphorylation at T148 (mediated by mTORC2) regulate chaperone capacity. Mutations in CRYAA (e.g., R116H, R116C) cause autosomal dominant congenital cataracts through loss of chaperone activity and increased protein aggregation (PMID:18407550). CRYAA also has anti-apoptotic activity, binding and sequestering pro-apoptotic Bax and Bcl-X(S) proteins (PMID:14752512).
- Existing/core annotation action counts: ACCEPT: 20; KEEP_AS_NON_CORE: 9; MARK_AS_OVER_ANNOTATED: 15; MODIFY: 9; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Priority-only record; no phase-1 dossier section exists yet. Local review status is `local_review_complete_not_phase1`. PN placement: Cytonuclear proteostasis > Chaperone > small HSP system > small HSP. Main issue: Positive control where PN placement and UPB holdase logic strongly converge
- **PN story / NEW pressure:** Current projection rows: GO:0044183 protein folding chaperone (new_to_goa).
- **Mapping strategy:** Use as a bridge case for ontology design: the PN placement may expose missing or underspecified GO proteostasis terms rather than a simple gene-to-existing-term propagation.
- **Verdict:** Create bridge dossier for small-HSP holdase/foldase ontology-gap analysis

## Priority Review Context

- Category: ontology_gap_bridge
- PN annotations: Cytonuclear proteostasis > Chaperone > small HSP system > small HSP
- Why interesting: Positive control where PN placement and UPB holdase logic strongly converge
- Suggested next step: Create bridge dossier for small-HSP holdase/foldase ontology-gap analysis
- Related project: UNFOLDED_PROTEIN_BINDING.md

## PN Projection Rows

- GO:0044183 protein folding chaperone - new_to_goa; scope=ok_for_propagation_to_go; mapping=chaperone_systems.yaml; PN=Cytonuclear proteostasis|Chaperone|small HSP system|small HSP

## PN Dossier Context

No phase-1 dossier exists for this priority-only gene. This note preserves the current PROTEOSTASIS boundary or exception decision and should be superseded by a dossier section if the gene is promoted into a full phase-1 batch.

## Note

This file is generated from the current PROTEOSTASIS priority table, PN projection outputs, and local gene-review artifacts. Edit those source records rather than this generated note when correcting the underlying curation.
