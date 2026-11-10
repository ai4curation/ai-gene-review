# Map3k5 (rat ASK1) - manual literature research

No deep-research API was available for this session, so this summary was compiled
by hand from the cached publications in `publications/`, the rat UniProt record
(A0A8I6AEL0, unreviewed TrEMBL), and the reviewed human ortholog record (Q99683,
`genes/human/MAP3K5/MAP3K5-uniprot.txt`). All statements carry inline provenance.

## Identity

- Rat Map3k5 (RGD:1306565, GeneID 365057), 1381 aa, TrEMBL entry A0A8I6AEL0. The
  entry has a protein kinase domain at 687-945 (PROSITE PS50011), an ATP-binding
  Lys at 716 and a catalytic proton acceptor at 810 (PROSITE-ProRule), and the
  ASK-specific domain set: ASK_PH (PF19039), DRHyd-ASK (PF20309), HisK-N-like
  (PF20302), MAP3K_TRAF_bd (PF13281), and a C-terminal coiled coil (1252-1286)
  [file:rat/Map3k5/Map3k5-uniprot.txt]. CDD classifies the kinase domain as
  cd06624 STKc_ASK. The rat entry carries no curated free text; function is
  inferred from the orthologs plus a set of rat physiology papers.

## Molecular function (ortholog-established)

- ASK1 was identified as a MAPKKK that "activated two different subgroups of MAP
  kinase kinases (MAPKK), SEK1 (or MKK4) and MKK3/MAPKK6 (or MKK6), which in turn
  activated stress-activated protein kinase (SAPK, also known as JNK ...) and p38"
  [PMID:8974401, abstract].
- Human UniProt: "acts as an upstream activator of the MKK/JNK signal transduction
  cascade and the p38 MAPK signal transduction cascade through the phosphorylation
  and activation of several MAP kinase kinases like MAP2K4/SEK1, MAP2K3/MKK3,
  MAP2K6/MKK6 and MAP2K7/MKK7" [file:human/MAP3K5/MAP3K5-uniprot.txt CC FUNCTION,
  ECO:0000269 with many PMIDs].
- Regulation: reduced thioredoxin binds the N-terminus and inhibits ASK1; "Expression
  of Trx inhibited ASK1 kinase activity and the subsequent ASK1-dependent apoptosis"
  [PMID:9564042]. ASK1 "appears to form a silent homo-oligomer through its C-terminal
  coiled-coil region in non-stressed cells" and H2O2 triggers trans-autophosphorylation
  of the activation-loop Thr [PMID:11920685]. TRAF2 binds ASK1 in a TNF-dependent manner
  and is required for TNF-induced ASK1 activation [PMID:9774977]. ER stress activates
  ASK1 "through formation of an IRE1-TRAF2-ASK1 complex" [PMID:12050113]. Negative
  regulators include 14-3-3 (phospho-Ser966/967), Akt (Ser83), PP5, IGF1R signalling
  [file:human/MAP3K5/MAP3K5-uniprot.txt; PMID:12556535; PMID:16648474; PMID:19451227].
  Positive upstream kinase MPK38/MELK phosphorylates Thr838 [PMID:18948261].

## Rat-specific experimental evidence

- **PMID:20550965 (full text)** - Isolated perfused rat heart. ASK1 was
  immunoprecipitated "from ischaemic and control hearts and assayed its activity in an
  immune-complex kinase assay" with myelin basic protein as substrate. "The MAPKKK,
  ASK1, was strongly activated late during ischaemia, with a similar time course to that
  of MKK6", and expression of ASK1 in neonatal rat cardiomyocytes "preferentially
  activated MKK6 rather than MKK3". The authors conclude "during cardiac ischaemia ASK1
  couples preferentially to p38 rather than JNK". Supports MAPKKK activity (IDA) and the
  p38 arm in rat heart; also supports response to ischaemia (IEP).
- **PMID:20716917 (full text)** - Rat intestinal epithelial RIE-1 cells; rat SMART-pool
  ASK1 siRNA: "ASK1 silencing resulted in significant reduction of JNK and p38
  phosphorylation levels in TNFα-treated cells". TNF raised ASK1 levels and caused
  "increased ASK1 accumulation at cell membranes".
- **PMID:12524169 (abstract)** - Rat hippocampal global ischaemia: late activation of
  ASK1 and JNK, and "phospho-SEK1 and phospho-JNK co-immunoprecipitated with ASK1".
- **PMID:12786973 (abstract)** - Rat seizure model: ASK1 held in a 14-3-3beta / PP5
  complex that dissociates on seizure, MKK3/6 and MKK4 phosphorylated, and "ASK1
  colocalized with the adaptor proteins Daxx and TNFR-activating factor 2 at the outer
  membrane of injured CA3 neurons".
- **PMID:16157298 (abstract)** - Neonatal rat ventricular myocytes: "H2O2 dramatically
  increased ASK-1 expression and JUN kinase activation".
- **PMID:22635076 (abstract)** - Rat myocardial ischaemia/reperfusion: a small-molecule
  ASK1 inhibitor reduced cardiomyocyte apoptosis and infarct size.
- **PMID:14638553 (abstract)** - Rat balloon-injured carotid artery: dominant-negative
  ASK1 reduced neointima and VSMC proliferation; ASK1-/- mouse VSMCs proliferate less.
- **PMID:17932313 (abstract)** - Dahl salt-sensitive rats: valsartan inhibited vascular
  ASK1; ASK1-/- mice resist angiotensin II-induced endothelial apoptosis.

## Mouse evidence behind ISO rows

- PMID:12050113: ASK1-/- neurons are defective in ER-stress-induced JNK activation and
  death.
- PMID:22337877: ASK1 and TAK1 bind Cdo and promote p38-dependent myoblast
  differentiation in C2C12 cells.
- PMID:18007661: dominant-negative ASK1 suppresses reactive-nitrogen-species-induced
  non-apoptotic cell death in MEFs.
- PMID:19451227: 14-3-3zeta Ser58 phosphorylation releases ASK1 to drive oxidant-induced
  death.

## Synthesis

Rat Map3k5 is the ortholog of human/mouse ASK1, a redox- and stress-activated Ser/Thr
MAP3K that phosphorylates MKK3/6 (p38 arm) and MKK4/7 (JNK arm). Rat data confirm kinase
activity in heart tissue and its coupling to p38 (cardiac ischaemia) and JNK (hippocampal
ischaemia, TNF in intestinal epithelium). The many tissue-level rat phenotypes (cardiac
apoptosis, VSMC proliferation, endothelial apoptosis) are downstream consequences of this
signalling and are non-core.
