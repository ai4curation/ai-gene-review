---
title: "PSEPK ppu03440 Homologous recombination batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03440: Homologous recombination

- Module seed: `bacterial_homologous_recombination`
- Candidate genes from membership table: 24
- Primary bucket genes: 12
- Existing review files: 24
- Curated review files: 24
- Existing Asta research files: 24

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research. Attempted 2026-07-09; Edison/Falcon returned HTTP 402 Payment Required before task creation, so no output file was produced.
- [x] Run module + pathway + PSEPK Falcon deep research. Attempted 2026-07-09; Edison/Falcon returned HTTP 402 Payment Required before task creation, so no output file was produced.
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
| [x] | `recF` | PP_0012 | Q88RW7 | kegg:ppu03440 | PRESENT | CURATED | PRESENT | DNA replication and repair protein RecF |
| [x] | `polA` | PP_0123 | Q88RK6 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | DNA polymerase I (EC 2.7.7.7) |
| [x] | `PP_0353` | PP_0353 | Q88QY1 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | Exonuclease |
| [x] | `ssb` | PP_0485 | Q88QK5 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | Single-stranded DNA-binding protein (SSB) |
| [x] | `holC` | PP_0979 | Q88P74 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | DNA polymerase III subunit chi (EC 2.7.7.7) |
| [x] | `ruvC` | PP_1215 | Q88NJ2 | kegg:ppu03440 | PRESENT | CURATED | PRESENT | Crossover junction endodeoxyribonuclease RuvC (EC 3.1.21.10) (Holliday junction nuclease RuvC) (Holliday junction resolv |
| [x] | `ruvA` | PP_1216 | Q88NJ1 | kegg:ppu03440 | PRESENT | CURATED | PRESENT | Holliday junction branch migration complex subunit RuvA |
| [x] | `ruvB` | PP_1217 | Q88NJ0 | kegg:ppu03440 | PRESENT | CURATED | PRESENT | Holliday junction branch migration complex subunit RuvB (EC 3.6.4.-) |
| [x] | `recO` | PP_1435 | Q88MY3 | kegg:ppu03440 | PRESENT | CURATED | PRESENT | DNA repair protein RecO (Recombination protein O) |
| [x] | `recJ` | PP_1477 | Q88MU1 | kegg:ppu03410 | PRESENT | CURATED | PRESENT | Single-stranded-DNA-specific exonuclease RecJ |
| [x] | `dnaEA` | PP_1606 | Q88MG5 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | DNA polymerase III subunit alpha (EC 2.7.7.7) |
| [x] | `recA` | PP_1629 | Q88ME4 | kegg:ppu03440 | PRESENT | CURATED | PRESENT | Protein RecA (Recombinase A) |
| [x] | `holB` | PP_1966 | Q88LG7 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | DNA polymerase III subunit delta' (EC 2.7.7.7) |
| [x] | `dnaQ` | PP_4141 | Q88FF6 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | DNA polymerase III subunit epsilon (EC 2.7.7.7) |
| [x] | `recR` | PP_4267 | Q88F32 | kegg:ppu03440 | PRESENT | CURATED | PRESENT | Recombination protein RecR |
| [x] | `dnaX` | PP_4269 | Q88F30 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | DNA polymerase III subunit gamma/tau (EC 2.7.7.7) |
| [x] | `recD` | PP_4672 | Q88DZ6 | kegg:ppu03440 | PRESENT | CURATED | PRESENT | RecBCD enzyme subunit RecD (EC 5.6.2.3) (DNA 5'-3' helicase subunit RecD) (Exonuclease V subunit RecD) (ExoV subunit Rec |
| [x] | `recB` | PP_4673 | Q88DZ5 | kegg:ppu03440 | PRESENT | CURATED | PRESENT | RecBCD enzyme subunit RecB (EC 3.1.11.5) (EC 5.6.2.4) (DNA 3'-5' helicase subunit RecB) (Exonuclease V subunit RecB) (Ex |
| [x] | `recC` | PP_4674 | Q88DZ4 | kegg:ppu03440 | PRESENT | CURATED | PRESENT | RecBCD enzyme subunit RecC (Exonuclease V subunit RecC) (ExoV subunit RecC) (Helicase/nuclease RecBCD subunit RecC) |
| [x] | `PP_4768` | PP_4768 | Q88DQ5 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | Exonuclease |
| [x] | `holA` | PP_4796 | Q88DM9 | kegg:ppu03030 | PRESENT | CURATED | PRESENT | DNA polymerase III subunit delta (EC 2.7.7.7) |
| [x] | `priA` | PP_5088 | Q88CU2 | kegg:ppu03440 | PRESENT | CURATED | PRESENT | Replication restart protein PriA (ATP-dependent DNA helicase PriA) (EC 5.6.2.4) (DNA 3'-5' helicase PriA) |
| [x] | `recG` | PP_5310 | Q88C73 | kegg:ppu03440 | PRESENT | CURATED | PRESENT | ATP-dependent DNA helicase RecG (EC 5.6.2.4) |

## Notes

Generated UTC: 2026-07-09T09:37:36.009013+00:00

- 2026-07-09: Completed first-pass ppu03440 curation and module validation. Falcon module-level and module+pathway+taxon jobs were run as real attempts but failed immediately with HTTP 402 Payment Required from Edison task creation; no Falcon artifacts were written.
