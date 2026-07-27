# ADPRH catalytic-residue census across PANTHER PTHR16222

Members analysed: **31 reviewed (Swiss-Prot) entries** out of a family total of **29860** proteins (0.104% of the family). Every statement below is about the reviewed subset only.

Catalytic positions tested (human ADPRH P54922, each a UniProt `MUTAGEN` with note "Complete loss of activity"): S54, D55, D56, D302, S305.

## Cross-tabulation: does GO:0003875 track the residues?

| | holds GO:0003875 | does not |
|---|---|---|
| all 5 residues retained | 5 | see table |
| >=1 residue lost | 11 | see table |

Members that hold `GO:0003875` while missing at least one catalytic residue:

| accession | gene | organism | residues retained | % identity to ADPRH | evidence |
|---|---|---|---|---|---|
| B0KTG8 | tri1 | Pseudomonas putida (strain GB-1) | 4/5 | 31.3 | IEA(GO_REF:0000120) |
| A8GG79 | tri1 | Serratia proteamaculans (strain 568) | 4/5 | 29.4 | IEA(GO_REF:0000120) |
| P14300 | draG | Rhodospirillum rubrum | 3/5 | 27.5 | IEA(GO_REF:0000116), EXP(PMID:19706507) |
| A0A168WVR6 | tri1 | Pseudomonas putida (strain DSM 28064 / B6-2) | 3/5 | 23.2 | ISS(GO_REF:0000024), IEA(GO_REF:0000120) |
| Q3ZBM1 | ADPRHL1 | Bos taurus | 2/5 | 42.6 | IEA(GO_REF:0000120) |
| Q5XJB9 | adprhl1 | Danio rerio | 2/5 | 44.4 | IEA(GO_REF:0000002) |
| Q8NDY3 | ADPRHL1 | Homo sapiens | 2/5 | 46.6 | IEA(GO_REF:0000120) |
| Q8BGK2 | Adprhl1 | Mus musculus | 2/5 | 46.1 | IEA(GO_REF:0000120) |
| Q5RCJ0 | ADPRHL1 | Pongo abelii | 2/5 | 46.3 | IEA(GO_REF:0000120) |
| Q5XIB3 | Adprhl1 | Rattus norvegicus | 2/5 | 45.6 | IEA(GO_REF:0000120) |
| Q6AZR2 | adprhl1 | Xenopus laevis | 1/5 | 47.7 | IEA(GO_REF:0000002) |

## By clade

| clade | n | % identity to ADPRH | catalytic residues retained | hold GO:0003875 |
|---|---|---|---|---|
| ADPRH (ARH1) | 5 | 48.4-100.0 | 5-5 of 5 | 5/5 |
| ADPRHL1 (ARH2) | 7 | 42.6-47.7 | 1-2 of 5 | 7/7 |
| ADPRS (ARH3) | 7 | 25.8-28.1 | 3-4 of 5 | 0/7 |
| other / non-vertebrate | 12 | 20.0-32.5 | 0-4 of 5 | 4/12 |

## Is a residue loss real, or an alignment artefact?

A single identity threshold was tried first and **rejected**: a single identity threshold from the largest observed gap; it lands at 65.4% between Dictyostelium ADPRH (48.4%) and mouse Adprh (82.4%), i.e. a taxonomic boundary, and would discard the ADPRHL1 signal.

Percent identity here is computed over **aligned columns only** (gaps excluded), which runs slightly above the conventional alignment-length denominator. It is applied identically to every member, so no comparison below is affected, but the absolute figures should not be set against externally quoted identities.

Two computed measures are used instead. **Clade consistency** -- the same substitution at the same column in every member of a clade is not alignment noise. **Substitution chemistry** -- S<->T (hydroxyl retained); D<->E (carboxylate retained).

| clade | n | disruptive in EVERY member | disruptive substitutions | example member | hold GO:0003875 |
|---|---|---|---|---|---|
| ADPRH (ARH1) | 5 | none | 0 of 5 | none | 5/5 |
| ADPRHL1 (ARH2) | 7 | S305, D56 | 2-3 of 5 | D56->N(disruptive), D302->E(conservative), S305->A(disruptive) | 7/7 |
| ADPRS (ARH3) | 7 | none | 0 of 5 | S305->T(conservative) | 0/7 |
| other / non-vertebrate | 12 | none | 0-5 of 5 | S305->T(conservative) | 4/12 |

Positive control -- a member with its own **experimental** annotation to `GO:0003875` despite scoring below 5/5. Its substitutions bound what catalysis tolerates:

