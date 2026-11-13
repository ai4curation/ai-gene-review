# ACIAD0131 (KgsD) curation notes

- Deep research: `just deep-research-falcon ACIAD ACIAD0131` failed on
  2026-11-11 (Edison API returned 403 "Failed to authenticate"). No provider
  file was written.
- Q6FFQ0 is the A. baylyi ADP1 alpha-ketoglutaric semialdehyde dehydrogenase
  of the alternative D-glucarate pathway [PMID:18364348, "We describe here the
  kinetic characterization of D-glucarate dehydratase, d-5-keto-4-deoxyglucarate
  dehydratase, and of cooperative alpha-ketoglutarate semialdehyde
  dehydrogenase."]. Only the abstract is cached; the full text (PMC3259651)
  was not retrieved.
- In the hydroxyproline-catabolism module it represents the terminal reaction
  (2,5-dioxopentanoate to 2-oxoglutarate, Rhea 11296), which is shared with
  hydroxyproline catabolism. Its own physiological pathway is D-glucarate
  degradation, and nothing shows a role in hydroxyproline catabolism in ADP1.
  For that reason the module lists it only as a characterized exemplar of the
  reaction, not of the hydroxyproline process.
- The broad IEA MF rows are changed (MODIFY) to GO:0047533. The UniProt
  FUNCTION comment says "D-glutarate", which looks like a typo for
  D-glucarate; it is recorded as a UniProt source defect.
- PANTHER PTHR43353:SF3, the same subfamily as KT2440 PP_1256.
