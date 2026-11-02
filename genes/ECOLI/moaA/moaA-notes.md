# moaA (P30745) notes, E. coli K-12

Deep research was unavailable for this gene (falcon 403, asta returned nothing in Phase 1
of the RADICAL_SAM project). These notes are built from cached publications, PubMed,
and the UniProt record.

## Identity

- UniProt P30745, GTP 3',8-cyclase, EC 4.1.99.22; synonyms chlA, bisA, narA; b0781.
  First gene of the moaABCDE operon.
- Radical SAM superfamily, MoaA family (HAMAP MF_01225, TIGR02666, IPR013483). Two
  [4Fe-4S] clusters: N-terminal radical SAM cluster (Cys24/28/31) and a C-terminal
  auxiliary cluster (Cys257/260/274) that binds the GTP substrate
  [file:ECOLI/moaA/moaA-uniprot.txt "Binds 1 [4Fe-4S] cluster coordinated with 3 cysteines and an exchangeable S-adenosyl-L-methionine and 1 [4Fe-4S] cluster coordinated with 3 cysteines and the GTP-derived substrate"].

## Reaction and division of labour with MoaC

- MoaA and MoaC together convert GTP to cPMP (precursor Z). Precursor Z was purified from
  E. coli overproducing MoaA and MoaC [PMID:14761975 "precursor Z purified from Escherichia coli overproducing MoaA and MoaC, two proteins essential for bacterial precursor Z synthesis"].
- Structural work on Staphylococcus aureus MoaA established GTP as the substrate and SAM as
  the fourth ligand of the radical SAM cluster [PMID:15317939 "SAM is the fourth ligand to the cluster and binds to its unique Fe as an N/O chelate"]; GTP binds the C-terminal cluster
  [PMID:16632608 "MoaA binds 5'-GTP with high affinity and interacts through its C-terminal [4Fe-4S] cluster with the guanine N1 and N2 atoms"].
- MoaA product is 3',8-cH2GTP; MoaC (or MOCS1B) performs the rearrangement to cPMP
  [PMID:23627491 "Instead, 3′,8-cH2GTP is transferred to MoaC where a complex rearrangement reaction proceeds."].
  MoaA itself cannot do the rearrangement
  [PMID:23627491 "MoaA is incapable of catalyzing the rearrangement reactions"].
  Begley lab substrate-analogue trapping (PMID:23848839, PMID:24955657) is mechanistic
  context; their early proposal that MoaA alone forms a later intermediate is superseded by
  the 3',8-cH2GTP identification.
- Substrate-triggered SAM cleavage via the C-terminal GG tail (S. aureus model, PMID:41183211).
- In E. coli the A-type carriers ErpA and IscA insert the [4Fe-4S] clusters into MoaA
  [PMID:33782054 "We show that ErpA and IscA can partially replace each other in their role to provide [4Fe-4S] clusters for MoaA."].

## Genetics

- chlA mutants lack Moco [PMID:6307982 "The chlA and chlE mutants had no detectable cofactor."];
  PMID:1090592 and PMID:2947896 are the classic chlorate-resistance genetics. Note the chlA
  locus historically covers the moa operon, so older chlA alleles are not all in moaA itself.
- Response to heat (PMID:24580753): a Keio-strain heat-shock survival screen of genes chosen by
  codon-usage signatures; indirect phenotype, not a MoaA activity.

## Curation decisions (summary)

- cPMP synthase IBA (GO:0061799) transferred from MOCS1, whose MOCS1B domain is a MoaC
  homolog; E. coli MoaA has no MoaC domain. Removed, same as PSEPK/moaA.
- Generic rows treated per the RADICAL_SAM treatment rule (GO:0003824, GO:0046872 and
  GO:0051536 MODIFY; GO:0051539 and GO:1904047 ACCEPT).
- PSEPK/moaA (older review) used MARK_AS_OVER_ANNOTATED / KEEP_AS_NON_CORE on the generic
  cluster and SAM rows; that predates the project treatment rule.
