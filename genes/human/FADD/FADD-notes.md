# FADD notes

## 2026-09-30

- The core human FADD/MORT1 activity is a death-fold adaptor function, not a catalytic one. The
  two original discovery papers identify FADD as a Fas/APO1 death-domain interactor and already
  separate its C-terminal death-domain receptor contact from an N-terminal self-association
  region [PMID:7538907 FADD, a novel death domain-containing protein, interacts with the death
  domain of Fas and initiates apoptosis, "identified a novel interacting protein, FADD";
  PMID:7536190 A novel protein that interacts with the death domain of Fas/APO1 contains a
  sequence motif related to the death domain, "the region upstream to the death domain prompts
  self-association of the protein"].
- In FAS/CD95 signaling, FADD is the DISC adaptor between the receptor death domain and
  initiator-caspase DEDs. Medema et al. found that CD95 recruits FADD/MORT1 into the DISC and
  that FLICE/CASP8 contacts FADD through its N-terminal DED [PMID:9184224 FLICE is activated by
  association with the CD95 death-inducing signaling complex (DISC), "Here we show that FLICE
  binds to FADD through"]. Later NMR/mutational data refine this to a death-domain contact with
  CD95 and a DED contact with procaspase-8 [PMID:16762833 The structure of FADD and its mode of
  interaction with procaspase-8, "self-association surface necessary to form a productive
  complex"].
- CASP10 and CFLAR/cFLIP bind the same FADD DED assembly logic: caspase-8 and caspase-10 DEDs
  both interact with FADD [PMID:11717445 Caspase-10 is an initiator caspase in death receptor
  signaling, "both interact with the death-effector domain of FADD"], and 2024 structures of
  FADD-procaspase-8-cFLIP complexes describe the ternary DED assemblies that route death-receptor
  inputs to apoptosis or survival/necroptosis decisions [PMID:38710704 Deciphering DED assembly
  mechanisms in FADD-procaspase-8-cFLIP complexes regulating apoptosis, "Fas-associated protein
  with death domain (FADD), procaspase-8, and cellular"].
- The TRAIL and TNFR1 rows should be curated as the same class of FADD adaptor biology rather
  than as many standalone generic `protein binding` assertions. In death-receptor pathways,
  ligand-bound FAS and TRAIL receptors recruit FADD, while TNFR1 can form a secondary TRADD/RIPK1
  complex that recruits FADD and caspase-8; enteropathogenic E. coli NleB1 blocks this by
  GlcNAcylating FADD Arg117 [PMID:24025841 Bacterial blockade of death receptor signaling by
  glycosylation of death domains, "FADD then recruits pro-caspase-8 forming the death-inducing
  signalling complex (DISC)"]. The NleB1 physical interaction itself belongs on the pathogen
  effector, not as a FADD molecular function.
- FADD also has noncanonical cytosolic branches that should remain non-core: it is part of
  RIPK1/CASP8/CFLAR ripoptosome complexes [PMID:21737330 cIAPs block Ripoptosome formation, a
  RIP1/caspase-8 containing intracellular cell death complex differentially regulated by cFLIP
  isoforms, "It contains RIP1, FADD, caspase-8, caspase-10"], and human FADD deficiency impairs
  both Fas-dependent apoptosis and interferon-mediated antiviral immunity [PMID:21109225
  Whole-exome-sequencing-based discovery of human FADD deficiency, "viral infections result from
  impaired interferon immunity"].
- I kept the broad mouse-derived lymphoid-organ, T-cell homeostasis, kidney, cocaine, mechanical
  stimulus, NF-kappaB, cytokine, and pathogen-response rows out of the core review. They read as
  downstream loss-of-function phenotypes or ARBA/Compara transfers, while the direct molecular
  work of FADD is assembling death receptor, ripoptosome, and antiviral adaptor complexes.
