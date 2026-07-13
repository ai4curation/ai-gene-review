---
title: "PSEPK ppu00450 Selenocompound metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00450: Selenocompound metabolism

- Module seed: `selenocompound_metabolism_boundary`
- Candidate genes from membership table: 12
- Primary bucket genes: 9
- Existing review files: 12
- Curated review files: 12
- Existing Asta research files: 12

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
| [x] | `selA` | PP_0493 | Q88QJ8 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | L-seryl-tRNA(Sec) selenium transferase (EC 2.9.1.1) (Selenocysteine synthase) (Sec synthase) (Selenocysteinyl-tRNA(Sec)  |
| [x] | `metB` | PP_0659 | Q88Q39 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | Cystathionine gamma-synthase |
| [x] | `selD` | PP_0823 | P59392 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | Selenide, water dikinase (EC 2.7.9.3) (Selenium donor protein) (Selenophosphate synthase) |
| [x] | `metG` | PP_1097 | Q88NV7 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | Methionine--tRNA ligase (EC 6.1.1.10) (Methionyl-tRNA synthetase) (MetRS) |
| [x] | `cysD` | PP_1303 | Q88NA9 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Sulfate adenylyltransferase subunit 2 (EC 2.7.7.4) (ATP-sulfurylase small subunit) (Sulfate adenylate transferase) (SAT) |
| [x] | `cysNC` | PP_1304 | Q88NA8 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Sulfate adenylyltransferase subunit 1 (EC 2.7.7.4) (ATP-sulfurylase large subunit) (Sulfate adenylate transferase) (SAT) |
| [x] | `mdeA` | PP_1308 | Q88NA4 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | L-methionine gamma-lyase (EC 4.4.1.11) |
| [x] | `metH` | PP_2375 | Q88KB5 | kegg:ppu04980 | PRESENT | CURATED | PRESENT | Methionine synthase (EC 2.1.1.13) (5-methyltetrahydrofolate--homocysteine methyltransferase) |
| [x] | `metE` | PP_2698 | Q88JF1 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | 5-methyltetrahydropteroyltriglutamate-homocysteine methyltransferase |
| [x] | `PP_4348` | PP_4348 | Q88EV4 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | Cystathionine beta-lyase |
| [x] | `PP_4594` | PP_4594 | Q88E72 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | Cystathionine gamma-synthase |
| [x] | `PP_4637` | PP_4637 | Q88E31 | kegg:ppu00450 | PRESENT | CURATED | PRESENT | 5-methyltetrahydropteroyltriglutamate-homocysteine S-methyltransferase family protein |

## Notes

Generated UTC: 2026-07-07T22:35:24.364967+00:00

Completed first-pass curation of `ppu00450` as a selenocompound boundary
module. The selenium-specific spine is `selD` selenide, water dikinase /
selenophosphate synthase followed by `selA` L-seryl-tRNA(Sec) selenium
transferase, which together support bacterial selenocysteinyl-tRNA(Sec)
formation and selenocysteine incorporation. `metG` was curated as canonical
methionyl-tRNA synthetase and kept as KEGG-map boundary context, not as a
selenium-specific enzyme.

The remaining members are methionine, cysteine, transsulfuration,
sulfate-assimilation, or candidate sulfur-amino-acid side nodes (`metB`,
`cysD`, `cysNC`, `mdeA`, `metH`, `metE`, `PP_4348`, `PP_4594`, `PP_4637`).
All 12 gene reviews and the module validate. Remaining validation warnings are
non-blocking older side-node warnings about uncited Asta retrieval files,
unreflected authored core-process terms, one PP_4348 location warning, and the
known lack of a defined core function for candidate `PP_4637`.

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon selenocompound_metabolism_boundary`
  and `just module-pathway-deep-research-falcon selenocompound_metabolism_boundary ppu00450 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/selenocompound_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__selenocompound_metabolism_boundary__ppu00450-deep-research-falcon.md`.
