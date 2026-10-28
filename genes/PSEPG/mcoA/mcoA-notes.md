# mcoA (B0KSN7, PputGB1_2665) — Pseudomonas putida GB-1

## Identity
- TrEMBL B0KSN7, 1,131 aa, locus PputGB1_2665, SubName "Multicopper oxidase type 2"
  (submitter). Folder `mcoA` follows the literature symbol (fetched with `--alias mcoA`).
- Domains: Pfam Big_9 (PF17963), Cu-oxidase_2 (PF07731, 800-891), CDD CuRO_2_BOD/CuRO_3_BOD,
  IPR045087 Cu-oxidase_fam, PANTHER PTHR48267:SF1 (bilirubin oxidase subfamily; CueO, CotA).
- N-terminus MKTPAVIHPNRYVFQLSSVTALMLSLGLITAMAS...: Phobius calls TM 12-33, while the
  review states McoA has a Sec signal peptide
  [PMID:42757987 "Both MnxG and McoA possess amino-terminal Sec system signal peptides"].
  Unresolved; left as a suggested question. No CC term added.

## Function (genetic)
- Independently sufficient for Mn(II)/Mn(III) oxidation; double knockout with mnxG
  abolishes oxidation [PMID:23124227 "PputGB1_2447 and PputGB1_2665 encode two
MCOs that are independently capable of oxidizing both Mn(II) and Mn(III)"].
- Strain retaining only McoA oxidizes Mn(III)-L complexes [PMID:29706936 "mutants expressing only MnxG
and McoA were able to directly oxidize both species at varying levels"].
- Expressed at higher Mn(II) and in colony centres; relieves MnxG substrate inhibition
  [PMID:40470839 "coexpression of mnxG and mcoA not only alleviates substrate saturation and
inhibition of MnxG at high Mn(II) concentrations"]; [PMID:40122939 "McoA contributes to biomineralization under conditions where MnxG activity is restricted."].
- Not purified/characterized [PMID:42757987 "While the biochemical characteristics of MnxG and McoA from P. putida GB-1 have not been investigated"].

## Paralogy
- Not a duplication product of MnxG [PMID:42757987 "suggesting they did not arise by gene duplication"];
  MopA is an unrelated heme peroxidase (see mnxG notes).

## GO
- copper ion binding IEA -> ACCEPT; oxidoreductase activity IEA -> MODIFY to GO:0016724.
- Proposed new term "manganese oxidase activity" (EC 1.16.3.3, no GO term).

## CMMMech record notes (data/records/manganese.yaml; not edited)
- Evidence text says McoA was "shown by clean deletion and overexpression in Wright et al.
  (2018) to oxidize Mn(II)". The clean deletion is from Geszvain et al. 2013
  (PMID:23124227); I found no McoA overexpression in Wright 2018 (it studied Mn(III)-L
  oxidation by single-oxidase strains). The edge "Mutant analysis of mcoA demonstrates
  independent Mn(II) oxidase activity" is fine as genetics; "oxidase activity" is inferred,
  not measured on the protein.
