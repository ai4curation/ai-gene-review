# NDUFA5 (Q16718) — gene review notes

## Identity
- HGNC symbol: NDUFA5; UniProt Q16718 (NDUA5_HUMAN); human (NCBITaxon:9606).
- Aliases: "NADH dehydrogenase [ubiquinone] 1 alpha subcomplex subunit 5"; "Complex I subunit B13";
  "CI-13kD-B"; "NADH-ubiquinone oxidoreductase 13 kDa-B subunit" [file:human/NDUFA5/NDUFA5-uniprot.txt "AltName: Full=Complex I subunit B13"].
- 116 aa, 13.4 kDa; belongs to "the complex I NDUFA5 subunit family"
  [file:human/NDUFA5/NDUFA5-uniprot.txt "Belongs to the complex I NDUFA5 subunit family"].

## Core biology
NDUFA5 (B13) is an **accessory / supernumerary subunit** of mitochondrial respiratory
Complex I (NADH:ubiquinone oxidoreductase). Complex I in humans is composed of 45 subunits:
14 core (conserved bacteria→human, catalytic) plus 31 accessory subunits
[PMID:27626371 "Bacterial and human complex I share 14 core subunits that are essential for enzymatic function; however, the role and necessity of the remaining 31 human accessory subunits is unclear"].

UniProt states NDUFA5 is an accessory subunit "believed not to be involved in catalysis"
[file:human/NDUFA5/NDUFA5-uniprot.txt "Accessory subunit of the mitochondrial membrane respiratory"];
[file:human/NDUFA5/NDUFA5-uniprot.txt "chain NADH dehydrogenase (Complex I), that is believed not to be"].
Thus its honest molecular function is **structural molecule activity (GO:0005198)**, not a
direct NADH-dehydrogenase / oxidoreductase catalytic activity. It has **no redox cofactor**
(no FMN, no Fe-S cluster) — those reside on the core subunits (NDUFV1/V2, NDUFS1/S2/S3/S7/S8, etc.).

The complex-level enzymatic activity is NADH dehydrogenase (ubiquinone) activity (GO:0008137),
to which NDUFA5 **contributes** as a structural member (use `contributes_to_molecular_function`,
not direct `enables`).

### Localization / topology
- Mitochondrion inner membrane, peripheral membrane protein, matrix side
  [file:human/NDUFA5/NDUFA5-uniprot.txt "SUBCELLULAR LOCATION: Mitochondrion inner membrane"];
  [file:human/NDUFA5/NDUFA5-uniprot.txt "Peripheral membrane protein"];
  [file:human/NDUFA5/NDUFA5-uniprot.txt "Matrix side"].
- Component of Complex I (part_of GO:0045271 respiratory chain complex I). It sits in the
  peripheral (matrix) arm of the L-shaped holoenzyme — consistent with the matrix-side
  peripheral-membrane topology and its non-membrane-integral, non-catalytic role.
- Structurally resolved in cryo-EM Complex I structures (PDB 5XTB, 9CWT, 9I4I, 9TI4 etc.,
  chain H/I) [file:human/NDUFA5/NDUFA5-uniprot.txt "PDB; 5XTB; EM"].

### Complex composition evidence
- Identified as a genuine subunit of purified human Complex I by immunopurification + MS
  [PMID:12611891 "we can resolve and identify the human"]; [PMID:12611891 "homologues of 42 polypeptides detected so far in the more extensively studied"].
- Complex I is composed of 45 different subunits
  [file:human/NDUFA5/NDUFA5-uniprot.txt "Complex I is composed of 45 different subunits"].
- Stroud et al. knocked out each accessory subunit; 25 are strictly required for assembly of a
  functional complex [PMID:27626371 "We show that 25 subunits are strictly"];
  [PMID:27626371 "required for assembly of a functional complex and 1 subunit is essential for"].
  Loss of each subunit destabilizes co-module subunits
  [PMID:27626371 "loss of each subunit affects the stability of other subunits residing in the same"].

### Biological process
Complex I transfers electrons from NADH to ubiquinone, coupled to proton translocation across
the inner membrane, feeding the respiratory chain / oxidative phosphorylation
[PMID:9878551 "Its main function is the transport of electrons from NADH to ubiquinone, which is"];
[PMID:9878551 "accompanied by translocation of protons from the mitochondrial matrix to the"].
UniProt FUNCTION: "Complex I functions in the transfer of electrons from NADH to the respiratory
chain. The immediate electron acceptor for the enzyme is believed to be ubiquinone"
[file:human/NDUFA5/NDUFA5-uniprot.txt "Complex I functions in the transfer of electrons"].

Appropriate BP terms for NDUFA5 as a Complex I subunit:
- GO:0006120 mitochondrial electron transport, NADH to ubiquinone (core BP)
- GO:0032981 mitochondrial respiratory chain complex I assembly (accessory subunits are integral
  for assembly per PMID:27626371) — not currently in GOA but a reasonable proposed term.
