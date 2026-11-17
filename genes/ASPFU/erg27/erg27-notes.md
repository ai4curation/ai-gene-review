# ASPFU erg27 notes

## 2026-11-17 PTHR43647 Erg27 review

The current GOA fetch for *Aspergillus fumigatus* `erg27` has no rows, but the PAINT leaf GAF projects the Erg27 IBAs for `GO:0000253` 3-beta-hydroxysteroid 3-dehydrogenase (NADP+) activity, `GO:0006696` ergosterol biosynthetic process, `GO:0005789` endoplasmic reticulum membrane, and `GO:0005811` lipid droplet to Q4WQ42.

Q4WQ42 is a reviewed representative member of `PTHR43647:SF1`, matching the direct *Candida albicans* and *S. cerevisiae* seeds for the exact Erg27 activity node. The cached *A. fumigatus* pathway paper is abstract-only; the abstract says sterol profiling in sterol-biosynthesis mutants "led to a better understanding of the ergosterol biosynthesis pathway in this important fungus" but does not directly assay `erg27` [PMID:18191972 "The analysis of the sterol composition in these mutant strains led to a better"]. The Q4WQ42 functional call is therefore a paralog-aware orthology inference, not a direct *A. fumigatus* biochemical result.

As in the *C. albicans* review, the lipid-droplet row is recorded because current PAINT propagates it from the S. cerevisiae Erg27 lipid-particle pool, but the core function is the ER C-4 demethylation reaction.
