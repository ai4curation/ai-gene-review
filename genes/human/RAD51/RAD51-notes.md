# RAD51 (Q06609) gene review notes

Human RAD51 = DNA repair protein RAD51 homolog 1; RAD51 homolog A; FANCR
(Fanconi anemia complementation group R). The eukaryotic ortholog of *E. coli*
RecA and yeast Rad51 — the central recombinase of homologous recombination (HR).

## Core biology (established)

- **Recombinase / DNA strand exchange (core MF).** RAD51 binds ssDNA in an
  ATP-dependent manner to form a helical nucleoprotein (presynaptic) filament,
  searches for homology in duplex DNA, and catalyzes strand invasion/exchange to
  form a D-loop. [PMID:7988572 "The human Rad51 protein binds to single- and
  double-stranded DNA and exhibits DNA-dependent ATPase activity."]; [PMID:8929543
  "hRad51 promotes homologous pairing and strand exchange reactions in vitro."];
  [PMID:27694622 "which binds the ssDNA tail to form a nucleoprotein filament known
  as a presynaptic filament"]; [PMID:27694622 "displacing the homologous strand to
  form a displacement loop (D-loop)"].
- **ATP binding/hydrolysis regulates filament dynamics.** RAD51 is a self-inactivating
  ATPase; the ATP-bound filament is active, ATP hydrolysis (and slow ADP release)
  inactivates it; Ca2+ preserves the active filament by slowing hydrolysis, stimulating
  strand exchange. [PMID:15226506 "hRad51 protein possesses DNA-dependent ATPase
  activity"]; [PMID:15226506 "due to relatively rapid ATP hydrolysis and slow
  dissociation of ADP"]; [PMID:15226506 "stimulates DNA strand exchange activity of
  hRad51 protein"].
- **DSB repair via HR (core BP).** Essential effector of HR-mediated double-strand
  break repair; loaded onto RPA-coated 3' ssDNA by BRCA2/PALB2 and the RAD51 paralog
  mediators (BCDX2, RAD51B/C/D, XRCC2/3). UniProt FUNCTION; many IDA annotations
  (PMID:12442171, 18417535, 19303847, 27941124, 37499663, 38509361, etc.).
- **Replication fork protection/restart (core BP).** Recruited to stalled forks under
  replication stress; protects nascent DNA and enables fork restart. [PMID:18417535
  "Identification of a novel human Rad51 variant that promotes DNA strand exchange"];
  [PMID:22778135 "RAD51 mutants cause replication defects and chromosomal instability"];
  PMID:25585578 (FBH1/RAD51 ubiquitylation & fork stability).
- **Interstrand crosslink repair.** RAD51 has a role in ICL repair; a dominant RAD51
  variant separates ICL repair from HR. [PMID:26253028 "Function in DNA Interstrand
  Crosslink Repair Independent of Homologous Recombination"].
- **Nucleosome interaction.** Cryo-EM: RAD51 filament binds nucleosomal DNA and peels
  it from the histone octamer. [PMID:38509361 "directly bind to the nucleosomal DNA"];
  filament peels nucleosomal DNA (GO:0031491 nucleosome binding IDA).

## Non-core / context-specific

- **Meiotic HR (accessory).** By similarity RAD51 acts as a non-catalytic accessory
  factor for the meiosis-specific recombinase DMC1 (chromosome pairing/crossover);
  meiotic terms (GO:0007131, GO:0070192, GO:1990918, GO:0007127, GO:0000800 lateral
  element, GO:0051321, GO:0000793/0000794 condensed chromosome) are kept as NON_CORE
  in the human somatic context.
- **Mitochondrial mtDNA maintenance (separable).** With RAD51C/XRCC3, regulates mtDNA
  copy number under oxidative stress. [PMID:20413593 "identify human mtDNA as a novel
  Rad51 substrate"]; mitochondrion/mitochondrial matrix localization (GO:0005739,
  GO:0005759) kept NON_CORE.
- **Telomere maintenance via recombination (ALT context).** GO:0000722/0010833/0000781
  kept NON_CORE (ortholog ISS/IEA).
- Minor localizations kept NON_CORE: centrosome (GO:0005813), PML body (GO:0016605,
  PMID:11309417), nucleolus (GO:0005730 HPA), cytosol/cytoplasm/perinuclear
  (GO:0005829/0005737/0048471).

## Curation flags

- **GO:0099182 "presynaptic intermediate filament cytoskeleton" (IDA, PMID:18003859)
  is a MIS-MAPPING.** PMID:18003859 concerns disruption of the RAD51 *presynaptic
  (nucleoprotein) filament* of recombination, NOT a neuronal presynaptic cytoskeleton.
  [PMID:18003859 "disruption of Rad51 presynaptic filaments"]. Action: MODIFY →
  GO:0032993 protein-DNA complex.
- **GO:0140664 "ATP-dependent DNA damage sensor activity" (IEA InterPro2GO)** is an
  over-annotation; RAD51 is a recombinase, not a checkpoint damage sensor. MARK_AS_OVER_ANNOTATED.
- **GO:0000152 "nuclear ubiquitin ligase complex" (IDA ComplexPortal, PMID:14636569)** —
  RAD51 is a component of the BRCC (BRCA1/BRCA2) holoenzyme reported to have ubiquitin
  ligase activity; experimental, kept as NON_CORE (defer to ComplexPortal curator).
- **GO:1904631 "response to glucoside" (IEA rat ortholog)** — tangential; MARK_AS_OVER_ANNOTATED.
- **GO:0005515 protein binding** (83 IPI rows) and **GO:0032991 protein-containing
  complex**, **GO:0019899 enzyme binding** → MARK_AS_OVER_ANNOTATED (uninformative;
  specific partners incl. BRCA2, PALB2, RAD51AP1, RAD54L, XRCC3, RAD51C, TP53, SPIDR,
  FIGNL1, TOPBP1, MCM8/9 captured in UniProt SUBUNIT).
- **GO:0042802 identical protein binding** (9 IPI) → ACCEPT: reflects RAD51 homo-
  oligomerization into the filament, which is functionally central.

## Disease

Biallelic/dominant-negative RAD51 variant causes a Fanconi anemia-like phenotype
(FANCR); [PMID:26681308 "dominant-negative mutation" in RAD51].
