# pdi-2 notes

## 2026-11-21

- Seeded the review with `just fetch-gene worm pdi-2`; this fetched the
  reviewed UniProtKB Q17770 record, 17 GOA rows, the local PTHR18929 PANTHER
  cache, and six PMID caches used by seeded annotations.
- `just deep-research-falcon worm pdi-2 --fallback perplexity-lite` failed
  because Falcon was not configured and the Perplexity Lite fallback mapped to
  an unavailable Perplexity provider. No provider deep-research file was
  written; this notes file records the manual evidence pass.
- `just mod-description-deep-research worm pdi-2` fetched the WormBase
  hand-written gene description as `pdi-2-deep-research-wormbase.md`. The core
  claims on PDI/beta function, ER oxidative folding, ER-stress induction, and
  hypodermal expression trace to cached primary literature. The WormBase
  claims that PDI-2 is required for locomotion, fertility and molting were not
  traced in this pass.
- `just paint-losses worm pdi-2` reported no IRD or IKR loss on the Q17770
  lineage. The PTHR18929 `PTHR18929-paint.tsv` cache places protein disulfide
  isomerase activity, endoplasmic reticulum localization, protein folding, and
  response to ER stress on PTN000432607.
- The core PDI-2 role is ER-lumen protein disulfide isomerase activity plus
  procollagen-proline 4-dioxygenase beta-subunit function. Karala et al.
  assayed PDI-2 thiol-disulfide exchange activity directly, while Veijola et
  al., Winter and Page, and Myllyharju et al. established PDI-2 as the beta
  subunit used in C. elegans collagen P4H complexes.
- Added a direct `collagen and cuticulin-based cuticle development` row for
  PDI-2. pdi-2 RNAi causes post-elongation lethality after the first
  collagenous cuticle forms, and the PDI-2 beta subunit performs real work in
  the ER collagen P4H complexes that modify nascent cuticle procollagens. I
  did not add a de novo `embryo development ending in birth or egg hatching`
  row: hatching failure is well supported, but the more precise cuticle
  development term captures the direct work PDI-2 performs.
- Kept the PTHR18929 `response to endoplasmic reticulum stress` row as
  non-core and marked the HEP `IRE1-mediated unfolded protein response` row as
  over-annotated. Urano et al. showed C07A12.4/pdi-2 induction by tunicamycin
  in an xbp-1-attenuated expression program; that supports PDI-2 as an ER
  stress target, not as an IRE1-mediated UPR signaling component.
- Left the `protein-glutamine gamma-glutamyltransferase activity` rows
  undecided. The cached PMID:12424233 abstract is explicitly about PDI-3, but
  full text would be needed before deciding whether WormBase's PDI-2 row is a
  curatable secondary activity or an upstream reference/gene mix-up.
