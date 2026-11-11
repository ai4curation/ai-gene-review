# Bacteriophage T7 Gene 18 (Small Terminase Subunit gp18) — Curation Notes

## Overview
Bacteriophage T7 gene *18* (`P03693`, 89 aa, ~10.1 kDa) encodes the DNA maturation protein gp18 (small terminase subunit, TerS) [PMID:6864790, PMID:3036832].

## Biochemical and Genetic Characterization
- **Essential Role in Concatemeric DNA Packaging**: White & Richardson (1987) overproduced, purified, and characterized gp18 and demonstrated that it is essential for packaging concatemeric T7 DNA into proheads (`GO:0019073`, `viral DNA genome packaging`), acting together with the large terminase subunit gp19, prohead portal protein gp8, and scaffolding protein gp9 [PMID:3036832, PMID:3298244].
- **DNA Recognition and Octameric Assembly**: Purified native gp18 is an acidic monomer of ~10 kDa that self-associates into a ~83 kDa octameric ring (`GO:0042802`, `identical protein binding`) and binds packaging recognition (`pac`) sequences on concatemeric viral DNA (`GO:0003677`, `DNA binding`) to recruit the gp19 large terminase motor [PMID:3036832].

## GO Annotation Review
- **Accept**: `GO:0003677` (`DNA binding`, `IEA` `GO_REF:0000043`).
- **New**:
  - `GO:0019073` (`viral DNA genome packaging`, `IMP`, `PMID:3036832`) based on direct genetic and in vitro packaging analyses [PMID:3036832, PMID:3298244].
  - `GO:0042802` (`identical protein binding`, `IDA`, `PMID:3036832`) based on purification and hydrodynamic characterization of the native gp18 homo-octamer [PMID:3036832].
