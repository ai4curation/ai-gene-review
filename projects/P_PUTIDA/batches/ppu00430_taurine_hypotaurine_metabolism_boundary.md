---
title: "PSEPK ppu00430 Taurine and hypotaurine metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00430: Taurine and hypotaurine metabolism

- Module seed: `taurine_hypotaurine_metabolism_boundary`
- Candidate genes from membership table: 5
- Primary bucket genes: 5
- Existing review files: 5
- Curated review files: 5
- Existing Asta research files: 5

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
| [x] | `tauD` | PP_0230 | Q88RA3 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | Alpha-ketoglutarate-dependent taurine dioxygenase (EC 1.14.11.17) |
| [x] | `pta` | PP_0774 | Q88PS4 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | Phosphate acetyltransferase (EC 2.3.1.8) (Phosphotransacetylase) |
| [x] | `gdhB` | PP_2080 | Q88L55 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | NAD-specific glutamate dehydrogenase (EC 1.4.1.2) |
| [x] | `PP_3535` | PP_3535 | Q88H30 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | Glutathione hydrolase proenzyme (EC 2.3.2.2) (EC 3.4.19.13) [Cleaved into: Glutathione hydrolase large chain; Glutathion |
| [x] | `ggt` | PP_4659 | Q88E09 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | Glutathione hydrolase proenzyme (EC 2.3.2.2) (EC 3.4.19.13) [Cleaved into: Glutathione hydrolase large chain; Glutathion |

## Notes

Generated UTC: 2026-07-07T22:12:49.227353+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon taurine_hypotaurine_metabolism_boundary`
  and `just module-pathway-deep-research-falcon taurine_hypotaurine_metabolism_boundary ppu00430 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/taurine_hypotaurine_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__taurine_hypotaurine_metabolism_boundary__ppu00430-deep-research-falcon.md`.
