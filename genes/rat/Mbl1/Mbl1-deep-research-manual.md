# Mbl1 (rat, UniProt P19999) - manual literature research

No deep-research API was available for this session. This file is a manual
literature synthesis built from cached publications in `publications/` and the
UniProt record (`Mbl1-uniprot.txt`). Every claim carries inline provenance.

## Identity

- Rat *Mbl1* encodes mannose-binding protein A (MBP-A, MBL-A), the serum
  mannose-binding lectin. Rodents have two MBL genes; *Mbl2* encodes MBP-C
  (the "liver" form). [PMID:15148336 "MBL-A and MBL-C, the respective gene products of the mbl1 and mbl2 genes, are 50% homologous"]
- MBP-A is identical to rat serum MBP. [PMID:3584121 "revealing that MBP-A is in fact identical with serum MBP"]
- Domain architecture: N-terminal cysteine-rich segment, collagen-like
  Gly-X-Y repeats, alpha-helical neck, C-terminal C-type CRD; signal peptide.
  [PMID:3009480 "Each protein is preceded by a cleaved, NH2-terminal signal sequence, consistent with the finding that this protein is found in serum as well as in the liver"]

## Carbohydrate recognition (core molecular function)

- Ca2+-dependent C-type lectin; Ca2+ directly coordinates the sugar ligand.
  [PMID:1436090 "reveals that Ca2+ forms coordination bonds with the carbohydrate ligand"]
- Binds high-mannose oligosaccharides; multivalent binding visualised.
  [PMID:1436090 "Two branches of the oligosaccharide crosslink neighbouring carbohydrate-recognition domains in the crystal"]
- Specificity for mannose and GlcNAc. [PMID:3584121 "Serum mannan-binding protein (MBP), a lectin specific for mannose and N-acetylglucosamine"]
- Ligand orientation in MBP-A depends on His189.
  [PMID:11850428 "monosaccharides or alpha1-6-linked mannose bind to MBP-A in one orientation"]
- Trimeric CRD/neck: binding sites 53 A apart, so MBP-A selects widely
  spaced repetitive sugar arrays typical of pathogens.
  [PMID:7704532 "MBPs can recognize pathogens selectively by binding avidly only to the widely spaced, repetitive sugar arrays on pathogenic cell surfaces"]
- In vitro, serum MBP binds phosphatidylinositol and PI4P (Ca2+-dependent);
  physiological relevance unknown. [PMID:9315725 "S- and L-MBPs bound to phosphatidylinositol 4-monophosphate"]

## Oligomeric structure

- Structural unit is a homotrimer; the neck is a triple coiled coil.
  [PMID:7704532 "The neck consists of a parallel triple-stranded coiled coil of alpha-helices"]
- Trimers associate into dimers, trimers and tetramers of subunits
  (near-planar fan-like structures). [PMID:22167201 "the carbohydrate-recognition domains in the MBL dimer, trimer, and tetramer are positioned close to each other in near-planar fan-like structures"]
- Oligomerisation needs glycosylated hydroxylysines in the collagen domain
  (LH3). [PMID:25419660 "loss of the terminal glucose units on the derivatized lysine residues in mouse embryonic fibroblasts lacking the LH3 protein leads to defective disulphide bonding and oligomerization of rat MBL-A"]

## MASP binding and lectin-pathway complement activation

- Serum MBP (MBP-A) activates complement in a sugar-dependent, C4-dependent
  manner; liver MBP (MBP-C) does not in that assay.
  [PMID:3584121 "The activation by serum MBP was inhibited effectively by the presence of haptenic sugars and dependent absolutely upon the presence of C4"]
- Binds MASP-1 and MASP-2 independently, Ca2+-dependently.
  [PMID:10913141 "both MASPs associate independently with rat MBP in a"]
- MASP binding is via a lysine in the collagenous domain.
  [PMID:20118239 "Overall, therefore, specificity of the MBL-MASP interaction appears to be driven mainly by a single lysine residue in the collagen-like domain."]
- MBP is the recognition subcomponent: it binds the target and triggers MASP-2
  autoactivation; the protease (MASP-2) performs the cleavage of C4/C2.
  [PMID:16272342 "reduced complement activation by both mutant MBLs is caused by failure to activate MASP-2 efficiently on binding to a mannan-coated surface"]
  [PMID:20118239 "the active rather than the zymogen state is default in lectin.MASP complexes and must be inhibited through additional regions in circulating MBLs until triggered by pathogen recognition"]
- Collagen-domain mutations equivalent to human immunodeficiency alleles
  impair secretion, oligomerisation and complement fixation.
  [PMID:10903744 "The mutations Gly25-->Asp and Gly28-->Glu disrupt the disulfide-bonding arrangement of the protein"]

## In vivo (mouse orthologue)

- Mbl1/Mbl2 double-null mice lack serum MBL and the MBL pathway and are
  susceptible to S. aureus; peritoneal macrophage uptake reduced by 40%.
  [PMID:15148336 "These MBL-null mice lack MBL in serum and lack the MBL complement pathway"]
  This is a double knockout, so the contribution of MBL-A alone is not
  separated.

## Not supported for MBP-A

- No evidence for MBP-A in multivesicular bodies or for a role in pulmonary
  surfactant homeostasis; these belong to surfactant collectins (SP-A, SP-D).
  MBP-A is a liver-made serum protein [PMID:3584121 "Serum mannan-binding protein (MBP)"].
