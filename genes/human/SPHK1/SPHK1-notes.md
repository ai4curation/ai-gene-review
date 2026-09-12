# SPHK1 (Q9NYA1) — curation notes

## Gene identity and core biochemistry

SPHK1 = sphingosine kinase 1 (HGNC:11240). A cytosolic, DAGK-like lipid kinase
that phosphorylates the free sphingoid base sphingosine to sphingosine
1-phosphate (S1P), the bioactive signaling lipid.

- UniProt RecName "Sphingosine kinase 1"; EC=2.7.1.91; belongs to a diacylglycerol
  kinase-like lipid kinase family (Pfam PF00781 DAGK_cat; DOMAIN 12..159 "DAGKc").
  [file:human/SPHK1/SPHK1-uniprot.txt]
- FUNCTION: "Catalyzes the phosphorylation of sphingosine to form sphingosine
  1-phosphate (SPP), a lipid mediator with both intra- and extracellular functions.
  Also acts on D-erythro-sphingosine and to a lesser extent sphinganine, but not
  other lipids" [file:human/SPHK1/SPHK1-uniprot.txt]
- Substrate specificity confirmed experimentally: "hSPHK1 also specifically
  phosphorylated D-erythro-sphingosine and to a lesser extent sphinganine, but not
  other lipids, such as D,L-threo-dihydrosphingosine, N, N-dimethylsphingosine,
  diacylglycerol, ceramide, or phosphatidylinositol." [PMID:10802064]
- Cofactor Mg2+ [file:human/SPHK1/SPHK1-uniprot.txt, "Name=Mg(2+)"]; kinetics
  KM=14 uM sphingosine, KM=77 uM ATP [PMID:10947957].
- Crystal structures (2.0–2.3 Å) show a two-domain architecture with the catalytic
  site in a cleft and a hydrophobic lipid-binding pocket; Asp81 is the catalytic
  proton donor/acceptor (D81A abolishes activity). [PMID:23602659]
- ATP-binding site: nucleotide-binding motif SGDGX(17-21)K; Gly82 involved in ATP
  binding (G82D loss of activity). [PMID:12393916; PMID:20577214]

## Localization and activation

- Predominantly cytosolic but shuttles to nucleus (two functional NES, CRM1-dependent
  export) [PMID:14575709] and translocates to plasma membrane on activation.
- Membrane translocation is driven by ERK1/2 phosphorylation at Ser225 and is
  CIB1 (calcium/integrin-binding protein 1)-dependent; CIB1 binds SK1 in a
  Ca2+-dependent manner at the "calmodulin-binding site" and acts as a
  Ca2+-myristoyl switch. [PMID:19854831]
- Phosphorylation-driven plasma-membrane translocation (not just increased catalytic
  activity) is what drives oncogenic signaling: the nonphosphorylatable S225A mutant
  retains full catalytic activity but loses transforming ability; artificially
  membrane-targeting S225A restores it. [PMID:15623571, full text]
- Dephosphorylation/deactivation is by PP2A; the B'α (PPP2R5A) regulatory subunit
  binds the SK1 C-terminus and is required for SK1 dephosphorylation. [PMID:21075214]
- Binds calmodulin (Ca2+-dependent) [PMID:10947957; PMID:12393916].
- Membrane recruitment via direct binding of anionic (negatively charged) lipids
  with preference for high positive membrane curvature: "SPHK1-FLAG bound to
  liposomes containing negatively charged" lipids; SPHK1 "binds to negatively
  charged membranes with a preference for high positive curvature". [PMID:24929359]

## Downstream / consequence-of-S1P functions (mostly non-core for SPHK1 itself)

- Pro-survival / anti-apoptotic and proliferative: overexpression blocks apoptosis
  and confers growth advantage; opposite of pro-apoptotic SPHK2. [PMID:12441135;
  PMID:16118219]
- Opposite of SPHK2 on ceramide: "SphK1 and SphK2 have opposing roles in the
  regulation of ceramide biosynthesis"; SPHK1 lowers ceramide. [PMID:16118219]
- Estrogen-dependent breast tumorigenesis, angiogenesis (higher microvessel density),
  ERK1/2 activation. [PMID:12441135]
