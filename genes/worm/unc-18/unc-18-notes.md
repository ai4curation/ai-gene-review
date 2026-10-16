# unc-18 (C. elegans Munc18-1/Sec1, UniProt P34815) - curation notes

## Identity
- Swiss-Prot UNC18_CAEEL, P34815, 591 aa. Sole worm member of the Sec1/Munc18 (SM) protein family;
  orthologs are yeast SEC1, Drosophila Rop and vertebrate Munc18-1/STXBP1
  [PMID:12973353 "The UNC-18 protein is similar to the yeast SEC1 protein"].

## Core biology: SM protein that binds syntaxin and delivers vesicles to the release site
- unc-18 mutants have severely reduced readily releasable pool and neurotransmission
  [PMID:12973353 "In the absence of UNC-18, the size of the readily releasable pool is severely reduced."].
- The Weimer 2003 analysis excluded the alternative models and favoured docking: UNC-18 is not
  required to traffic or stabilize syntaxin sufficiently to explain the phenotype, is not required
  to open syntaxin, and its loss reduces docked vesicles at the active zone
  [PMID:12973353 "syntaxin distribution in unc-18 mutant animals is indistinguishable from that in wild type"; "we found a reduction of docked vesicles at the active zone in unc-18 mutants"].
  Syntaxin levels are halved in unc-18 mutants, but halving syntaxin genetically does not phenocopy
  unc-18 [PMID:12973353 "Quantitative western analysis demonstrated that syntaxin levels are reduced roughly by half in unc-18 mutants"].
- Higher-resolution (high-pressure-freeze) EM resolved two UNC-18-dependent pools: vesicles tethered
  within 25 nm of the plasma membrane and vesicles docked at it, and attributed tethering to the
  UNC-18/closed-syntaxin interaction
  [PMID:21423527 "those tethered within 25 nm of the plasma"; "suggesting UNC-18/closed syntaxin interactions are responsible for vesicle tethering"].
  The contrast with unc-13 (priming-defective, tethered vesicles accumulate) separates the two steps
  [PMID:21423527 "In contrast, priming defective unc-13 mutants accumulate tethered vesicles, while docked vesicles are greatly reduced"].
- UNC-18 requires syntaxin for its own plasma-membrane localization, and tomosyn (TOM-1) competes for
  syntaxin, so TOM-1 loss increases membrane UNC-18 and both vesicle pools
  [PMID:21423527 "Since UNC-18 requires syntaxin (UNC-64) for plasma membrane localization"; "tom-1 mutants exhibit enhanced UNC-18 plasma membrane localization"].
- Direct syntaxin binding is the molecular function, and it is regulated: PKC-2 phosphorylates
  UNC-18 on Ser322, reducing binding to closed syntaxin, and this modification in AFD neurons sets
  the temperature dependence of locomotion
  [PMID:22593072 "support a role for PKC phosphorylation in reducing closed-conformation syntaxin binding"].
- UNC-18 is a cytosolic/peripherally membrane-associated protein and, in a UNC-4/UNC-37 study, was
  explicitly used as a non-vesicular neuronal marker
  [PMID:11245684 "are not affected, however"].
- A separate axonal role: UNC-18 is part of a transport complex with syntaxin-1a and Kinesin-1
  assembled through the FEZ1/UNC-76 adaptor, and unc-76 mutation impairs axonal syntaxin transport
  [PMID:22451907 "Mutation of the FEZ1 ortholog UNC-76 in Caenorhabditis elegans causes defects in the axonal transport of Stx"].

## GO decisions (summary)
- Core: syntaxin-1 binding (GO:0017075, replacing the generic syntaxin binding for the worm
  UNC-64-specific IPI) at the plasma membrane, promoting vesicle tethering/docking and hence
  positive regulation of neurotransmitter secretion (GO:0001956) with establishment of vesicle
  localization (GO:0051650).
- The generic protein binding IPI (UNC-76/FEZ1) is removed as uninformative; the underlying
  transport-complex role is retained under intracellular protein transport.
- Dense-core-vesicle rows citing PMID:18031683 are left UNDECIDED: that paper's abstract documents
  UNC-31 (not UNC-18) as required for DCV docking, and the full text is not cached, so the
  unc-18-specific evidence cannot be checked.
