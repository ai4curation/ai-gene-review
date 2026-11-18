# MSLN curation notes

Deep research (falcon/perplexity-lite) unavailable; notes from UniProt Q13421 and cached papers.

- Precursor (622 aa) -> furin cleavage -> secreted MPF (37-286) + GPI-anchored mesothelin (296-598)
  (UniProt PTM, PMID:8552591).
- Surface/GPI: [PMID:8552591 "the antigen was found on the cell surface and could be released by treatment with phosphatidylinositol-specific phospholipase C"].
- CA125/MUC16 binding mediates heterotypic adhesion [PMID:14676194 "Binding of CA125 to membrane-bound mesothelin mediates heterotypic cell adhesion"].
- MPF secreted, elevated in mesothelioma serum (PMID:16857795); MPF activity (PMID:7665620).
- N-terminal fragment structure with MORAb-009 overlapping CA125 footprint (PMID:22787150).

Localization conclusion: PM outer leaflet (GPI-anchored), mature ectodomain fully extracellular and
surface-accessible; shed/soluble and MPF pools extracellular; ER/Golgi only in transit.

## 2026-11-18 ORGANELLES Golgi batch 3 (Golgi apparatus rows)

- One GO:0005794 row: IEA GO_REF:0000044 (UniProtKB-SubCell SL-0132), `located_in`. Changed
  KEEP_AS_NON_CORE -> MARK_AS_OVER_ANNOTATED.
- Check: the UniProt location item "Golgi apparatus" has no ECO tag (uncited assertion). UniProt cites
  PMID:8552591 (cloning; abstract reports PI-PLC-releasable surface antigen) and PMID:22787150
  (MORAb-009 crystal structure) for subcellular location; both are abstract-only in the cache.
  PMC full texts requested 2026-11-18: PMC40193 (DOI 10.1073/pnas.93.1.136) and PMC3460419 (DOI
  10.1074/jbc.M112.381756) returned only front matter from NCBI efetch, and Europe PMC returned HTTP
  500, so no body text was read. No paper with a Golgi marker or brefeldin A on mesothelin was found;
  HPA annotates plasma membrane. A GPI-anchored, furin-processed protein transits the Golgi, but under
  the transit rule a row resting only on transit is MARK_AS_OVER_ANNOTATED (consistent with the ER
  lumen row). UNDECIDED was the close alternative because PMID:22787150 was not read.