- Vascular tone / RhoA-Rho kinase myogenic responses in smooth muscle. [PMID:12847068]
- TNF/NF-κB inflammatory signaling: intracellular S1P produced by SphK1 is the
  "missing cofactor" that binds the RING domain of TRAF2 and stimulates its E3
  ligase activity, driving Lys63-linked polyubiquitination of RIP1 and NF-κB
  activation → IL-17. This is S1P-receptor-independent ("inside-out"-independent).
  [PMID:20577214, full text]
- In parallel to NF-κB, SphK1 promotes TNF-induced p38 MAPK phosphorylation and
  thereby SUPPRESSES RANTES/CCL5 (loss of SK1 potentiates RANTES). [PMID:23935096]
- Osteoclastogenesis regulation (dichotomous, RANKL-induced). [PMID:17124500]
- S1P/S1PR2-driven ERM phosphorylation and filopodia formation — SPHK1 supplies the
  S1P endogenously; the receptor activity is S1PR2, not SPHK1. [PMID:23106337]

## Endocytosis / membrane trafficking (a partly kinase-independent role)

- SPHK1 is recruited to early endocytic intermediates and clathrin-coated pits;
  it is "highly enriched in nerve terminals" (presynapse). It coats narrow N-BAR-
  positive tubular invaginations. [PMID:24929359]
- Sphingosine and SPHK1 drive endocytic membrane trafficking / dilated late
  endosomes; SPHK1 recruits endophilin-A2/B1; role in later endosomal
  maturation/membrane fusion is partly independent of kinase activity.
  [PMID:24929359; PMID:28049734]

## Moonlighting acetyltransferase (neuronal, By similarity from mouse Q8CI15)

- Neuronal SphK1 acetylates COX2/PTGS2 (serine acetyltransferase, acetyl-CoA
  dependent), promoting secretion of specialized pro-resolving mediators (15-R-
  lipoxin A4); relevant to Alzheimer's disease neuroinflammation. In human this is
  ISS/By similarity to mouse Q8CI15. [PMID:29662056; file:human/SPHK1/SPHK1-uniprot.txt]

## Interactors (IPI, mostly "protein binding" — over-annotated as bare GO:0005515)

- SPHKAP/SKIP (Q2M3C7), negative regulator [PMID:12080051]
- FHL2/SLIM3 (Q14192), inhibitor in cardiomyocytes [PMID:16888242]
- CTSB/cathepsin B (P07858), proteolytic cleavage in vitro [PMID:17064696]
- TRAF6 (Q9Y4K3) — IntAct with/from in RANKL/osteoclast paper [PMID:17124500]
- EEF1A1 (P68104), directly enhances SK1 catalytic activity ~3-fold [PMID:18263879;
  PMID:20838377]
- CIB1 (Q99828), Ca2+-dependent, mediates PM translocation [PMID:19854831]
- PP2A B'α / PPP2R5A (Q15172), protein phosphatase 2A binding, dephosphorylation
  [PMID:21075214]

## Curation flags

- GO:0038036 "sphingosine-1-phosphate receptor activity" (IMP PMID:23106337 and
  IEA ARBA) is WRONG for SPHK1: SPHK1 is the kinase that PRODUCES S1P; the receptor
  in that paper is S1PR2. Bioinformatic/IEA propagation error. MF wrong-branch.
- GO:0003677 "DNA binding" (IDA MGI, PMID:12393916): that paper is about the
  ATP/nucleotide-binding site (FSBA affinity labeling), NOT DNA binding. Almost
  certainly a curation slip (nucleotide-binding → DNA binding). Experimental so
  not REMOVE; MARK_AS_OVER_ANNOTATED / UNDECIDED.
- GO:0046512 "sphingosine biosynthetic process" is the biosynthesis of the
  sphingosine base itself; SPHK1 CONSUMES sphingosine. Better BP is sphingosine
  metabolic process (GO:0006670) / sphingolipid metabolic/biosynthetic. IMP/IGI/IBA.
- Many downstream physiology terms (angiogenesis, smooth-muscle contraction,
  cell growth/migration, IL-17, phagocytosis, neuroinflammation, apoptosis) are
  consequences of S1P signaling, not the core molecular function → KEEP_AS_NON_CORE
  or MARK_AS_OVER_ANNOTATED.

## Core functions (summary)

- MF: sphingosine kinase activity (GO:0008481); ATP binding (GO:0005524);
  calmodulin binding (GO:0005516).
- BP: sphingosine metabolic process (GO:0006670) → S1P production; sphingolipid
  biosynthesis.
- CC: cytosol (GO:0005829); plasma membrane (GO:0005886, on activation).
