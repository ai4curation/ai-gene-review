# rps-18 (Y57G11C.16; UniProt O18240) - manual literature review

No deep-research API was available; this summary was compiled manually from the
UniProt record, cached publications, PubMed searches and a structural contact
analysis (October 2026).

## Identity and family

- C. elegans rps-18 (ORF Y57G11C.16, WBGene00004487, GeneID 178408) encodes the
  154-aa small ribosomal subunit protein uS13 (40S ribosomal protein S18); the
  UniProt entry O18240 is unreviewed (TrEMBL)
  [file:worm/rps-18/rps-18-uniprot.txt "DR   WormBase; Y57G11C.16; CE14956; WBGene00004487; rps-18."].
- Family: universal ribosomal protein uS13 family
  [file:worm/rps-18/rps-18-uniprot.txt "Belongs to the universal ribosomal protein uS13 family."],
  with HAMAP MF_01315, Pfam PF00416 (Ribosomal_S13), PIRSF002134, PROSITE
  PS00646/PS50159, NCBIfam PRK04053.1 and PANTHER PTHR10871:SF3
  [file:worm/rps-18/rps-18-uniprot.txt "DR   HAMAP; MF_01315; Ribosomal_uS13; 1."].
- The PANTHER family PTHR10871 covers bacterial S13 and eukaryotic cytosolic S18;
  mitochondrial ribosomes lack an S13 homolog
  [PMID:11279123 "No mitochondrial homologs to prokaryotic ribosomal proteins S1, S3, S4, S8, S13, S19, and S20 could be found"],
  so the single C. elegans uS13 protein is a cytosolic ribosomal protein.
  (Note: "S18" in the mitoribosome literature refers to the unrelated bS18
  family; the C. elegans mitochondrial S18 homologs are different genes.)
- In other organisms uS13 sits at the head of the small subunit, contacts
  several helices of the small-subunit rRNA, and its C-terminal tail reaches the
  P-site tRNA (general background; the UniProt FUNCTION line for O18240 is an
  ARBA prediction and is not used as evidence).

## Experimental structural evidence in C. elegans

- Sehgal et al. 2024 (PMID:39209556) determined the cryo-EM structure of the
  C. elegans 80S ribosome purified by sucrose gradient fractionation
  [PMID:39209556 "We purified ribosomes from C. elegans via sucrose gradient
  fractionation."], modelling all ribosomal proteins except stalk proteins,
  eL28 and RACK-1 [PMID:39209556 "We also modeled the ribosomal proteins, with
  the exceptions of those bound to the P- and L-stalks (uL10/P0, P1, P2, uL1,
  uL11), eL28, and RACK-1"]. RPS-18 is modelled full length as chain AS
  [file:worm/rps-18/rps-18-uniprot.txt "DR   PDB; 9CAI; EM; 2.59 A; AS=1-154."].
- Contact analysis of 9CAI (rps-18-bioinformatics/RESULTS.md): 50 uS13 residues
  lie within 4 A of 35 nucleotides of 18S rRNA, from the N-terminal helix-two-
  turn-helix region and the basic C-terminal region; five C-terminal tail
  residues (144-149) contact the modelled tRNA
  [file:worm/rps-18/rps-18-bioinformatics/RESULTS.md "RNA chain B2 ('18S rRNA'): 50 uS13 residues within 4.0 A of 35 nucleotides"].
  This is direct structural evidence for rRNA binding by the worm protein.

## Genetic / phenotypic data

- In an RNAi control experiment in a paper on CAR-1/CGH-1, depletion of RPS-18
  (with five other RPS proteins) caused penetrant sterility; partial depletion
  gave osmotically sensitive embryos without cytokinesis defects, consistent with
  a general translation defect [PMID:16247027 "Depletions of six different
  ribosomal subunits (RPS-1, -3, -5, -11, -18, and -23) each resulted in
  penetrant sterility (unpublished data)."]. This is necessity evidence only.
- No other C. elegans papers specifically on rps-18 were found (PubMed search
  "(rps-18 OR "ribosomal protein S18" OR Y57G11C.16) AND elegans" returned two
  hits: PMID:11279123, on the mammalian mitoribosome small subunit, and
  PMID:9790748, on the rat Sacm2l gene adjacent to Rps18; neither concerns worm
  RPS-18 function).

## Synthesis

- Core: structural constituent of ribosome (MF); rRNA binding (MF, structural);
  part of cytosolic small ribosomal subunit (CC); cytoplasmic translation (BP);
  cytosol (CC).
- No basis for additional process terms: RNAi phenotypes (sterility, osmotic
  sensitivity) reflect general loss of translation capacity.
