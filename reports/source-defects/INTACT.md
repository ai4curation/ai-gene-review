# Source-record defects for INTACT

1 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_WITH_FROM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q39192 enables GO:0005515 protein binding (IPI, PMID:19407142)
- **Field:** With/From
- **Change:** check UniProtKB:P49597 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/ARATH/SnRK2.2/SnRK2.2-ai-review.yaml`

This IPI row (protein binding, PMID:19407142) gives ABI1 (P49597) as the interacting partner of SnRK2.2 (Q39192). The main text of the paper names only PP2CA/AHG3 (P49598) and AHG1 (Q9FLI3) as the PP2Cs tested against SnRK2.2 by yeast two-hybrid; AHG1 is already the partner of the companion row from this paper. P49597 and P49598 differ by one digit. We could not see the supplementary figure (SOM Figure 3) that the text cites. Please check it: if ABI1 was not tested with SnRK2.2 there, the partner should be P49598 (PP2CA); if ABI1 was tested, the row is correct and a P49598 row may be missing.

> we observe interaction of SnRK2.2 with PP2CA/AHG3 and AHG1 using the Y2H assay (SOM Figure 3)
> — PMID:19407142
