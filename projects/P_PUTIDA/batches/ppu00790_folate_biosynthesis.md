---
title: "PSEPK ppu00790 Folate biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00790: Folate biosynthesis

- Module seed: `folate_biosynthesis`
- Candidate genes from membership table: 32
- Primary bucket genes: 19
- Existing review files: 32
- Curated review files: 32
- Existing Asta research files: 32

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted 2026-07-07; Edison returned HTTP 402 Payment Required before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted 2026-07-07; Edison returned HTTP 402 Payment Required before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `folB` | PP_0392 | Q88QU4 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | 7,8-dihydroneopterin aldolase (EC 4.1.2.25) |
| [x] | `PP_0393` | PP_0393 | Q88QU3 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | 2-amino-4-hydroxy-6-hydroxymethyldihydropteridine diphosphokinase (EC 2.7.6.3) |
| [x] | `ribAB-I` | PP_0516 | Q88QH7 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) |
| [x] | `ribA` | PP_0522 | Q88QH1 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | GTP cyclohydrolase-2 (EC 3.5.4.25) (GTP cyclohydrolase II) |
| [x] | `queE` | PP_1225 | Q88NI4 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | 7-carboxy-7-deazaguanine synthase (CDG synthase) (EC 4.3.99.3) (Queuosine biosynthesis protein QueE) |
| [x] | `queC` | PP_1226 | Q88NI3 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | 7-cyano-7-deazaguanine synthase (EC 6.3.4.20) (7-cyano-7-carbaguanine synthase) (PreQ(0) synthase) (Queuosine biosynthes |
| [x] | `moaC` | PP_1292 | Q88NC0 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Cyclic pyranopterin monophosphate synthase (EC 4.6.1.17) (Molybdenum cofactor biosynthesis protein C) |
| [x] | `moaE` | PP_1294 | Q88NB8 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Molybdopterin synthase catalytic subunit (EC 2.8.1.12) (MPT synthase subunit 2) (Molybdenum cofactor biosynthesis protei |
| [x] | `folE1` | PP_1823 | Q88LV4 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | GTP cyclohydrolase 1 1 (EC 3.5.4.16) (GTP cyclohydrolase I 1) (GTP-CH-I 1) |
| [x] | `pabC` | PP_1917 | Q88LL3 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | Aminodeoxychorismate lyase (EC 4.1.3.38) |
| [x] | `PP_1969` | PP_1969 | Q88LG4 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Molybdenum cofactor biosynthesis protein A |
| [x] | `folC` | PP_1997 | Q88LD8 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | Dihydrofolate synthase/folylpolyglutamate synthase (EC 6.3.2.12) (EC 6.3.2.17) (Folylpoly-gamma-glutamate synthetase-dih |
| [x] | `moaB-I` | PP_2122 | Q88L15 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Molybdenum cofactor biosynthesis protein B |
| [x] | `moeA` | PP_2123 | Q88L14 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | Molybdopterin molybdenumtransferase (EC 2.10.1.1) |
| [x] | `queF` | PP_2160 | Q88KX9 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | NADPH-dependent 7-cyano-7-deazaguanine reductase (EC 1.7.1.13) (7-cyano-7-carbaguanine reductase) (NADPH-dependent nitri |
| [x] | `pabB` | PP_2329 | Q88KG1 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | aminodeoxychorismate synthase (EC 2.6.1.85) |
| [x] | `queD` | PP_2341 | Q88KE9 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | 6-carboxy-5,6,7,8-tetrahydropterin synthase (EC 4.-.-.-) |
| [x] | `PP_2482` | PP_2482 | Q88K11 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Molybdenum cofactor biosynthesis protein A |
| [x] | `PP_2483` | PP_2483 | Q88K10 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | MobA-like NTP transferase domain-containing protein |
| [x] | `folE2__Q88JY1` | PP_2512 | Q88JY1 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | GTP cyclohydrolase 1 2 (EC 3.5.4.16) (GTP cyclohydrolase I 2) (GTP-CH-I 2) |
| [x] | `folE2__Q88HM9` | PP_3324 | Q88HM9 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | GTP cyclohydrolase FolE2 (EC 3.5.4.16) |
| [x] | `mobA` | PP_3457 | Q88HA3 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | Molybdenum cofactor guanylyltransferase (MoCo guanylyltransferase) (EC 2.7.7.77) (GTP:molybdopterin guanylyltransferase) |
| [x] | `ribAB-II` | PP_3813 | Q88GB1 | kegg:ppu00740 | PRESENT | CURATED | PRESENT | 3,4-dihydroxy-2-butanone 4-phosphate synthase (DHBP synthase) (EC 4.1.99.12) |
| [x] | `PP_4230` | PP_4230 | Q88F68 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | MobA-like NTP transferase domain-containing protein |
| [x] | `phhA` | PP_4490 | Q88EH3 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | Phenylalanine-4-hydroxylase (EC 1.14.16.1) (Phe-4-monooxygenase) |
| [x] | `phhB` | PP_4491 | Q88EH2 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | Pterin-4-alpha-carbinolamine dehydratase (PHS) (EC 4.2.1.96) (4-alpha-hydroxy-tetrahydropterin dehydratase) (Pterin carb |
| [x] | `moaA` | PP_4597 | Q88E69 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | GTP 3',8-cyclase (EC 4.1.99.22) (Molybdenum cofactor biosynthesis protein A) |
| [x] | `moaB-II` | PP_4600 | Q88E67 | kegg:ppu04122 | PRESENT | CURATED | PRESENT | Molybdenum cofactor biosynthesis protein B |
| [x] | `folM` | PP_4632 | Q88E36 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Dihydromonapterin reductase (EC 1.5.1.3) (EC 1.5.1.50) (Dihydrofolate reductase) |
| [x] | `folK` | PP_4698 | Q88DX0 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | 2-amino-4-hydroxy-6-hydroxymethyldihydropteridine pyrophosphokinase (EC 2.7.6.3) (6-hydroxymethyl-7,8-dihydropterin pyro |
| [x] | `folP` | PP_4717 | Q88DV2 | kegg:ppu00790 | PRESENT | CURATED | PRESENT | Dihydropteroate synthase (DHPS) (EC 2.5.1.15) (Dihydropteroate pyrophosphorylase) |
| [x] | `folA` | PP_5132 | Q88CP8 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Dihydrofolate reductase (EC 1.5.1.3) |

## Notes

Generated UTC: 2026-07-07T14:01:56.441232+00:00

## Workflow Notes

- Created and validated `modules/folate_biosynthesis.yaml`.
- Fetched all 32 candidate review folders, including duplicate-symbol `folE2__Q88JY1` by accession with `--alias`.
- Ran Asta for all 32 candidates; Asta is retained as fast retrieval/identity context for this first pass.
- Curated all 32 review YAMLs to remove `PENDING` actions, then rendered all 32 gene pages.
- Validation passed for all 32 gene reviews and the module. Remaining warnings are expected first-pass notices: Asta files are not cited as hypothesis evidence, some core-function context terms are not mirrored as accepted existing annotations, and `PP_2483`/`PP_4230` intentionally have no core function pending substrate evidence.

## Curation Notes

- Strict folate coverage is represented by FolE/FolE2 GTP cyclohydrolase I paralogs, FolB, HPPK candidates `folK` and `PP_0393`, pABA branch genes `pabB` and `pabC`, `folP`, `folC`, and `folA`.
- Queuosine, molybdenum-cofactor, BH4/phenylalanine-hydroxylase, riboflavin, and MobA-like proteins are retained as ppu00790 boundary nodes rather than strict tetrahydrofolate steps.
- `pabB` removes the stray electronic tryptophan-biosynthesis transfer and keeps the pABA/folate aminodeoxychorismate synthase role.
- `PP_2483` and `PP_4230` remain unresolved MobA-like NTP transferase-domain proteins with only non-core broad nucleotidyltransferase annotations.
