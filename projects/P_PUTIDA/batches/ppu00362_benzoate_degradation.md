---
title: "PSEPK ppu00362 Benzoate degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00362: Benzoate degradation

- Module seed: `benzoate_degradation`
- Candidate genes from membership table: 40
- Primary bucket genes: 8
- Existing review files: 40
- Curated review files: 40
- Existing Asta research files: 40

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
- [x] Run module + pathway + PSEPK Falcon deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `gcdH` | PP_0158 | Q88RH2 | kegg:ppu00380 | PRESENT | CURATED | PRESENT | glutaryl-CoA dehydrogenase (ETF) (EC 1.3.8.6) |
| [x] | `PP_0582` | PP_0582 | Q88QB2 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Thiolase family protein |
| [x] | `fdx` | PP_0847 | Q88PK3 | kegg:ppu00362 | PRESENT | CURATED | PRESENT | 2Fe-2S ferredoxin |
| [x] | `PP_1218` | PP_1218 | Q88NI9 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | Acyl-CoA thioesterase (EC 3.1.2.-) |
| [x] | `pcaF-I` | PP_1377 | Q88N39 | kegg:ppu00362 | PRESENT | CURATED | PRESENT | Beta-ketoadipyl-CoA thiolase (EC 2.3.1.174) (3-oxoadipyl-CoA thiolase) |
| [x] | `pcaB` | PP_1379 | Q88N37 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | 3-carboxy-cis,cis-muconate cycloisomerase (EC 5.5.1.2) |
| [x] | `pcaD` | PP_1380 | Q88N36 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | 3-oxoadipate enol-lactonase 2 (EC 3.1.1.24) |
| [x] | `pcaC` | PP_1381 | Q88N35 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | 4-carboxymuconolactone decarboxylase (EC 4.1.1.44) |
| [x] | `PP_1791` | PP_1791 | Q88LY5 | kegg:ppu00621 | PRESENT | CURATED | PRESENT | Aldolase/synthase |
| [x] | `PP_1950` | PP_1950 | Q88LI2 | kegg:ppu00362 | PRESENT | CURATED | PRESENT | Cytochrome P450 |
| [x] | `fadA__Q88L84` | PP_2051 | Q88L84 | kegg:ppu00592 | PRESENT | CURATED | PRESENT | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) |
| [x] | `fadB` | PP_2136 | Q88L02 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomeras |
| [x] | `fadA__Q88L01` | PP_2137 | Q88L01 | kegg:ppu00592 | PRESENT | CURATED | PRESENT | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex sub |
| [x] | `PP_2215` | PP_2215 | Q88KS4 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `PP_2217` | PP_2217 | Q88KS2 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | enoyl-CoA hydratase (EC 4.2.1.17) |
| [x] | `PP_2504` | PP_2504 | Q88JY9 | kegg:ppu00621 | PRESENT | CURATED | PRESENT | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate tautomerase) |
| [x] | `galD` | PP_2513 | Q88JY0 | kegg:ppu00362 | PRESENT | CURATED | PRESENT | 4-oxalomesaconate tautomerase (EC 5.3.2.8) (Gallate degradation protein D) |
| [x] | `galC` | PP_2514 | Q88JX9 | kegg:ppu00660 | PRESENT | CURATED | PRESENT | 4-carboxy-4-hydroxy-2-oxoadipic acid aldolase (CHA aldolase) (EC 4.1.3.17) (Gallate degradation protein C) |
| [x] | `galB` | PP_2515 | Q88JX8 | kegg:ppu00362 | PRESENT | CURATED | PRESENT | 4-oxalmesaconate hydratase (OMA hydratase) (EC 4.2.1.83) (Gallate degradation protein B) |
| [x] | `benA` | PP_3161 | Q88I40 | kegg:ppu00622 | PRESENT | CURATED | PRESENT | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10) |
| [x] | `benB` | PP_3162 | Q88I39 | kegg:ppu00622 | PRESENT | CURATED | PRESENT | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10) |
| [x] | `benC` | PP_3163 | Q88I38 | kegg:ppu00622 | PRESENT | CURATED | PRESENT | Benzoate 1,2-dioxygenase electron transfer component (EC 1.14.12.10, EC 1.18.1.3) |
| [x] | `benD` | PP_3164 | Q88I37 | kegg:ppu00622 | PRESENT | CURATED | PRESENT | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (EC 1.3.1.25) |
| [x] | `catA-II` | PP_3166 | Q88I35 | kegg:ppu00361 | PRESENT | CURATED | PRESENT | catechol 1,2-dioxygenase (EC 1.13.11.1) |
| [x] | `paaJ` | PP_3280 | Q88HS3 | kegg:ppu00362 | PRESENT | CURATED | PRESENT | 3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase (EC 2.3.1.-, EC 2.3.1.174) |
| [x] | `paaH` | PP_3282 | Q88HS1 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | 3-hydroxyadipyl-CoA dehydrogenase (EC 1.1.1.35) |
| [x] | `paaF` | PP_3284 | Q88HR9 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) |
| [x] | `PP_3355` | PP_3355 | Q88HK1 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase |
| [x] | `pobA` | PP_3537 | Q88H28 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | 4-hydroxybenzoate 3-monooxygenase (EC 1.14.13.2) |
| [x] | `PP_3648` | PP_3648 | Q88GS0 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | Carboxymuconolactone decarboxylase family protein |
| [x] | `catA-I` | PP_3713 | Q88GK8 | kegg:ppu00361 | PRESENT | CURATED | PRESENT | catechol 1,2-dioxygenase (EC 1.13.11.1) |
| [x] | `catC` | PP_3714 | Q88GK7 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | Muconolactone Delta-isomerase (MIase) (EC 5.3.3.4) |
| [x] | `catB` | PP_3715 | Q88GK6 | kegg:ppu00361 | PRESENT | CURATED | PRESENT | Muconate cycloisomerase 1 (EC 5.5.1.1) |
| [x] | `bktB` | PP_3754 | Q88GH0 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) |
| [x] | `hbd` | PP_3755 | Q88GG9 | kegg:ppu00360 | PRESENT | CURATED | PRESENT | 3-hydroxybutyryl-CoA dehydrogenase (EC 1.1.1.157) |
| [x] | `pcaI` | PP_3951 | Q88FX5 | kegg:ppu00362 | PRESENT | CURATED | PRESENT | 3-oxoadipate CoA-transferase (EC 2.8.3.6) |
| [x] | `pcaJ` | PP_3952 | P0A101 | kegg:ppu00362 | PRESENT | CURATED | PRESENT | 3-oxoadipate CoA-transferase subunit B (EC 2.8.3.6) (Beta-ketoadipate:succinyl-CoA transferase subunit B) |
| [x] | `yqeF` | PP_4636 | Q88E32 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `pcaG` | PP_4655 | Q88E13 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | Protocatechuate 3,4-dioxygenase alpha chain (EC 1.13.11.3) |
| [x] | `pcaH` | PP_4656 | Q88E12 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | Protocatechuate 3,4-dioxygenase beta chain (EC 1.13.11.3) |

## Notes

Generated UTC: 2026-07-06T21:51:27.016919+00:00