| accession | gene | organism | % id | retained | disruptive | substitutions | evidence |
|---|---|---|---|---|---|---|---|
| P14300 | draG | Rhodospirillum rubrum | 27.5 | 3/5 | 0 | S54->T(conservative), S305->T(conservative) | IEA(GO_REF:0000116), EXP(PMID:19706507) |

## Per-member detail

| accession | entry | gene | organism | % id | S54 | D55 | D56 | D302 | S305 | ident/5 | ident+own-site/5 | GO:0003875 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Q32KR8 | ADPRH_BOVIN | ADPRH | Bos taurus | 88.5 | S59 | D60 | D61 | D307 | S310 | 5/5 | 5 | ISS(GO_REF:0000024), ISS(GO_REF:0000024), IBA(GO_REF:0000033), IEA(GO_REF:0000120) |
| Q54H71 | ADPRH_DICDI | adprh | Dictyostelium discoideum | 48.4 | S79 | D80 | D81 | D348 | S351 | 5/5 | 5 | ISS(GO_REF:0000024), ISS(GO_REF:0000024), IEA(GO_REF:0000120) |
| P54922 | ADPRH_HUMAN | ADPRH | Homo sapiens | 100.0 | S54 | D55 | D56 | D302 | S305 | 5/5 | 5 | IBA(GO_REF:0000033), IEA(GO_REF:0000120), IDA(PMID:30472116), IMP(PMID:8349667) |
| P54923 | ADPRH_MOUSE | Adprh | Mus musculus | 82.4 | S59 | D60 | D61 | D307 | S310 | 5/5 | 5 | ISS(GO_REF:0000024), ISS(GO_REF:0000024), IBA(GO_REF:0000033), ISO(GO_REF:0000096), ISO(GO_REF:0000119), IEA(GO_REF:0000120), IMP(PMID:8349667) |
| Q02589 | ADPRH_RAT | Adprh | Rattus norvegicus | 82.9 | S59 | D60 | D61 | D307 | S310 | 5/5 | 5 | ISS(GO_REF:0000024), IBA(GO_REF:0000033), IEA(GO_REF:0000120), ISO(GO_REF:0000121), ISO(GO_REF:0000121), IDA(PMID:1375222), IMP(PMID:1375222) |
| Q5UQP4 | ADPRL_MIMIV | - | Acanthamoeba polyphaga mimivirus | 30.5 | S185 | D186 | D187 | D437 | T440* | 4/5 | n/a | - |
| Q66HT8 | ADPRS_DANRE | adprs | Danio rerio | 26.6 | S65 | D66 | D67 | D304 | T307* | 4/5 | 3 | - |
| B0KTG8 | TRI1_PSEPG | tri1 | Pseudomonas putida (strain GB-1) | 31.3 | T112* | D113 | D114 | D311 | S314 | 4/5 | 2 | IEA(GO_REF:0000120) |
| A8GG79 | TRI1_SERP5 | tri1 | Serratia proteamaculans (strain 568) | 29.4 | T116* | D117 | D118 | D315 | S318 | 4/5 | 2 | IEA(GO_REF:0000120) |
| Q58588 | Y1187_METJA | - | Methanocaldococcus jannaschii (strain ATCC 43067 / DSM 2661 / JAL-1 / JCM 10045 / NBRC 100440) | 28.8 | T60* | D61 | D62 | D253 | S256 | 4/5 | n/a | - |
| O28550 | Y1724_ARCFU | - | Archaeoglobus fulgidus (strain ATCC 49558 / DSM 4304 / JCM 9628 / NBRC 100126 / VC-16) | 32.5 | T54* | D55 | D56 | D254 | S257 | 4/5 | n/a | - |
| Q5UQA6 | ADPRM_MIMIV | - | Acanthamoeba polyphaga mimivirus | 23.7 | T62* | D63 | D64 | D277 | T280* | 3/5 | n/a | - |
| Q3SYV9 | ADPRS_BOVIN | ADPRS | Bos taurus | 26.5 | T77* | D78 | D79 | D315 | T318* | 3/5 | 3 | - |
| Q5ZI51 | ADPRS_CHICK | ADPRS | Gallus gallus | 25.8 | T79* | D80 | D81 | D317 | T320* | 3/5 | 3 | - |
| Q9NX46 | ADPRS_HUMAN | ADPRS | Homo sapiens | 27.8 | T76* | D77 | D78 | D314 | T317* | 3/5 | 3 | - |
| H3BCW1 | ADPRS_LATCH | adprs | Latimeria chalumnae | 26.1 | T62* | D63 | D64 | D303 | T306* | 3/5 | 3 | - |
| Q8CG72 | ADPRS_MOUSE | Adprs | Mus musculus | 27.9 | T82* | D83 | D84 | D320 | T323* | 3/5 | 3 | - |
| Q28FQ6 | ADPRS_XENTR | adprs | Xenopus tropicalis | 28.1 | T57* | D58 | D59 | D295 | T298* | 3/5 | 3 | - |
| P14300 | DRAG_RHORU | draG | Rhodospirillum rubrum | 27.5 | T59* | D60 | D61 | D243 | T246* | 3/5 | 1 | IEA(GO_REF:0000116), EXP(PMID:19706507) |
| A0A168WVR6 | TRI1_PSEP8 | tri1 | Pseudomonas putida (strain DSM 28064 / B6-2) | 23.2 | L63* | S64* | D65 | D322 | S325 | 3/5 | 0 | ISS(GO_REF:0000024), IEA(GO_REF:0000120) |
| P76418 | YEGU_ECOLI | yegU | Escherichia coli (strain K12) | 27.7 | T60* | D61 | D62 | D280 | T283* | 3/5 | n/a | - |
| Q3ZBM1 | ARHL1_BOVIN | ADPRHL1 | Bos taurus | 42.6 | S56 | D57 | N58* | E304* | A307* | 2/5 | n/a | IEA(GO_REF:0000120) |
| Q5XJB9 | ARHL1_DANRE | adprhl1 | Danio rerio | 44.4 | S53 | D54 | G55* | E300* | A303* | 2/5 | n/a | IEA(GO_REF:0000002) |
| Q8NDY3 | ARHL1_HUMAN | ADPRHL1 | Homo sapiens | 46.6 | S56 | D57 | N58* | E304* | A307* | 2/5 | n/a | IEA(GO_REF:0000120) |
| Q8BGK2 | ARHL1_MOUSE | Adprhl1 | Mus musculus | 46.1 | S55 | D56 | N57* | E303* | A306* | 2/5 | n/a | IEA(GO_REF:0000120) |
| Q5RCJ0 | ARHL1_PONAB | ADPRHL1 | Pongo abelii | 46.3 | S56 | D57 | N58* | E304* | A307* | 2/5 | n/a | IEA(GO_REF:0000120) |
| Q5XIB3 | ARHL1_RAT | Adprhl1 | Rattus norvegicus | 45.6 | S55 | D56 | N57* | E303* | A306* | 2/5 | n/a | IEA(GO_REF:0000120) |
| Q6AZR2 | ARHL1_XENLA | adprhl1 | Xenopus laevis | 47.7 | S56 | N57* | N58* | E304* | A307* | 1/5 | n/a | IEA(GO_REF:0000002) |
| Q03442 | CRJ1A_TRICY | - | Tripedalia cystophora | 21.5 | Y67* | G68* | E69* | C274* | P277* | 0/5 | n/a | - |
| Q03443 | CRJ1B_TRICY | - | Tripedalia cystophora | 20.0 | D60* | N61* | G62* | C274* | A277* | 0/5 | n/a | - |
| P40821 | CRJ1C_TRICY | - | Tripedalia cystophora | 20.1 | Y67* | G68* | E69* | C274* | P277* | 0/5 | n/a | - |

