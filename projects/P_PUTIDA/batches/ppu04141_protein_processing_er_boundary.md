---
title: "PSEPK ppu04141 Protein processing in endoplasmic reticulum batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu04141: Protein processing in endoplasmic reticulum

- Module seed: `protein_processing_er_boundary`
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
| [x] | `PP_3234` | PP_3234 | Q88HW9 | kegg:ppu04141 | PRESENT | CURATED | PRESENT | Heat shock protein, HSP20 family |
| [x] | `PP_3312` | PP_3312 | Q88HP1 | kegg:ppu04141 | PRESENT | CURATED | PRESENT | Heat shock protein |
| [x] | `htpG` | PP_4179 | Q88FB9 | kegg:ppu04141 | PRESENT | CURATED | PRESENT | Chaperone protein HtpG (Heat shock protein HtpG) (High temperature protein G) |

## Notes

Generated UTC: 2026-07-09T07:13:32.844849+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon protein_processing_er_boundary`
  and `just module-pathway-deep-research-falcon protein_processing_er_boundary ppu04141 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/protein_processing_er_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__protein_processing_er_boundary__ppu04141-deep-research-falcon.md`.
