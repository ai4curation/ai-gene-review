# Source-record defects for GO_CENTRAL

1 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9Y6C2 involved_in GO:0045766 positive regulation of angiogenesis (IBA, GO_REF:0000033)
- **Field:** GO_ID
- **Change:** check GO:0045766 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/EMILIN1/EMILIN1-ai-review.yaml`

QuickGO record UniProtKB:Q9Y6C2!118992708 inherits positive regulation of angiogenesis through the genuine PAINT node PTN000396130 and MGI:1926189. The current mouse Q99K41 donor has conflicting PMID25056700 records: !178640421 BHF-UCL IMP negative regulation and !178640431 ComplexPortal IDA positive regulation. The operative mouse knockout study shows increased angiogenesis after Emilin1 loss, supporting contextual negative regulation. Please check the signed donor interpretation and resulting PAINT propagation; the node placement itself and positive matrix role are not disputed. The proposed negative term is context-specific, not a universal inactivity claim.

- **Evidence reference:** PMID:25056700

- **Evidence reference:** file:human/EMILIN1/EMILIN1-source-guide.md
