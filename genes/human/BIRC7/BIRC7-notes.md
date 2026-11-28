# BIRC7 manual curation notes

## 2026-11-27 PTHR10044 family review

- Reviewed BIRC7 as the PTHR10044:SF163 human member, alongside BIRC8/SF167 and the
  already-curated XIAP review. `just deep-research-falcon human BIRC7 --fallback
  perplexity-lite` could not run in this environment because those providers were not
  installed; no provider-branded deep-research file was fabricated.
- BIRC7/Livin has two separable core activities. PMID:11024045 reports direct binding
  to active caspases 3 and 7 and coimmunoprecipitation of unprocessed and cleaved
  caspase 9 with Livin; PMID:16729033 reports RING-dependent autoubiquitination and
  ubiquitination of DIABLO/SMAC. The generic GO:0004842 row is therefore narrowed to
  GO:0061630, and the direct CASP9 and DIABLO protein-binding rows are decomposed to
  the supported caspase-inhibitor or E3-ligase activities.
- Most IntAct `GO:0005515 protein binding` rows are removed under the project bare-binding
  policy. The review keeps one existing row per GOA line and cites the row's interacting
  partner from the current UniProt interaction block where the underlying interaction
  itself is not disputed.
- The direct TNF/JNK rows from PMID:11865055 are kept: dominant-negative JNK1 or TAK1
  interfered with ML-IAP protection from TNF- and ICE/caspase-1-triggered death. This is
  distinct from BIRC8/ILP-2, which the founding paper reported did not protect from TNF
  or Fas.
- Full-length BIRC7 is cytoplasmic, while caspase-cleaved tLivin localizes to the Golgi
  region and can be pro-apoptotic (PMID:17294084). Nuclear and Golgi rows are retained
  as contextual locations, while the cytoplasmic/cytosolic rows capture the main
  anti-apoptotic protein pool.
- The broad PAINT cell-cycle row at PTN000005168 was marked over-annotated for BIRC7:
  the BIRC7 literature and the reviewed human rows support apoptosis regulation,
  TAK1/JNK protection and RING E3 activity, not a direct cell-cycle regulatory step.
