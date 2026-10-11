# gcy-23 notes

## Session 2026-10-08 (claude-code)

Deep research: `just deep-research-falcon worm gcy-23 --fallback perplexity-lite` failed
(falcon killed at the 600 s timeout; perplexity provider not available in this environment).
No deep-research file was created. Review based on cached publications in `publications/`,
the UniProt record, and GOA.

Annotation actions: {'MARK_AS_OVER_ANNOTATED': 1, 'ACCEPT': 21, 'REMOVE': 1, 'KEEP_AS_NON_CORE': 7}

Key evidence:
- AFD-specific; modulatory, redundant [PMID:16415369 "The thermotaxis mutant phenotype of the gcy triple-mutant strain was rescued by expression of any one of the three GCY proteins"]
- Single mutant alters IT range but not AFD response threshold [PMID:21315599 "Mutations in gcy-23 affect the temperature range of IT behavior without affecting T*AFD"]. The IMP detection-of-temperature row was accepted with a caveat (redundant contribution).
- Protein kinase activity IEA REMOVED (pseudokinase); peptide receptor IBA over-annotated.
