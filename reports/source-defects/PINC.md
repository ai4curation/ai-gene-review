# Source-record defects for PINC

1 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_GENE_PRODUCT (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:P52566 located_in GO:0031410 cytoplasmic vesicle (TAS, PMID:9113980)
- **Field:** DB_Object_ID
- **Change:** UniProtKB:P52566 → UniProtKB:Q99819 (ARHGDIG, Rho GDP-dissociation inhibitor 3 (RhoGDIgamma))
- **Likely cause:** OTHER
- **Recorded in:** `genes/human/ARHGDIB/ARHGDIB-ai-review.yaml`

TAS annotation (assigned by PINC) of ARHGDIB (P52566) to cytoplasmic vesicle citing PMID:9113980. That paper reports perinuclear vesicular localization for the newly cloned RhoGDIgamma (ARHGDIG, Q99819) and states that GFP-tagged GDI/D4 (ARHGDIB) shows only a diffuse cytoplasmic distribution. The row should be moved to ARHGDIG or deleted for ARHGDIB.

> A similar construction with GFP tagged to the amino terminus of GDI/D4 or RhoGDI showed only a diffuse distribution in the cytoplasm without any of the perinuclear aggregates seen with RhoGDIγ (figure not shown).
> — PMID:9113980
