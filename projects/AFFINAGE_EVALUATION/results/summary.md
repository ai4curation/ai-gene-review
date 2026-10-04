# Affinage vs AIGR — automated GO overlap (n=12)

**Core MF captured exactly:** 2/12 genes with an authored `core_functions` MF term had that exact term in Affinage's `molecular_activity` profile.

**Slim-level (goslim_generic, is_a+part_of closure over `go-basic-2026-03-25.obo`):** core MF bin emitted 11/12; Affinage's top-supported MF is a bin of a core MF 10/12; core location bin emitted 10/12.

**Shared exact ids:** 31 in total, 31 after excluding GOA terms the review wholly REMOVEd / MARK_AS_OVER_ANNOTATED.

| gene | Aff MF | Aff CC | GOA terms | shared (exact) | shared, excl. rejected | Aff-only | core MF exact | core MF slim bin | top Aff MF in core bin | core CC slim bin |
|------|-------:|-------:|----------:|---------------:|------:|---------:|:---:|:---:|:---:|:---:|
| GPX4 | 5 | 4 | 26 | 4 | 4 | 5 | ❌ | ✅ | ✅ | ✅ |
| TP53 | 2 | 3 | 202 | 3 | 3 | 2 | ❌ | ✅ | ❌ | ✅ |
| AATF | 5 | 5 | 14 | 3 | 3 | 7 | ✅ | ✅ | ✅ | ✅ |
| ABCA1 | 5 | 3 | 78 | 2 | 2 | 6 | ❌ | ✅ | ✅ | ✅ |
| ACADM | 2 | 1 | 21 | 1 | 1 | 2 | ❌ | ✅ | ✅ | ✅ |
| ABL1 | 4 | 4 | 139 | 5 | 5 | 3 | ✅ | ✅ | ✅ | ✅ |
| ACTB | 3 | 3 | 100 | 3 | 3 | 3 | ❌ | ✅ | ✅ | ✅ |
| AHR | 5 | 2 | 49 | 3 | 3 | 4 | ❌ | ✅ | ✅ | ✅ |
| ADRB2 | 2 | 1 | 49 | 1 | 1 | 2 | ❌ | ✅ | ✅ | ✅ |
| AGO2 | 3 | 5 | 53 | 3 | 3 | 5 | ❌ | ✅ | ✅ | ❌ |
| ADA | 5 | 0 | 32 | 0 | 0 | 5 | ❌ | ❌ | ❌ | ❌ |
| ACSL4 | 3 | 2 | 26 | 3 | 3 | 2 | ❌ | ✅ | ✅ | ✅ |
