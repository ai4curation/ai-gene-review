# NDUFA11 (B14.7) review notes

UniProt: Q86Y39 (NDUAB_HUMAN). HGNC:20371. Gene on chromosome 19.
141 aa; MW ~14.9 kDa. Names: NADH dehydrogenase [ubiquinone] 1 alpha subcomplex
subunit 11; Complex I-B14.7 (CI-B14.7); NADH-ubiquinone oxidoreductase subunit B14.7.

## Core biology (grounded in the local UniProt record)

- **Accessory (supernumerary) subunit of Complex I, non-catalytic.** UniProt FUNCTION:
  "Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase
  (Complex I), that is believed not to be involved in catalysis. Complex I functions in the
  transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor
  for the enzyme is believed to be ubiquinone."
  [file:human/NDUFA11/NDUFA11-uniprot.txt, ECO:0000269|PubMed:27626371]
- **Complex I is a 45-subunit holoenzyme.** UniProt SUBUNIT: "Complex I is composed of 45
  different subunits." [file:human/NDUFA11/NDUFA11-uniprot.txt; PMID:12611891, PMID:27626371]
- **Membrane-arm, multi-pass inner-membrane protein, matrix side.** UniProt SUBCELLULAR
  LOCATION: "Mitochondrion inner membrane ... Multi-pass membrane protein ... Matrix side."
  Two predicted transmembrane helices (TRANSMEM 21..43 and 58..80).
  [file:human/NDUFA11/NDUFA11-uniprot.txt]
- **Tim17/Tim22/Tim23-like fold.** B14.7 has homology to the Tim17/22/23 mitochondrial
  carrier/translocase family fold, but it is a genuine structural subunit of Complex I, NOT
  a functional protein translocase/insertase — its MF is structural, not transporter. (Family
  assignment: UniProt SIMILARITY "Belongs to the complex I NDUFA11 subunit family";
  InterPro IPR039205; membrane-arm module of the holoenzyme.) Do not assign transporter/
  insertase MF from the fold.
- **Bona fide stable subunit of the mature holoenzyme**, resolved in cryo-EM structures
  (PDB 5XTC/5XTD/5XTH/5XTI/9CWT/9I4I/9TI4; chain V, residues 2-141).
  [file:human/NDUFA11/NDUFA11-uniprot.txt]

## Honest GO representation (per curation policy)

- **MF = GO:0005198 structural molecule activity** (non-catalytic structural subunit).
- **Contributes to (not enables) GO:0008137 NADH dehydrogenase (ubiquinone) activity** —
  this is the complex-level catalytic activity; NDUFA11 is non-catalytic and carries no redox
  cofactor, so it should NOT directly `enable` GO:0008137, nor any direct NADH-dehydrogenase MF.
- **Core BP = GO:0006120 mitochondrial electron transport, NADH to ubiquinone**, and
  **GO:0032981 mitochondrial respiratory chain complex I assembly** (accessory subunits are
  required for assembly/stability; PMID:27626371).
- **part_of GO:0045271 respiratory chain complex I**; location GO:0005743 mitochondrial inner
  membrane.

## Disease

- **Mitochondrial complex I deficiency, nuclear type 14 (MC1DN14), MIM:618236**, autosomal
  recessive; caused by a deleterious NDUFA11 mutation. [file:human/NDUFA11/NDUFA11-uniprot.txt,
  ECO:0000269|PubMed:18306244 — Berger et al. 2008, Ann. Neurol.]

## Reference notes

- **PMID:12611891** (Murray et al. 2003): immunopurification + MS subunit composition of human
  Complex I; primary IDA evidence for complex membership. Abstract-only in cache.
- **PMID:27626371** (Stroud et al. 2016, Nature): systematic knockout + quantitative proteomics
  of all accessory subunits; "25 subunits are strictly required for assembly of a functional
  complex"; loss of a subunit destabilizes co-module subunits. Establishes accessory-subunit
  assembly role. Cited by UniProt FUNCTION. Abstract-only in cache.
- **PMID:28844695** (Guo et al. 2017, Cell): cryo-EM of human megacomplex I2III2IV2; "reveals
  the precise assignment of individual subunits of human CI"; basis for ComplexPortal IDA/IPI.
  Abstract-only in cache.
- **PMID:30030361** (Signes & Fernandez-Vizarra 2018): OXPHOS assembly review; "supernumerary
  subunits that play essential roles in assembly, regulation and stability"; source of
  ComplexPortal NAS pathway-level BP annotations (aerobic respiration, ATP synthesis).
  Abstract-only in cache.
- **PMID:32296183** (Luck et al. 2020, HuRI): genome-wide Y2H binary interactome. Source of the
  bare "protein binding" (GO:0005515) IPI. The UniProt INTERACTION block lists the partner as
  MEOX2 (Q6FHY5) — a homeobox transcription factor, not a plausible functional partner for a
  Complex I membrane subunit; treat as high-throughput Y2H, uninformative for MF. Full text in
  cache but NDUFA11 not discussed individually (one PPI in a >50,000-PPI dataset).
- **PMID:34800366** (Morgenstern et al. 2021, MitoCoP): high-confidence human mito proteome
  (>1,100 proteins); source of HTP mitochondrion localization. NDUFA11 not named individually
  in body. Full text in cache.
- **Reactome R-HSA-163217** and biogenesis events (6799178/6799179/6799191/6799196/6799197/
  6799202): TAS inner-membrane localization from Complex I electron-transfer and biogenesis
  reactions.

## Action plan

- part_of GO:0045271 (all evidence: IBA/IEA/IDA/IPI): ACCEPT (core CC).
- GO:0005743 mitochondrial inner membrane (IEA/IDA/TAS x7): ACCEPT (most specific membrane loc).
- GO:0005739 mitochondrion (HTP, ISS): KEEP_AS_NON_CORE (less specific than inner membrane).
- GO:0006120 (IEA InterPro, involved_in): ACCEPT (core complex-level BP for this subunit).
- GO:0005515 protein binding (IPI, PMID:32296183): MARK_AS_OVER_ANNOTATED (bare protein
  binding, HuRI Y2H; never REMOVE an IPI protein-binding per policy).
- GO:0009060 aerobic respiration (NAS): KEEP_AS_NON_CORE (downstream pathway-level).
- GO:0042776 proton-motive-force ATP synthesis (NAS): KEEP_AS_NON_CORE (downstream pathway).
