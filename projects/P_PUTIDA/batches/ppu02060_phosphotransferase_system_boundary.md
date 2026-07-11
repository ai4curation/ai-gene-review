---
title: "PSEPK ppu02060 Phosphotransferase system (PTS) batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu02060: Phosphotransferase system (PTS)

- Module seed: `phosphotransferase_system_boundary`
- Candidate genes from membership table: 6
- Primary bucket genes: 6
- Existing review files: 6
- Curated review files: 6
- Existing Asta research files: 6

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
| [x] | `fruB` | PP_0793 | Q88PQ5 | kegg:ppu02060 | PRESENT | CURATED | PRESENT | phosphoenolpyruvate--protein phosphotransferase (EC 2.7.3.9) |
| [x] | `fruK` | PP_0794 | Q88PQ4 | kegg:ppu02060 | PRESENT | CURATED | PRESENT | Phosphofructokinase |
| [x] | `fruA` | PP_0795 | Q88PQ3 | kegg:ppu02060 | PRESENT | CURATED | PRESENT | protein-N(pi)-phosphohistidine--D-fructose phosphotransferase (EC 2.7.1.202) |
| [x] | `ptsH` | PP_0948 | Q88PA2 | kegg:ppu02060 | PRESENT | CURATED | PRESENT | Phosphocarrier protein HPr (EC 2.7.11.-) |
| [x] | `ptsN` | PP_0950 | Q88PA0 | kegg:ppu02060 | PRESENT | CURATED | PRESENT | Phosphotransferase system enzyme IIA, regulation of potassium transport |
| [x] | `ptsP` | PP_5145 | Q88CN5 | kegg:ppu02060 | PRESENT | CURATED | PRESENT | phosphoenolpyruvate--protein phosphotransferase (EC 2.7.3.9) |

## Notes

Generated UTC: 2026-07-09T07:36:20.168976+00:00

Falcon module-level and module+pathway+PSEPK deep research commands were
attempted on 2026-07-09 and both failed at Edison task creation with HTTP 402.
