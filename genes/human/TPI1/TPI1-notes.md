# TPI1 (human) review notes

UniProtKB:P60174, HGNC:12009, gene TPI1 (syn. TPI). Triosephosphate isomerase / TIM.

## Core biology (grounded in UniProt + cached PMIDs)

- Homodimer; 248-residue mature chain (Met1 removed), subunit ~26.7 kDa
  [PMID:6434534 "The enzyme is a dimeric molecule consisting of two identical polypeptide
  chains with 248 amino acid residues and a calculated subunit molecular mass of 26,750 daltons."].
- Catalyzes reversible interconversion of DHAP <-> D-glyceraldehyde-3-phosphate (G3P),
  EC 5.3.1.1, in glycolysis and gluconeogenesis
  [file:human/TPI1/TPI1-uniprot.txt FUNCTION: "catalyzes the interconversion between
  dihydroxyacetone phosphate (DHAP) and D-glyceraldehyde-3-phosphate (G3P) in glycolysis
  and gluconeogenesis"]. Near-perfect, diffusion-limited catalyst (textbook).
- Minor/side activity: methylglyoxal synthase (EC 4.2.3.3), producing the cytotoxic
  side-product methylglyoxal from DHAP
  [file:human/TPI1/TPI1-uniprot.txt "It is also responsible for the non-negligible
  production of methylglyoxal a reactive cytotoxic side-product"]. NON-CORE.
- Cytoplasmic/cytosolic [UniProt SUBCELLULAR LOCATION: Cytoplasm].
- Disease: Triosephosphate isomerase deficiency (TPID, MIM 615512): autosomal recessive
  multisystem disorder — congenital hemolytic anemia, progressive neuromuscular
  dysfunction, susceptibility to infection, cardiomyopathy; usually fatal in childhood.
  Most common allele = Glu104Asp (position 104), which impairs dimer formation /
  thermostability rather than catalysis
  [PMID:18562316 "the purified, recombinant mutant enzyme E104D, while exhibiting normal
  catalytic activity, shows impairments in the formation of active dimers and low
  thermostability"; PMID:2876430 "results in a thermolabile enzyme"].

## Annotation review reasoning

- MF triose-phosphate isomerase activity (GO:0004807): CORE. Multiple lines (IBA, IEA,
  EXP PMID:6434534, IDA PMID:18562316, TAS PMID:2579079, NAS PMID:2876430). ACCEPT the
  IBA/EXP/IDA; the older TAS/NAS are ACCEPT (redundant but not wrong).
- BP glycolytic process (GO:0006096), gluconeogenesis (GO:0006094), canonical glycolysis
  (GO:0061621): CORE processes. ACCEPT IBA / representative; IEA/TAS ACCEPT.
- glyceraldehyde-3-phosphate biosynthetic process (GO:0046166) and G3P metabolic process
  (GO:0019682): describe the reaction product/metabolism; ACCEPT (consistent with the
  glycolysis step producing G3P). IDA PMID:18562316 characterized the isomerase reaction.
- protein homodimerization activity (GO:0042803, IDA PMID:18562316): ACCEPT — obligate
  homodimer, structurally characterized; relevant to enzyme function (dimer = active unit).
- methylglyoxal synthase activity (GO:0008929) + methylglyoxal biosynthetic process
  (GO:0019242): real but minor SIDE activity -> KEEP_AS_NON_CORE (MARK_AS_OVER_ANNOTATED
  would understate it; it's genuine but not core). These are ISS/IEA from P00939 ortholog.
- protein binding (GO:0005515, IPI x4 refs): bare 'protein binding' — uninformative.
  Per policy, MARK_AS_OVER_ANNOTATED (do not REMOVE experimental IPIs). Partners are
  PCNA, TERF1, HTT, PKM/PLK/GAPDH-type (sperm), etc. — mostly interactome/moonlighting
  screens, not core catalytic function.
- ubiquitin protein ligase binding (GO:0031625, IPI PMID:19725078, Parkin/PARK2 O60260):
  MARK_AS_OVER_ANNOTATED — from a Parkin interactome proteomics screen; TPI1 is one of
  many glycolytic/mitochondrial proteins co-purifying; not a core molecular function.
- Localization: cytosol (GO:0005829) / cytoplasm (GO:0005737): ACCEPT (core location).
- extracellular exosome (GO:0070062), extracellular region (GO:0005576), nucleus
  (GO:0005634): HDA mass-spec detections in exosomes/body fluids/sperm nucleus. These
  are secondary detections (moonlighting/secretion/contamination), not the site of the
  core glycolytic function -> KEEP_AS_NON_CORE.
- isomerase activity (GO:0016853): parent of GO:0004807; too general -> MODIFY to the
  specific triose-phosphate isomerase activity term.

## Core functions
- MF: GO:0004807 triose-phosphate isomerase activity
- directly_involved_in: GO:0006096 glycolytic process; GO:0006094 gluconeogenesis
- located_in: GO:0005829 cytosol
