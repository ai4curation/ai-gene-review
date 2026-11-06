# SEC2 notes

## PTHR14430 / Sec2 review, 2026-11-06

- `CANAL/SEC2` was fetched with the explicit UniProt accession `Q5AL49` after
  symbol lookup timed out for the CGD entry.
- A manual newer-paper search for `Candida albicans SEC2/Sec2` after the 2014
  SEC2 mRNA paper did not recover a newer direct Sec2 functional study. The
  post-2014 hits were broad Candida hyphal-growth, Spitzenkorper, and mRNA
  hitchhiking reviews or pathway-level polarized-secretion studies, so the
  review stays anchored to the two direct cached papers already in GOA.
- PANTHER `PTHR14430` is the Sec2/Rabin3 Rab GEF family. `Q5AL49` is a
  full-length fungal `PTHR14430:SF0` Sec2 member like budding-yeast Sec2 and
  fission-yeast Sec2, not the short meiotic `spo13` paralog.
- The `GO:0005085` GEF IBA from Opisthokonta `PANTHER:PTN000374167` is a
  sound transfer to C. albicans Sec2; the UniProt record and Caballero-Lima et
  al. 2014 both describe Sec2p as the GEF for the Sec4 Rab.
- The fungal `GO:0051286` cell-tip IBA from `PANTHER:PTN001024876` is sound
  for Candida. The target is one of PAINT's direct experimental seeds via the
  CGD row, and Bishop et al. 2010 directly localized functional Sec2-YFP to the
  Spitzenkorper at hyphal tips.
- Bishop et al. 2010 showed morphology-dependent Sec2 localization: the
  cytokinetic ring at the mother-bud neck in yeast-form cells, a surface
  crescent at pseudohyphal tips, and an FM4-64-marked Spitzenkorper in true
  hyphae. The same paper showed that S584 phosphorylation by a Cdc28-dependent
  route is required to sustain normal hyphal growth.
- Caballero-Lima et al. 2014 showed that SEC2 mRNA binds Sec2p and
  cofractionates with secretory vesicles in hyphal cells, directly supporting
  CGD's `GO:0070319` Golgi-to-plasma-membrane transport vesicle row.
- The same Caballero-Lima paper directly supports a new
  `GO:0003729 mRNA binding` assertion: SEC2 mRNA is enriched in Sec2p RIPs and
  Sec2p cross-links to oligo-dT-purified mRNA. This is left out of
  `core_functions` because the paper leaves the downstream role of that binding
  unresolved between translational autoregulation, reinforcing Spitzenkorper
  localization, and allowing Sec2 recycling from vesicles back to the Golgi.
