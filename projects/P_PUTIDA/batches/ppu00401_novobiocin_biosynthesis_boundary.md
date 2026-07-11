---
title: "PSEPK ppu00401 Novobiocin biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00401: Novobiocin biosynthesis

- Module seed: `novobiocin_biosynthesis_boundary`
- Candidate genes from membership table: 4
- Primary bucket genes: 4
- Existing review files: 4
- Curated review files: 4
- Existing Asta research files: 4

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
| [x] | `hisC` | PP_0967 | Q88P86 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) |
| [x] | `aroA` | PP_1770 | Q88M05 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | 3-phosphoshikimate 1-carboxyvinyltransferase (EC 2.5.1.19) (5-enolpyruvylshikimate-3-phosphate synthase) (EPSP synthase) |
| [x] | `tyrB` | PP_1972 | Q88LG1 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | Aminotransferase (EC 2.6.1.-) |
| [x] | `amaC` | PP_3590 | Q88GX7 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | Aminotransferase (EC 2.6.1.-) |

## Notes

Generated UTC: 2026-07-07T21:59:13.645777+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon novobiocin_biosynthesis_boundary`
  and `just module-pathway-deep-research-falcon novobiocin_biosynthesis_boundary ppu00401 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/novobiocin_biosynthesis_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__novobiocin_biosynthesis_boundary__ppu00401-deep-research-falcon.md`.
