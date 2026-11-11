# vha-19 review notes

## 2026-10-28 initial review

- Fetched Q9TYW1 (VAS1_CAEEL); 7 GOA rows (2 IBA, 1 IEA, 3 IMP from PMID:22768351, 1 HDA
  from PMID:21070894).
- Deep research providers unavailable; manual survey in vha-19-deep-research-manual.md.
- Key paper PMID:22768351 read in full. All three IMP rows derive from RNAi phenotypes:
  - GO:0090314 positive regulation of protein targeting to membrane: RME-2::GFP fails to
    reach the oocyte plasma membrane and accumulates in perinuclear Golgi-like aggregates
    [PMID:22768351 "the majority of RME-2::GFP aggregated around the nucleus of
    vha-19(RNAi) oocytes and did not reach the plasma membrane"]. Direct assay of a cargo
    trafficking step; kept as non-core because the most parsimonious mechanism is a
    general V-ATPase/secretory-pathway pH requirement rather than a dedicated targeting role.
  - GO:0060282 positive regulation of oocyte development: based on fewer and endomitotic
    oocytes. The "regulation" framing over-interprets a pleiotropic requirement;
    marked over-annotated, not removed.
  - GO:0009992 intracellular water homeostasis: embryos swell/shrink abnormally; the
    authors attribute this to a defective eggshell. Kept as non-core.
- No worm experiment shows VHA-19 binding the V-ATPase; complex membership rests on
  family membership (Ac45/ATP6AP1, PTHR12471) and the PAINT IBA, with strong mammalian
  structural evidence for the ortholog [PMID:33065002 "ATP6AP1 as a structural hub for Vo
  complex assembly"].
- No NEW terms proposed: the remaining process data are RNAi necessity phenotypes
  (embryo development, larval development, eggshell formation) that fail the NEW bar.
- Kanaki 2019 (PMID:30445613): vha-19 RNAi phenocopies the N-glycosylation enzyme
  algn-7, consistent with an ATP6AP1-CDG-like Golgi glycosylation role.
