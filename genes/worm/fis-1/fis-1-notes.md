# fis-1 (C. elegans) — Gene Review Notes

UniProt: Q20291 (FIS11_CAEEL); WormBase F41G3.4 / WBGene00001424; ORF F41G3.4.
Human ortholog: FIS1 (Q9Y3D6). Paralog in worm: fis-2 (a second FIS1 homologue).
Part of the flagship `projects/CAEEL_MITOPHAGY.md` project.

143 aa tail-anchored protein: cytosol-facing TPR-fold body + a single C-terminal
transmembrane helix (residues ~121–141) that anchors it in the mitochondrial outer
membrane. Belongs to the FIS1 family (PIRSF008835; CDD cd12212; PANTHER PTHR13247:SF1).

## Deep research provenance
Falcon deep research (`just deep-research-falcon worm fis-1 --fallback perplexity-lite`) was
attempted TWICE (initial run stalled >15 min with zero output under heavy concurrent Edison
load; a bounded retry was killed by a 6-min timeout, exit 143). No `-deep-research-falcon.md`
file was produced, and the perplexity-lite fallback also did not yield a file. This review is
therefore grounded directly in UniProt (Q20291), GOA, and cached FULL-TEXT primary literature
(PMID:24196833, PMID:24058863, PMID:21248201 all have full text; PMID:18722182 abstract-only).
Because every existing annotation could be adjudicated from the cached full text, no UNDECIDED
calls were required.

## Provenance sources
- UniProt Q20291 record (`fis-1-uniprot.txt`)
- GOA (`fis-1-goa.tsv`) — 12 annotations
- Primary literature (cached, full text unless noted):
  - PMID:24196833 Shen et al. 2014 Mol Biol Cell — "Mutations in Fis1 disrupt orderly disposal of defective mitochondria" (full text; studies BOTH C. elegans fis-1/fis-2 AND mammalian FIS1)
  - PMID:24058863 Bess et al. 2013 Worm — UVC / mtDNA damage removal (full text)
  - PMID:21248201 Head et al. 2011 Mol Biol Cell — MOMA-1 paper (full text; uses YFP::FIS-1 as a bona fide mito OM marker)
  - PMID:18722182 Breckenridge et al. 2008 Mol Cell — drp-1/fis-2 cell-death (ABSTRACT ONLY in cache; abstract foregrounds fis-2)

## KNOWN (well supported)

### Localization: mitochondrial outer membrane (KNOWN)
- YFP::FIS-1 is used as a reference mitochondrial outer-membrane marker in C. elegans.
  [PMID:21248201 "Fluorescence labeling showed a pattern similar to patterns observed with YFP fused to a bona fide mitochondrial OM protein (YFP::FIS-1)"]
- Tail-anchored topology: cytosolic TPR body + single C-terminal TM helix (UniProt FT TRANSMEM 121..141; DOMAIN "The C-terminus is required for mitochondrial or peroxisomal localization, while the N-terminus is necessary for mitochondrial or peroxisomal fission").
- This underpins the IDA (PMID:21248201), ISS (from human Q9Y3D6), and IEA(SubCell) mito-OM annotations. Peroxisomal-membrane localization is by ISS/IBA from mammalian/plant homologues; NOT directly demonstrated in worm.

### Molecular function: adaptor/receptor in the fission machinery (KNOWN at family level, consistent in worm)
- FIS1 family proteins are Drp1 recruitment/adaptor factors anchored in the OMM.
  [PMID:24196833 "Recruitment of Drp1 to mitochondria is mediated by proteins that are anchored in the mitochondrial outer membrane"]
- In worm, fission-inducing stress drives Drp1 into a complex with Fis1 (shown for mammalian cells; worm Fis1 is part of the MAM fission complex).
  [PMID:24196833 "Fis1 is part of the MAM complex and contributes to a late stage of the removal process but is not required for entry of Drp1 into the MAM or fission"]
- Supports GOA IBA GO:0060090 molecular adaptor activity (core MF).

### Core role in C. elegans: orderly disposal of defective mitochondria / stress-induced mitophagy (KNOWN)
- fis-1;fis-2 (Fis1) mutants accumulate LGG-1 (worm LC3) autophagic aggregates, enlarged by mitochondrial stress (Paraquat/ROS, antimycin A).
  [PMID:24196833 "Fis1 mutants showed a modest but consistent increase in the number and size of LGG-1::CFP clusters when compared with wild type or Mff mutants"]
- Aggregates contain remnants of mitochondria + DRP-1 (and Parkin/ER).
  [PMID:24196833 "We conclude that mutations in Fis1 affect autophagy in C. elegans, causing the formation of large aggregates containing LGG-1, DRP-1, and remnants of mitochondria"]
