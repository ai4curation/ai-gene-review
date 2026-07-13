---
title: "PSEPK ppu00633 Nitrotoluene degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00633: Nitrotoluene degradation

- Module seed: `nitrotoluene_degradation_boundary`
- Candidate genes from membership table: 3
- Primary bucket genes: 3
- Existing review files: 3
- Curated review files: 3
- Existing Asta research files: 3

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted on 2026-07-11; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted on 2026-07-11; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `nfnB` | PP_2432 | Q88K59 | kegg:ppu00633 | PRESENT | CURATED | PRESENT | 6,7-dihydropteridine reductase (EC 1.5.1.34) |
| [x] | `PP_2486` | PP_2486 | Q88K07 | kegg:ppu00633 | PRESENT | CURATED | PRESENT | NADH-dependent flavin oxidoreductase, Oye family |
| [x] | `nemA` | PP_3173 | Q88I29 | kegg:ppu00633 | PRESENT | CURATED | PRESENT | N-ethylmaleimide reductase, FMN-linked (EC 1.-.-.-) |

## Notes

Generated UTC: 2026-07-08T13:15:17.032819+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon nitrotoluene_degradation_boundary`
  and `just module-pathway-deep-research-falcon nitrotoluene_degradation_boundary ppu00633 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/nitrotoluene_degradation_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__nitrotoluene_degradation_boundary__ppu00633-deep-research-falcon.md`.
