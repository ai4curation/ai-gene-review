---
title: "PSEPK ppu04156 Integrated stress response (ISR) signaling pathway batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu04156: Integrated stress response (ISR) signaling pathway

- Module seed: `integrated_stress_response_boundary`
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
| [x] | `groEL` | PP_1361 | Q88N55 | kegg:ppu04156 | PRESENT | CURATED | PRESENT | Chaperonin GroEL (EC 5.6.1.7) (60 kDa chaperonin) (Chaperonin-60) (Cpn60) |
| [x] | `htpG` | PP_4179 | Q88FB9 | kegg:ppu04141 | PRESENT | CURATED | PRESENT | Chaperone protein HtpG (Heat shock protein HtpG) (High temperature protein G) |
| [x] | `dnaK` | PP_4727 | Q88DU2 | kegg:ppu04156 | PRESENT | CURATED | PRESENT | Chaperone protein DnaK (HSP70) (Heat shock 70 kDa protein) (Heat shock protein 70) |
| [x] | `PP_5211` | PP_5211 | Q88CH0 | kegg:ppu04156 | PRESENT | CURATED | PRESENT | glutathione-specific gamma-glutamylcyclotransferase (EC 4.3.2.7) |

## Notes

Generated UTC: 2026-07-09T07:22:16.322815+00:00

Falcon module-level and module+pathway+PSEPK deep research commands were
attempted on 2026-07-09 and both failed at Edison task creation with HTTP 402.
