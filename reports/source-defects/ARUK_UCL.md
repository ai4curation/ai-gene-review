# Source-record defects for ARUK_UCL

1 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P08246 enables GO:0002020 protease binding (IPI, PMID:6980881)
- **Field:** GO_ID
- **Change:** check GO:0002020 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/ELANE/ELANE-ai-review.yaml`

The BHF-UCL annotation represented by QuickGO UniProtKB:P08246!58684890 cites PMID:6980881 with UniProtKB:P08697. P08697 is SERPINF2/alpha-2-antiplasmin, a protease inhibitor rather than a protease or peptidase. The original directly demonstrates human leukocyte elastase cleavage and inactivation of that inhibitor, so the positive enzyme–substrate evidence does not support protease binding as defined by GO:0002020. Please check the source term and retain the demonstrated proteolytic evidence; no replacement specific binding term or mistaken source identifier is asserted.

- **Evidence reference:** PMID:6980881
