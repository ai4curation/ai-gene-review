# NT5C3A (Q9H0P0) — curator notes

## Identity / nomenclature
- HGNC symbol **NT5C3A** (HGNC:17820); synonyms NT5C3, P5N1, UMPH1; ORFName HSPC233.
- UniProt Q9H0P0 = "Cytosolic 5'-nucleotidase 3A" (5NT3A_HUMAN). Many historical names for the same protein:
  Pyrimidine 5'-nucleotidase 1 (**P5'N-1 / P5N-1 / PN-I**), Uridine 5'-monophosphate hydrolase 1, cN-III,
  Cytosolic 5'-nucleotidase III, and **p36** (an interferon-alpha-induced protein).
  [file:human/NT5C3A/NT5C3A-uniprot.txt "AltName: Full=Pyrimidine 5'-nucleotidase 1"]
- Identity of PN-I and p36 established directly: [PMID:10942414 "We conclude that p36 and PN-I are identical proteins"].

## Core enzymatic function
- Cytosolic HAD-superfamily hydrolase (EC 3.1.3.5 5'-nucleotidase; also EC 3.1.3.91 for m7GMP).
  [file:human/NT5C3A/NT5C3A-uniprot.txt "EC=3.1.3.5"]
- Dephosphorylates pyrimidine (ribo)nucleoside 5'-monophosphates -> nucleoside + Pi. Strong pyrimidine
  preference. UniProt FUNCTION: "Nucleotidase which shows specific activity towards cytidine monophosphate
  (CMP) and 7-methylguanosine monophosphate (m(7)GMP)"; "CMP seems to be the preferred substrate".
  [file:human/NT5C3A/NT5C3A-uniprot.txt]
- Biochemical characterization of purified/recombinant enzyme: "PN-I is specific for pyrimidine nucleoside
  monophosphates, including the antineoplastic agents 5'-AZTMP and 5'-Ara-CMP" [PMID:11795870].
- "They preferentially hydrolyse pyrimidine 5'-monophosphates and 3'-monophosphates respectively" (PN-I vs
  PN-II) [PMID:9428647].
- Mg(2+)-dependent: "The activity is dependent on Mg(2+)" [PMID:11795870]; structure shows two active-site
  Asp (D88 nucleophile, D90 proton donor) and Mg2+ coordination [file:human/NT5C3A/NT5C3A-uniprot.txt
  "ACT_SITE ... Nucleophile" / "BINDING ... Mg(2+)"].
- Also possesses a **phosphotransferase** activity transferring phosphate between pyrimidine
  monophosphates and pyrimidine nucleosides (incl. drugs AZT, AraC, 5FdUrd):
  "PN-I possess phosphotransferase activity able to exchange phosphate between pyrimidine nucleoside
  monophosphates and pyrimidine nucleosides" [PMID:11795870];
  "soluble pyrimidine nucleotidases are endowed with pyrimidine-specific phosphotransferase activity"
  [PMID:9428647]. E135 mutant abolishes phosphotransferase but not nucleotidase activity
  [file:human/NT5C3A/NT5C3A-uniprot.txt MUTAGEN 135].

## Biological role
- Erythroid pyrimidine nucleotide catabolism: "Erythrocyte maturation is accompanied by RNA degradation
  and release of mononucleotides. Pyrimidine 5'-nucleotidase, PN-I ... " [PMID:11795870]. During
  reticulocyte maturation, ribosomal RNA is degraded; NT5C3A dephosphorylates the released pyrimidine
  ribonucleotides so the resulting nucleosides can diffuse out, preventing toxic accumulation.
- Highly expressed in reticulocytes/erythrocytes (isoforms 1, 3, 4 expressed in reticulocytes)
  [file:human/NT5C3A/NT5C3A-uniprot.txt "Isoforms 1, 3 and 4 are expressed in reticulocytes"].

## Disease
- **Pyrimidine 5'-nucleotidase deficiency (P5ND; MIM:266120)**: autosomal recessive hemolytic anemia
  with marked basophilic stippling and accumulation of pyrimidine nucleotides in erythrocytes; implicated
  in anemia of lead poisoning.
  [file:human/NT5C3A/NT5C3A-uniprot.txt "P5N deficiency (P5ND) [MIM:266120]: Autosomal recessive condition
  causing hemolytic anemia characterized by marked basophilic stippling"].
  [PMID:12930399 "characterized by haemolytic anaemia, marked basophilic stippling and accumulation of
  pyrimidine nucleotides within the erythrocytes"].
- Many loss-of-function missense/frameshift/splice variants documented (D137V, L181P, N229S, G207R,
  G280R, C113R, I297T, R95G, etc.), several with reduced/abolished catalytic activity
  [file:human/NT5C3A/NT5C3A-uniprot.txt VARIANT block].

## Subcellular location
- Cytoplasm / cytosol (main soluble enzyme). [file:human/NT5C3A/NT5C3A-uniprot.txt "SUBCELLULAR LOCATION:
  Cytoplasm"]. IDA cytosol from MGI [PMID:11795870].
- Isoform 2 (the ER-anchored p36-like isoform with an N-terminal membrane segment) is reported in the
  **endoplasmic reticulum** and is interferon-alpha-induced: "p36 is a new interferon-alpha-induced protein
  that localizes in the endoplasmic reticulum" [PMID:8557639]; UniProt: "[Isoform 2]: Endoplasmic reticulum".
  ER localization is thus isoform-2-specific, not the location of the soluble enzymatic isoforms.

## Interferon / antiviral context
- p36 (= NT5C3A) is induced by IFN-alpha (originally described associated with lupus inclusions)
  [PMID:8557639]. NT5C3A appears in a large IFN-stimulated-gene (ISG) overexpression antiviral screen
  [PMID:21478870]; in that screen NT5C3A was among genes whose post-infection expression impacted HCV
  replication by less than 20% ("less than 20% (DDIT4, NT5C3, IFI44L, MAP3K14, IRF2)"), i.e. it was NOT a
  strong antiviral effector. This is weak/indirect evidence for a "defense response to virus" role.

## Notable annotation issues
- **GO:0000215 tRNA 2'-phosphotransferase activity** (two annotations, TAS PMID:10942414 and NAS
  PMID:9428647). This does not match the characterized enzyme. Both cited papers are about pyrimidine
  5'-nucleotidase / phosphotransferase activity between pyrimidine mononucleotides and nucleosides, NOT
  tRNA 2'-phosphotransferase (the enzyme that removes the 2'-phosphate at tRNA splice junctions, e.g.
  TRPT1). This looks like a legacy mis-annotation, plausibly confusing the enzyme's "phosphotransferase"
  activity with the unrelated tRNA 2'-phosphotransferase. Neither cited paper mentions tRNA. Not
  experimental (TAS/NAS) → flag as over-annotation.
- **GO:0005739 mitochondrion** (HTP, FlyBase, PMID:34800366) — high-throughput mitochondrial proteome
  spatial-proteomics hit. The characterized enzyme is cytosolic; low-level co-purification/spatial-proteome
  assignment. Keep as non-core.
- **GO:0051607 defense response to virus** (IDA, PMID:21478870) — from a broad ISG screen where NT5C3A was
  a weak/non-effector; keep as non-core (interferon-inducible isoform 2), not a core evolved function.
- **GO:0005783 endoplasmic reticulum** (IDA PMID:8557639; also HPA IDA and IEA) — genuine but isoform-2
  specific; keep as non-core location.
- **GO:0005515 protein binding** (IPI, PMID:32296183 = HuRI systematic Y2H) — two interactors DESI1
  (Q6ICB0) and UBQLN2 (Q9UHD9), matching the UniProt INTERACTION block. Systematic binary-interactome hits;
  uninformative bare "protein binding" → over-annotated.

## Core function summary
- MF: **5'-nucleotidase activity (GO:0008253)** — pyrimidine-preferring cytosolic 5'-nucleotidase
  (UMP/CMP -> uridine/cytidine + Pi); Mg2+-dependent. (GO has no pyrimidine-specific 5'-nucleotidase MF
  term; GO:0008253 is the standard curated term, its definition "a 5'-ribonucleotide + H2O = a ribonucleoside
  + phosphate" matches EC 3.1.3.5.)
- BP: **UMP catabolic process (GO:0046050)** and **CMP catabolic process (GO:0006248)** — pyrimidine
  ribonucleotide monophosphate catabolism (RNA-turnover product recycling in erythroid cells).
- Cofactor: **magnesium ion binding (GO:0000287)**.
- Location: **cytosol (GO:0005829)** / cytoplasm.
