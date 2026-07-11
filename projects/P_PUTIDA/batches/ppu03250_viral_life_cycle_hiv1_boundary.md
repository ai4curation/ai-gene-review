---
title: "PSEPK ppu03250 Viral life cycle - HIV-1 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03250: Viral life cycle - HIV-1

- Module seed: `viral_life_cycle_hiv1_boundary`
- Candidate genes from membership table: 1
- Primary bucket genes: 1
- Existing review files: 1
- Curated review files: 1
- Existing Asta research files: 1

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
| [x] | `ppiA` | PP_4541 | Q88EC5 | kegg:ppu03250 | PRESENT | CURATED | PRESENT | Peptidyl-prolyl cis-trans isomerase (PPIase) (EC 5.2.1.8) |

## Notes

Generated UTC: 2026-07-09T06:36:08.611022+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon viral_life_cycle_hiv1_boundary`
  and `just module-pathway-deep-research-falcon viral_life_cycle_hiv1_boundary ppu03250 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/viral_life_cycle_hiv1_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__viral_life_cycle_hiv1_boundary__ppu03250-deep-research-falcon.md`.