- GO:0022904 respiratory electron transport chain (IBA, more general; keep as non-core).

### Expression
Expressed in all tissues examined, highest in heart, skeletal muscle and brain
[file:human/NDUFA5/NDUFA5-uniprot.txt "Expressed in all tissues examined with highest"];
[PMID:9048877 "Human B13 mRNA expression was observed in all tissues examined with highest levels in heart, skeletal muscle and brain"].

## Annotation-by-annotation reasoning

### Molecular function
- **GO:0008137 NADH dehydrogenase (ubiquinone) activity** (NAS PMID:9878551; TAS PMID:9048877,
  qualifier `enables`). This is the complex-level catalytic activity. NDUFA5 is non-catalytic
  and has no redox cofactor, so it does NOT directly `enable` this. → MARK_AS_OVER_ANNOTATED
  (the essence — participation in the Complex I reaction — is captured better by
  `contributes_to_molecular_function` in core_functions, and by part_of GO:0045271 + BP terms).
  Both are NAS/TAS (not experimental), so downgrading is appropriate.
- **GO:0005515 protein binding** (7 IPI rows, from high-throughput interactome / affinity-MS
  screens: PMID:24344204, 27499296, 28514442, 32296183, 32814053, 33961781). The most
  biologically meaningful of these is the interaction with NDUFS3 (UniProtKB:O75489), a
  co-Complex-I core subunit [file:human/NDUFA5/NDUFA5-uniprot.txt "Q16718; O75489: NDUFS3"].
  Per policy, bare "protein binding" IPI is never REMOVEd → MARK_AS_OVER_ANNOTATED (uninformative
  MF; real function is structural within Complex I).

### Cellular component
- **GO:0045271 respiratory chain complex I** — multiple lines (IDA PMID:12611891, IDA
  PMID:27626371, IPI PMID:28844695, IBA, NAS PMID:9878551, IEA). This is the single most
  accurate/core CC. IDA experimental rows → ACCEPT. IBA/IEA/NAS duplicates → ACCEPT / KEEP_AS_NON_CORE.
- **GO:0005743 mitochondrial inner membrane** — IDA PMID:28844695 (ComplexPortal), IEA, and 7
  Reactome TAS rows. Correct per UniProt subcellular location → ACCEPT the experimental IDA;
  the Reactome/IEA duplicates KEEP_AS_NON_CORE.
- **GO:0005739 mitochondrion** — HTP PMID:34800366 (mito proteome). Correct but general (parent
  of inner membrane) → KEEP_AS_NON_CORE.
- **GO:0032991 protein-containing complex** — IEA GO_REF:0000107. Correct but far too general
  (Complex I is the specific complex) → MARK_AS_OVER_ANNOTATED (redundant with GO:0045271).

### Biological process
- **GO:0006120 mitochondrial electron transport, NADH to ubiquinone** — NAS PMID:9878551. This
  is the core Complex-I BP for NDUFA5 → ACCEPT.
- **GO:0022904 respiratory electron transport chain** — IBA GO_REF:0000033 and IEA
  GO_REF:0000002 (InterPro). More general than GO:0006120 but correct → KEEP_AS_NON_CORE.
- **GO:0009060 aerobic respiration** — NAS PMID:30030361 (ComplexPortal). Correct at complex
  level, general/downstream → KEEP_AS_NON_CORE.
- **GO:0042776 proton motive force-driven mitochondrial ATP synthesis** — NAS PMID:30030361.
  This is really the function of ATP synthase (Complex V) downstream of the proton gradient that
  Complex I helps establish; annotating NDUFA5 to ATP synthesis over-reaches → MARK_AS_OVER_ANNOTATED.
- **GO:1902600 proton transmembrane transport** — IEA GO_REF:0000108 (inferred from GO:0008137
  logical link). Complex I does pump protons, but proton pumping is done by the membrane-arm
  core subunits (ND2/ND4/ND5 antiporter-like); NDUFA5 is a matrix-arm accessory subunit not
  part of the proton-translocation machinery. This IEA is an over-propagated inference →
  MARK_AS_OVER_ANNOTATED (not REMOVE, since Complex I as a whole does translocate protons, so
  it is not clearly wrong at complex level; but it over-annotates this specific subunit).

## Core functions summary
NDUFA5 is a structural (non-catalytic) accessory subunit of the peripheral/matrix arm of
mitochondrial respiratory Complex I. It contributes to the holoenzyme's NADH:ubiquinone
oxidoreductase activity and is required for stable assembly/function of the complex, thereby
participating in mitochondrial electron transport from NADH to ubiquinone within the respiratory
chain.

Honest MF: GO:0005198 structural molecule activity; contributes_to GO:0008137.
part_of: GO:0045271 respiratory chain complex I.
Location: GO:0005743 mitochondrial inner membrane (peripheral, matrix side).
Core BP: GO:0006120 mitochondrial electron transport, NADH to ubiquinone; and GO:0032981
mitochondrial respiratory chain complex I assembly (proposed new term).
