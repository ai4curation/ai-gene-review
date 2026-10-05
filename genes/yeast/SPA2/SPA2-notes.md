# SPA2 notes

## 2026-09-29 IBA propagation rereview

- Checked all ten SPA2 IBA rows against GOA and the current `PTHR21601` PAINT cache.
- Six 2017 rows still trace cleanly to `PANTHER:PTN001091461`: incipient bud site,
  cellular bud tip, cellular bud neck, bipolar bud site selection, pseudohyphal
  growth, and invasive filamentous growth.
- Two 2017 rows now have stale GOA PTNs but matching current PAINT assertions. The
  MAP kinase scaffold row points to old `PTN000492368` in GOA and mating projection
  tip points to old `PTN001091461`; current PAINT now places both at the broad
  Eukaryota node `PTN004550576` with a 2026-06-03 date.
- Two 2017 rows point to `PANTHER:PTN001091460`, which is absent from the current
  PAINT export. `GO:0005826 actomyosin contractile ring` remains an incorrect
  cross-species transfer from fission-yeast Spa2 to budding-yeast Spa2 and should
  be removed; `GO:1902716 cell cortex of growing cell tip` should be modified to
  the existing direct `GO:0005934 cellular bud tip` and `GO:0005938 cell cortex`
  rows.
- Current `PTN004550576` carries five IBDs: the S. cerevisiae-seeded
  `GO:0043332` and `GO:0005078`, the PomBase-only `GO:0120105 mitotic actomyosin
  contractile ring, intermediate layer`, and broader `GO:0008104` and
  `GO:0030010` process assertions. The PomBase-only GO:0120105 row is a live
  fission-yeast ring assertion, not a live successor for the old S. cerevisiae
  `GO:1902716` row, and should be narrowed away from budding yeast if the
  current Eukaryota placement would export to S. cerevisiae SPA2.
- Cached and read PMID:38802374, the 2024 Nature Communications paper reporting that
  S. cerevisiae Spa2 remodels ADP-actin under glucose starvation. This supports the
  existing actin-cytoskeleton interpretation; no new GO term was needed because the
  review already carries `GO:0032956 regulation of actin cytoskeleton organization`.
- Cached and read PMID:40931936, a 2025 Journal of Cell Science paper on
  Schizosaccharomyces pombe Spa2. It supports a conserved cortical growth-zone
  focusing role and emphasizes species-specific Spa2 interaction networks, which
  reinforces caution around old cross-species CC propagation from PomBase Spa2 to
  S. cerevisiae-specific polarisome locations.
- Re-fetched `PTHR21601` on 2026-10-01. GOA now reports the live S. pombe-derived
  `GO:0120105` row from `PANTHER:PTN001091459`, while the current local PAINT TSV
  has the same PomBase-only IBD on `PTN004550576`; the GOA source was preserved
  exactly and the PAINT node drift was recorded in the row-level `propagation_review`.
- Searched 2025-2026 PubMed and broader web results for newer S. cerevisiae SPA2
  papers. The newly indexed PMID:41527849 full text identifies a Spa2 SHD1-binding
  short linear motif in Msb3, Msb4, Ste7 and Mkk1 and identifies Dse3 as a new
  Spa2-binding partner, which refines the scaffold mechanism without changing the
  GO surface.
- During PR review, cached and read PMID:31699995 from the refreshed UniProt
  record and PMID:29601579 for Foltman et al.'s budding-yeast division-site
  counterexample. The Spa2/Aip5 papers support a second core Spa2 adaptor activity
  in polarisome actin assembly, while Foltman supports a budding-yeast Chs2/IPCs
  role that still does not rescue the fission-yeast GO:0120105 contractile-ring
  intermediate-layer IBA.
