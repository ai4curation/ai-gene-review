# Source-record defects for GO_CENTRAL

1 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** PANTHER:PTN002795969
- **Subject:** UniProtKB:Q99527
- **Field:** GO_ID
- **Change:** GO:0030284 → GO:0038054 (G protein-coupled estrogen receptor activity)
- **Likely cause:** OTHER
- **Recorded in:** `genes/human/GPER1/GPER1-ai-review.yaml`

PAINT IBD on PTN002795969 (GPER subfamily, PTHR24226) asserts GO:0030284 nuclear estrogen receptor activity, a DNA-binding transcription factor activity. All descendants are GPER seven-transmembrane GPCRs without DNA-binding domains; the conserved activity (human and Atlantic croaker GPER bind estradiol and activate Gs) is GO:0038054 G protein-coupled estrogen receptor activity. Please re-place the IBD with GO:0038054.

> croaker and human GPER have very similar estrogen binding characteristics, typical of estrogen membrane receptors, and activate the same estrogen signaling pathways via stimulatory G proteins (Gs) resulting in increased cAMP production
> — PMID:19931550
