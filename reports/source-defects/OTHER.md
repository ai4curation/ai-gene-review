# Source-record defects for OTHER

1 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_REFERENCE (CONFIRMED, NOT_REPORTED)

- **Record:** InterPro:IPR047151
- **Subject:** UniProtKB:Q9BQ52
- **Field:** metadata.literature.PUB00102035.PMID
- **Change:** check PMID:2159360 (alternatives in the explanation)
- **Recorded in:** `genes/human/ELAC2/ELAC2-ai-review.yaml`

InterPro IPR047151 uses description citation PUB00102035 for mitochondrial tRNA processing, but that literal literature entry identifies PMID:2159360 and a cerebral-blood-flow/NMDA-receptor study unrelated to ELAC2 or tRNase Z. Check the intended citation in the InterPro record; no replacement identifier is established here. The target family match and GO:0042781 mapping agree with independent human enzymatic evidence and are retained.
