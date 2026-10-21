# Source-record defects for OTHER

2 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** InterPro:IPR047151
- **Subject:** UniProtKB:Q9BQ52
- **Field:** metadata.literature.PUB00102035.PMID
- **Change:** check PMID:2159360 (alternatives in the explanation)
- **Recorded in:** `genes/human/ELAC2/ELAC2-ai-review.yaml`

InterPro IPR047151 uses description citation PUB00102035 for mitochondrial tRNA processing, but that literal literature entry identifies PMID:2159360 and a cerebral-blood-flow/NMDA-receptor study unrelated to ELAC2 or tRNase Z. Check the intended citation in the InterPro record; no replacement identifier is established here. The target family match and GO:0042781 mapping agree with independent human enzymatic evidence and are retained.

## 2. WRONG_TERM (PROBABLE, NOT_REPORTED)

- **Record:** UniProtKB:Q9GZR5 involved_in GO:0009584 detection of visible light (IEA, GO_REF:0000108)
- **Field:** GO_ID
- **Change:** check GO:0009584 (alternatives in the explanation)
- **Likely cause:** UNKNOWN
- **Recorded in:** `genes/human/ELOVL4/ELOVL4-ai-review.yaml`

Assigned-by resource: GOC (GO_REF:0000108 logical inference). The GO_REF:0000108 assertion is supported by GO:0008020. Recheck this logical consequence if the upstream photoreceptor molecular-function assertion is removed; this query concerns visible-light detection, not retinal lipid requirements.
