# NDUFA6 (B14 / CI-B14 / LYRM6) review notes

## Identity
- UniProt P56556, HGNC:7690, gene NDUFA6 (synonyms LYRM6, NADHB14). 128 aa, ~15 kDa.
  RecName "NADH dehydrogenase [ubiquinone] 1 alpha subcomplex subunit 6"; AltName
  "Complex I-B14 / CI-B14"; AltName "LYR motif-containing protein 6"
  [file:human/NDUFA6/NDUFA6-uniprot.txt].
- Belongs to the complex I LYR family
  [file:human/NDUFA6/NDUFA6-uniprot.txt "Belongs to the complex I LYR family."].

## Core biology (what it is)
- Accessory / supernumerary (non-core) structural subunit of mitochondrial respiratory
  Complex I (NADH:ubiquinone oxidoreductase). UniProt FUNCTION:
  "Accessory subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase
  (Complex I), that is believed to be not involved in catalysis. Required for proper
  complex I assembly (PubMed:30245030)."
  [file:human/NDUFA6/NDUFA6-uniprot.txt].
- **Non-catalytic.** Explicitly "believed to be not involved in catalysis"
  [file:human/NDUFA6/NDUFA6-uniprot.txt]. Catalysis (NADH oxidation, ubiquinone
  reduction, proton pumping) is a property of the 14 conserved core subunits, not the
  accessory subunits.
- Sits in the peripheral (matrix) arm of Complex I, part of the **Q-module** (near the
  ubiquinone-reduction site). PMID:30245030 describes NDUFA6 as "a 15 kDa
  LYR-motif-containing complex I subunit that forms part of the Q-module" and, on loss,
  a "concomitant reduction in other Q-module subunits, including NDUFAB1, NDUFA7, and
  NDUFA12" [PMID:30245030].
- LYR motif binds the mitochondrial acyl carrier protein NDUFAB1 (an
  acyl-carrier/NADPH-related regulatory element of the complex):
  "the LYR motif of NDUFA6 has been demonstrated to be critical for NDUFAB1 binding in
  the model aerobic yeast, Yarrowia lipolytica" [PMID:30245030]. This is a
  protein-protein interaction/regulatory association, not a catalytic activity of NDUFA6.

## Localization
- Mitochondrial inner membrane; peripheral membrane protein on the matrix side
  [file:human/NDUFA6/NDUFA6-uniprot.txt "Mitochondrion inner membrane";
  "Peripheral membrane protein"; "Matrix side"].
- Detected in mitochondrion by HTP proteomics (PMID:34800366) and localized to
  mitochondrial inner membrane / Complex I by IDA (ComplexPortal CPX-577; PMID:28844695,
  PMID:12611891, PMID:17209039, PMID:27626371).

## Assembly / function evidence
- IPI/IDA membership in Complex I established biochemically:
  - PMID:12611891 immunopurified human Complex I and identified 42 subunits by MS
    (NDUFA6 among them) [PMID:12611891 abstract-only].
  - PMID:17209039 traced tagged NDUFS3 to map CI assembly intermediates (IDA membership)
    [PMID:17209039 abstract-only].
  - PMID:27626371 (Stroud et al., Nature 2016) generated knockouts of each accessory
    subunit; accessory subunits are "integral for assembly and function of human
    mitochondrial complex I"; "25 subunits are strictly required for assembly of a
    functional complex" [PMID:27626371 abstract-only]. FUNCTION evidence in UniProt cites
    this paper.
  - PMID:28844695 (Guo et al., Cell 2017) cryo-EM of the human respiratory megacomplex
    I2III2IV2, assigning individual CI subunits including NDUFA6 (IPI/IDA to CI).
- **Required for complex I assembly (IMP):** PMID:30245030 (Alston et al., AJHG 2018) —
  bi-allelic NDUFA6 variants cause isolated Complex I deficiency (MC1DN33, MIM:618253):
  - "revealing likely causative variants in an accessory subunit of complex I, NDUFA6"
  - "NDUFA6 encodes an accessory structural subunit of complex I"
  - "NDUFA6 is one of 27 accessory subunits that have been shown to be essential for
    complex I assembly and activity"
  - patient fibroblasts show "a reduction of fully assembled complex I levels, whereas
    all other OXPHOS complexes were unaffected" (isolated CI defect), rescued by
    lentiviral re-expression [PMID:30245030 full text].

## GO annotation assessment (summary)
- **MF:** The honest MF is **GO:0005198 structural molecule activity**. Complex-level
  activity GO:0008137 (NADH dehydrogenase (ubiquinone) activity) belongs to the holoenzyme
  and should be captured via `contributes_to_molecular_function`, NOT direct `enables`.
  Existing `enables GO:0008137` (NAS PMID:9878551; TAS PMID:9345899) are over-annotations:
  those refs are a cDNA-characterization paper and an in-situ-hybridisation gene-mapping
  paper respectively — neither demonstrates catalytic activity of NDUFA6, and UniProt
  states NDUFA6 is "believed to be not involved in catalysis". → MARK_AS_OVER_ANNOTATED.
- **CC:** part_of GO:0045271 respiratory chain complex I — strongly supported (IBA, IEA,
  IPI PMID:28844695, IDA PMID:12611891/17209039/27626371, NAS PMID:9878551). ACCEPT the
  experimental/IBA ones; the many Reactome TAS GO:0005743 duplicates and IEA are
  KEEP_AS_NON_CORE (correct but redundant location annotations). GO:0005739 mitochondrion
  (HTP) and GO:0031966 mitochondrial membrane (IDA) are correct but less specific than
  GO:0005743 / GO:0045271.
- **BP:** GO:0032981 mitochondrial respiratory chain complex I assembly (IMP,
  PMID:30245030) — ACCEPT, core. GO:0006120 mitochondrial electron transport, NADH to
  ubiquinone (NAS) — the process the complex performs; KEEP as core BP (NDUFA6
  contributes structurally). GO:1902600 proton transmembrane transport (IEA, inferred
  from GO:0008137) and GO:0009060 aerobic respiration / GO:0042776 PMF-driven ATP
  synthesis (NAS, ComplexPortal) — these describe the whole OXPHOS system, broader than
  NDUFA6's direct role → KEEP_AS_NON_CORE.

## Core functions chosen
- MF GO:0005198 structural molecule activity; contributes_to GO:0008137;
  part_of/in_complex GO:0045271; locations GO:0005743.
- BP: GO:0032981 (CI assembly, IMP) and GO:0006120 (electron transport NADH→ubiquinone).
