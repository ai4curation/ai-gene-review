---
title: "PSEPK ppu00999 Biosynthesis of various plant secondary metabolites batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00999: Biosynthesis of various plant secondary metabolites

- Module seed: `plant_secondary_metabolite_biosynthesis_boundary`
- Candidate genes from membership table: 5
- Primary bucket genes: 5
- Existing review files: 5
- Curated review files: 5
- Existing Asta research files: 5

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
| [x] | `aroE__Q88RQ5` | PP_0074 | Q88RQ5 | kegg:ppu00999 | PRESENT | CURATED | PRESENT | Shikimate dehydrogenase (NADP(+)) (SDH) (EC 1.1.1.25) |
| [x] | `bglX` | PP_1403 | Q88N13 | kegg:ppu00999 | PRESENT | CURATED | PRESENT | Periplasmic beta-glucosidase (EC 3.2.1.21) (Beta-D-glucoside glucohydrolase) (Cellobiase) (Gentiobiase) |
| [x] | `aroE__Q88IJ7` | PP_3002 | Q88IJ7 | kegg:ppu00999 | PRESENT | CURATED | PRESENT | Shikimate dehydrogenase (NADP(+)) (SDH) (EC 1.1.1.25) |
| [x] | `PP_3768` | PP_3768 | Q88GF6 | kegg:ppu00999 | PRESENT | CURATED | PRESENT | Shikimate 5-dehydrogenase (EC 1.1.1.-) |
| [x] | `metK` | PP_4967 | Q88D60 | kegg:ppu00999 | PRESENT | CURATED | PRESENT | S-adenosylmethionine synthase (AdoMet synthase) (EC 2.5.1.6) (MAT) (Methionine adenosyltransferase) |

## Notes

Generated UTC: 2026-07-08T18:19:24.832942+00:00

2026-07-11 PDT status sync: `modules/plant_secondary_metabolite_biosynthesis_boundary.yaml` is curated and validates with both module validators. `aroE__Q88RQ5`, `bglX`, `aroE__Q88IJ7`, `PP_3768`, and `metK` all validate cleanly. This is a KEGG boundary/absence bucket: the mapped genes are shikimate/chorismate precursor, beta-glucoside hydrolysis, and SAM methyl-donor side nodes, not a satisfiable plant secondary metabolite biosynthesis route in KT2440.

Real Falcon commands were run:

```bash
just module-deep-research-falcon plant_secondary_metabolite_biosynthesis_boundary
just module-pathway-deep-research-falcon plant_secondary_metabolite_biosynthesis_boundary ppu00999 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/plant_secondary_metabolite_biosynthesis_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__plant_secondary_metabolite_biosynthesis_boundary__ppu00999-deep-research-falcon.md`
