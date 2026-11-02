# MKC1 curation notes

## 2026-11-01

- Fetched the `CANAL/MKC1` review, GOA, UniProt record, nine cached GOA
  publications, and the local `PTHR24055` PAINT table as part of the fungal MAP
  kinase family review.
- Searched for newer Candida albicans `MKC1` literature. The main newer primary
  hit was Pang et al. 2025 [PMID:39688394], which places Sdd3 upstream of Rho1
  and the PKC-MAPK pathway that controls `CHS2`/`CHS8` expression and chitin
  abundance during biofilm formation. It corroborates the Mkc1 cell-wall/chitin
  model but does not create a distinct MKC1 annotation need. A 2026 pathogen-MAPK
  review was useful background only.
- Accepted the fungal `PANTHER:PTN001171896` transfer to
  `GO:0004707 MAP kinase activity`; MKC1 is one of the Candida seeds for that
  node and the original Navarro-Garcia et al. complementation paper confirms its
  Slt2-like MAPK function [PMID:7891715].
- Kept the broad `PANTHER:PTN000622075` nucleus and cytoplasm rows as non-core
  and modified its `GO:0035556 intracellular signal transduction` transfer to
  the more informative `GO:0000196 cell integrity MAPK cascade`.
- Accepted the direct Candida cell-wall rows. Navarro-Garcia et al. 1998 support
  Mkc1's role in cell-wall construction and morphologic transitions
  [PMID:9493378], Navarro-Garcia et al. 1995 support Slt2-pathway conservation
  and weak-wall phenotypes [PMID:7891715], and Roman et al. place Mkk2 upstream
  of Mkc1 during cell-wall stress and oxidative-stress signaling
  [PMID:26197240].
- Kept invasive growth, biofilm formation, heat, oxidative/nitric-oxide, and
  caspofungin/xenobiotic rows as non-core outputs. CGD curated these from direct
  Candida experimental papers; several caches are abstract-only, but the
  abstracts are consistent with a real MKC1 phenotype.
- Removed four EnsemblFungi transfers from fission-yeast Spm1/Pmk1:
  `GO:0050850 positive regulation of calcium-mediated signaling`,
  `GO:1902413 negative regulation of mitotic cytokinesis`, `GO:1902660
  negative regulation of glucose mediated signaling pathway`, and `GO:1905665
  positive regulation of calcium ion import across plasma membrane`. Those are
  source-side fission-yeast outputs, not conserved Candida Mkc1 functions.
