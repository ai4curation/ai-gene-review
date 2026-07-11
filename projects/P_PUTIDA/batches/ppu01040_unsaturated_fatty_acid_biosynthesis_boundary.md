---
title: "PSEPK ppu01040 Biosynthesis of unsaturated fatty acids batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu01040: Biosynthesis of unsaturated fatty acids

- Module seed: `unsaturated_fatty_acid_biosynthesis_boundary`
- Candidate genes from membership table: 3
- Primary bucket genes: 3
- Existing review files: 3
- Curated review files: 3
- Existing Asta research files: 3

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
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
| [x] | `tesA` | PP_2318 | Q88KH2 | kegg:ppu01040 | PRESENT | CURATED | PRESENT | Acyl-CoA thioesterase I/protease I/lysophospholipase L1 (EC 3.1.1.5, EC 3.1.2.14, EC 3.1.2.2) |
| [x] | `tesB` | PP_4762 | Q88DR1 | kegg:ppu01040 | PRESENT | CURATED | PRESENT | Acyl-CoA thioesterase 2 (EC 3.1.2.20) (Thioesterase II) |
| [x] | `PP_5331` | PP_5331 | Q88C52 | kegg:ppu01040 | PRESENT | CURATED | PRESENT | Long-chain acyl-CoA thioester hydrolase |

## Notes

Generated UTC: 2026-07-08T18:31:17.072586+00:00

2026-07-11 PDT status sync: `modules/unsaturated_fatty_acid_biosynthesis_boundary.yaml` is curated and validates with both module validators. `tesA`, `tesB`, and `PP_5331` all validate cleanly. This is a thioesterase/acyl-pool boundary bucket: KEGG ppu01040 contains lipid ester or acyl-thioester hydrolases, while the canonical bacterial unsaturated-acyl-ACP branch is handled in the broader `fatty_acid_biosynthesis` module through FabA/FabB context.

Real Falcon commands were run:

```bash
just module-deep-research-falcon unsaturated_fatty_acid_biosynthesis_boundary
just module-pathway-deep-research-falcon unsaturated_fatty_acid_biosynthesis_boundary ppu01040 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/unsaturated_fatty_acid_biosynthesis_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__unsaturated_fatty_acid_biosynthesis_boundary__ppu01040-deep-research-falcon.md`
