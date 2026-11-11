# rfbB (E. coli K-12) curation notes

## 2026-11-10 review (dTDP-L-rhamnose biosynthesis module)

- Reviewed every GOA row against the cached publications and the UniProt record.
  Deep-research generation was not run (no provider API keys in this session); the
  review rests on UniProt curated text, cached abstracts/full texts and PANTHER/PAINT files.
- Consistent treatment across the four rfb-cluster genes (rfbA/B/C/D):
  core MF and GO:0019305 ACCEPT; cytosol ACCEPT; polymer-level processes
  (GO:0000271, GO:0009103, GO:0009243) MARK_AS_OVER_ANNOTATED, because these enzymes make
  the soluble dTDP-L-rhamnose donor and form no glycosidic bond; the polymer is assembled by
  glycosyltransferases
  [PMID:7517391 "the rhamnose transferase gene is identified by assay of its product"].
  This follows the project decision for the PSEPK RmlC paralogs in
  projects/TREEGRAFTER/rereview-2026-09-24/batch-07.yaml.
- Most K-12 lines are O-antigen negative (rfb-50/rfb-51)
  [PMID:7512872 "the rough phenotype of this strain is due to the presence of one of two independent mutations in the rfb gene cluster"].

## Review follow-up (2026-11-11, PR #6252)

- involved_in polymer-level rows (GO:0000271, GO:0009103, GO:0009243) stay
  MARK_AS_OVER_ANNOTATED: involved_in claims participation, and these enzymes only supply the
  dTDP-L-rhamnose donor.
- GO:0009225 (IEA, InterPro2GO) is MODIFY to GO:0019305, but its descendant GO:0009226 (IDA,
  PMID:14235522) is KEEP_AS_NON_CORE. This is deliberate. The 1964 paper, judged from its title
  only (no cached abstract), concerns dTDP-4-acetamido-4,6-dideoxyhexoses, which branch from the
  same dehydratase product. The generic biosynthetic term therefore carries information that
  GO:0019305 does not. The InterPro mapping has no such context, so it is refined to the
  documented rhamnose pathway.
- PMID:4307450 purified the enzyme from E. coli B, so the purified enzyme could be the RfbB
  ortholog or RffG; recorded in its reference_review.
