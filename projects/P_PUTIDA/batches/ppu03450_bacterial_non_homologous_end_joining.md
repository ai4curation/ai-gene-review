---
title: "PSEPK ppu03450 Non-homologous end-joining batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03450: Non-homologous end-joining

- Module seed: `bacterial_non_homologous_end_joining`
- Candidate genes from membership table: 2
- Primary bucket genes: 2
- Existing review files: 2
- Curated review files: 2
- Existing Asta research files: 2

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
| [x] | `ku` | PP_3255 | Q88HU8 | kegg:ppu03450 | PRESENT | CURATED | PRESENT | Non-homologous end joining protein Ku |
| [x] | `ligD` | PP_3260 | Q88HU3 | kegg:ppu03450 | PRESENT | CURATED | PRESENT | DNA ligase (ATP) (EC 6.5.1.1) (NHEJ DNA polymerase) |

## Notes

Generated UTC: 2026-07-09T06:08:12.116977+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon bacterial_non_homologous_end_joining`
  and `just module-pathway-deep-research-falcon bacterial_non_homologous_end_joining ppu03450 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/bacterial_non_homologous_end_joining-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__bacterial_non_homologous_end_joining__ppu03450-deep-research-falcon.md`.
