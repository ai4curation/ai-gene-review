# CANGA ERG27 notes

## 2026-11-17 PTHR43647 Erg27 review

`CANGA/ERG27` first appeared to have no GOA rows because the standard QuickGO fetch left `ERG27-goa.tsv` header-only and then considered it up to date. A direct Q6FIV3 QuickGO query without `taxonName` returns 10 rows, including UniProt exact reductase and ergosterol-biosynthesis IEAs, three stale CGD `ND` placeholders, ER/ER-membrane/lipid-droplet/catalytic-complex transfers, and a TreeGrafter mitochondrial outer membrane transfer.

Q6FIV3 is a UniProt-reviewed *Nakaseomyces glabratus* `ERG27` protein in `PTHR43647:SF1`, the same PANTHER subfamily as characterized *S. cerevisiae* Erg27, experimentally grounded *C. albicans* Erg27, and *S. pombe* erg27. UniProt curates the broad Rhea/EC 1.1.1.270 reaction and the zymosterol-from-lanosterol pathway, and the direct *C. albicans* seed reports that ERG27 is "required for sterol C-4 demethylation" [PMID:15552648 "required for sterol C-4 demethylation"].

Unlike Q5A888 from *C. albicans* and Q4WQ42 from *A. fumigatus*, Q6FIV3 does not currently receive GO-Central PAINT IBAs from `PTHR43647`, so this review keeps the PAINT propagation question in `suggested_questions` instead of creating self-issued IBA rows.
