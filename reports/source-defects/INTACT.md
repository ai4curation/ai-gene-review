# Source-record defects for INTACT

2 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_WITH_FROM (SUSPECTED, NOT_REPORTED)

- **Record:** UniProtKB:Q39192 enables GO:0005515 protein binding (IPI, PMID:19407142)
- **Field:** With/From
- **Change:** check UniProtKB:P49597 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/ARATH/SnRK2.2/SnRK2.2-ai-review.yaml`

This IPI row (protein binding, PMID:19407142) gives ABI1 (P49597) as the interacting partner of SnRK2.2 (Q39192). The main text of the paper names only PP2CA/AHG3 (P49598) and AHG1 (Q9FLI3) as the PP2Cs tested against SnRK2.2 by yeast two-hybrid; AHG1 is already the partner of the companion row from this paper. P49597 and P49598 differ by one digit. We could not see the supplementary figure (SOM Figure 3) that the text cites. Please check it: if ABI1 was not tested with SnRK2.2 there, the partner should be P49598 (PP2CA); if ABI1 was tested, the row is correct and a P49598 row may be missing.

> we observe interaction of SnRK2.2 with PP2CA/AHG3 and AHG1 using the Y2H assay (SOM Figure 3)
> — PMID:19407142

## 2. WRONG_WITH_FROM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P00533 enables GO:0005515 protein binding (IPI, PMID:16954185)
- **Field:** With/From
- **Change:** check UniProtKB:Q15109 (alternatives in the explanation)
- **Likely cause:** SYMBOL_COLLISION
- **Recorded in:** `genes/human/EGFR/EGFR-ai-review.yaml`

The enclosing PMID:16954185 annotation supplies Q15109 (AGER/RAGE) as the partner. The original Methods and Figure 6 describe human V5-tagged AGER1 and reciprocal EGFR coimmunoprecipitation in HEK293 and mouse mesangial cells; the paper distinguishes AGER1 from RAGE. Official identity maps AGER1/OST48 to DDOST/P39656. Frozen QuickGO record UniProtKB:P00533!447040847 is assigned by IntAct. The saved current IntAct export contains no matching PMID:16954185 pair, so the intended interaction record could not be authenticated. Please check that upstream record and its With/From mapping before repointing it to P39656; the positive AGER1 association is retained, and this does not assert that an EGFR–RAGE interaction is biologically impossible.

- **Evidence reference:** PMID:16954185

- **Evidence reference:** UniProtKB:P39656
