# ade7 (SPBC409.10, UniProt Q9UUB4) notes

Naming: S. pombe ade7 = SAICAR synthetase (PurC), ortholog of S. cerevisiae ADE1 (not budding-yeast ADE7). `just fetch-gene` fetched the correct accession Q9UUB4 (PUR7_SCHPO).

## Evidence
- Activity: CAIR + L-aspartate + ATP -> SAICAR + ADP + Pi (EC 6.3.2.6) [file:SCHPO/ade7/ade7-uniprot.txt "Reaction=5-amino-1-(5-phospho-D-ribosyl)imidazole-4-carboxylate + L-"]; SAICAR synthetase family [UniProt:Q9UUB4].
- Partially purified S. pombe enzyme assayed in vitro, also uses cysteine sulfinate [PMID:8346915 "partially purified adenylosuccinate synthetase and SAICAR synthetase are capable of utilizing cysteine sulfinate in vitro to form sulfur analog products"]. Genetic link to phytochelatin-Cd-sulfide complex / Cd tolerance (same abstract).
- ade7+ used as an auxotrophic marker; ade7::loxP host [PMID:15704224 "We developed three new auxotrophic marker genes (arg12(+), tyr1(+) and ade7(+))"].
- Localisation: cytosol (+ nuclear signal) in ORFeome YFP screen [PMID:16823372].

## Decisions
- 11 GOA rows: 9 ACCEPT, 1 KEEP_AS_NON_CORE (nucleus HDA), 1 MODIFY (adenine biosynthetic process IMP -> 'de novo' IMP biosynthetic process; the de novo pathway does not make free adenine; same call as yeast ADE8/ADE57 reviews).
- Core MF GO:0004639, BP GO:0006189, cytosol; consistent with S. cerevisiae ADE1 review and PomBase GO-CAM 663d668500001911.
