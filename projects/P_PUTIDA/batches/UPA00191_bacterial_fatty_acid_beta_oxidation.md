---
title: "PSEPK UPA00191 rubredoxin electron-transfer boundary batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00191: rubredoxin electron-transfer boundary

- Module seed: `bacterial_fatty_acid_beta_oxidation`
- Candidate genes from membership table: 1
- Primary bucket genes: 1
- Existing review files: 1
- Curated review files: 1
- Existing Asta research files: 1

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `rubA` | PP_5315 | Q88C68 | unipathway:UPA00191 | PRESENT | CURATED | PRESENT | Rubredoxin |

## Notes

Generated UTC: 2026-07-10T01:30:39.584759+00:00

- Fetched, Asta-backed, curated, and validated the single UniPathway member:
  `rubA` / PP_5315 / Q88C68.
- Extended `modules/bacterial_fatty_acid_beta_oxidation.yaml` with RubA under
  the existing alkane/rubredoxin electron-transfer boundary node.
- Reused the existing generic Falcon module report:
  `modules/bacterial_fatty_acid_beta_oxidation-deep-research-falcon.md`.
- `rubA` accepts electron transfer activity and alkane catabolic process context,
  while iron ion binding, metal ion binding, and cytoplasm are retained as
  non-core supporting features.
- This UniPathway support bucket should not be interpreted as making RubA a core
  beta-oxidation spiral enzyme; it is upstream hydrocarbon/alkane oxidation
  boundary context.
- Falcon PSEPK module+pathway research was attempted with
  `just module-pathway-deep-research-falcon bacterial_fatty_acid_beta_oxidation UPA00191 PSEPK`
  and failed before report generation with Edison HTTP 402. Expected output
  remains queued:
  `projects/P_PUTIDA/deep-research/PSEPK__bacterial_fatty_acid_beta_oxidation__upa00191-deep-research-falcon.md`.
