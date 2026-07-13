---
title: "PSEPK ppu01220 Degradation of aromatic compounds batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu01220: Degradation of aromatic compounds

- Module seed: `aromatic_compound_degradation`
- Candidate genes from membership table: 20
- Primary bucket genes: 8
- Existing review files: 20
- Curated review files: 20
- Existing Asta research files: 20

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
| [x] | `ubiX` | PP_0548 | Q88QE6 | kegg:ppu00627 | PRESENT | CURATED | PRESENT | Flavin prenyltransferase UbiX (EC 2.5.1.129) |
| [x] | `pcaB` | PP_1379 | Q88N37 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | 3-carboxy-cis,cis-muconate cycloisomerase (EC 5.5.1.2) |
| [x] | `pcaD` | PP_1380 | Q88N36 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | 3-oxoadipate enol-lactonase 2 (EC 3.1.1.24) |
| [x] | `pcaC` | PP_1381 | Q88N35 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | 4-carboxymuconolactone decarboxylase (EC 4.1.1.44) |
| [x] | `frmA` | PP_1616 | Q88MF5 | kegg:ppu00626 | PRESENT | CURATED | PRESENT | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrog |
| [x] | `PP_1791` | PP_1791 | Q88LY5 | kegg:ppu00621 | PRESENT | CURATED | PRESENT | Aldolase/synthase |
| [x] | `PP_2504` | PP_2504 | Q88JY9 | kegg:ppu00621 | PRESENT | CURATED | PRESENT | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate tautomerase) |
| [x] | `benA` | PP_3161 | Q88I40 | kegg:ppu00622 | PRESENT | CURATED | PRESENT | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10) |
| [x] | `benB` | PP_3162 | Q88I39 | kegg:ppu00622 | PRESENT | CURATED | PRESENT | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10) |
| [x] | `benC` | PP_3163 | Q88I38 | kegg:ppu00622 | PRESENT | CURATED | PRESENT | Benzoate 1,2-dioxygenase electron transfer component (EC 1.14.12.10, EC 1.18.1.3) |
| [x] | `benD` | PP_3164 | Q88I37 | kegg:ppu00622 | PRESENT | CURATED | PRESENT | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (EC 1.3.1.25) |
| [x] | `catA-II` | PP_3166 | Q88I35 | kegg:ppu00361 | PRESENT | CURATED | PRESENT | catechol 1,2-dioxygenase (EC 1.13.11.1) |
| [x] | `pobA` | PP_3537 | Q88H28 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | 4-hydroxybenzoate 3-monooxygenase (EC 1.14.13.2) |
| [x] | `PP_3648` | PP_3648 | Q88GS0 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | Carboxymuconolactone decarboxylase family protein |
| [x] | `catA-I` | PP_3713 | Q88GK8 | kegg:ppu00361 | PRESENT | CURATED | PRESENT | catechol 1,2-dioxygenase (EC 1.13.11.1) |
| [x] | `catC` | PP_3714 | Q88GK7 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | Muconolactone Delta-isomerase (MIase) (EC 5.3.3.4) |
| [x] | `catB` | PP_3715 | Q88GK6 | kegg:ppu00361 | PRESENT | CURATED | PRESENT | Muconate cycloisomerase 1 (EC 5.5.1.1) |
| [x] | `adhP` | PP_3839 | Q88G86 | kegg:ppu00626 | PRESENT | CURATED | PRESENT | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) |
| [x] | `pcaG` | PP_4655 | Q88E13 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | Protocatechuate 3,4-dioxygenase alpha chain (EC 1.13.11.3) |
| [x] | `pcaH` | PP_4656 | Q88E12 | kegg:ppu01220 | PRESENT | CURATED | PRESENT | Protocatechuate 3,4-dioxygenase beta chain (EC 1.13.11.3) |

## Notes

Generated UTC: 2026-07-06T22:02:00.112023+00:00
