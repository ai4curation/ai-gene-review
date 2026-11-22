# KIT (human, P10721) — curation notes

Research journal for the GO annotation review of human **KIT** (Mast/stem cell growth
factor receptor Kit; SCFR / c-Kit / CD117). All assertions carry inline provenance.

## Identity and architecture

- KIT is a 976-aa, ~145 kDa type III (class III) single-pass transmembrane receptor
  tyrosine kinase, EC 2.7.10.1. Extracellular region = five Ig-like domains (D1–D5);
  single TM helix; cytoplasmic juxtamembrane autoinhibitory segment; split
  (kinase-insert–interrupted) tyrosine kinase domain (UniProt P10721; deep-research
  falcon report). Aliases: SCFR, c-Kit, CD117, Piebald trait protein.
- Ligand = stem cell factor (SCF), encoded by **KITLG** (P21583; mouse Kitl P05532);
  soluble and membrane-bound forms; noncovalent homodimer.

## Core molecular function

- KIT is a **stem cell factor receptor** and **transmembrane receptor tyrosine kinase**.
  SCF binding drives receptor homodimerization, relieving juxtamembrane autoinhibition and
  enabling reciprocal trans-autophosphorylation, which activates the kinase and creates
  phosphotyrosine docking sites for SH2/PTB effectors
  [PMID:17662946 "KIT dimerization is driven by SCF binding whose sole role is to bring two KIT molecules together"].
- Ligand-independent constitutive kinase activation is the disease mechanism (D816V, JM
  ITDs)
  [PMID:21640708 "induced constitutive activation of c-KIT kinase in the absence of ligand"].
- KIT has intrinsic catalytic activity increased by ligand-induced dimerization
  [PMID:20100931 "Unlike the BCR, KIT possesses inherent catalytic activity which is increased upon SCF-induced KIT dimerization"].
- Early demonstration of ligand-induced dimerization coupled to kinase activation
  [PMID:1721869 "dimerization of the receptor is correlated with activation of its kinase"].

## Downstream signaling (the Kit signaling pathway, GO:0038109)

- Autophosphorylated KIT activates RAS–RAF–MEK–ERK (MAPK), PI3K–AKT, PLCγ–PKC/Ca²⁺,
  SRC-family kinase and JAK–STAT pathways (UniProt FUNCTION; Roskoski review
  PMID:16129412; deep-research falcon report). UniProt: "Activates the AKT1 signaling
  pathway by phosphorylation of PIK3R1"; "Promotes activation of STAT family members
  STAT1, STAT3, STAT5A and STAT5B".
- STAT activation downstream of KIT is experimentally established
  [PMID:21135090 "STAT1, -3, and -5 proteins are activated downstream of the KIT-Asp(816) mutant"];
  [PMID:21135090 "can directly phosphorylate STATs on the activation-specific tyrosine residues in vitro"].
- Effector recruitment: KIT phosphotyrosines are bound by SH2-domain proteins GRB2/GRB7
  (PMID:10377264), PI3K regulatory subunit PIK3R1 (PMID:1382595, PMID:7537096,
  PMID:25241761), PLCG1, SHP2/PTPN11 (PMID:7523381), SHP1/PTPN6, PTPRU (PMID:10397721),
  CRK (PMID:12878163), MPDZ/MUPP1 (PMID:11018522), and many others (UniProt SUBUNIT
  section; large-scale interactome PMID:24728074, PMID:36115835). These interactions are
  captured as generic GO:0005515 "protein binding" IPI rows.

## Biological roles (lineage / developmental outputs — non-core to the receptor activity)

- KIT–SCF signaling is essential in hematopoietic stem/progenitor cells, mast cells
  (development, survival, proliferation, chemotaxis, degranulation), melanocytes
  (development, migration, adhesion → pigmentation), germ cells / gametogenesis, and
  gastrointestinal interstitial cells of Cajal (pacemaker; smooth muscle contraction)
  (UniProt FUNCTION; deep-research falcon report; Roskoski PMID:16129412).
- Loss of function → piebaldism (KIT dominant-negative / LOF variants, e.g. PMID:1717985);
  gain of function → GIST, mastocytosis (D816V), subsets of AML, germ-cell tumors,
  melanoma (UniProt variants; PMID:9990072 D816V mastocytosis).
- Mast-cell effector responses shown to be KIT/SCF dependent (in a CD72 study)
  [PMID:20100931 "significantly reducing SCF-induced human mast cell chemotaxis"].
- SCF-activated KIT induces actin reorganization and chemotaxis
  [PMID:1721869 "induce circular actin reorganization"].

## Localization

- Mature full-length KIT functions at the **plasma membrane** (type I topology: ectodomain
  external, kinase domain cytoplasmic) (UniProt SUBCELLULAR LOCATION; deep-research).
- The KIT ectodomain is shed by TACE/ADAM17, producing a soluble extracellular form
  [PMID:14625290 "release of c-Kit ectodomain"].
- TR-KIT, a truncated intracellular isoform (P10721-4), is cytoplasmic and expressed in
  haploid germ cells / spermatozoa
  [PMID:20601678 "localized both in the equatorial segment and in the sub-acrosomal region"].

## Points relevant to specific annotations

- GO:0005515 "protein binding" (IPI, ~90 rows): uninformative generic term; per repo
  policy REMOVE (interactions are real but the term conveys no function). The KITLG
  interaction (PMID:17662946) is the ligand and is MODIFY → stem cell factor receptor
  activity (GO:0005020).
- GO:0004672 "protein kinase activity" (IEA, InterPro): too general; KIT is specifically a
  transmembrane receptor tyrosine kinase → MODIFY to GO:0004714.
- GO:0046686 "response to cadmium ion" (IEA from rat ortholog): a well-known promiscuous
  over-transfer with no KIT-specific mechanistic basis → MARK_AS_OVER_ANNOTATED.
- GO:0002020 "protease binding" (IEA ortholog): cannot verify which protease / mechanism →
  UNDECIDED.
- GO:1905065 vSMC differentiation (IDA PMID:19088079): paper foregrounds miR-221/PDGF; KIT
  is a downregulated target whose loss shifts vSMC to a less contractile phenotype
  [PMID:19088079 "down-regulation of the targets c-Kit and p27Kip1"] — peripheral, non-core.
- Plasma membrane (GO:0005886) has one IBA/IDA/IEA plus a large block of Reactome TAS rows;
  all ACCEPT (correct core location).
