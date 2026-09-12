# CPT1A (P50416) review notes

## Deep research status
`just deep-research human CPT1A --provider falcon` did NOT produce a
`CPT1A-deep-research-falcon.md` file within the polling window (the running
`deep-research-client` process on the machine was for CPT2, a concurrent batch job,
not CPT1A). Review therefore grounded in `CPT1A-uniprot.txt` (UniProt P50416,
entry v221) and cached `publications/PMID_*.md`. No `-deep-research-*.md` file was
fabricated (per policy).

## Verified biology (UniProt P50416 + primary literature)
- RecName: **Carnitine O-palmitoyltransferase 1, liver isoform** (Short CPT1-L);
  AltName CPT I, liver isoform; AltName Carnitine palmitoyltransferase 1A;
  AltName Succinyltransferase CPT1A. EC 2.3.1.21.
- Liver isoform of CPT1. Catalyses the committed, rate-limiting step of long-chain
  fatty-acid import for mitochondrial beta-oxidation: transfer of a long-chain acyl
  group from acyl-CoA to L-carnitine, giving long-chain acylcarnitine + CoA
  (RHEA:12661; (R)-carnitine + hexadecanoyl-CoA = O-hexadecanoyl-(R)-carnitine + CoA).
- Location: **mitochondrion outer membrane**, multi-pass membrane protein
  (TOPO_DOM/TRANSMEM: two TM helices 48-73, 103-122; large C-terminal cytoplasmic
  catalytic domain 123-773). Confirmed EXP in PubMed:11350182, PubMed:14517221.
- Key regulatory point of fatty-acid oxidation; allosterically **inhibited by
  malonyl-CoA** (ACTIVITY REGULATION, PubMed:14517221; N-terminal 1-42 conformational
  switch, PubMed:21990363/PDB 2LE3).
- Deficiency: **CPT1A deficiency (CPT1AD, MIM:255120)** — autosomal recessive
  hypoketotic hypoglycemia; many characterised loss-of-function variants
  (D454G, G709E, G710E, etc.).
- Secondary/moonlighting functions (from UniProt + primary papers):
  - **Lysine succinyltransferase** activity (EC 2.3.1.-; succinyl-CoA + protein Lys),
    e.g. on ENO1, independent of the O-palmitoyltransferase activity
    (PubMed:29425493 — NOT cached).
  - **Scaffold/adaptor**: recruits ER-localized ZDHHC4 to palmitoylate MAVS
    (Cys79) at mitochondria, stabilising/activating MAVS and sustaining the
    type-I IFN response / antitumor immunity; catalytically-dead H473A retains this
    scaffolding activity (PubMed:38016475). This underlies the
    protein-macromolecule adaptor activity (GO:0030674) and positive regulation of
    innate immune response (GO:0045089) IDA annotations.

## Annotation review decisions (summary)
- Core MF GO:0004095 carnitine O-palmitoyltransferase activity: ACCEPT (EXP/IDA/IBA;
  multiple: PMID:11350182 IDA, PMID:7892212 IDA/TAS, PMID:14517221 EXP/IMP,
  PMID:16651524 EXP, PMID:9691089 IMP). Core function.
- CC mitochondrial outer membrane (GO:0005741): ACCEPT (EXP PMID:11350182, IMP
  PMID:14517221, plus ISS/IEA/TAS). This is the specific correct compartment.
- CC mitochondrion (GO:0005739) IBA/IDA/HTP/TAS: less specific than outer membrane;
  KEEP_AS_NON_CORE (redundant parent).
- CC membrane (GO:0016020) HDA PMID:19946888 (NK cell membrane proteome): correct
  but very general and off-context; MARK_AS_OVER_ANNOTATED.
- BP fatty acid beta-oxidation (GO:0006635), carnitine shuttle (GO:0006853),
  long-chain fatty acid metabolic process (GO:0001676), carnitine metabolic process
  (GO:0009437): ACCEPT — directly informed by function; these + fatty acid metabolic
  process (GO:0006631, parent, KEEP_AS_NON_CORE) frame the core process.
- MF acyltransferase activity (GO:0016746) IEA InterPro: correct but general parent
  of GO:0004095; MARK_AS_OVER_ANNOTATED / could MODIFY to GO:0004095.
- BP positive regulation of innate immune response (GO:0045089) IDA + MF
  protein-macromolecule adaptor activity (GO:0030674) IDA (PMID:38016475): ACCEPT
  as real but non-core moonlighting scaffold function (MAVS/ZDHHC4). Kept out of
  core_functions location claims (mito outer surface vs ER contact unresolved).
- Ensembl GO_REF:0000107 rat-ortholog IEA physiology terms (response to hypoxia,
  glucose metabolic process, triglyceride metabolic process, response to nutrient,
  response to xenobiotic, response to nutrient levels, eating behavior, response to
  alkaloid, response to ethanol, regulation of insulin secretion, cellular response
  to fatty acid, liver regeneration, response to tetrachloromethane, identical
  protein binding, positive regulation of fatty acid beta-oxidation, regulation of
  fatty acid oxidation): mostly downstream physiology / rat-transferred; kept as
  KEEP_AS_NON_CORE or MARK_AS_OVER_ANNOTATED individually. `identical protein
  binding` is uninformative -> MARK_AS_OVER_ANNOTATED. `positive regulation of fatty
  acid beta-oxidation` (a positive-regulation term for the enzyme itself) is
  arguably a self-referential over-call -> MARK_AS_OVER_ANNOTATED; the plain
  `regulation of fatty acid oxidation` retained NON_CORE (malonyl-CoA is CPT1's
  own regulator, not CPT1 regulating others).
- GO:0006006 glucose metabolic process / GO:0001678 intracellular glucose
  homeostasis (ISS from mouse): indirect physiology, KEEP_AS_NON_CORE.
- GO:0030855 epithelial cell differentiation IEP PMID:21492153 (Caco-2 proteomics,
  CPT1A up on differentiation): correlative only; MARK_AS_OVER_ANNOTATED.

## core_functions
1. MF GO:0004095 carnitine O-palmitoyltransferase activity; directly involved in
   fatty acid beta-oxidation (GO:0006635), carnitine shuttle (GO:0006853),
   long-chain fatty acid metabolic process (GO:0001676); located in mitochondrial
   outer membrane (GO:0005741).
</content>
</invoke>
