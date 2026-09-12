# PDXP (chronophin / pyridoxal 5'-phosphate phosphatase) — review notes

UniProt: Q96GD0 (PLPP_HUMAN). Gene: PDXP (HGNC:30259). Synonyms: CIN, PLP, PLPP, "chronophin".
Taxon: Homo sapiens (9606). 296 aa, ~31.7 kDa. HAD-like hydrolase superfamily. PE 1 (protein level).

## Two documented physiological activities (a genuine moonlighting enzyme)

PDXP is one enzyme with two well-characterized, mechanistically distinct catalytic activities:

### 1. Pyridoxal 5'-phosphate (PLP) phosphatase — vitamin B6 homeostasis (primary/ancestral)
- "Functions as a pyridoxal phosphate (PLP) phosphatase, which also catalyzes the dephosphorylation
  of pyridoxine 5'-phosphate (PNP) and pyridoxamine 5'-phosphate (PMP), with order of substrate
  preference PLP > PNP > PMP and therefore plays a role in vitamin B6 metabolism"
  [file:human/PDXP/PDXP-uniprot.txt CC FUNCTION; ECO:0000269|PubMed:14522954, PubMed:8132548].
- EC 3.1.3.74 (pyridoxal phosphatase). Rhea RHEA:20533 PLP + H2O = pyridoxal + phosphate.
- Km for PLP = 2.5 uM; kcat = 1.52 s^-1 (PLP the best substrate); PNP Km 43.4 uM; PMP Km 80.6 uM
  [file:human/PDXP/PDXP-uniprot.txt BIOPHYSICOCHEMICAL PROPERTIES].
