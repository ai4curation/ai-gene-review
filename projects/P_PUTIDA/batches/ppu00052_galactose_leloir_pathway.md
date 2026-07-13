---
title: "PSEPK ppu00052 Galactose metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00052: Galactose metabolism

- Module seed: `galactose_leloir_pathway`
- Candidate genes from membership table: 8
- Primary bucket genes: 7
- Existing review files: 8
- Curated review files: 8
- Existing Asta research files: 8

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
- [x] Run module + pathway + PSEPK Falcon deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `PP_0501` | PP_0501 | Q88QJ1 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | NAD-dependent epimerase/dehydratase family protein |
| [x] | `glk` | PP_1011 | Q88P42 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Glucokinase (EC 2.7.1.2) (Glucose kinase) |
| [x] | `PP_1165` | PP_1165 | Q88NP2 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Aldose 1-epimerase |
| [x] | `cpsG` | PP_1777 | Q88LZ9 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | phosphomannomutase (EC 5.4.2.8) |
| [x] | `galE` | PP_3129 | Q88I72 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | UDP-glucose 4-epimerase (EC 5.1.3.2) |
| [x] | `pgm` | PP_3578 | Q88GY7 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Phosphoglucomutase (EC 5.4.2.2) |
| [x] | `galU` | PP_3821 | Q88GA4 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) |
| [x] | `algC` | PP_5288 | Q88C93 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) |

## Notes

Generated UTC: 2026-07-07T02:00:57.751076+00:00
