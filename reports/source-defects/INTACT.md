# Source-record defects for INTACT

1 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_WITH_FROM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P00533 enables GO:0005515 protein binding (IPI, PMID:16954185)
- **Field:** With/From
- **Change:** check UniProtKB:Q15109 (alternatives in the explanation)
- **Likely cause:** SYMBOL_COLLISION
- **Recorded in:** `genes/human/EGFR/EGFR-ai-review.yaml`

The enclosing PMID:16954185 annotation supplies Q15109 (AGER/RAGE) as the partner. The original Methods and Figure 6 describe human V5-tagged AGER1 and reciprocal EGFR coimmunoprecipitation in HEK293 and mouse mesangial cells; the paper distinguishes AGER1 from RAGE. Official identity maps AGER1/OST48 to DDOST/P39656. Frozen QuickGO record UniProtKB:P00533!447040847 is assigned by IntAct. The saved current IntAct export contains no matching PMID:16954185 pair, so the intended interaction record could not be authenticated. Please check that upstream record and its With/From mapping before repointing it to P39656; the positive AGER1 association is retained, and this does not assert that an EGFR–RAGE interaction is biologically impossible.

- **Evidence reference:** PMID:16954185

- **Evidence reference:** UniProtKB:P39656
