---
title: "PSEPK UPA00392 UniPathway UPA00392 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00392: UniPathway UPA00392

- Module seed: `queuosine_biosynthesis_boundary`
- Candidate genes from membership table: 4
- Primary bucket genes: 3
- Existing review files: 4
- Curated review files: 4
- Existing Asta research files: 4

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted on 2026-07-09; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted on 2026-07-09; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `queA` | PP_0832 | Q88PL8 | unipathway:UPA00392 | PRESENT | CURATED | PRESENT | S-adenosylmethionine:tRNA ribosyltransferase-isomerase (EC 2.4.99.17) (Queuosine biosynthesis protein QueA) |
| [x] | `tgt` | PP_0833 | Q88PL7 | unipathway:UPA00392 | PRESENT | CURATED | PRESENT | Queuine tRNA-ribosyltransferase (EC 2.4.2.29) (Guanine insertion enzyme) (tRNA-guanine transglycosylase) |
| [x] | `queF` | PP_2160 | Q88KX9 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | NADPH-dependent 7-cyano-7-deazaguanine reductase (EC 1.7.1.13) (7-cyano-7-carbaguanine reductase) (NADPH-dependent nitri |
| [x] | `queG` | PP_4900 | Q88DC7 | unipathway:UPA00392 | PRESENT | CURATED | PRESENT | Epoxyqueuosine reductase (EC 1.17.99.6) (Queuosine biosynthesis protein QueG) |

## Notes

Generated UTC: 2026-07-09T22:59:58.336373+00:00

- 2026-07-09: Created and validated `modules/queuosine_biosynthesis_boundary.yaml`.
- 2026-07-09: Attempted `just module-deep-research-falcon queuosine_biosynthesis_boundary`; Edison returned HTTP 402 Payment Required at task creation, so no Falcon module output was written.
- 2026-07-09: Attempted `just module-pathway-deep-research-falcon queuosine_biosynthesis_boundary UPA00392 PSEPK`; Edison returned HTTP 402 Payment Required at task creation, so no Falcon pathway+taxon output was written.
