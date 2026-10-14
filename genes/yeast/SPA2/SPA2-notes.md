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

## 2026-10-10 PTHR21601 family pass: bring review to COMPLETE

- Removed stray files from an earlier session (`CURATION-INDEX.txt`, `CURATION-SUMMARY.md`,
  `README-CURATION.md`, `SPA2-CURATION-ANALYSIS.md`, `SPA2-REVIEW-COMPLETE.md`,
  `SPA2-ai-review-UPDATED.yaml`, `update_annotations.py`). They had been tracked in git since
  commit dccca414ec. Their content duplicated decisions already in `SPA2-ai-review.yaml`
  (GO:0005515 rows removed, contractile-ring IBA removed, filamentous growth and stress
  responses kept as non-core). The only extra item was a citation, PMID:9790978, attached to the
  contractile-ring removal; it was never verified, so it was not carried forward.
- MAP kinase scaffold activity (GO:0005078) is correct and core for S. cerevisiae Spa2
  [PMID:12361575 "Spa2p functions as a scaffold-like protein to recruit the Mpk1p MAP kinase
  module to sites of polarized growth"]. The motif-level basis is now known
  [PMID:41527849 "We identified a conserved short linear motif in the Rab GTPase-activating
  proteins (RabGAPs) Msb3 and Msb4, and the MAP kinase kinases Ste7 and Mkk1, which mediates
  their interaction with Spa2."].
- The current PAINT IBD for GO:0005078 sits on the Eukaryota root node PTN004550576 with SPA2 as
  its only seed. That is too deep: S. pombe Spa2 has negative data
  [PMID:25428987 "We did not detect physical or genetic interactions between Spa2 and the S.
  pombe homologues of Bni1, Bud6, or MAP kinases"]. The node should probably be moved down to
  the Saccharomycetaceae Spa2/Sph1 clade. Sph1 binds Mkk1/Mkk2/Ste7 by two-hybrid
  [PMID:9443897].
- Added a NEW GO:0030674 protein-macromolecule adaptor activity row so the existing second core
  function is reflected in existing_annotations. Support: Aip5 localization
  [PMID:31362951 "Both interactions collaborate to localize Aip5 at bud tip and neck, and are
  required to stimulate the formation of actin cables."] and Msb3/Msb4 binding [PMID:16166638].
  The S. pombe ortholog already carries this term by PomBase EXP (PMID:40931936).
- Corrected the description: SPA2 is nonessential (deletion is viable; PMID:9214378), so
  "essential for" was replaced with "required for normal".
- Status DRAFT -> COMPLETE. Companion reviews from the same pass: `genes/yeast/SPH1`,
  `genes/SCHPO/spa2`.
