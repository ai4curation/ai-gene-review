# BRUMA bma-dpy-18.2 notes

## 2026-11-21

- The review is pinned to A0A1P6BZ71, the 541-aa Bm3843/bma-dpy-18.2
  transcript-level UniProt record for WBGene00224104. Its UniProt record lacks
  a `Bma-PHY-1` synonym, but NCBI sequence records resolve the identity: the
  AJ297845.1 mRNA record has the definition `Brugia malayi mRNA for prolyl
  4-hydroxylase (phy gene)`, the AJ421993.1 genomic record has the definition
  `Brugia malayi phy-1 gene for prolyl 4-hydroxylase, exons 1-12`; the
  bioinformatics check records their CDS-level match to A0A1P6BZ71.
- PMID:12417582 cloned and biochemically characterized Bma-PHY-1, reporting
  that recombinant PHY-1 is a soluble, active P4H even in the absence of
  protein disulfide isomerase [PMID:12417582, "The recombinant B. malayi alpha
  subunit, PHY-1, is a soluble and active P4H by itself"].
- PMID:23223450 later placed Bma-PHY-1 in the native B. malayi collagen P4H
  system: Bma-PHY-1 and Bma-PHY-2 are each detected in Bma-PDI-2-containing
  adult worm complexes, including a parasite-specific covalently linked form,
  and simultaneous Bma-phy-1/Bma-phy-2 RNAi produced stunted, lumpy immotile
  first-stage larvae [PMID:23223450, "Our co-IP analysis showed that in vivo
  Bma-PHY-1 and -2"].
- The parasite RNAi experiment supports Bma-PHY-1 in larval development and
  collagenous cuticle formation, but only in the combined alpha-subunit
  knockdown: single bma-phy-1 or bma-phy-2 RNAi had no visible effect, while
  simultaneous bma-phy-1/bma-phy-2 RNAi produced stunted, lumpy immotile
  first-stage larvae [PMID:23223450, "when Bma-phy-1 and Bma-phy-2 were
  disrupted simultaneously, but not singly"].
- A0A1P6BZ71 has PANTHER subfamily `PTHR10869:SF244`, the same subfamily as
  *C. elegans* DPY-18/Q10576 and Bma-PHY-2/Q68VC1 according to UniProt. The
  local PANTHER member cache for PTHR10869 does not include unreviewed parasite
  entries, so the review cites the UniProt assignment rather than claiming a
  local PANTHER match.
- `just paint-losses BRUMA bma-dpy-18.2` reported that A0A1P6BZ71 is not a
  leaf in the local PTHR10869 tree, so no PTHR10869 PAINT loss could be checked
  for this lineage.
- Falcon deep research failed because provider `falcon` was unavailable. No
  `bma-dpy-18.2-deep-research-falcon.md` was written, and no MOD-description
  provider is configured for `BRUMA`, so this pass used the A0A1P6BZ71 UniProt
  record, the GOA seed, NCBI AJ297845/AJ421993 sequence records, PMID:12417582,
  the cached full text of PMID:23223450, and the nematode cuticle module.
