---
title: "PSEPK ppu00361 Chlorocyclohexane and chlorobenzene degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00361: Chlorocyclohexane and chlorobenzene degradation

- Module seed: `chlorocyclohexane_chlorobenzene_degradation_boundary`
- Candidate genes from membership table: 3
- Primary bucket genes: 3
- Existing review files: 3
- Curated review files: 3
- Existing Asta research files: 3

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted 2026-07-09 PDT / 2026-07-10 UTC; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted 2026-07-09 PDT / 2026-07-10 UTC; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `catA-II` | PP_3166 | Q88I35 | kegg:ppu00361 | PRESENT | CURATED | PRESENT | catechol 1,2-dioxygenase (EC 1.13.11.1) |
| [x] | `catA-I` | PP_3713 | Q88GK8 | kegg:ppu00361 | PRESENT | CURATED | PRESENT | catechol 1,2-dioxygenase (EC 1.13.11.1) |
| [x] | `catB` | PP_3715 | Q88GK6 | kegg:ppu00361 | PRESENT | CURATED | PRESENT | Muconate cycloisomerase 1 (EC 5.5.1.1) |

## Notes

Generated UTC: 2026-07-07T21:39:21.523932+00:00

2026-07-09 PDT / 2026-07-10 UTC: Revalidated `catA-II`, `catA`, and `catB`;
all passed. Revalidated
`modules/chlorocyclohexane_chlorobenzene_degradation_boundary.yaml` with both
LinkML and the module validator; both passed. The real generic module Falcon
command and the real taxon-aware module/pathway Falcon command both failed
before report generation with Edison HTTP 402, leaving the Falcon report paths
queued for rerun.