- Cloned/expressed as the human PLP phosphatase; recombinant enzyme mirrors the erythrocyte enzyme
  [PMID:14522954 "Catalytically active human PLP phosphatase was expressed in Escherichia coli, and
  characteristics of the recombinant enzyme were similar to those of erythrocyte enzyme"].
- Erythrocyte PLP-specific phosphatase; essential active-site cysteine, protected by substrate PLP
  [PMID:8132548 "Pyridoxal-specific phosphatase purified from human erythrocytes was inactivated by
  a variety of thiol-specific reagents"; "The presence of pyridoxal phosphate, a substrate, or
  inorganic phosphate, a competitive inhibitor, protected the enzyme from inactivation"].
- By degrading PLP (the active B6 cofactor) it opposes PDXK/PNPO (which make PLP), setting cellular
  PLP levels. GO BP for this is pyridoxal 5'-phosphate catabolic process (GO:0032361).

### 2. Cofilin/ADF (phospho-Ser3) protein-serine phosphatase — actin dynamics (moonlighting)
- "Also functions as a protein serine phosphatase that specifically dephosphorylates 'Ser-3' in
  proteins of the actin-depolymerizing factor (ADF)/cofilin family like CFL1 and DSTN. Thereby,
  regulates cofilin-dependent actin cytoskeleton reorganization, being required for normal progress
  through mitosis and normal cytokinesis. Does not dephosphorylate phosphothreonines in LIMK1. Does
  not dephosphorylate peptides containing phosphotyrosine"
  [file:human/PDXP/PDXP-uniprot.txt CC FUNCTION; ECO:0000269|PubMed:15580268].
- EC 3.1.3.16 (protein-serine phosphatase); Rhea RHEA:20629.
- Discovery paper: "chronophin (CIN), a unique cofilin-activating phosphatase of the haloacid
  dehalogenase (HAD) superfamily. CIN directly dephosphorylates cofilin with high specificity and
  colocalizes with cofilin in motile and dividing cells. Loss of CIN activity blocks phosphocycling
  of cofilin, stabilizes F-actin structures and causes massive cell division defects" [PMID:15580268].
- Active-site nucleophile Asp25; D25N mutation abolishes protein phosphatase activity
  [file:human/PDXP/PDXP-uniprot.txt FT MUTAGEN 25 "D->N: Abolishes protein phosphatase activity"].

## Cofactor / catalytic mechanism
- Mg(2+)-dependent HAD phosphatase. "Name=Mg(2+) ... Note=Divalent metal ions. Mg(2+) is the most
  effective" [file:human/PDXP/PDXP-uniprot.txt COFACTOR]. Structures show Mg(2+) coordinated by
  Asp25/Asp27/Asp238 [FT BINDING]. Inhibited by NaF, Zn2+, Ca2+, Mn2+ and EDTA
  [file:human/PDXP/PDXP-uniprot.txt ACTIVITY REGULATION].
- Magnesium ion binding (GO:0000287) is a legitimate core MF supporting both catalytic activities.

## Quaternary structure & localization
- Homodimer [file:human/PDXP/PDXP-uniprot.txt SUBUNIT "Homodimer" ECO:0000269|PubMed:14522954].
- Cytoplasm/cytosol; also cytoskeleton and (peripherally) ruffle/lamellipodium/cell membrane, where
  it colocalizes with the actin cytoskeleton; dynamic relocalization through mitosis to cell poles,
  cleavage furrow, contractile ring, midbody during cytokinesis
  [file:human/PDXP/PDXP-uniprot.txt SUBCELLULAR LOCATION; ECO:0000269|PubMed:15580268].
- Primary/soluble location is cytosol (GO:0005829, IDA). The membrane/cytoskeleton localizations
  reflect where the actin-regulatory pool acts; peripheral, not integral membrane.

## Hsp90 / ATP-sensing / cofilin-actin rod formation (energy stress; neurodegeneration link)
- PMID:19000834 (full text available) shows CIN binds Hsp90β; the CIN/Hsp90 interaction is
  ATP-enhanced, and Hsp90 inhibits CIN cofilin-phosphatase activity in vitro. ATP depletion (or
  Hsp90 inhibition with 17AAG) releases CIN, driving cofilin dephosphorylation and assembly of
  cofilin/actin rods in HeLa cells and primary neurons.
  - "GST-CIN ... co-precipitated an endogenous ~90kDa band ... identified as Hsp90β" → heat shock
    protein binding (GO:0031072) [PMID:19000834].
  - "the addition of Hsp90 attenuated CIN-dependent cofilin dephosphorylation ... indicating that
    Hsp90 has inhibitory effects on CIN activity" [PMID:19000834].
  - CIN required for cofilin/actin rod formation under ATP depletion → actin rod assembly
    (GO:0031247) and cellular response to ATP (GO:0071318) [PMID:19000834].
  - These MGI-assigned IDA annotations (GO:0004721, GO:0031072, GO:0031247, GO:0071318) derive from
    this paper; work spans human CIN (HeLa/bovine brain) and mouse neurons. Keep; the actin-rod /
    ATP-response and Hsp90-binding roles are downstream/regulatory (non-core) of the two core MFs.

## PMID:17500066 (protein binding, IntAct) — cofilin pathway scaffolding via beta-arrestin
- Abstract-only. PAR-2 → beta-arrestin-dependent cofilin dephosphorylation "requires ... the
  activity of a recently identified cofilin-specific phosphatase (chronophin)"; "Beta-arrestins can
  interact with cofilin, LIMK, and chronophin and colocalize with them in membrane protrusions"
  [PMID:17500066]. Supports the actin/cofilin context and a physical interaction (beta-arrestin);
  GO:0005515 bare "protein binding" IPI is uninformative → MARK_AS_OVER_ANNOTATED (do not remove IPI).

## Curation summary (actions)
- Core MF #1: GO:0033883 pyridoxal phosphatase activity (IDA, PMIDs 14522954/8132548) — ACCEPT.
- Core MF #2: GO:0004721 phosphoprotein phosphatase activity (IDA, PMID:15580268) — the cofilin/ADF
  Ser3 protein-serine phosphatase; genuine second physiological MF. ACCEPT as core.
  - GO:0004722 protein serine/threonine phosphatase activity: EXP (PMID:15580268) is defensible but
    slightly imprecise (PDXP acts on Ser only, NOT Thr — it does not dephosphorylate LIMK1 pThr);
    MODIFY toward GO:0004721. The IEA/EC-derived GO:0004722 (from EC 3.1.3.16) is an over-broad
    electronic call → MARK_AS_OVER_ANNOTATED.
- Core cofactor MF: GO:0000287 magnesium ion binding (ISS/IEA) — ACCEPT (ISS)/KEEP.
- Core BP #1: GO:0032361 pyridoxal 5'-phosphate catabolic process (IDA) — ACCEPT.
- Core CC: GO:0005829 cytosol (IDA, PMID:15580268) — ACCEPT.
- GO:0016311 dephosphorylation (IDA) is a redundant generic parent of the specific catabolic/protein
  dephosphorylation processes → MARK_AS_OVER_ANNOTATED (too general).
- GO:0016791 phosphatase activity (IEA, InterPro) and GO:0004722 (IEA EC) — over-broad electronic →
  MARK_AS_OVER_ANNOTATED / MODIFY.
- Actin-cytoskeleton BP (GO:0030836 positive reg. actin filament depolymerization IMP, GO:0006470
  protein dephosphorylation IDA) — ACCEPT (moonlighting actin role, well supported by PMID:15580268).
- Mitosis/cytokinesis BP (GO:0007088, GO:0032465 IMP PMID:15580268) — KEEP_AS_NON_CORE (downstream
  cellular consequence of cofilin regulation, not the molecular core).
- Actin-rod / ATP / Hsp90 (GO:0031247, GO:0071318, GO:0031072 IDA PMID:19000834) — KEEP_AS_NON_CORE
  (energy-stress / neuronal regulatory branch).
- Colocalization CCs (actin cytoskeleton, lamellipodium, midbody, cleavage furrow, ruffle membrane,
  contractile ring, plasma membrane; colocalizes_with IDA) — KEEP_AS_NON_CORE (where the actin pool
  acts; not the primary soluble location).
- SubCell IEA CCs (cytoskeleton, plasma membrane, lamellipodium membrane, ruffle membrane) — these
  are peripheral/dynamic; KEEP_AS_NON_CORE. Duplicate cytosol IEA — ACCEPT (redundant with IDA).
- IBA cytoplasm/cytosol (GO:0005737, GO:0005829) — ACCEPT/KEEP_AS_NON_CORE.
- GO:0042803 protein homodimerization activity (IEA, Ensembl) — homodimer is documented (SUBUNIT);
  KEEP_AS_NON_CORE (structural, not the enzymatic core).
- GO:0005515 protein binding IPI (PMID:17500066, beta-arrestin) — MARK_AS_OVER_ANNOTATED (bare
  protein binding, uninformative; never REMOVE an IPI).
