# rps-18 notes

- 2026-10-28: fetched O18240 (unreviewed TrEMBL; GeneID 178408, WBGene00004487,
  ORF Y57G11C.16); accession confirmed. Two transient UniProt read timeouts on
  fetch-gene before it succeeded.
- GOA: 9 rows, all IBA/IEA; no experimental rows.
- Literature: PMID:39209556 (C. elegans 80S cryo-EM; uS13 = chain AS of 9CAI)
  [PMID:39209556 "We also modeled the ribosomal proteins, with the exceptions of those bound to the P- and L-stalks"];
  PMID:16247027 (RNAi control, sterility)
  [PMID:16247027 "Depletions of six different ribosomal subunits (RPS-1, -3, -5, -11, -18, and -23) each resulted in penetrant sterility (unpublished data)."].
  PubMed hits PMID:11279123 and PMID:9790748 are not about worm RPS-18 (cached by
  the search; used only for background on the absence of a mitochondrial S13).
- Bioinformatics: contact analysis of 9CAI shows extensive 18S rRNA contacts
  (rps-18-bioinformatics/RESULTS.md) -> supports rRNA binding as the specific
  replacement for nucleic acid binding / RNA binding IEA rows.
- PAINT: PTN000093238 is family-wide (includes E. coli S13 P0A7S9); cytosol IBD
  placed there, with a NOT (IRD) at PTN000093341. Worm protein is a cytosolic
  ribosomal protein, so cytosol ACCEPT; small ribosomal subunit -> cytosolic
  small ribosomal subunit.
- No NEW terms: RNAi phenotypes are necessity evidence only. tRNA contact of the
  C-terminal tail noted but not annotated (one structure; site not established).
