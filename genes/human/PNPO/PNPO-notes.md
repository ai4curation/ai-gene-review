# PNPO (human) — gene review notes

## Identity
- UniProt: Q9NVS9 (PNPO_HUMAN), 261 aa, chromosome 17. HGNC:30260.
- RecName: Pyridoxine-5'-phosphate oxidase; AltName: Pyridoxamine-phosphate oxidase. EC 1.4.3.5.
  [file:human/PNPO/PNPO-uniprot.txt "RecName: Full=Pyridoxine-5'-phosphate oxidase"]
  [file:human/PNPO/PNPO-uniprot.txt "AltName: Full=Pyridoxamine-phosphate oxidase"]

## Core molecular function — FMN-dependent oxidase
- Catalyzes the terminal, rate-limiting step of pyridoxal 5'-phosphate (PLP, active vitamin B6) synthesis:
  oxidation of pyridoxine 5'-phosphate (PNP) OR pyridoxamine 5'-phosphate (PMP) to PLP.
  [file:human/PNPO/PNPO-uniprot.txt "Catalyzes the oxidation of either pyridoxine 5'-phosphate"]
- Reaction 1: PNP + O2 = PLP + H2O2 (Rhea:15149; EC 1.4.3.5).
  [file:human/PNPO/PNPO-uniprot.txt "pyridoxine 5'-phosphate + O2 = pyridoxal 5'-phosphate + H2O2"]
- Reaction 2: PMP + O2 + H2O = PLP + H2O2 + NH4(+) (Rhea:15817).
  [file:human/PNPO/PNPO-uniprot.txt "pyridoxamine 5'-phosphate + O2 + H2O = pyridoxal 5'-phosphate"]
- Cofactor: FMN, 1 per subunit (flavoprotein).
  [file:human/PNPO/PNPO-uniprot.txt "Binds 1 FMN per subunit"]
