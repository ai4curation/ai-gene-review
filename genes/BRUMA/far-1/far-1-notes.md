# BRUMA far-1 notes

## 2026-11-21 cross-check

- The local GOA snapshot has five rows for Q93142/FAR1_BRUMA: two
  extracellular-region rows, direct `fatty acid binding`, direct
  `retinol binding`, and the InterPro2GO parent `lipid binding`. No row was
  PENDING before the cross-check.
- UniProtKB identifies Q93142 as *Brugia malayi* `far-1`/Bm20, a 178-aa
  reviewed precursor with a predicted residues 1-16 signal peptide, a mature
  residues 17-178 chain, two predicted coiled-coil spans, and PANTHER family
  `PTHR31418:SF7`.
- PANTHER `PTHR31418:SF7` places B. malayi Q93142 in the same subfamily as the
  *C. elegans* FAR-1 exemplar P34382; *C. elegans* FAR-2 P34383 falls in
  `PTHR31418:SF19`, so it is a useful paralog comparator but not the same
  subfamily exemplar. These assignments are recorded in
  `interpro/panther/PTHR31418/PTHR31418-entries.csv`.
- PMID:12106870 directly supports the two molecular-function rows and the
  secreted location: recombinant Bm-FAR-1 and Ov-FAR-1 bound
  all-trans-retinol, DAUDA, and oleic acid in fluorescence assays, and the FAR
  proteins were "released into culture medium" by all filarial species and
  developmental stages tested [PMID:12106870 The FAR proteins of filarial
  nematodes: secretion, glycosylation and lipid binding characteristics.,
  "Both were found to bind all-trans-retinol"].
- PMID:10569745 cloned and expressed Bm20, the B. malayi homolog of O. volvulus
  Ov20, to compare filarial immune recognition and glycosylation patterns; the
  paper describes cloning "homologues of Ov20" from B. malayi and A. viteae
  [PMID:10569745 Comparative analysis of glycosylated and nonglycosylated
  filarial homologues of the 20-kilodalton retinol binding protein from
  Onchocerca volvulus (Ov20)., "homologues of Ov20 from two closely related
  filarial species"].
- PMID:7770083 isolated the O. volvulus Ov20 cDNA, detected lower-stringency
  Brugia malayi homologs by Southern blot, and detected the Ov20 antigen in
  adult-culture supernatants; its Brugia evidence is comparative family
  context rather than direct Bm-FAR-1 biochemistry [PMID:7770083
  Characterisation of an immunodominant glycoprotein antigen of Onchocerca
  volvulus with homologues in other filarial nematodes and Caenorhabditis
  elegans., "Homologues of the Ov 20 gene were detected"].

Bm-FAR-1 has direct in vitro fatty-acid and retinol binding and secretion
evidence, but native in vivo cargoes, uptake routes, and immunomodulatory
phenotypes in B. malayi remain inferred from the FAR family model rather than
directly assayed for Q93142.
