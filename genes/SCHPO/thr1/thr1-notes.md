# thr1 (SPBC4C3.03, UniProt O43056) notes

Homoserine kinase (EC 2.7.1.39), GHMP kinase, PTHR20861:SF1.

- [UniProt:O43056 "Reaction=L-homoserine + ATP = O-phospho-L-homoserine + ADP + H(+);"]; [UniProt:O43056 "FUNCTION: Commits homoserine to the threonine biosynthesis pathway by"] (by similarity to S. cerevisiae Thr1, P17423).
- HDA cytoplasm, PMID:16823372; IC cytosol from GO-CAM 678073a900003175.
- S. cerevisiae: [PMID:2176637 "Disruption of the THR1 gene results in threonine auxotrophy in yeast."]

## Decisions
- PomBase ISS (from P17423) "L-methionine metabolic process": SGD has no such THR1 annotation (checked genes/yeast/THR1/THR1-goa.tsv). Homoserine kinase competes with the methionine branch rather than participating -> MARK_AS_OVER_ANNOTATED.
- Core = GO:0004413 / GO:0009088 / cytosol, same as THR1 review and GO-CAM.
