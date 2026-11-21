# phy-2 notes

## 2026-11-21

- Seeded the review with `just fetch-gene worm phy-2`; this fetched the
  reviewed UniProtKB Q20065 record, 11 GOA rows, two PMID caches used by seeded
  annotations, and the local PTHR10869 PANTHER cache.
- `just deep-research-falcon worm phy-2 --fallback perplexity-lite` failed
  because Falcon was not configured and the Perplexity Lite fallback mapped to
  an unavailable Perplexity provider. No provider deep-research file was
  written; this notes file records the manual evidence pass.
- `just mod-description-deep-research worm phy-2` fetched the WormBase
  hand-written gene description as `phy-2-deep-research-wormbase.md`. The
  cuticle-collagen, phy-1/phy-2 redundancy, and cyclic hypodermal expression
  claims trace to the cached primary literature; the excretory-cell and
  spermatheca expression claims were not traced in this pass.
- `just paint-losses worm phy-2` reported no IRD or IKR loss on the Q20065
  lineage. The PTHR10869 `PTHR10869-paint.tsv` cache places
  procollagen-proline 4-dioxygenase activity and complex membership on
  PTN000852959.
- The core PHY-2 role is ER-lumen procollagen prolyl 4-hydroxylation.
  Myllyharju et al. showed that PHY-2 assembles with PDI-2 in vivo as a
  PHY-2/PDI-2 dimer and in the main mixed PHY-1/PHY-2/(PDI-2)2 form, while
  Winter and Page showed that the two conserved phy alpha genes and pdi-2 are
  expressed cyclically in cuticle-synthesizing hypodermis and that combined
  disruption of the two phy genes blocks embryonic development.
- Added a conservative direct `collagen and cuticulin-based cuticle
  development` row for the PHY-2 catalytic step in cuticle procollagen
  hydroxylation. No direct molting-cycle, hatching or body-morphogenesis row
  was proposed because the phy-2 single mutant is buffered by the DPY-18/PHY-1
  paralog and the seeded GOA rows do not contain direct process annotations.
