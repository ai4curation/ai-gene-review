# Source-record defects for GOA_EBI

2 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I2J4 involved_in GO:2000142 regulation of DNA-templated transcription initiation (IEA, GO_REF:0000108)
- **Field:** Gene product
- **Change:** delete the record asserting UniProtKB:Q9I2J4
- **Likely cause:** OVER_PROPAGATION
- **Recorded in:** `genes/PSEAE/femA/femA-ai-review.yaml`

This row is derived by logical inference from GO:0016987 on the same gene, which the accompanying defect requests be repointed to Q9I2J2. It should disappear when that row moves, so it is reported as a consequence to be re-derived rather than as an independent error: the inference is sound and only its input is wrong. Reported at PROBABLE rather than CONFIRMED because it depends on the repoint being accepted, and because femI already carries the equivalent inferred row.

## 2. WRONG_GENE_PRODUCT (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9I2J2 involved_in GO:0033214 siderophore-iron import into cell (IEA, GO_REF:0000108)
- **Field:** Gene product
- **Change:** delete the record asserting UniProtKB:Q9I2J2
- **Likely cause:** OVER_PROPAGATION
- **Recorded in:** `genes/PSEAE/femI/femI-ai-review.yaml`

This row is derived by logical inference from GO:0015344 on the same entry, which the accompanying defect requests be repointed to Q9I2J4. It should disappear when that row moves, so it is reported as a consequence to be re-derived rather than as an independent error: the inference is sound and only its input is wrong. Reported at PROBABLE because it depends on the repoint being accepted. Q9I2J4 already carries GO:0033214 by IBA, so the claim is not lost from the pair. The same pattern applies in mirror image to GO:2000142 on Q9I2J4, which was inferred from the sigma factor activity misplaced there.
