# selB (P14081) review notes

Deep research: no provider deep-research file was available for this gene in this
session; the review rests on the cached GOA publications and the reviewed UniProt
record.

- Translation factor: [PMID:2531290 "purified SELB protein binds guanine nucleotides
  in a 1:1 molar ratio and specifically complexes selenocysteyl-tRNAUCA, but does not
  interact with seryl-tRNAUCA"]
- SECIS binding: [PMID:8483932 "SELB binds to the loop region of the hairpin
  structure"]
- tRNA(Sec) acceptor stem as SelB determinant: [PMID:1939093 "The aminoacyl-acceptor
  helix of tRNA(Sec), therefore, is a major determinant directing binding to SELB"]
- GTPase: [PMID:9454578 "GTPase activity of SelB is stimulated by the presence of E.
  coli 70S ribosomes"]; SECIS adds 3-4-fold, ribosome-dependent.
- Not needed for Sec-tRNA synthesis: [PMID:2524495 "The formation of selenocysteine
  depended on the presence of functional products of the selA and selD genes but not
  of the selB gene"]
- Protein binding (SerC, P23721) from two HT AP-MS studies: REMOVE per policy.
- RNA binding IEA: MODIFY to both SECIS binding and tRNA binding (gene carries both).
  GO:1904678 alpha-aminoacyl-tRNA binding was considered for the tRNA row but is not a
  descendant of tRNA binding in the current GO, so tRNA binding was accepted.
- PANTHER: UniProt places P14081 in PTHR42854 (SF3, eIF2gamma-like display name)
  [file:ECOLI/selB/selB-uniprot.txt "DR   PANTHER; PTHR42854; EUKARYOTIC TRANSLATION
  INITIATION FACTOR 2 SUBUNIT 3 FAMILY MEMBER; 1."], while P. putida SelB Q88QJ7 is
  PTHR43721. The IBA node PTN000562733 (GO:0035368, GO:0001514) lies in the PTHR43721
  PAINT tree and is seeded by P14081 itself
  (interpro/panther/PTHR43721/PTHR43721-paint.tsv). Recorded, not acted on.
- PAINT: no IRD/IKR loss on the lineage.
