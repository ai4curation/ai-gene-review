# fis-2 (C. elegans) — Gene Review Notes

UniProt: Q6AHP8 (FIS12_CAEEL); WormBase F13B9.8 / WBGene00001425; ORF F13B9.8; Chromosome X.
Human ortholog: FIS1 (Q9Y3D6). Paralog in worm: fis-1 (Q20291, WBGene00001424) — a first FIS1
homologue reviewed separately (PR #1672, merged). Part of the flagship
`projects/CAEEL_MITOPHAGY.md` project.

151 aa tail-anchored protein: cytosol-facing TPR-fold body (CDD cd12212 Fis1; Pfam PF14852
Fis1_TPR_N + PF14853 Fis1_TPR_C) + a single C-terminal transmembrane helix (UniProt FT
TRANSMEM 126..146) that anchors it in the mitochondrial outer membrane. Belongs to the FIS1
family (PIRSF008835; PANTHER PTHR13247:SF0). PE 3: Inferred from homology (no experimental
protein-level evidence beyond localization/genetics).

## Deep research provenance
Falcon deep research (`just deep-research-falcon worm fis-2 --fallback perplexity-lite`) was
attempted TWICE. Both runs timed out after the built-in 600 s falcon limit under heavy
concurrent Edison load (multiple sibling worktrees were simultaneously running falcon jobs for
other worm genes), and the perplexity-lite fallback failed with an HTTP 401
`insufficient_quota` error on both attempts. No `fis-2-deep-research-falcon.md` (or
perplexity-lite) file was produced, so none is committed (never fabricate a `-deep-research-*`
file). This review is therefore grounded directly in UniProt (Q6AHP8), GOA (15 annotations),
and cached primary literature. Critically, the one paper that directly characterises worm
fis-2 loss-of-function (PMID:24196833, full text cached) and the paper that reports a
fis-2-specific apoptotic phenotype (PMID:18722182, ABSTRACT-ONLY in cache) were both read
directly, so every existing annotation could be adjudicated without an UNDECIDED call.

## Provenance sources
- UniProt Q6AHP8 record (`fis-2-uniprot.txt`)
- GOA (`fis-2-goa.tsv`) — 15 annotations
- Primary literature (cached):
  - PMID:24196833 Shen et al. 2014 Mol Biol Cell — "Mutations in Fis1 disrupt orderly disposal
    of defective mitochondria" (FULL TEXT). Directly studies C. elegans fis-1/fis-2 using the
    fis-1(tm1867); fis-2(gk414) double mutant (referred to throughout as the "Fis1 mutant") plus
    drp-1 fis-1 fis-2 and pink-1 fis-1 fis-2 triple mutants.
  - PMID:18722182 Breckenridge et al. 2008 Mol Cell — "C. elegans drp-1 and fis-2 regulate
    distinct cell-death execution pathways downstream of ced-3 and independent of ced-9"
    (ABSTRACT ONLY in cache; abstract explicitly foregrounds fis-2). Source of the fis-2 IDA
    mitochondrion localization and the fis-2 IGI apoptosis annotation.
  - PMID:16184190 Shen et al. 2005 PLoS Genet — C. elegans UPR microarray study (FULL TEXT).
    fis-2 (F13B9.8) is NOT named in the abstract/main text; the HEP annotation
    (GO:0036498, IRE1-mediated UPR) derives from supplementary microarray tables where fis-2
    scored as a UPR-regulated (target) gene. No verbatim fis-2 quote is available from this
    paper.

## KNOWN (well supported)

### Localization: mitochondrion / mitochondrial outer membrane (KNOWN for fis-2)
- Direct experimental (IDA) mitochondrial localization was assigned by WormBase from
  PMID:18722182 (UniProt: "SUBCELLULAR LOCATION: ... Mitochondrion
  {ECO:0000269|PubMed:18722182}"). The cached abstract does not restate the localization
  (full text has the fis-2::GFP data); defer to the WB curator for the IDA.
- Outer-membrane sub-localization is by ISS from human FIS1 (Q9Y3D6) and by the tail-anchor
  topology (UniProt DOMAIN: "The C-terminus is required for mitochondrial or peroxisomal
  localization, while the N-terminus is necessary for mitochondrial or peroxisomal fission").
  This is family-level / homology-based for worm fis-2, not directly demonstrated at OM
  resolution. Peroxisomal-membrane localization is purely ISS/IBA from mammalian/plant FIS1.

### fis-2-specific role: minor pro-apoptotic / cell-death-execution function (KNOWN, minor)
- This is the ONLY function experimentally demonstrated for fis-2 individually.
  [PMID:18722182 "minor proapoptotic roles for drp-1 and fis-2, a homolog of human Fis1, are revealed in sensitized genetic backgrounds"]
- Acts downstream of the CED-3 caspase, independent of drp-1 and of CED-9, to eliminate
  mitochondria in dying cells.
  [PMID:18722182 "downstream of the CED-3 caspase to promote elimination of mitochondria in dying cells, an event that could facilitate cell-death execution"]
  [PMID:18722182 "reveal distinct roles for drp-1 and fis-2 as mediators of cell-death execution downstream of caspase activation"]
- Basis of the GOA IGI GO:0006915 apoptotic process annotation (genetic interaction with ced-3,
  WB:WBGene00000423). Note: minor, only in sensitized backgrounds; the fis-2 single mutant has
  only "minor" effects on cell corpses (UniProt DISRUPTION PHENOTYPE from PMID:18722182).

### Redundant role in orderly disposal of defective mitochondria / mitophagy (KNOWN, but only via the double mutant)
- In PMID:24196833 the "Fis1 mutant" is the fis-1(tm1867); fis-2(gk414) double.
  [PMID:24196833 "generating fis-1(tm1867); fis-2(gk414) and mff-1(tm2955); mff-2(tm3041) double mutants"]
- The double mutant accumulates large LGG-1 (worm LC3) autophagic aggregates containing
  mitochondrial remnants and DRP-1 under mitochondrial stress.
  [PMID:24196833 "causing the formation of large aggregates containing LGG-1, DRP-1, and remnants of mitochondria"]
- fis-2 is genetically part of the disposal pathway: a drp-1 fis-1 fis-2 triple mutant suppresses
  the aggregates, and a pink-1 fis-1 fis-2 triple mutant abolishes mitophagosome spots.
  [PMID:24196833 "a drp-1 fis-1 fis-2 triple mutant strain also had reduced number and size of aggregates when treated with Paraquat"]
  [PMID:24196833 "pink-1 single and pink-1 fis-1 fis-2 triple mutant animals had no colocalizing spots, as expected for a complete block of mitophagy"]
- Model (family level, largely mammalian coIP): FIS1 is a MOM factor in the DRP-1/MAM fission
  complex acting at a late disposal step.
  [PMID:24196833 "Fis1 is part of the MAM complex and contributes to a late stage of the removal process but is not required for entry of Drp1 into the MAM or fission"]

## NOT known / important negatives

### fis-2 is NOT required for mitochondrial fission in C. elegans (fis-2-specific negative)
- The fis-2 SINGLE mutant (and the fis-1;fis-2 double) has wild-type mitochondrial morphology.
  [PMID:24196833 "Our results show that fis-1 and fis-2 single and double mutants have wild-type mitochondrial morphologies, as also shown by others"]
- Fis1 homologues are not essential for fission or for DRP-1 recruitment in worm (Mff is the
  relevant recruiter; drp-1 the essential mechanochemical GTPase).
  [PMID:24196833 "Mff and Fis1 are not essential for fission or for Drp1 recruitment to mitochondria in C. elegans"]
- So the family-propagated GO:0000266 mitochondrial fission (IBA + IEA) is defensible only at
  the family/machinery level; it is NOT the core essential fission role in worm → non-core.

### fis-2 is NOT required for peroxisome fission in C. elegans (negative)
- Fis1 mutants (= fis-1;fis-2 double) have normal punctate peroxisomes; only Mff/Drp1 loss gives
  tubular (fission-defective) peroxisomes.
  [PMID:24196833 "showing punctate peroxisomes in wild-type and Fis1 mutants and tubular peroxisomes in drp-1 mutant and Mff double mutants"]
- GO:0016559 peroxisome fission (IBA) and GO:0005778 peroxisomal membrane (IBA/ISS/IEA) are
  family-level propagations with no direct worm support → non-core.

### lipid binding (GO:0008289, IBA) — weakly supported
- No worm fis-2 evidence for lipid binding. The C-terminal TM helix mediates membrane anchoring,
  which is not a "lipid binding" molecular function. Generic family-level over-propagation →
  over-annotated.

### molecular adaptor activity (GO:0060090, IBA) — best available MF, but undemonstrated for fis-2
- Assigned purely by phylogenetic propagation from the FIS1 family. It is the most informative
  MF term available and is consistent with fis-2 being a tail-anchored MOM protein in the
  fission/disposal machinery, but NO worm fis-2 protein has been shown to bind DRP-1, an
  adaptor, or any partner. Accept as the representative MF, but flag as an MF-dark knowledge gap.

## Difference from the fis-1 paralog (why fis-2 needs its own evidence)
- fis-1 review concluded fis-1 is dispensable for fission and acts (redundantly with fis-2) in
  orderly mitochondrial disposal; its individually demonstrated data were localization
  (YFP::FIS-1 as OM marker, PMID:21248201) and the UVC/mtDNA-damage-removal role
  (fis-1 RNAi, PMID:24058863).
- fis-2's individually demonstrated datum is different: the minor pro-apoptotic / cell-death
  execution role (PMID:18722182, Breckenridge — which foregrounds fis-2, not fis-1). The
  mitophagy/LGG-1 disposal phenotype (PMID:24196833) was only ever scored in the fis-1;fis-2
  DOUBLE mutant, so it demonstrates a redundant contribution, not an fis-2-autonomous role.
- Open question: do the two paralogs partition (fis-2 → apoptotic disposal per Breckenridge;
  fis-1 → UVC/mtDNA damage removal per Bess/Shen; both → stress mitophagy), or are they fully
  interchangeable? Not resolved in the literature.

## Unknowns (candidate knowledge gaps — the point for a dark paralog)
1. MF-dark: the molecular activity of fis-2 is entirely inferred. "Molecular adaptor activity"
   is a family-level IBA; there is no worm fis-2 binding/biochemical data at all.
2. Whether fis-2 has ANY non-redundant function distinct from fis-1 is unresolved: the disposal
   phenotype requires loss of BOTH paralogs (double mutant), and both single mutants have normal
   mitochondrial morphology. fis-2's autonomous contribution to mitophagy is undetermined.
3. fis-2's interactome is unmapped: no worm data on whether fis-2 binds DRP-1 (directly or via an
   adaptor), participates in a MAM/ER-mitochondria complex, or what distinguishes it from fis-1.
4. The mechanism and physiological significance of the minor, sensitized-background pro-apoptotic
   role, and whether it reflects the same disposal machinery acting in dying cells, is unknown.

## Curation decisions summary (see fis-2-ai-review.yaml)
- ACCEPT (core/representative): GO:0060090 molecular adaptor activity (IBA, best MF, flagged
  MF-dark); GO:0005739 mitochondrion (IDA, fis-2-specific); GO:0005741 mitochondrial outer
  membrane (ISS, IEA-SubCell); GO:0005739 mitochondrion (IEA); GO:0006915 apoptotic process
  (IGI, the one demonstrated fis-2-specific function).
- KEEP_AS_NON_CORE: GO:0000266 mitochondrial fission (IBA, IEA); GO:0005741 mito OM (IBA
  is_active_in); GO:0005778 peroxisomal membrane (IBA/ISS/IEA); GO:0016559 peroxisome fission
  (IBA); GO:0036498 IRE1-mediated UPR (HEP, expression-only).
- MARK_AS_OVER_ANNOTATED: GO:0008289 lipid binding (IBA).
- NEW (proposed): GO:0000423 mitophagy (IGI, redundant with fis-1; only shown in the double
  mutant) — flagged as redundant, not fis-2-autonomous.
