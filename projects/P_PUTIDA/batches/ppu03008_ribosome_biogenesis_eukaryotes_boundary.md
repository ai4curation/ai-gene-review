---
title: "PSEPK ppu03008 Ribosome biogenesis in eukaryotes batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03008: Ribosome biogenesis in eukaryotes

- Module seed: `ribosome_biogenesis_eukaryotes_boundary`
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
| [x] | `rnc` | PP_1433 | Q88MY5 | kegg:ppu03008 | PRESENT | CURATED | PRESENT | Ribonuclease 3 (EC 3.1.26.3) (Ribonuclease III) (RNase III) |
| [x] | `PP_2912` | PP_2912 | Q88IT7 | kegg:ppu03008 | PRESENT | CURATED | PRESENT | non-specific serine/threonine protein kinase (EC 2.7.11.1) |
| [x] | `orn` | PP_4902 | Q88DC5 | kegg:ppu03008 | PRESENT | CURATED | PRESENT | Oligoribonuclease (EC 3.1.15.-) |

## Notes

Generated UTC: 2026-07-09T07:02:55.930102+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon ribosome_biogenesis_eukaryotes_boundary`
  and `just module-pathway-deep-research-falcon ribosome_biogenesis_eukaryotes_boundary ppu03008 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/ribosome_biogenesis_eukaryotes_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__ribosome_biogenesis_eukaryotes_boundary__ppu03008-deep-research-falcon.md`.
