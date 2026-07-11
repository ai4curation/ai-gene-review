---
title: "PSEPK ppu01053 Biosynthesis of siderophore group nonribosomal peptides batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu01053: Biosynthesis of siderophore group nonribosomal peptides

- Module seed: `siderophore_biosynthesis_boundary`
- Candidate genes from membership table: 2
- Primary bucket genes: 1
- Existing review files: 2
- Curated review files: 2
- Existing Asta research files: 2

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
| [x] | `PP_1183` | PP_1183 | Q88NM4 | kegg:ppu00074 | PRESENT | CURATED | PRESENT | Enterobactin synthase component D (4'-phosphopantetheinyl transferase EntD) (Enterochelin synthase D) |
| [x] | `PP_2170` | PP_2170 | Q88KW9 | kegg:ppu01053 | PRESENT | CURATED | PRESENT | chorismate mutase (EC 5.4.99.5) |

## Notes

Generated UTC: 2026-07-08T18:39:14.956372+00:00

2026-07-11 PDT status sync: `modules/siderophore_biosynthesis_boundary.yaml` is curated and validates with both module validators. `PP_1183` and `PP_2170` both validate cleanly. This shared boundary module covers the ppu01053 carrier-activation and chorismate precursor context together with the ppu00975 precursor/tailoring context and routed pyoverdine NRPS spillovers; ppu01053 alone should not be interpreted as a complete siderophore-group NRPS biosynthesis route.

Real Falcon commands were run:

```bash
just module-deep-research-falcon siderophore_biosynthesis_boundary
just module-pathway-deep-research-falcon siderophore_biosynthesis_boundary ppu01053 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/siderophore_biosynthesis_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__siderophore_biosynthesis_boundary__ppu01053-deep-research-falcon.md`
