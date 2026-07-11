---
title: "PSEPK ppu03430 Mismatch repair batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03430: Mismatch repair

- Module seed: `bacterial_mismatch_repair`
- Candidate genes from membership table: 19
- Primary bucket genes: 5
- Existing review files: 19
- Curated review files: 19
- Existing Asta research files: 19

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
| [x] | `dnaN` | PP_0011 | P0A120 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | Beta sliding clamp (Beta clamp) (Sliding clamp) (Beta-clamp processivity factor) (DNA polymerase III beta sliding clamp  |
| [x] | `PP_0353` | PP_0353 | Q88QY1 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | Exonuclease |
| [x] | `ssb` | PP_0485 | Q88QK5 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | Single-stranded DNA-binding protein (SSB) |
| [x] | `xseB` | PP_0529 | Q88QG5 | kegg:ppu03430 | PRESENT | CURATED | PRESENT | Exodeoxyribonuclease 7 small subunit (EC 3.1.11.6) (Exodeoxyribonuclease VII small subunit) (Exonuclease VII small subun |
| [x] | `holC` | PP_0979 | Q88P74 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | DNA polymerase III subunit chi (EC 2.7.7.7) |
| [x] | `xseA` | PP_1027 | Q88P26 | kegg:ppu03430 | PRESENT | CURATED | PRESENT | Exodeoxyribonuclease 7 large subunit (EC 3.1.11.6) (Exodeoxyribonuclease VII large subunit) (Exonuclease VII large subun |
| [x] | `sbcB` | PP_1365 | Q88N51 | kegg:ppu03430 | PRESENT | CURATED | PRESENT | Exodeoxyribonuclease I (EC 3.1.11.1) |
| [x] | `recJ` | PP_1477 | Q88MU1 | kegg:ppu03410 | PRESENT | CURATED | PRESENT | Single-stranded-DNA-specific exonuclease RecJ |
| [x] | `dnaEA` | PP_1606 | Q88MG5 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | DNA polymerase III subunit alpha (EC 2.7.7.7) |
| [x] | `mutS` | PP_1626 | Q88ME7 | kegg:ppu03430 | PRESENT | CURATED | PRESENT | DNA mismatch repair protein MutS |
| [x] | `holB` | PP_1966 | Q88LG7 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | DNA polymerase III subunit delta' (EC 2.7.7.7) |
| [x] | `dnaQ` | PP_4141 | Q88FF6 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | DNA polymerase III subunit epsilon (EC 2.7.7.7) |
| [x] | `dnaX` | PP_4269 | Q88F30 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | DNA polymerase III subunit gamma/tau (EC 2.7.7.7) |
| [x] | `ligA` | PP_4274 | Q88F25 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | DNA ligase (EC 6.5.1.2) (Polydeoxyribonucleotide synthase [NAD(+)]) |
| [x] | `PP_4768` | PP_4768 | Q88DQ5 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | Exonuclease |
| [x] | `holA` | PP_4796 | Q88DM9 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | DNA polymerase III subunit delta (EC 2.7.7.7) |
| [x] | `mutL` | PP_4896 | Q88DD1 | kegg:ppu03430 | PRESENT | CURATED | PRESENT | DNA mismatch repair protein MutL |
| [x] | `ligB` | PP_4968 | Q88D59 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | DNA ligase B (EC 6.5.1.2) (Polydeoxyribonucleotide synthase [NAD(+)] B) |
| [x] | `uvrD` | PP_5352 | Q88C31 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | DNA helicase II (EC 5.6.2.4) (DNA 3'-5' helicase II) |

## Notes

Generated UTC: 2026-07-09T08:09:43.903487+00:00

- 2026-07-09: Added and validated `modules/bacterial_mismatch_repair.yaml` as a boundary module. The strict ppu03430 core is MutS/MutL mismatch recognition and coordination; UvrD, exonucleases, SSB, DNA polymerase III/clamp-loader/proofreading subunits, and ligases are shared repair/replication context.
- 2026-07-09: Real Falcon module and module+pathway+taxon commands were attempted. Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon output files were produced.
