# EMENI maiA (O43123) notes

## Deep research

No provider deep-research file exists and no deep-research API keys are available
in this session; none was generated. Notes are from cached publications
(abstract-only), the UniProt record and PTHR42673 PAINT data.

## Identity

- UniProt O43123 (MAAI_EMENI), gene maiA, ORF AN1895, 230 aa. Zeta-class GST
  (IPR005955, TIGR01262 maiA, PTHR42673:SF4). Glutathione cofactor; GSH-binding
  residues by similarity.

## Function

- First MAAI gene from any organism; recombinant MaiA active [PMID:9417084 "The MaiA
  protein shows strong amino acid sequence identity to glutathione S-transferases and
  has MAAI activity when expressed in Escherichia coli."].
- Disruption [PMID:9417084 "maiA disruption prevents growth on phenylalanine (Phe)
  and phenylacetate and results in the absence of MAAI activity in vitro and Phe
  toxicity."]; disruptants are succinylacetone-negative and secrete
  2,4-dioxohept-2-enoic acid isomers [PMID:9417084].
- Led to identification of human MAAI (GSTZ1) [PMID:9417084].
- UniProt: cytoplasm by similarity (ECO:0000250); induced by Phe/phenylacetate.

## Curation decisions

- GO:0016034 and GO:0006559 rows: ACCEPT.
- GO:0004364 GST activity (IBA): KEEP_AS_NON_CORE (zeta-class family property, untested
  for MaiA, not the physiological role).
- GO:0006749 glutathione metabolic process (IBA): MARK_AS_OVER_ANNOTATED (GSH is a
  cofactor, not a metabolite processed by MaiA).
- GO:0005739 mitochondrion (IBA, mammalian GSTZ1 sources only): UNDECIDED, no fungal
  localization data.
- GO:0005737 cytoplasm (IEA): ACCEPT. Generic catalytic/aromatic aa metabolic: TOO_GENERAL.
- Did not add GO:1902000 homogentisate catabolic process: human GSTZ1 does not carry it
  and MaiA acts on maleylacetoacetate rather than homogentisate; left for discussion.

## 2026-10-24 follow-up

- GO:0005739 mitochondrion (IBA, PTN000137159) changed from UNDECIDED to
  MARK_AS_OVER_ANNOTATED. The IBD seeds are mammalian GSTZ1 only, where the
  mitochondrial matrix pool is minor relative to the cytosolic enzyme; there is
  no fungal localization evidence and UniProt places MaiA in the cytoplasm by
  similarity, so the propagated term likely overstates MaiA localization. Not
  removed because a mitochondrial fraction has never been tested.

## 2026-11-01 review follow-up (PR 5356)

- GO:1902000 homogentisate catabolic process is now asserted uniformly for all nine
  homogentisate-pathway exemplars (KT2440 hmgA/hmgC/hmgB, human HGD/GSTZ1/FAH,
  A. nidulans hmgA/maiA/fahA), as NEW where GOA lacks it: each enzyme performs one of
  the three catalytic steps of homogentisate breakdown.
