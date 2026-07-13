---
title: "PSEPK ppu03410 Base excision repair batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03410: Base excision repair

- Module seed: `bacterial_base_excision_repair`
- Candidate genes from membership table: 14
- Primary bucket genes: 11
- Existing review files: 14
- Curated review files: 14
- Existing Asta research files: 14

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
| [x] | `tag` | PP_0062 | Q88RR7 | kegg:ppu03410 | PRESENT | CURATED | PRESENT | DNA-3-methyladenine glycosylase I (EC 3.2.2.20) |
| [x] | `polA` | PP_0123 | Q88RK6 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | DNA polymerase I (EC 2.7.7.7) |
| [x] | `mutY` | PP_0286 | Q88R48 | kegg:ppu03410 | PRESENT | CURATED | PRESENT | Adenine DNA glycosylase (EC 3.2.2.31) |
| [x] | `PP_0705` | PP_0705 | Q88PZ3 | kegg:ppu03410 | PRESENT | CURATED | PRESENT | DNA-3-methyladenine glycosylase II (EC 3.2.2.21) |
| [x] | `nth` | PP_1092 | Q88NW2 | kegg:ppu03410 | PRESENT | CURATED | PRESENT | Endonuclease III (EC 4.2.99.18) (DNA-(apurinic or apyrimidinic site) lyase) |
| [x] | `ung` | PP_1413 | Q88N05 | kegg:ppu03410 | PRESENT | CURATED | PRESENT | Uracil-DNA glycosylase (UDG) (EC 3.2.2.27) |
| [x] | `recJ` | PP_1477 | Q88MU1 | kegg:ppu03410 | PRESENT | CURATED | PRESENT | Single-stranded-DNA-specific exonuclease RecJ |
| [x] | `PP_2707` | PP_2707 | Q88JE2 | kegg:ppu03410 | PRESENT | CURATED | PRESENT | Exodeoxyribonuclease III |
| [x] | `xthA` | PP_2890 | Q88IV9 | kegg:ppu03410 | PRESENT | CURATED | PRESENT | Exodeoxyribonuclease III / apurinic/apyrimidinic endodeoxyribonuclease VI (EC 3.1.11.2) |
| [x] | `ligA` | PP_4274 | Q88F25 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | DNA ligase (EC 6.5.1.2) (Polydeoxyribonucleotide synthase [NAD(+)]) |
| [x] | `PP_4812` | PP_4812 | Q88DL3 | kegg:ppu03410 | PRESENT | CURATED | PRESENT | Putative 3-methyladenine DNA glycosylase (EC 3.2.2.-) |
| [x] | `ligB` | PP_4968 | Q88D59 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | DNA ligase B (EC 6.5.1.2) (Polydeoxyribonucleotide synthase [NAD(+)] B) |
| [x] | `mutM` | PP_5125 | Q88CQ5 | kegg:ppu03410 | PRESENT | CURATED | PRESENT | Formamidopyrimidine-DNA glycosylase (Fapy-DNA glycosylase) (EC 3.2.2.23) (DNA-(apurinic or apyrimidinic site) lyase MutM |
| [x] | `PP_5292` | PP_5292 | Q88C91 | kegg:ppu03410 | PRESENT | CURATED | PRESENT | Catabolite repression control protein |

## Notes

Generated UTC: 2026-07-09T09:04:04.280023+00:00

- 2026-07-09: Completed first-pass ppu03410 curation and module validation. Falcon module-level and module+pathway+taxon jobs were run as real attempts but failed immediately with HTTP 402 Payment Required from Edison task creation; no Falcon artifacts were written.
