# KAO1 (ent-kaurenoic acid oxidase, CYP88A3; At1g05160; UniProt O23051) - curation notes

- Accession verified against UniProt (KAO1_ARATH).
- Falcon deep research attempted and failed (exit code 1).

## Function
- ent-kaurenoic acid -> GA12 in three steps (RHEA:33219, EC 1.14.14.107) [PMID:11172076 "Yeast strains expressing cDNAs encoding each of the two Arabidopsis and the barley CYP88A enzymes catalyze the three steps of the GA biosynthesis pathway from ent-kaurenoic acid to GA(12)."]
- KAO1/KAO2 redundant: single mutants wild-type, double mutant non-germinating GA dwarf [PMID:25146977 "the kao1 kao2 double mutant exhibits typical non-germinating GA-dwarf phenotypes"].

## Location
- Leader sequence targets GFP to ER [PMID:11722763 "The leader sequences of the two ent-kaurenoic acid oxidases (AtKAO1 and AtKAO2) from Arabidopsis direct GFP to the endoplasmic reticulum."].

## Curation decisions
- Generic P450 MF terms -> MODIFY to GO:0051777.
- pollen tube development IBA (from rice KAO/RPE1): kept as non-core (downstream GA-dependent phenotype).
