# GALK2 notes

## 2026-11-24

- `just fetch-gene human GALK2` returned 17 GOA rows plus the header, so the GOA cache was a real fetch rather than a header-only file.
- Deep research via `just deep-research-falcon human GALK2 --fallback perplexity-lite` failed because the configured Falcon and Perplexity providers are unavailable in this checkout. This review therefore uses the local UniProt record, GOA, PAINT data and cached PubMed abstracts directly.
- Human GALK2 is the chromosome-15 `GK2` sequence that was first cloned by yeast complementation and then reidentified as GalNAc kinase. The most direct GalNAc evidence is PMID:8798585, which reports that chromosome-15 GK2 is GalNAc kinase, and PMID:16006554, which solved the human GalNAc kinase structure with GalNAc and nucleotide or product in the active site.
- The galactokinase rows are kept as `MARK_AS_OVER_ANNOTATED`, not `REMOVE`: PMID:8798585 says GalNAc kinase can also phosphorylate galactose at millimolar sugar concentrations, so the activity is not fictitious, but PMID:7542884 and PMID:16006554 separate GALK2 from GALK1 and show that GalNAc is the preferred substrate.
- The existing `modules/galactose_leloir_pathway.yaml` should stay GALK1-specific. GALK2 is not established as a Leloir-pathway galactokinase, and a single GalNAc kinase reaction is too small for a standalone module.
- `gocams/index.tsv` has no human GALK2 activity. No production GO-CAM covering a human GALK2 GalNAc-salvage role is cached.
