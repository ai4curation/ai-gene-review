# catB (Acinetobacter baylyi ADP1, Q43931) notes

## Provenance

- Deep research was attempted with `just deep-research ACIAD catB --provider falcon`
  (2026-10-23) and failed with "Failed to authenticate"; no other provider key is
  configured. The review uses the UniProt record and cached primary literature.
- Reviewed as the ADP1 exemplar of the CatB step in
  `modules/catechol_ortho_cleavage.yaml`.

## Evidence summary

- catB encodes muconate lactonizing enzyme in the A. calcoaceticus catBCDE cluster
  [PMID:3003031 "catB, muconate lactonizing enzyme (EC 5.5.1.1)"], and the cloned
  fragment complements P. putida catB mutants [PMID:3003031 "The recombinant plasmid,
  pAN1, complemented P. putida mutants with lesions in catB, catC, pcaD, and pcaE
  genes"].
- Substrate specificity of the ADP1 enzyme was measured directly: it converts
  cis,cis-muconate and methyl/fluoro analogues but not chlorinated muconates
  [PMID:9726873 "the muconate cycloisomerases from Pseudomonas putida PRS2000 and
  Acinetobacter \"calcoaceticus\" ADP1"; "but not 2-fluoro-, 2-chloro-, 3-chloro-, or
  2,4-dichloro-cis,cis-muconate"]. This is the basis for removing GO:0018850.
- catB is induced by muconate via CatM [PMID:7592340 "catA and catB were still
  inducible by muconate"].
- Family: NCBIfam TIGR02534 (muconate cycloisomerase), PANTHER PTHR48073:SF2,
  PROSITE MR_MLE motifs. Mn(2+) cofactor in UniProt is by similarity to P. putida
  CatB (P08310), whose Mn(2+) site was measured [PMID:6652062].

## Review decisions

- Accept GO:0018849 (core) and GO:0030145.
- Remove GO:0018850 (directly contradicted for this enzyme), GO:0006518 and
  GO:0009063 (enolase-superfamily over-transfer; consistent with the KT2440 catB review).
- Refine GO:0003824 to GO:0018849 and GO:0042952 to GO:0019615.
