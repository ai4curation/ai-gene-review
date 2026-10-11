# LDLR review notes

Deep research: `just deep-research-falcon human LDLR` was attempted on 2026-10-09 and failed
(provider timed out after 600 s). The review was done manually from the GOA-cited publications
cached in `publications/` and the UniProt record.

## Core biology (with provenance)

- LDLR binds LDL and carries it into cells by endocytosis; complexes must cluster in clathrin-coated
  pits [file:human/LDLR/LDLR-uniprot.txt "Binds low density lipoprotein /LDL, the major
  cholesterol-carrying lipoprotein of plasma, and transports it into cells by endocytosis."]
- Functional surface receptors after cDNA transfection [PMID:6091915 "Transfection of simian COS cells
  with the human LDL receptor cDNA linked to the SV40 early promoter resulted in expression of
  functional cell surface receptors."]
- FH alleles dissect synthesis, transport and binding [PMID:6299582 "The other three mutations
  specify precursors (100, 120, and 170 kd) that undergo a normal 40 kd increase in molecular weight
  and reach the surface, but do not bind LDL normally."]
- Internalization signal FDNPVY is read by AP-2 mu2 (so the clathrin-heavy-chain-binding annotation
  was modified to AP-2 adaptor complex binding) [PMID:12121421 "The endocytic sorting signal on the
  low-density lipoprotein receptor for clathrin-mediated internalization is the sequence FDNPVY in the
  receptor's cytosolic tail."]
- apoE-containing ligands (beta-VLDL) also bind [PMID:2777800 "This mutant receptor could not bind
  LDL, but could bind other ligands for the LDL receptor, beta-migrating very low density
  lipoprotein, and the apolipoprotein E-lipid complex."]
- Endosomal closed conformation and recycling [PMID:26526611 "In the endosomes, it adopts a closed
  conformation important for recycling"]
- Degradation by PCSK9 [PMID:17452316 "As a consequence, the LDLR is rerouted from the endosome to the
  lysosome where it is degraded."] and by IDOL [PMID:19520913 "an E3 ubiquitin ligase that triggers
  ubiquitination of the LDLR on its cytoplasmic domain, thereby targeting it for degradation."]

## Curation decisions worth flagging

- PCSK9-driven regulation terms (negative regulation of receptor recycling, negative regulation of
  LDL particle clearance) annotated to LDLR describe the regulator's role; marked over-annotated on
  LDLR (they are accepted on PCSK9).
- GO:0030299 intestinal cholesterol absorption (IMP, PMID:17142622): the cached full text of this UK
  FH genetics study contains no intestinal data; marked over-annotated rather than removed.
- Brain amyloid-beta / apoE clearance terms from mouse overexpression (PMID:20005821) kept as non-core;
  downstream neuroinflammation terms marked over-annotated.

## Disease alignment

dismech `LDLR-Related_Familial_Hypercholesterolemia` binds the trigger node to GO:0005041 (DECREASED),
matching core function 1 here. Its class-3 node was corrected (2026-10-09) from GO:0050750 (the
ligand-side receptor-binding term) to GO:0030169 low-density lipoprotein particle binding, the
receptor's own binding function.