- GO:0004733 "pyridoxamine phosphate oxidase activity" is the correct catalytic MF; the GO definition
  explicitly covers BOTH PNP and PMP oxidation ("This activity can also oxidize pyridoxine 5'-phosphate
  to pyridoxal 5'-phosphate + H2O2") — verified via OLS. So the single GO term captures both UniProt reactions.
- Kinetics: KM 2.1 uM (PNP), 6.2 uM (PMP); low turnover (~0.2 s^-1).
  [file:human/PNPO/PNPO-uniprot.txt "KM=2.1 uM for pyridoxine 5'-phosphate"]
  [PMID:12824491 "exhibits a low catalytic rate constant of approximately 0.2 sec(-1)"]

## Structure / quaternary
- Homodimer; binds one PLP tightly per subunit (product inhibition).
  [file:human/PNPO/PNPO-uniprot.txt "SUBUNIT: Homodimer"]
  [PMID:12824491 "The purified human enzyme is a homodimer"]
  [PMID:12824491 "the human enzyme binds one molecule of pyridoxal 5'-phosphate tightly on each subunit"]
- Crystal structure 1.95 A of residues 49-161 in complex with FMN and PLP (PDB 1NRG), plus later
  structures (6H00, 8ROS, etc.). Fold = FMN-binding split barrel; PNPOx family.
  [file:human/PNPO/PNPO-uniprot.txt "SIMILARITY: Belongs to the pyridoxamine 5'-phosphate oxidase family"]
- Product inhibition by PLP: "Pyridoxal 5'-phosphate is an effective product inhibitor."
  [PMID:12824491 "Pyridoxal 5'-phosphate is an effective product inhibitor"]

## Domain / truncation biology (PMID:15182361)
- Human brain PNPO expressed in E. coli; N- and C-terminal truncation series.
- Deletion of N-terminal 56 residues does NOT affect coenzyme binding or catalysis (so the N-terminal
  ~56 aa is dispensable), whereas deletion of residues 1-72 or the C-terminal 238-261 abolishes activity.
  [PMID:15182361 "deletion of the N-terminal 56 residues affects neither the binding of coenzyme nor catalytic activity"]
  [file:human/PNPO/PNPO-uniprot.txt "1..56 ... Missing: Has no effect on the catalytic activity"]
  [file:human/PNPO/PNPO-uniprot.txt "238..261 ... Missing: Loss of catalytic activity"]
- Tissue distribution: ubiquitous ("housekeeping"), highest in liver, skeletal muscle, kidney.
  [PMID:15182361 "The major sites of PNPO expression are liver, skeletal muscle and kidneys"]

## Pathway / localization
- Pathway: cofactor metabolism; PLP salvage — PLP from PMP (step 1/1) and PLP from PNP (step 1/1).
  [file:human/PNPO/PNPO-uniprot.txt "Cofactor metabolism; pyridoxal 5'-phosphate salvage"]
- Reactome: Vitamin B6 activation to pyridoxal phosphate (R-HSA-964975); reactions R-HSA-965019
  (PDXP->PXLP) and R-HSA-965079 (PXAP->PXLP), both localized to cytosol.
  [file:human/PNPO/PNPO-uniprot.txt "Reactome; R-HSA-964975; Vitamin B6 activation to pyridoxal phosphate"]
- Localization: cytosol (Reactome TAS; consistent with a soluble metabolic enzyme). A mitochondrion
  call exists via IBA (GO_Central) and HTP (FlyBase, PMID:34800366) but PNPO is canonically cytosolic;
  the cached PMID:34800366 (mouse mitochondrial proteome, Cell Metab 2021) does not mention PNPO in its
  extracted text. Treated as over-annotation, not removed (HTP is experimental-derived; IBA propagated).

## Disease
- PNPO deficiency (PNPOD, MIM:610090): neonatal/early-infantile epileptic encephalopathy; seizures
  respond to PLP but are resistant to pyridoxine.
  [file:human/PNPO/PNPO-uniprot.txt "onset within hours of birth of a severe seizure disorder"]
  [PMID:15772097 "Seizures ceased with the administration of PLP, having been resistant to treatment with pyridoxine"]
- Pathogenic variants R229W (strong activity decrease), R229Q, R225H; expression studies confirmed
  R229W markedly reduces oxidase activity, splice/stop mutations null.
  [PMID:15772097 "the missense mutation (R229W) markedly reduced pyridox(am)ine phosphate oxidase activity"]
  [file:human/PNPO/PNPO-uniprot.txt "R -> W (in PNPOD; strong activity decrease"]

## Interactions (GOA GO:0005515 IPI)
- Six bare "protein binding" IPI annotations from proteome-scale interactome / IntAct screens
  (PMID:25910212, 28514442, 32296183, 33961781) with partners AGTRAP(Q6RW13-2), CMTM5(Q96DZ9-2),
  LIME1(Q9H400), MTERF1(Q99551). UniProt lists the same IntAct partners.
  [file:human/PNPO/PNPO-uniprot.txt "AGTRAP; NbExp=6"]
- These are non-informative "protein binding" (GO:0005515) with no functional/complex interpretation for
  a metabolic enzyme; kept but MARK_AS_OVER_ANNOTATED per curation policy (do not REMOVE IPI).

## Review decisions summary
- Core MF: GO:0004733 (pyridoxamine phosphate oxidase activity, covers PNP+PMP) + GO:0010181 (FMN binding).
- Core BP: GO:0042823 (PLP biosynthetic process). GO:0008615 (pyridoxine biosynthetic process, IEA-KW) is
  a mislabel of the pathway (PNPO makes PLP from already-phosphorylated B6 vitamers, it does not synthesize
  pyridoxine) -> MODIFY to GO:0042823 / KEEP as vitamin B6 biosynthesis context.
- Cofactor-binding MFs GO:0030170 (PLP binding) and GO:0042803 (homodimerization) are real (structure)
  but supportive, not the core catalytic function -> ACCEPT / KEEP_AS_NON_CORE.
- Location cytosol (Reactome TAS) ACCEPT; mitochondrion (IBA + HTP) MARK_AS_OVER_ANNOTATED.
