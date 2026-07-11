---
title: "PSEPK ppu00400 Phenylalanine, tyrosine and tryptophan biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00400: Phenylalanine, tyrosine and tryptophan biosynthesis

- Module seed: `tryptophan_biosynthesis`
- Candidate genes from membership table: 28
- Primary bucket genes: 20
- Existing review files: 28
- Curated review files: 28
- Existing Asta research files: 28

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
- [x] Run module + pathway + PSEPK Falcon deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway: [PR #1874](https://github.com/ai4curation/ai-gene-review/pull/1874).
- [x] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `aroE__Q88RQ5` | PP_0074 | Q88RQ5 | kegg:ppu00999 | PRESENT | CURATED | PRESENT | Shikimate dehydrogenase (NADP(+)) (SDH) (EC 1.1.1.25) |
| [x] | `trpA` | PP_0082 | Q88RP7 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Tryptophan synthase alpha chain (EC 4.2.1.20) |
| [x] | `trpB` | PP_0083 | Q88RP6 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Tryptophan synthase beta chain (EC 4.2.1.20) |
| [x] | `trpE` | PP_0417 | Q88QS1 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Anthranilate synthase component 1 (EC 4.1.3.27) |
| [x] | `pabA` | PP_0420 | Q88QR8 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Aminodeoxychorismate synthase / para-aminobenzoate synthase multi-enzyme complex (EC 2.6.1.85) |
| [x] | `trpD` | PP_0421 | Q88QR7 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Anthranilate phosphoribosyltransferase (EC 2.4.2.18) |
| [x] | `trpC` | PP_0422 | Q88QR6 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Indole-3-glycerol phosphate synthase (IGPS) (EC 4.1.1.48) |
| [x] | `aroQ1` | PP_0560 | Q88QD4 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | 3-dehydroquinate dehydratase 1 (3-dehydroquinase 1) (EC 4.2.1.10) (Type II DHQase 1) |
| [x] | `hisC` | PP_0967 | Q88P86 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | Histidinol-phosphate aminotransferase (EC 2.6.1.9) (Imidazole acetol-phosphate transaminase) |
| [x] | `pheA` | PP_1769 | Q88M06 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Bifunctional chorismate mutase/prephenate dehydratase (EC 4.2.1.51) (EC 5.4.99.5) (Chorismate mutase-prephenate dehydrat |
| [x] | `aroA` | PP_1770 | Q88M05 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | 3-phosphoshikimate 1-carboxyvinyltransferase (EC 2.5.1.19) (5-enolpyruvylshikimate-3-phosphate synthase) (EPSP synthase) |
| [x] | `aroC` | PP_1830 | Q88LU7 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Chorismate synthase (CS) (EC 4.2.3.5) (5-enolpyruvylshikimate-3-phosphate phospholyase) |
| [x] | `aroH` | PP_1866 | Q88LR3 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Phospho-2-dehydro-3-deoxyheptonate aldolase (EC 2.5.1.54) |
| [x] | `tyrB` | PP_1972 | Q88LG1 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | Aminotransferase (EC 2.6.1.-) |
| [x] | `trpF` | PP_1995 | Q88LE0 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | N-(5'-phosphoribosyl)anthranilate isomerase (PRAI) (EC 5.3.1.24) |
| [x] | `aroF-I` | PP_2324 | Q88KG6 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Phospho-2-dehydro-3-deoxyheptonate aldolase (EC 2.5.1.54) |
| [x] | `aroE__Q88K85` | PP_2406 | Q88K85 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Shikimate dehydrogenase (NADP(+)) (SDH) (EC 1.1.1.25) |
| [x] | `aroQ2` | PP_2407 | Q88K84 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | 3-dehydroquinate dehydratase 2 (3-dehydroquinase 2) (EC 4.2.1.10) (Type II DHQase 2) |
| [x] | `quiC1` | PP_2554 | Q88JU3 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | 3-dehydroshikimate dehydratase (DSD) (EC 4.2.1.118) |
| [x] | `aroE__Q88IJ7` | PP_3002 | Q88IJ7 | kegg:ppu00999 | PRESENT | CURATED | PRESENT | Shikimate dehydrogenase (NADP(+)) (SDH) (EC 1.1.1.25) |
| [x] | `aroQ-III` | PP_3003 | Q88IJ6 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | 3-dehydroquinate dehydratase (3-dehydroquinase) (EC 4.2.1.10) (Type II DHQase) |
| [x] | `aroF-II` | PP_3080 | Q88IB9 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Phospho-2-dehydro-3-deoxyheptonate aldolase (EC 2.5.1.54) |
| [x] | `quiA` | PP_3569 | Q88GZ6 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Quinate dehydrogenase (Quinone) (EC 1.1.5.8) |
| [x] | `amaC` | PP_3590 | Q88GX7 | kegg:ppu00401 | PRESENT | CURATED | PRESENT | Aminotransferase (EC 2.6.1.-) |
| [x] | `PP_3768` | PP_3768 | Q88GF6 | kegg:ppu00999 | PRESENT | CURATED | PRESENT | Shikimate 5-dehydrogenase (EC 1.1.1.-) |
| [x] | `phhA` | PP_4490 | Q88EH3 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | Phenylalanine-4-hydroxylase (EC 1.14.16.1) (Phe-4-monooxygenase) |
| [x] | `aroB` | PP_5078 | Q88CV2 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | 3-dehydroquinate synthase (DHQS) (EC 4.2.3.4) |
| [x] | `aroK` | PP_5079 | Q88CV1 | kegg:ppu00400 | PRESENT | CURATED | PRESENT | Shikimate kinase (SK) (EC 2.7.1.71) |

## Notes

Generated UTC: 2026-07-06T03:48:55.229299+00:00

2026-07-11 PDT status sync: species-neutral module curation, generic Falcon
module research, PSEPK module+pathway Falcon research, and PR shepherding are
complete. PR #1874 has merged.
