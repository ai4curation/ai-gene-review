---
title: "PSEPK ppu04148 Efferocytosis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu04148: Efferocytosis

- Module seed: `efferocytosis_boundary`
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
| [x] | `speC` | PP_0864 | Q88PI6 | kegg:ppu04148 | PRESENT | CURATED | PRESENT | ornithine decarboxylase (EC 4.1.1.17) |
| [x] | `petA` | PP_1317 | Q88N95 | kegg:ppu04148 | PRESENT | CURATED | PRESENT | Ubiquinol-cytochrome c reductase iron-sulfur subunit (EC 7.1.1.8) |

## Notes

Generated UTC: 2026-07-09T06:41:54.909303+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon efferocytosis_boundary`
  and `just module-pathway-deep-research-falcon efferocytosis_boundary ppu04148 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/efferocytosis_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__efferocytosis_boundary__ppu04148-deep-research-falcon.md`.
