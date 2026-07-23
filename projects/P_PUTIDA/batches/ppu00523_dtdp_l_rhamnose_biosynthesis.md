---
title: "PSEPK ppu00523 Polyketide sugar unit biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00523: Polyketide sugar unit biosynthesis

- Module seed: `dtdp_l_rhamnose_biosynthesis`
- Candidate genes from membership table: 6
- Primary bucket genes: 4
- Existing review files: 0
- Curated review files: 0
- Existing OpenScientist research files: 5

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `rmlC` | PP_0265 | Q88R69 | kegg:ppu00523 | PRESENT | CURATED | FAILED_TIMEOUT | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13) (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) |
| [x] | `PP_0500` | PP_0500 | Q88QJ2 | kegg:ppu00523 | PRESENT | CURATED | PRESENT | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) |
| [x] | `rfbC` | PP_1782 | Q88LZ4 | kegg:ppu00523 | PRESENT | CURATED | PRESENT | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13) (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) |
| [x] | `rfbA` | PP_1783 | Q88LZ3 | kegg:ppu00525 | PRESENT | CURATED | FAILED_TIMEOUT | Glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24) |
| [x] | `rfbD` | PP_1784 | Q88LZ2 | kegg:ppu00523 | PRESENT | CURATED | FAILED_TIMEOUT | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) |
| [x] | `rffG` | PP_1785 | Q88LZ1 | kegg:ppu00525 | PRESENT | CURATED | PRESENT | dTDP-glucose 4,6-dehydratase (EC 4.2.1.46) |

## Notes

Generated UTC: 2026-07-16T17:37:22.097822+00:00

2026-07-16: OpenScientist timed out after 7200s for `rfbA`, `rmlC`, and `rfbD`; no report files were produced for those runs.
