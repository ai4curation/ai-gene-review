# Affinage vs AIGR — automated GO overlap (n=12)

**Core MF captured exactly:** 1/12 genes with an authored `core_functions` MF term had that exact term in Affinage's `molecular_activity` profile.

**Slim-level (goslim_generic, is_a+part_of closure over `go-basic-2026-03-25.obo`):** core MF bin emitted 10/12; Affinage's top-supported MF is a bin of a core MF 6/11; core location bin emitted 8/10.

**Shared exact ids:** 26 in total, 24 after excluding GOA terms the review wholly REMOVEd / MARK_AS_OVER_ANNOTATED.

| gene | Aff MF | Aff CC | GOA terms | shared (exact) | shared, excl. rejected | Aff-only | core MF exact | core MF slim bin | top Aff MF in core bin | core CC slim bin |
|------|-------:|-------:|----------:|---------------:|------:|---------:|:---:|:---:|:---:|:---:|
| ILK | 4 | 3 | 41 | 2 | 2 | 5 | ❌ | ✅ | ✅ | ❌ |
| ROR1 | 4 | 3 | 20 | 1 | 1 | 6 | ❌ | ✅ | ✅ | ✅ |
| CPT1C | 4 | 1 | 22 | 2 | 1 | 3 | ❌ | ✅ | ❌ | ✅ |
| CASP12 | 0 | 0 | 12 | 0 | 0 | 0 | ❌ | ❌ | — | ❌ |
| PARK7 | 5 | 4 | 119 | 3 | 3 | 6 | ❌ | ✅ | ❌ | ✅ |
| UCHL1 | 2 | 3 | 20 | 1 | 1 | 4 | ❌ | ✅ | ✅ | ✅ |
| HDAC6 | 7 | 5 | 100 | 4 | 4 | 8 | ❌ | ✅ | ✅ | — |
| NDUFA4 | 1 | 1 | 14 | 1 | 1 | 1 | ❌ | ❌ | ❌ | ✅ |
| PLD3 | 6 | 4 | 25 | 3 | 3 | 7 | ❌ | ✅ | ✅ | ✅ |
| RASA1 | 5 | 4 | 28 | 2 | 2 | 7 | ❌ | ✅ | ❌ | ✅ |
| GAPDH | 8 | 4 | 49 | 5 | 4 | 7 | ✅ | ✅ | ✅ | ✅ |
| KEAP1 | 5 | 2 | 24 | 2 | 2 | 5 | ❌ | ✅ | ❌ | — |
