# Source-record defects for CACAO

1 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q03456 involved_in GO:0019290 siderophore biosynthetic process (IMP, PMID:8478325)
- **Change:** GO:0019290 → GO:1900705 (negative regulation of siderophore biosynthetic process)
- **Likely cause:** OTHER
- **Recorded in:** `genes/PSEAE/fur/fur-ai-review.yaml`

CACAO annotation of GO:0019290 siderophore biosynthetic process (IMP, PMID:8478325) to P. aeruginosa Fur (Q03456). Fur mutants constitutively produce siderophores, showing that Fur represses the pathway, not that it performs biosynthesis. Repoint to GO:1900705.

> These manganese-resistant Fur mutants constitutively produce siderophores and exotoxin A when grown in concentrations of iron that normally repress their production.
> — PMID:8478325
