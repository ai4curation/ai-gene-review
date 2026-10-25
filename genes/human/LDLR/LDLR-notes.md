# LDLR review notes

Deep research: the client reported a timeout after 600 s on 2026-10-09, so the review was done
manually from the GOA-cited publications cached in `publications/` and the UniProt record. The
provider in fact finished (run ended 2026-10-09T16:41) and `LDLR-deep-research-falcon.md` was
written afterwards. It was checked against this review on 2026-10-11:

- It agrees on the core annotation: surface recognition and clathrin-mediated endocytosis of
  apoB-100- and apoE-bearing lipoprotein particles, acid-dependent cargo release in the
  endosome via the LA-repeat/beta-propeller closed conformation, and receptor recycling. It
  stresses that the substrate is the apolipoprotein-bearing particle rather than free
  cholesterol, and that LDLR is not an enzyme or a sterol transporter. This matches core
  functions 1 and 2 and the review's rejection of generic transporter terms.
- It confirms the regulatory layer the review annotates: SREBP-2/SCAP transcriptional control,
  PCSK9 binding to EGF-A diverting the receptor to lysosomes (including an intracellular
  trans-Golgi route), and LXR-induced IDOL/MYLIP ubiquitination of the cytosolic tail.
- It adds the Reimund et al. cryo-EM structure of apoB-100-containing LDL bound to LDLR
  (Nature 638, online 2024-12-11; ~5.6 and ~7.9 A), which resolves two interfaces: the LA
  modules contact basic regions of the apoB-100 beta-belt, and the beta-propeller contacts the
  apoB-100 N-terminal domain. This is direct structural support for core function 1; the
  resolution does not support residue-level claims.
- It flags a specificity caveat the review should not overstate: the 2024 Commander/Retriever
  recycling work (Butkovic et al.) used LRP1 and other cargoes, not LDLR, so endosomal
  recycling machinery beyond the FDNPVY/ARH/AP-2 step is not LDLR-specific evidence. The
  review annotates only the adaptor step (GO:0035612), which is unaffected.
- It does not discuss the VSV entry-receptor role (PMID:23589850), reviewed here separately.

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
