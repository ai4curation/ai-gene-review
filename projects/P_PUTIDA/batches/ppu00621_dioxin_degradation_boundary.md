---
title: "PSEPK ppu00621 Dioxin degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00621: Dioxin degradation

- Module seed: `dioxin_degradation_boundary`
- Candidate genes from membership table: 2
- Primary bucket genes: 2
- Existing review files: 2
- Curated review files: 2
- Existing Asta research files: 2

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted 2026-07-11 PDT; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted 2026-07-11 PDT; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `PP_1791` | PP_1791 | Q88LY5 | kegg:ppu00621 | PRESENT | CURATED | PRESENT | Aldolase/synthase |
| [x] | `PP_2504` | PP_2504 | Q88JY9 | kegg:ppu00621 | PRESENT | CURATED | PRESENT | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate tautomerase) |

## Notes

Generated UTC: 2026-07-08T12:05:12.285275+00:00

2026-07-11 PDT Falcon status: real Falcon commands were run for both the
generic module report and the PSEPK module+pathway report:

```bash
just module-deep-research-falcon dioxin_degradation_boundary
just module-pathway-deep-research-falcon dioxin_degradation_boundary ppu00621 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon
reports were written. Expected output paths remain:

- `modules/dioxin_degradation_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__dioxin_degradation_boundary__ppu00621-deep-research-falcon.md`
