# CFAP44 (Q96MT7) curation notes

## Deep research status

- `just deep-research human CFAP44 --provider falcon` failed: the Edison client raised
  `Exception: Failed to authenticate` (Falcon authentication error).
- `just deep-research human CFAP44 --provider perplexity` failed: the tool reported
  `Provider 'perplexity' not available. Available: falcon, asta, openscientist`.
- No `*-deep-research-*.md` file was written. The literature synthesis below was done
  manually with PubMed searches (title search `CFAP44[Title]` returned six records) and
  the cached publications in `publications/`. Abstract-only caches are flagged.

## Identity and domain architecture

- 1,854-aa protein, alias WDR52; N-terminal WD40 / EML-like beta-propeller repeats
  (residues ~226-895) and a predicted coiled-coil region; PANTHER PTHR14885:SF3, in the
  same family as CFAP43 [file:human/CFAP44/CFAP44-uniprot.txt "PANTHER; PTHR14885:SF3; CILIA- AND FLAGELLA-ASSOCIATED PROTEIN 44; 1."].
- No catalytic protease domain is annotated in UniProt/InterPro (only WD40 and
  beta-propeller entries) [file:human/CFAP44/CFAP44-uniprot.txt "Pfam; PF00400; WD40; 3."].
- Human CFAP44 is modelled in the human respiratory doublet-microtubule cryo-EM structure
  PDB 8J07 [file:human/CFAP44/CFAP44-uniprot.txt "PDB; 8J07; EM; 4.10 A; i7/i9=1-1854."].

## Structural role: tether/tether-head (T/TH) complex with CFAP43

- In Chlamydomonas, FAP43 and FAP44 form the T/TH complex linking inner dynein arm f (I1)
  to the doublet [PMID:37258679 "a stellate structure formed by the entwining of two structurally similar proteins, FAP43 and FAP44"].
- The FAP44 N-terminal beta-propellers bind the f-alpha motor [PMID:37258679 "The N terminus of FAP44 binds the fα motor through a pair of β-propellers"].
- Chlamydomonas fap44 mutant axonemes lack the whole T/TH complex [PMID:29514928 "suggesting that FAP44 is required for the stable assembly of the T/TH complex in Chlamydomonas"].
- Bovine (mammalian) axoneme models: [PMID:39743588 "the β-propeller domains of the T/TH subunit, CFAP44, engage the motor domain of IDAa (DNAH12)"].
- Tetrahymena: Fap43 and Fap44 interact; Fap43 is absent from cilia of FAP44 knockouts
  [PMID:29687140 "Fap43p was absent in cilia purified from Tetrahymena FAP44 knockout mutants"]; fap44 mutants have normal-length
  flagella but slow swimming [PMID:29687140 "Chlamydomonas fap43 and fap44 mutants have normal flagella length but reduced swimming speed"].

## Sperm flagellum (human, mouse, trypanosome)

- Human: biallelic CFAP44 variants cause MMAF (SPGF20) [PMID:28552195 "a homozygous frameshift mutation in CFAP44 in one subject"] (abstract only);
  [PMID:29277146 "This study demonstrated that biallelic mutations in CFAP44 and CFAP43 cause MMAF"] (abstract only);
  [PMID:29449551 "Five different homozygous variants were identified in six unrelated patients"].
- Human patient TEM: absent central pair in most sections [PMID:29449551 "the main defect observed was the absence of the CPC (9+0 conformation)"].
- Mouse Cfap44 KO males are sterile with MMAF-like sperm [PMID:28552195 "both Cfap43- and Cfap44-deficient male mice presented with MMAF phenotypes"];
  in the Coutton KO, 9+2 is preserved in most sections but ODF/fibrous sheath/mitochondrial
  sheath are disorganized and sperm are poorly motile
  [PMID:29449551 "the 9+2 organization of the axoneme was preserved in 70% of cases"];
  [PMID:29449551 "the observed structural flagellum defects were associated with severe motility deficiencies"].
- T. brucei orthologue sits along the axoneme near DMT 5-6, and RNAi causes abnormal
  beating [PMID:29449551 "TbCFAP44 and TbCFAP43 are necessary for flagellar function"].
- Tissue: testis-specific expression in the Coutton RNA data, but the protein is also
  present in human respiratory axonemes (8J07), so the location is not sperm-restricted.

## The peptidase claim (PMID:28887034)

- A single report (abstract only in cache) describes a cDNA encoding the central region
  of Cfap44 whose product cleaved beta-tubulin and bacterial FtsZ in transfected cells and
  in vitro [PMID:28887034 "the unspliced form showed proteolytic activity with low substrate specificity"].
- Not replicated; no protease domain or catalytic residues are annotated for CFAP44, and
  all structural work places full-length CFAP44 as a non-catalytic tether scaffold. The
  experiment used fragments/spliced forms in overexpression. Treated as UNDECIDED (IDA,
  full text not seen) and over-annotated as an IBA propagation.

## Interaction data

- HuRI yeast two-hybrid reports CFAP44-GADD45G (IPI); no biological follow-up
  [PMID:32296183 "approximately 53,000 protein-protein interactions"].

## Synthesis

CFAP44 is a non-catalytic structural component of the axonemal T/TH complex (with
CFAP43) that docks onto inner dynein arm f and the doublet; loss destabilizes T/TH and
I1 positioning (protists) and, in mammalian sperm, disorganizes flagellar architecture and
abolishes motility. Core: structural constituent of the axoneme; involved in sperm axoneme
assembly and flagellated sperm motility.
