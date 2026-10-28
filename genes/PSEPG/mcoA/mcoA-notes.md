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

## EC 1.16.3.3 (ExplorEnz, looked up 2026-10-28)
Recorded verbatim-ish so it need not be re-checked (see also mnxG notes):
- Accepted name: **manganese oxidase**
- Reaction: 4 Mn2+ + 2 O2 + 4 H2O = 4 Mn(IV)O2 + 8 H+ (overall reaction)
  - (1a) 4 Mn2+ + O2 + 4 H+ = 4 Mn3+ + 2 H2O
  - (1b) 4 Mn3+ + O2 + 6 H2O = 4 Mn(IV)O2 + 12 H+
- Other name(s): mnxG (gene name); mofA (gene name); moxA (gene name); cotA (gene name)
- Systematic name: manganese(II):oxygen oxidoreductase
- Comments: "The enzyme, which belongs to the multicopper oxidase family, is found in many
  bacterial strains. It oxidizes soluble manganese(II) to insoluble manganese(IV) oxides."

The overall product is Mn(IV)O2; Mn(III) is an intermediate (step 1a), not the product, so
the proposed term's definition states MnO2 and the one-electron steps live in
`justification` as mechanism. The definition quotes the ExplorEnz overall reaction in that
entry's own canonical form (4 Mn2+ + 2 O2 + 4 H2O = 4 Mn(IV)O2 + 8 H+); an earlier draft
wrote the same reaction halved (2 Mn2+ + O2 + 2 H2O = 2 MnO2 + 4 H+), which balances but
does not match the form quoted two lines above it. Note that cotA, one of the EC entry's gene names, is also the
protein that dominates McoA's PANTHER subfamily (below).

## GO
- copper ion binding IEA -> ACCEPT; oxidoreductase activity IEA -> MODIFY to GO:0016724.
  The copper-centre claim is cited at the **subfamily** level, PTHR48267:SF1 (BILIRUBIN
  OXIDASE), rather than the bare family PTHR48267 (CUPREDOXIN SUPERFAMILY PROTEIN). The
  reason is the family's *name*, not its membership: `PTHR48267-metadata.yaml` gives
  `subfamilies: 1`, `proteins: 7748` and `integrated: IPR045087`, and every row of
  `PTHR48267-entries.csv` is `PTHR48267:SF1`, so family and subfamily are coextensive in
  membership and the family does carry the three-domain multicopper oxidase claim via
  IPR045087. What "CUPREDOXIN SUPERFAMILY PROTEIN" does not state is the type-1-copper-plus-
  trinuclear-cluster architecture, whereas SF1's name and member composition do: all 36
  listed members are CotA laccases, E. coli CueO, FtsP/SufI and fungal bilirubin oxidase,
  i.e. canonical three-domain MCOs. (An earlier draft of these notes said the bare family
  "also contains single-domain type-1-only cupredoxins with no trinuclear cluster"; that is
  false - the fetched data show one subfamily and a single member set - and is superseded by
  the naming argument above. The GO call is unaffected.)
- Proposed new term "manganese oxidase activity" (EC 1.16.3.3, no GO term). The MODIFY
  replacement is GO:0016724 because that is what is annotatable today; when GO creates the
  proposed term, `proposed_replacement_terms` should become it and
  `core_functions.molecular_function` should take its id.
- No BP added: no lineage-neutral biomineralization process term exists. A sibling review
  (SIL1, ai4curation/ai-gene-review#5636) ran that OLS search; every hit is GO:0031214
  biomineral tissue development or a descendant.

## CMMMech record notes (CMMMech repository, data/records/manganese.yaml; not edited here)
- Evidence text says McoA was "shown by clean deletion and overexpression in Wright et al.
  (2018) to oxidize Mn(II)". The clean deletion is from Geszvain et al. 2013
  (PMID:23124227); I found no McoA overexpression in Wright 2018 (it studied Mn(III)-L
  oxidation by single-oxidase strains). The edge "Mutant analysis of mcoA demonstrates
  independent Mn(II) oxidase activity" is fine as genetics; "oxidase activity" is inferred,
  not measured on the protein.
