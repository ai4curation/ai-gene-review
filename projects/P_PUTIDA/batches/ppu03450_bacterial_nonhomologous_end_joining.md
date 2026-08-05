---
title: "PSEPK ppu03450 Non-homologous end-joining batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03450: Non-homologous end-joining

- Module seed: `bacterial_nonhomologous_end_joining`
- Candidate genes from membership table: 2
- Primary bucket genes: 2
- Existing review files: 0
- Curated review files: 0
- Existing OpenScientist research files: 1

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [ ] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `ku` | PP_3255 | Q88HU8 | kegg:ppu03450 | PRESENT | CURATED | FAILED_TIMEOUT | Non-homologous end joining protein Ku |
| [x] | `ligD` | PP_3260 | Q88HU3 | kegg:ppu03450 | PRESENT | CURATED | FAILED_TIMEOUT | DNA ligase (ATP) (EC 6.5.1.1) (NHEJ DNA polymerase) |

## Notes

Generated UTC: 2026-07-16T17:23:50.275098+00:00

2026-07-16: OpenScientist timed out after 7200s for the module + pathway + PSEPK report, `ku`, and `ligD`; no report files were produced for those runs.
