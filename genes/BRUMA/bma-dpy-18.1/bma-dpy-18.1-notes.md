# BRUMA bma-dpy-18.1 notes

## 2026-11-21

- The project page prioritized `BRUMA` `bma-dpy-18.1` as Q68VC1. A first
  unpinned `fetch-gene` call resolved the symbol to the shorter 460-aa
  WBParaSite duplicate A0A4E9F4D5, which maps to the same WormBase gene
  `WBGene00231085` but lacks the experimental `GO:0002119` row. The review is
  pinned to Q68VC1, the 551-aa transcript-level `Q68VC1_BRUMA` entry with EMBL
  cDNA AJ628347 and WormBase `Bm10824b`.
- Q68VC1 has PANTHER subfamily `PTHR10869:SF244`, the same subfamily as
  *C. elegans* DPY-18/Q10576. The second *C. elegans* alpha subunit
  PHY-2/Q20065 falls in PTHR10869 but a separate subfamily, `PTHR10869:SF156`.
- Falcon deep research failed because the provider was unavailable, and the
  configured Perplexity Lite fallback was also unavailable. No MOD-description
  provider is configured for `BRUMA`, so this pass used the Q68VC1 UniProt
  record, the GOA seed, the local PANTHER cache, the nematode cuticle module,
  and the cached full text of PMID:23223450.
- PMID:23223450 directly cloned Bma-phy-2/Q68VC1, reported conservation of
  Bma-PHY-2 residues needed for protein structure, complex formation, and
  enzyme activity, and detected Bma-PHY-2 in native Bma-PDI-2-containing adult
  worm complexes [PMID:23223450 Prolyl 4-hydroxlase activity is essential for
  development and cuticle formation in the human infective parasitic nematode
  Brugia malayi., "Our co-IP analysis showed that in vivo Bma-PHY-1 and -2"].
- The parasite RNAi experiment supports Bma-PHY-2 in larval development and
  collagenous cuticle formation, but only in the combined alpha-subunit
  knockdown: single bma-phy-1 or bma-phy-2 RNAi had no visible effect, while
  simultaneous bma-phy-1/bma-phy-2 RNAi produced stunted, lumpy immotile
  first-stage larvae [PMID:23223450, "when Bma-phy-1 and Bma-phy-2 were
  disrupted simultaneously, but not singly"].
- The broad embryonic and growth process rows come from EnsemblMetazoa transfer
  from *C. elegans* DPY-18/Q10576. They are not outright impossible for Brugia
  P4H alpha subunits, but they overreach the direct B. malayi experiment, which
  tested first-stage microfilariae produced by adult females rather than embryo
  hatching, embryonic morphogenesis, or growth rate.
- The recombinant insect-cell data need to be read with care. Bma-PHY-2 formed
  a soluble homotetramer by itself but was not detectably active, and
  co-expression of Bma-PHY-1, Bma-PHY-2 and Bma-PDI-2 formed complexes that
  also lacked detectable enzyme activity. The paper inferred that active
  B. malayi C-P4H depends on the covalently linked parasite-native PHY/PDI-2
  complex rather than on the insect-cell recombinant complexes.
