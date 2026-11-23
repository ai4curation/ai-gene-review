# CANGA ERG27 notes

## 2026-11-17 PTHR43647 Erg27 review

`CANGA/ERG27` first appeared to have no GOA rows because the repository QuickGO fetch left `ERG27-goa.tsv` header-only and then considered it up to date. A forced repo fetch on 2026-11-20 still rewrote the file to a header-only slice, so the 10 Q6FIV3 QuickGO rows were recovered directly; they include UniProt exact reductase and ergosterol-biosynthesis IEAs, three CGD `ND` placeholders, ER/ER-membrane/lipid-droplet/catalytic-complex transfers, and a TreeGrafter mitochondrial outer membrane transfer.

Q6FIV3 is a UniProt-reviewed *Nakaseomyces glabratus* `ERG27` protein in `PTHR43647:SF1`, the same PANTHER subfamily as characterized *S. cerevisiae* Erg27, experimentally grounded *C. albicans* Erg27, and *S. pombe* erg27. UniProt curates the broad Rhea/EC 1.1.1.270 reaction and the zymosterol-from-lanosterol pathway, and the direct *C. albicans* seed reports that ERG27 is "required for sterol C-4 demethylation" [PMID:15552648 "required for sterol C-4 demethylation"].

No N. glabratus or C. glabrata paper found in this review directly assayed or localized Erg27: searches for Q6FIV3, CAGL0M11506g, Candida glabrata ERG27, and Nakaseomyces glabratus ERG27 found Swiss-Prot/EnsemblFungi-derived records but no species-specific Erg27 functional paper.

Unlike Q5A888 from *C. albicans* and Q4WQ42 from *A. fumigatus*, Q6FIV3 does not currently receive GO-Central PAINT IBAs from `PTHR43647`, so this review keeps the PAINT propagation question in `suggested_questions` instead of creating self-issued IBA rows.
