# gcy-18 notes

## Session 2026-10-08 (claude-code)

Deep research: `just deep-research-falcon worm gcy-18 --fallback perplexity-lite` failed
(falcon killed at the 600 s timeout; perplexity provider not available in this environment).
No deep-research file was created. Review based on cached publications in `publications/`,
the UniProt record, and GOA.

Annotation actions: {'MARK_AS_OVER_ANNOTATED': 1, 'ACCEPT': 20, 'REMOVE': 1, 'KEEP_AS_NON_CORE': 7}

Key evidence:
- AFD-specific; primary AFD cyclase at 20-25 C [PMID:16415369 "suggesting that gcy-18 functions as the primary guanylyl cyclase in these temperature ranges"]
- Sets Tc memory/operating range; lowers T*AFD [PMID:21315599 "Consistent with a larger downward shift in Tc memory of gcy-18 mutants grown at 20°C, the T*AFD in their AFD neurons was also significantly lower"]
- Microvillar localization of thermosensory GCs requires BBS-8/DAF-25 [PMID:25335890 "requires BBS-8 and DAF-25 (known as Ankmy2 in mammals) for correct localization of guanylyl cyclases needed for thermosensation"]
- Protein kinase activity IEA REMOVED (pseudokinase); peptide receptor IBA over-annotated.
