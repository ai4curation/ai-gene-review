# SPA2 notes

## 2026-09-29 IBA propagation rereview

- Checked all ten SPA2 IBA rows against GOA and the current `PTHR21601` PAINT cache.
- Six 2017 rows still trace cleanly to `PANTHER:PTN001091461`: incipient bud site,
  cellular bud tip, cellular bud neck, bipolar bud site selection, pseudohyphal
  growth, and invasive filamentous growth.
- Two 2017 rows now have stale GOA PTNs but matching current PAINT assertions. The
  MAP-kinase scaffold row points to old `PTN000492368` in GOA and mating projection
  tip points to old `PTN001091461`; current PAINT now places both at
  `PTN004550576` with a 2026-06-03 date.
- Two 2017 rows point to `PANTHER:PTN001091460`, which is absent from the current
  PAINT export. `GO:0005826 actomyosin contractile ring` remains a stale/unsupported
  over-transfer and should be removed; `GO:1902716 cell cortex of growing cell tip`
  remains biologically true but no longer has a current PAINT source.
- Cached and read PMID:38802374, the 2024 Nature Communications paper reporting that
  S. cerevisiae Spa2 remodels ADP-actin under glucose starvation. This supports the
  existing actin-cytoskeleton interpretation; no new GO term was needed because the
  review already carries `GO:0032956 regulation of actin cytoskeleton organization`.
- Cached and read PMID:40931936, a 2025 Journal of Cell Science paper on
  Schizosaccharomyces pombe Spa2. It supports a conserved cortical growth-zone
  focusing role and emphasizes species-specific Spa2 interaction networks, which
  reinforces caution around old cross-species CC propagation to the contractile ring.
- Searched 2025-2026 PubMed and broader web results for newer S. cerevisiae SPA2
  papers; no direct budding-yeast paper newer than the cached 2024 ADP-actin study
  changed the review.
