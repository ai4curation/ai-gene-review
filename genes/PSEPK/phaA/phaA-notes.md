# phaA (PP_5003 / phaC1) - P. putida KT2440 Notes

## Gene Identity

- **UniProt**: Q88D25 (TrEMBL, unreviewed)
- **Locus tag**: PP_5003
- **Gene name**: phaA (also called phaC1 in literature)
- **Product**: Poly(3-hydroxyalkanoate) polymerase 1 (PHA synthase, Class II)
- **EC**: 2.3.1.- (acyltransferase)
- **Length**: 559 AA
- **PANTHER family**: PTHR36837 (PHA/PHB synthase), subfamily SF5 (Poly-3-hydroxybutyrate synthase)

## Gene Nomenclature Note

The gene is annotated as "phaA" in the P. putida KT2440 genome (PP_5003), but in the broader PHA literature it is referred to as **phaC1**. This is the first of two PHA synthases in the pha operon. The "phaA" nomenclature in P. putida should not be confused with phaA in Cupriavidus necator, which encodes beta-ketothiolase (a different enzyme in the PHB pathway).

## PHA Operon Organization

The pha locus in P. putida KT2440 contains:
- **phaC1** (PP_5003) - PHA synthase 1 (this gene)
- **phaZ** (PP_5004) - PHA depolymerase
- **phaC2** (PP_5005) - PHA synthase 2
- **phaD** - TetR-like transcriptional regulator

The operon is transcribed as phaC1ZC2D and regulated by PhaD [PMID:20406286 "PhaD behaves as a carbon source-dependent activator of the pha cluster"].

## Enzyme Classification

- **Class II PHA synthase**: Distinguished from Class I (e.g., C. necator PhaC) by substrate preference for medium-chain-length (mcl, C6-C14) 3-hydroxyalkanoyl-CoA substrates
- **Catalytic mechanism**: α/β-hydrolase fold with conserved catalytic triad Cys-His-Asp
- **PhaC box motif**: G-G/S-X-C-X-G/A-G (modified lipase box)
- **Domain**: PhaC_N domain (Pfam PF07167, residues 75-243)

## Function

PhaC1 catalyzes the polymerization of (R)-3-hydroxyalkanoyl-CoA thioesters into polyhydroxyalkanoates (PHAs) with concomitant release of CoA. The reaction is a transesterification.

**Substrate specificity**: Class II PHA synthases like PhaC1 from P. putida preferentially polymerize medium-chain-length (mcl) substrates (C6-C14), producing mcl-PHAs. This is distinct from Class I synthases that produce short-chain-length PHB.

**Biological role**: PHAs accumulate as intracellular granules and serve as carbon and energy storage reserves under nutrient-limiting conditions (especially nitrogen limitation).

## Key Literature Findings

- PhaC1 is the **primary PHA synthase** in P. putida; overexpression of phaC1 enhanced mcl-PHA biosynthesis up to 2.86-fold, while phaC2 did not activate biosynthesis [PMID:17137299 "The biosynthesis of mcl-PHA was enhanced only by the overexpressed phaC1 gene"]
- Deletion of the pha operon (phaC1-phaZ-phaC2, 3437 bp) creates PHA-deficient strain PpUW2
- Deletion of PhaC1 causes morphological changes including reduced cell size
- PHA metabolism involves simultaneous synthesis and degradation (turnover), controlled by coordinated expression of synthases and depolymerase [PMID:20406286]
- The phaC1ZC2D transcription unit is regulated by PhaD, which controls its own transcription and that of the phaIF operon
- P. putida KT2440 genome was sequenced [PMID:12534463] and revisited [PMID:26913973]

## Existing GO Annotations (GOA)

Only 2 IEA annotations:
1. GO:0016746 (acyltransferase activity) - IEA via InterPro:IPR011287
2. GO:0042619 (poly-hydroxybutyrate biosynthetic process) - IEA via InterPro:IPR010941, IPR011287

## Assessment of Current Annotations

- GO:0016746 is quite general; more specific acyltransferase terms may be appropriate
- GO:0042619 refers specifically to poly-hydroxybutyrate (PHB, short-chain), but P. putida PhaC1 produces medium-chain-length PHAs (mcl-PHA), not PHB. This may be an over-specific or incorrect term assignment.

## Relevant GO Terms to Consider

- GO:0016746 (acyltransferase activity) - current, but may need more specific child
- GO:0042619 (poly-hydroxybutyrate biosynthetic process) - may be incorrect for mcl-PHA producer
- GO:0016747 (acyltransferase activity, transferring groups other than amino-acyl groups) - more specific MF
- polyhydroxyalkanoate biosynthetic process - need to check if a broader PHA term exists
- GO:0005737 (cytoplasm) - PHA granules are cytoplasmic
- carbon storage/reserve metabolic process terms
