# NDUFB11 (ESSS) — gene review notes

UniProt: Q9NX14 (NDUBB_HUMAN). Gene symbol NDUFB11 (HGNC:20372). X-linked (Chromosome X).
Aliases: Complex I-ESSS / CI-ESSS; NADH-ubiquinone oxidoreductase ESSS subunit; Neuronal
protein 17.3 (Np17.3 / p17.3); ORF UNQ111/PRO1064.

## Core biology (from UniProt Q9NX14)

- **Accessory / supernumerary (non-catalytic) subunit of Complex I** (mitochondrial
  respiratory chain NADH:ubiquinone oxidoreductase):
  [file:human/NDUFB11/NDUFB11-uniprot.txt "Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I), that is believed not to be involved in catalysis."]
- Complex I transfers electrons from NADH to ubiquinone:
  [file:human/NDUFB11/NDUFB11-uniprot.txt "Complex I functions in the transfer of electrons from NADH to the respiratory chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone."]
- Part of the 45-subunit human holoenzyme:
  [file:human/NDUFB11/NDUFB11-uniprot.txt "Complex I is composed of 45 different subunits"]. FUNCTION evidence anchored to
  PMID:27626371 (ECO:0000269|PubMed:27626371).
- **Subcellular location: mitochondrion inner membrane; single-pass membrane protein.**
  UniProt: `Mitochondrion inner membrane {ECO:0000269|PubMed:31206022, ECO:0000305|PubMed:12611891}; Single-pass membrane protein`.
  Sequence features: mitochondrial transit peptide 1..29; CHAIN 30..153; a single
  TRANSMEM helix 89..109; a disordered N-terminal region 40..76. So it is anchored in the
  inner membrane via one TM helix — consistent with membrane-arm placement.
- Belongs to the complex I NDUFB11 subunit family; InterPro IPR019329 (ESSS subunit),
  Pfam PF10183 (ESSS), PANTHER PTHR13327:SF0. Single-copy ortholog family (KOG4808).
- Structural evidence in the mature holoenzyme: PDB 5XTC/5XTD/5XTH/5XTI (Guo et al. 2017
  megacomplex), 9CWT/9I4I/9TI4 cryo-EM; ComplexPortal CPX-577 (Complex I).

## Disease (X-linked; structural role, but included for completeness)

- **LSDMCA3 / MLS-like** (Linear skin defects with multiple congenital anomalies 3;
  microphthalmia with linear skin defects syndrome): PMID:25772934
  (van Rahden et al. 2015, Am J Hum Genet) —
  [file:human/NDUFB11/NDUFB11-uniprot.txt "Mutations in NDUFB11, encoding a complex I component of the mitochondrial respiratory chain, cause microphthalmia with linear skin defects syndrome."]
- **Histiocytoid cardiomyopathy**: PMID:25921236 (Shehata et al. 2015) — de novo NDUFB11
  truncating variants (VARIANT 85..153 Missing; 108..153 Missing).
- **Mitochondrial complex I deficiency, nuclear type 30 (MC1DN30)**: PMID:26741492
  (Kohda et al. 2016); variant p.Glu121Lys (VAR_076277).
- These establish NDUFB11 as required for a functional Complex I, but the **molecular
  role is structural/assembly**, not catalytic.

## Interactions

- UniProt SUBUNIT / INTERACTION: Complex I (45 subunits); **Interacts with BCAP31**
  (PMID:31206022). BAP31 (BCAP31) forms an ER–mitochondria bridge that stimulates
  Complex I biogenesis (translocation of NDUFS4); NDUFB11 co-purifies in this context.
  [PMID:31206022 "Disruption of the BAP31-Tom40 complex inhibits mitochondrial complex I activity"]
- IntAct binary hits (large-scale Y2H / HuRI): CLDN7, EBP, FATE1, GJB1, GPR101, GPR152,
  GPR42, HIBADH, TIMMDC1. Several are ER/membrane proteins from proteome-scale binary
  interactome maps (PMID:25416956, PMID:32296183, PMID:33961781); TIMMDC1 is a Complex I
  assembly factor (biologically plausible), the GPCRs/claudins are typical high-throughput
  binary-screen partners of unclear physiological relevance. All are bare "protein binding"
  (GO:0005515) IPI — informative of interactome membership, not of NDUFB11's own MF.

## Curation reasoning summary

- Honest MF = **GO:0005198 structural molecule activity**, contributing to complex-level
  **GO:0008137 NADH dehydrogenase (ubiquinone) activity** (via `contributes_to_molecular_function`,
  NOT direct enables). Do NOT assign direct NADH-dehydrogenase / oxidoreductase MF to this subunit.
- part_of **GO:0045271 respiratory chain complex I** — strongly supported (IDA PMID:12611891,
  PMID:27626371; IPI PMID:28844695; IBA). ACCEPT as core.
- Location **GO:0005743 mitochondrial inner membrane** — supported by EXP/IDA and the single
  TM helix; ACCEPT (multiple redundant IEA/TAS/IDA rows KEEP_AS_NON_CORE / ACCEPT). GO:0005739
  mitochondrion is a correct but less specific parent — KEEP_AS_NON_CORE.
- BP: **GO:0006120** (mitochondrial electron transport, NADH to ubiquinone) and
  **GO:0032981** (Complex I assembly) are the honest core processes. GOA carries
  GO:0009060 (aerobic respiration, NAS) and GO:0042776 (proton motive force-driven ATP
  synthesis, NAS) from ComplexPortal — these are complex-level roles; keep as non-core
  (true of the holoenzyme, over-broad for the individual accessory subunit's specific role).
- All "protein binding" GO:0005515 IPI rows → MARK_AS_OVER_ANNOTATED (per policy, never REMOVE
  a bare protein-binding IPI); the BCAP31/TIMMDC1 interactions are real but uninformative as MF.
