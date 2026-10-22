# Source-record defects for MGI

1 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:P54320!148349945
- **Subject:** UniProtKB:P15502
- **Field:** DB_Object_ID
- **Change:** check UniProtKB:P54320 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/ELN/ELN-ai-review.yaml`

The current mouse Eln GO:0071953 IDA donor record cites PMID:17099216. Its recovered Methods and Results use bovine tropoelastin-EGFP in mouse MEF 3T3 cells and state that parental cells lack tropoelastin expression. Please check whether the donor annotation is intended to describe the expressed bovine construct or has separate evidence for endogenous mouse Eln. No replacement accession is asserted. Independent human elastic-fiber localization remains supported; this query concerns the source gene-product attribution, not the location itself.

- **Evidence reference:** PMID:17099216
