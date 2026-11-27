# Affinage vs AIGR — automated GO overlap (n=13)

**Core MF captured exactly:** 0/13 genes with an authored `core_functions` MF term had that exact term in Affinage's `molecular_activity` profile.

**Slim-level (goslim_generic, is_a+part_of closure over `go-basic-2026-03-25.obo`):** core MF bin emitted 13/13; Affinage's top-supported MF is a bin of a core MF 12/13; core location bin emitted 11/11.

**Shared exact ids:** 36 in total, 33 after excluding GOA terms the review wholly REMOVEd / MARK_AS_OVER_ANNOTATED.

| gene | Aff MF | Aff CC | GOA terms | shared (exact) | shared, excl. rejected | Aff-only | core MF exact | core MF slim bin | top Aff MF in core bin | core CC slim bin |
|------|-------:|-------:|----------:|---------------:|------:|---------:|:---:|:---:|:---:|:---:|
| SOD1 | 3 | 3 | 85 | 3 | 3 | 3 | ❌ | ✅ | ✅ | ✅ |
| MYC | 3 | 2 | 94 | 3 | 3 | 2 | ❌ | ✅ | ✅ | ✅ |
| STAT3 | 4 | 3 | 131 | 3 | 3 | 4 | ❌ | ✅ | ✅ | ✅ |
| EGFR | 5 | 3 | 120 | 5 | 5 | 3 | ❌ | ✅ | ✅ | ✅ |
| CFTR | 4 | 5 | 62 | 1 | 1 | 8 | ❌ | ✅ | ✅ | ✅ |
| LDHA | 3 | 1 | 20 | 2 | 2 | 2 | ❌ | ✅ | ✅ | ✅ |
| PKM | 4 | 5 | 37 | 6 | 6 | 3 | ❌ | ✅ | ✅ | — |
| MAPK1 | 5 | 6 | 70 | 3 | 2 | 8 | ❌ | ✅ | ✅ | ✅ |
| GSK3B | 3 | 2 | 128 | 2 | 2 | 3 | ❌ | ✅ | ✅ | ✅ |
| CASP3 | 2 | 1 | 72 | 1 | 1 | 2 | ❌ | ✅ | ✅ | ✅ |
| SIRT1 | 3 | 3 | 168 | 2 | 2 | 4 | ❌ | ✅ | ✅ | — |
| FASN | 3 | 1 | 32 | 3 | 1 | 1 | ❌ | ✅ | ✅ | ✅ |
| HMOX1 | 3 | 3 | 46 | 2 | 2 | 4 | ❌ | ✅ | ❌ | ✅ |
