---
title: "PSEPK ppu04981 Folate transport and metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu04981: Folate transport and metabolism

- Module seed: `folate_transport_metabolism_boundary`
- Candidate genes from membership table: 6
- Primary bucket genes: 5
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
| [x] | `glyA1` | PP_0322 | Q88R12 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Serine hydroxymethyltransferase 1 (SHMT 1) (Serine methylase 1) (EC 2.1.2.1) |
| [x] | `glyA2` | PP_0671 | Q88Q27 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine methylase 2) (EC 2.1.2.1) |
| [x] | `metH` | PP_2375 | Q88KB5 | kegg:ppu04980 | PRESENT | CURATED | PRESENT | Methionine synthase (EC 2.1.1.13) (5-methyltetrahydrofolate--homocysteine methyltransferase) |
| [x] | `folA` | PP_5132 | Q88CP8 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Dihydrofolate reductase (EC 1.5.1.3) |
| [x] | `thyA` | PP_5141 | Q88CN9 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Thymidylate synthase (TS) (TSase) (EC 2.1.1.45) |
| [x] | `fau` | PP_5203 | Q88CH8 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | 5-formyltetrahydrofolate cyclo-ligase (EC 6.3.3.2) |

## Notes

Generated UTC: 2026-07-09T07:47:03.608140+00:00

- 2026-07-09: Added and validated `modules/folate_transport_metabolism_boundary.yaml` as a boundary module. The PSEPK ppu04981 membership contains folate-linked enzymes (`glyA1`, `glyA2`, `metH`, `folA`, `thyA`, `fau`) but no folate transporter; transport remains an absence/boundary note.
- 2026-07-09: Real Falcon module and module+pathway+taxon commands were attempted. Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon output files were produced.