`*` = not identical to the ADPRH residue. `ident+own-site/5` is `n/a` where the entry has no
BINDING/ACT_SITE features of its own, so the second condition cannot be evaluated; those
counts are NOT promoted to matches.

## Metals actually present in the ADPRH structures

| PDB | resolution (A) | bound non-polymer components | MG | K | PubMed |
|---|---|---|---|---|---|
| 3HFW | 1.92 | K, MG | yes | yes | - |
| 6G28 | 1.23 | AR6, MG | yes | no | 30472116 |
| 6G2A | 1.8 | A3R, MG | yes | no | 30472116 |
| 6IUX | 1.195 | AR6, MG | yes | no | - |

Magnesium is present in **4 of 4** structures (3HFW, 6G28, 6G2A, 6IUX). Potassium is present in **1 of 4** (3HFW).

Every structure containing potassium is at the worst resolution in the set (1.92 A); all 3 better-resolved structures (6G28, 6G2A, 6IUX) contain none.

## InterPro signature membership (the annotation route)

- `P54922`: IPR005502, IPR012108, IPR036705, IPR050792
- `Q8NDY3`: IPR005502, IPR012108, IPR036705, IPR050792
- `Q9NX46`: IPR005502, IPR036705, IPR050792

`IPR012108` ("ADP-ribosylarginine hydrolase") is the family-specific signature whose interpro2go mapping supplies `GO:0000287`, `GO:0003875` and `GO:0051725`.