- Aggregate formation requires upstream Mff/Drp1 fission and Pink1 → fis-1 acts downstream, coupling fission to mitophagy. Model:
  [PMID:24196833 "Fis1 acts after Drp1 and Mff initiate mitochondrial fission, guiding this process toward major cellular stress response pathways"]
- pink-1 fis-1 fis-2 triple mutant loses colocalizing mitophagosome spots ("as expected for a complete block of mitophagy") and has fewer/smaller LGG-1 aggregates than the Fis1 double.

### Role in removal of UVC-induced mtDNA damage (KNOWN)
- RNAi knockdown of fis-1 blocks removal of UVC-induced mtDNA damage, like drp-1.
  [PMID:24058863 "RNAi knockdown of fis-1 inhibited mtDNA damage removal similarly to drp-1"]
- fis-1 knockout does not exacerbate UVC-induced larval arrest (redundancy/buffering by fusion).
  Figure legend: [PMID:24058863 "fis-1 is required for removal of UVC-induced mtDNA damage but not recovery from larval arrest"]
- This is the experimental basis for the UniProt "DNA damage" keyword (GO:0006974 DNA damage response, IEA-KW; no GOA annotation for it directly).

## NOT known / important negatives

### fis-1 is NOT required for mitochondrial fission in C. elegans (organism-specific negative)
- fis-1 and fis-2 single/double mutants have WILD-TYPE mitochondrial morphology; loss of function has no obvious fission defect.
  [PMID:24196833 "Our results show that fis-1 and fis-2 single and double mutants have wild-type mitochondrial morphologies, as also shown by others"]
  [PMID:24196833 "whereas Fis1 homologues have no obvious effects"]
- Corroborated by UVC paper: [PMID:24058863 "While knockout of these genes alone does not affect mitochondrial morphology or development"]
- BUT overexpressed FIS-1 can drive fragmentation, and it is part of the fission complex → the GO:0000266 "mitochondrial fission" IBA/IEA is defensible at the family/machinery level but is NOT the core essential fission determinant in worm (that is mff-1/mff-2 + drp-1). Treat as non-core.

### fis-1 is NOT required for peroxisome fission in C. elegans (organism-specific negative)
- fis-1 mutants have normal (punctate) peroxisomes; only Mff/Drp1 loss gives tubular peroxisomes.
  [PMID:24196833 "showing punctate peroxisomes in wild-type and Fis1 mutants and tubular peroxisomes in drp-1 mutant and Mff double mutants"]
- So GO:0016559 peroxisome fission (IBA) is a family-level propagation not supported by direct worm evidence; non-core.

### lipid binding (GO:0008289, IBA) — weakly supported
- No worm-specific evidence that fis-1 binds lipid. The tail anchor inserts into membrane but that is membrane anchoring, not a "lipid binding" molecular function. Likely a generic family-level over-propagation; non-core / over-annotated.

## Unknowns (candidate knowledge gaps)
1. The precise molecular activity by which Fis1 couples completed fission to the mitophagy/degradation machinery is undefined. It is not a Drp1 receptor essential for fission in worm (Mff is), yet its loss stalls an intermediate step of orderly disposal. Whether it acts by a direct partner (a downstream autophagy/MAM factor), by remodeling the ER–mitochondrial interface, or by handing off DRP-1, is unresolved.
   [PMID:24196833 "Fis1 is part of the MAM complex and contributes to a late stage of the removal process but is not required for entry of Drp1 into the MAM or fission"]
2. Whether C. elegans fis-1 has any endogenous (loss-of-function) role in mitochondrial or peroxisome fission at all, versus being entirely dispensable, is unresolved: LOF is phenotypically silent for morphology while overexpression is sufficient to fragment.
   [PMID:24196833 "These dominant effects show that overexpressed Fis1 can affect mitochondrial fission even though C. elegans Fis1 proteins are not required for fission"]
3. The direct binding partners of worm FIS-1 (does it use adaptor proteins analogous to yeast Mdv1/Caf4? does it bind DRP-1 directly under stress?) have not been mapped in C. elegans.

## Curation decisions summary (see fis-1-ai-review.yaml)
- ACCEPT (core): GO:0060090 molecular adaptor activity (IBA); GO:0005741 mitochondrial outer membrane (IDA/ISS/IEA/IBA).
- KEEP_AS_NON_CORE: GO:0000266 mitochondrial fission (IBA, IEA); GO:0005778 peroxisomal membrane (IBA/ISS/IEA); GO:0016559 peroxisome fission (IBA).
- MARK_AS_OVER_ANNOTATED: GO:0008289 lipid binding (IBA).
- Core biological role captured in core_functions = orderly disposal of defective mitochondria (stress-induced mitophagy coupling), MF = molecular adaptor activity at the mito OM.
