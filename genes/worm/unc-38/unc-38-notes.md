# unc-38 notes

## 2026-11-21

- Fetched `worm/unc-38` with UniProt Q23022 and cached the seeded GOA
  references. `just fetch-gene-pmids worm unc-38` found all ten existing GOA
  PMIDs. `just mod-description-deep-research worm unc-38` cached the WormBase
  hand-written description, and `just paint-losses worm unc-38` reported no IRD
  or IKR loss on this gene's lineage.
- Deep research was attempted with `just deep-research-falcon worm unc-38
  --fallback perplexity-lite`; both providers were unavailable in this
  environment, so the review used the cached primary papers, the WormBase MOD
  description, UniProt, the existing `unc-29` and `lev-1` reviews, and the
  PTHR18945 family review instead.
- The core L-AChR evidence is direct and module-relevant. Native TAP
  purifications of UNC-29-tagged receptor recovered peptides from UNC-29,
  UNC-38, UNC-63, LEV-8 and LEV-1 in all four purifications, and live
  surface labeling showed UNC-38 puncta apposed to presynaptic synaptobrevin
  and colocalizing with UNC-29 and LEV-1 [PMID:15990870, "Multiple peptides of
  each of the levamisole receptor subunits, UNC-29, UNC-38, UNC-63, LEV-8, and
  LEV-1"]. Richmond and Jorgensen showed that levamisole current in body-wall
  muscles requires both `unc-38` and `unc-29` and functions at neuromuscular
  synapses [PMID:10461217, "The levamisole response was eliminated in both
  mutants"].
- The later ACR-2R work defines a second UNC-38-containing receptor in
  cholinergic motor neurons. ACR-2R is made from the non-alpha subunits ACR-2
  and ACR-3 and the alpha subunits UNC-38, UNC-63 and ACR-12; adding `acr-3` to
  ACR-2/ACR-12/UNC-38/UNC-63 plus RIC-3/UNC-50/UNC-74 produced robust
  acetylcholine-gated currents in Xenopus oocytes [PMID:20027209, "robust
  expression of an acetylcholine-gated ion channel was observed"].
- The 1995/1997 ACR-2 and ACR-3 papers support UNC-38-dependent ligand-gated
  current in partial oocyte assemblies but predate the mature L-AChR and ACR-2R
  stoichiometries. I treated those rows as correct-but-general support for
  acetylcholine-gated cation channel activity and cation transmembrane
  transport rather than as evidence for a separate two-subunit receptor.
- WormBase's MOD gene description still conflates subunit sets by saying the
  UNC-38 multimer formed with ACR-2, ACR-3, UNC-29 and LEV-1 can make
  levamisole-gated channels. The five-subunit muscle L-AChR is
  UNC-29/LEV-1/UNC-38/UNC-63/LEV-8, while ACR-2R is
  ACR-2/ACR-3/ACR-12/UNC-38/UNC-63 and is essentially levamisole-insensitive.
- The calcium-specific `GO:0098703` row from PMID:20027209 looks too narrow for
  the cited experiment. The paper measured an ACR-2R acetylcholine-gated cation
  channel and calcium-dependent gain-of-function circuit output; the discussion
  only inferred that the hyperactive channel might increase calcium influx. I
  refined that row to `GO:0098655` and recorded a WormBase `WRONG_TERM` query.
- PMID:23351035 is abstract-only locally and the abstract identifies ACR-5 and
  ACR-15, not UNC-38, as the nAChR subunits needed for nicotine-motivated
  behavior. I left that locomotory-behavior row undecided rather than asserting
  a wrong reference without the full text.
