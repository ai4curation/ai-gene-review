# Affinage vs AIGR — automated GO overlap (n=5)

**Core MF captured exactly:** 1/5 genes with an authored `core_functions` MF term had that exact term in Affinage's `molecular_activity` profile.

**Slim-level (goslim_generic, is_a+part_of closure over `go-basic-2026-03-25.obo`):** core MF bin emitted 4/5; Affinage's top-supported MF is a bin of a core MF 4/4; core location bin emitted 4/5.

**Shared exact ids:** 6 in total, 6 after excluding GOA terms the review wholly REMOVEd / MARK_AS_OVER_ANNOTATED.

| gene | Aff MF | Aff CC | GOA terms | shared (exact) | shared, excl. rejected | Aff-only | core MF exact | core MF slim bin | top Aff MF in core bin | core CC slim bin |
|------|-------:|-------:|----------:|---------------:|------:|---------:|:---:|:---:|:---:|:---:|
| CALM1 | 2 | 1 | 61 | 1 | 1 | 2 | ❌ | ✅ | ✅ | ✅ |
| OTC | 2 | 1 | 24 | 1 | 1 | 2 | ❌ | ✅ | ✅ | ✅ |
| G6PD | 2 | 1 | 33 | 1 | 1 | 2 | ❌ | ✅ | ✅ | ✅ |
| KRAS | 4 | 2 | 42 | 3 | 3 | 3 | ✅ | ✅ | ✅ | ✅ |
| INS | 0 | 0 | 77 | 0 | 0 | 0 | ❌ | ❌ | — | ❌ |
