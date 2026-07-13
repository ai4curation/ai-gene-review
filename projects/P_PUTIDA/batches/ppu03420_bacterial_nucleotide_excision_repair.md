---
title: "PSEPK ppu03420 Nucleotide excision repair batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03420: Nucleotide excision repair

- Module seed: `bacterial_nucleotide_excision_repair`
- Candidate genes from membership table: 10
- Primary bucket genes: 10
- Existing review files: 10
- Curated review files: 10
- Existing Asta research files: 10

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
| [x] | `polA` | PP_0123 | Q88RK6 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | DNA polymerase I (EC 2.7.7.7) |
| [x] | `uvrA` | PP_0483 | Q88QK7 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | UvrABC system protein A (UvrA protein) (Excinuclease ABC subunit A) |
| [x] | `uvrB` | PP_1974 | Q88LF9 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | UvrABC system protein B (Protein UvrB) (Excinuclease ABC subunit B) |
| [x] | `mfd` | PP_2148 | Q88KZ1 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | Transcription-repair-coupling factor (TRCF) (EC 3.6.4.-) |
| [x] | `PP_2839` | PP_2839 | Q88J10 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | Helicase ATP-binding domain-containing protein |
| [x] | `PP_3087` | PP_3087 | Q88IB2 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | UvrABC system protein A (Excinuclease ABC subunit A) |
| [x] | `uvrC` | PP_4098 | Q88FJ7 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | UvrABC system protein C (Protein UvrC) (Excinuclease ABC subunit C) |
| [x] | `ligA` | PP_4274 | Q88F25 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | DNA ligase (EC 6.5.1.2) (Polydeoxyribonucleotide synthase [NAD(+)]) |
| [x] | `ligB` | PP_4968 | Q88D59 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | DNA ligase B (EC 6.5.1.2) (Polydeoxyribonucleotide synthase [NAD(+)] B) |
| [x] | `uvrD` | PP_5352 | Q88C31 | kegg:ppu03420 | PRESENT | CURATED | PRESENT | DNA helicase II (EC 5.6.2.4) (DNA 3'-5' helicase II) |

## Notes

Generated UTC: 2026-07-09T08:25:59.517448+00:00

- 2026-07-09: Created and validated `modules/bacterial_nucleotide_excision_repair.yaml`.
- 2026-07-09: Attempted `just module-deep-research-falcon bacterial_nucleotide_excision_repair`; Edison returned HTTP 402 Payment Required at task creation, so no Falcon module output was written.
- 2026-07-09: Attempted `just module-pathway-deep-research-falcon bacterial_nucleotide_excision_repair ppu03420 PSEPK`; Edison returned HTTP 402 Payment Required at task creation, so no Falcon pathway+taxon output was written.
