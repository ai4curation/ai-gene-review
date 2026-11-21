# RHOA (human, P61586) curation notes

Deep research providers were unavailable in this environment; evidence below is from cached
publications and the UniProt record.

## Localization (benchmark-relevant)
- RHOA is **intracellular**: UniProt `SUBCELLULAR LOCATION: Cell membrane; Lipid-anchor; Cytoplasmic
  side.` plus cytosol (RhoGDI-bound), cell cortex, cleavage furrow, midbody, apical junction complex
  and postsynapse. It is not surface-exposed.
- `GO:0009898 cytoplasmic side of plasma membrane` accepted as the most precise membrane term;
  `cytoplasm` and `cell periphery` marked TOO_GENERAL; `cytoskeleton` modified to cell cortex +
  cleavage furrow (RHOA regulates rather than constitutes the cytoskeleton).
- Equatorial cortex recruitment: UniProt "Translocates to the equatorial region before furrow
  formation in a ECT2-dependent manner."

## Core functions
1. GTPase switch driving actomyosin contractility: "Regulates a signal transduction pathway linking
   plasma membrane receptors to the assembly of focal adhesions and actin stress fibers".
2. Cleavage furrow specification and cytokinesis: "Involved in a microtubule-dependent signal that
   is required for the myosin contractile ring formation during cell cycle cytokinesis";
   "Plays an essential role in cleavage furrow formation."
3. Apical junction assembly in epithelia: "Required for the apical junction formation of
   keratinocyte cell-cell adhesion".
- Postsynaptic actin remodelling retained as accepted process/location rows
  [PMID:21423166 "Local, persistent activation of Rho GTPases during plasticity of single dendritic
  spines"].

## Review decisions
- 54 generic `GO:0005515` rows REMOVEd under the protein-binding policy; myosin binding and protein
  kinase binding retained as informative.
- `GO:0090324 negative regulation of oxidative phosphorylation` and `GO:1903427 negative regulation
  of ROS biosynthetic process` marked over-annotated (electronically transferred, no mechanism).
- Numerous tissue/organismal outputs (bone, tooth, T-cell development, angiogenesis, valve
  formation) kept as non-core.
