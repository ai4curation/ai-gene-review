# FVE / MSI4 (At2g19520, UniProt O22607) curation notes

## 2026-10 review session (autonomous pathway module)

- Accession verified: O22607 MSI4_ARATH; UniProt primary name MSI4, synonyms FVE, ACG1. Folder uses the flowering-pathway symbol FVE (gene_symbol FVE in stub).
- Deep research (falcon) failed (HTTP 402).
- RbAp48-like WD40 protein; FLC chromatin hyperacetylated in fve [PMID:14745447 "We conclude that FVE participates in a protein complex repressing FLC transcription through a histone deacetylation mechanism."]
- CUL4-DDB1 and CLF-PRC2 [PMID:21282611 "the MSI4 protein is a DDB1 and CUL4-associated factor that represses FLC expression through its association with a CLF-Polycomb Repressive Complex 2 (PRC2)"]
- PDP/LHP1 PRC2 [PMID:29314758 "We demonstrated that FVE, MSI5, and PDP3 were co-purified with LHP1."]
- HDA5/HDA6/FLD complex [PMID:25922987].
- RdDM via SUVH9 [PMID:33942410]; cold-response repressor (acg1) [PMID:14745450].

## Decisions
- Core: histone binding (IBA) in PRC2 (ESC/E(Z) complex) and HDAC complexes.
- 12 bare protein-binding rows removed (complex memberships captured by CC terms).
- Metal ion binding -> zinc ion binding (non-core).
- Photoperiodism flowering term -> GO:0048510.
