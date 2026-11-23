# dpy-18 notes

## 2026-11-21

- Seeded the review with `just fetch-gene worm dpy-18`; this fetched the
  reviewed UniProtKB Q10576 record, 18 GOA rows, the local PTHR10869 PANTHER
  cache, and the eight PMID caches used by seeded annotations.
- `just deep-research-falcon worm dpy-18 --fallback perplexity-lite` failed
  because Falcon was not configured and the Perplexity Lite fallback mapped to
  an unavailable Perplexity provider. No provider deep-research file was
  written; this notes file records the manual evidence pass.
- `just mod-description-deep-research worm dpy-18` fetched the WormBase
  hand-written gene description as `dpy-18-deep-research-wormbase.md`. The
  cuticle-collagen, phy-1/phy-2 redundancy, and ten-1/collagen-IV claims trace
  to cached primary literature; the head/posterior-neuron expression claim was
  not traced in this pass.
- `just paint-losses worm dpy-18` reported no IRD or IKR loss on the Q10576
  lineage. The PTHR10869 `PTHR10869-paint.tsv` cache places
  procollagen-proline 4-dioxygenase activity on PTN000852959, seeded by the
  C. elegans dpy-18 and phy-2 genes plus vertebrate collagen P4H alpha
  subunits.
- The core DPY-18 role is ER-lumen procollagen prolyl 4-hydroxylation.
  Winter and Page showed that `phy-1` is the classical `dpy-18` locus and that
  null dpy-18 alleles reduce the hydroxyproline content of cuticle collagens.
  Myllyharju et al. then showed that PHY-1, PHY-2 and PDI-2 assemble in vivo as
  a PHY-1/PHY-2/(PDI-2)2 mixed tetramer plus PHY-1/PDI-2 and PHY-2/PDI-2
  dimers.
- Kept the embryonic hatching, embryonic body morphogenesis, and
  multicellular-growth rows as non-core phenotype/context terms. They are
  supported by direct C. elegans genetics, but they sit downstream of the
  primary collagen P4H reaction.
- Marked the HEP `IRE1-mediated unfolded protein response` row as
  over-annotated. PMID:16184190 was a tunicamycin/UPR expression screen; a
  dpy-18 expression change does not show that the collagen hydroxylase executes
  the IRE-1 branch of UPR signaling.
