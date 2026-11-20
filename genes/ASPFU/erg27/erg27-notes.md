# ASPFU erg27 notes

## 2026-11-17 PTHR43647 Erg27 review

The repository QuickGO fetch for *Aspergillus fumigatus* `erg27` still returns a header-only `erg27-goa.tsv` when it
asks QuickGO to expand `taxonName`, but a direct QuickGO query without that expansion returned nine rows for Q4WQ42:
`GO:0000253` 3-beta-hydroxysteroid 3-dehydrogenase (NADP+) activity, `GO:0006696` ergosterol biosynthetic process,
`GO:0016126` sterol biosynthetic process, and three ER-membrane / lipid-droplet evidence pairs from PAINT, UniProt
ISS, and UniProtKB-SubCell. These are therefore treated as existing annotations to adjudicate, not as new
review-proposed annotations.

Q4WQ42 is a reviewed representative member of `PTHR43647:SF1`, matching the direct *Candida albicans* and *S. cerevisiae* seeds for the exact Erg27 activity node. The cached *A. fumigatus* pathway paper is abstract-only; the abstract says sterol profiling in sterol-biosynthesis mutants "led to a better understanding of the ergosterol biosynthesis pathway in this important fungus" but does not directly assay `erg27` [PMID:18191972 "The analysis of the sterol composition in these mutant strains led to a better"]. The Q4WQ42 functional call is therefore a paralog-aware orthology inference, not a direct *A. fumigatus* biochemical result.

The lipid-droplet row is recorded as a non-core inherited location from the S. cerevisiae Erg27 lipid-particle pool,
while the core A. fumigatus function remains the ER C-4 demethylation reaction. A. fumigatus-specific experiments
could test whether Erg27 also stabilizes oxidosqualene cyclase Erg7, because the cached C. albicans null study found
"complete loss of both 3-keto reductase and oxidosqualene cyclase" activities [PMID:15552648 "complete loss of both
3-keto reductase and oxidosqualene cyclase"].
