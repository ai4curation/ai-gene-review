---
title: "PSEPK ppu00030 Pentose phosphate pathway batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00030: Pentose phosphate pathway

- Module seed: `pentose_phosphate_pathway`
- Candidate genes from membership table: 36
- Primary bucket genes: 19
- Existing review files after this pass: 23
- Curated review files after this pass: 23
- OpenScientist pathway/taxon research: present
- OpenScientist module research: present
- OpenScientist selected-gene research: present

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected core genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes.
- [x] Curate each selected first-pass gene review.
- [x] Validate module and selected gene reviews.
- [ ] Render module and project pages.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Curated Scope

Core PPP module:

- Oxidative branch: `zwfA`, `zwfB`, `zwf`/zwfC, `pgl`, `gntZ`.
- Non-oxidative branch: `rpiA`, `rpe`, `tktA`, `tal`.
- PRPP synthesis (`prs`, `PP_2744`) is treated as a nucleotide-biosynthesis exit, not a required PPP part.
- ED genes (`edd`, `eda`), peripheral glucose/gluconate oxidation (`gcd`, `gnuK`, `kguK`, `PP_3382`-`PP_3384`, `adhB`, `ghrB`, `PP_1661`), lower glycolysis/gluconeogenesis (`fba`, `fbp`, `PP_3443`), redox/phosphonate/ribose-salvage genes (`trxB`, `ptxD`, `phnN`, `ttuD`, `rbsK`), and nucleotide-sugar genes (`pgm`, `algC`, `cpsG`) are spillovers from the broad KEGG ppu00030 bucket.

OpenScientist pathway/taxon review concludes that the canonical PPP is satisfiable in KT2440 and that the dominant curation issue is bucket boundary cleanup, not hole filling.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `rpe` | PP_0415 | Q88QS3 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | Ribulose-phosphate 3-epimerase (EC 5.1.3.1) |
| [ ] | `prs` | PP_0722 | Q88PX6 | kegg:ppu00030 | PRESENT | CURATED | MISSING | Ribose-phosphate pyrophosphokinase (RPPK) (EC 2.7.6.1) (5-phospho-D-ribosyl alpha-1-diphosphate synthase) (Phosphoribosy |
| [ ] | `trxB` | PP_0786 | Q88PR2 | kegg:ppu00030 | MISSING | MISSING | MISSING | Thioredoxin reductase (EC 1.8.1.9) |
| [ ] | `edd` | PP_1010 | Q88P43 | kegg:ppu00030 | PRESENT | CURATED | MISSING | Phosphogluconate dehydratase (EC 4.2.1.12) |
| [x] | `zwfA` | PP_1022 | Q88P31 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) |
| [x] | `pgl` | PP_1023 | Q88P30 | kegg:ppu00030 | PRESENT | CURATED | PRESENT | 6-phosphogluconolactonase (6PGL) (EC 3.1.1.31) |
| [ ] | `eda` | PP_1024 | Q88P29 | kegg:ppu00030 | PRESENT | CURATED | MISSING | 2-dehydro-3-deoxy-phosphogluconate aldolase (EC 4.1.2.14) |
| [ ] | `ghrB` | PP_1261 | Q88NF1 | kegg:ppu00030 | MISSING | MISSING | MISSING | 2-ketoaldonate reductase / hydroxypyruvate/glyoxylate reductase (EC 1.1.1.215, EC 1.1.1.79, EC 1.1.1.81) |
| [ ] | `gcd` | PP_1444 | Q88MX4 | kegg:ppu00030 | PRESENT | CURATED | MISSING | Quinoprotein glucose dehydrogenase (EC 1.1.5.2) |
| [ ] | `PP_1661` | PP_1661 | Q88MB3 | kegg:ppu00030 | MISSING | MISSING | MISSING | Dehydrogenase subunit |
| [x] | `cpsG` | PP_1777 | Q88LZ9 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | phosphomannomutase (EC 5.4.2.8) |
| [x] | `pgi1` | PP_1808 | Q88LW9 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9) (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (P |
| [ ] | `ppgL` | PP_2021 | Q88LB4 | kegg:ppu00030 | MISSING | MISSING | MISSING | L-alpha-hydroxyglutaric acid gamma-lactonase |
| [x] | `tal` | PP_2168 | Q88KX1 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Transaldolase (EC 2.2.1.2) |
| [ ] | `rbsK` | PP_2458 | Q88K34 | kegg:ppu00030 | MISSING | MISSING | MISSING | Ribokinase (RK) (EC 2.7.1.15) |
| [ ] | `PP_2744` | PP_2744 | Q88JA5 | kegg:ppu00030 | MISSING | MISSING | MISSING | ribose-phosphate diphosphokinase (EC 2.7.6.1) |
| [ ] | `ptxD` | PP_3376 | Q88HI1 | kegg:ppu00480 | MISSING | MISSING | MISSING | Phosphonate dehydrogenase (EC 1.20.1.1) |
| [ ] | `kguK` | PP_3378 | Q88HH9 | kegg:ppu00030 | MISSING | MISSING | MISSING | 2-ketogluconokinase (EC 2.7.1.13) |
| [x] | `PP_3382` | PP_3382 | Q88HH6 | kegg:ppu00030 | PRESENT | CURATED | PRESENT | Gluconate 2-dehydrogenase cytochrome c subunit (EC 1.1.99.3) |
| [ ] | `PP_3383` | PP_3383 | Q88HH5 | kegg:ppu00030 | MISSING | MISSING | MISSING | Gluconate 2-dehydrogenase flavoprotein subunit (EC 1.1.99.3) |
| [ ] | `PP_3384` | PP_3384 | Q88HH4 | kegg:ppu00030 | MISSING | MISSING | MISSING | Gluconate 2-dehydrogenase gamma subunit (EC 1.1.99.3) |
| [ ] | `gnuK` | PP_3416 | Q88HE4 | kegg:ppu00030 | MISSING | MISSING | MISSING | Gluconokinase (EC 2.7.1.12) |
| [x] | `PP_3443` | PP_3443 | Q88HB7 | kegg:ppu00030 | PRESENT | CURATED | PRESENT | Glyceraldehyde-3-phosphate dehydrogenase (EC 1.2.1.59) |
| [x] | `pgm` | PP_3578 | Q88GY7 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Phosphoglucomutase (EC 5.4.2.2) |
| [x] | `adhB` | PP_3623 | Q88GU4 | kegg:ppu00030 | PRESENT | CURATED | PRESENT | Alcohol dehydrogenase cytochrome c subunit |
| [x] | `zwfB` | PP_4042 | Q88FP7 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) |
| [x] | `gntZ` | PP_4043 | Q88FP6 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | 6-phosphogluconate dehydrogenase, decarboxylating (EC 1.1.1.44) |
| [ ] | `ttuD` | PP_4300 | Q88F00 | kegg:ppu00561 | MISSING | MISSING | MISSING | Hydroxypyruvate reductase (EC 1.1.1.81) |
| [ ] | `phnN` | PP_4469 | Q88EJ3 | kegg:ppu00030 | MISSING | MISSING | MISSING | Ribose 1,5-bisphosphate phosphokinase PhnN (EC 2.7.4.23) (Ribose 1,5-bisphosphokinase) |
| [x] | `pgi2` | PP_4701 | Q88DW7 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9) (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (P |
| [x] | `fba` | PP_4960 | Q88D67 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC 4.1.2.13) |
| [x] | `tktA` | PP_4965 | Q88D62 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Transketolase (EC 2.2.1.1) |
| [x] | `fbp` | PP_5040 | Q88CY9 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class |
| [x] | `rpiA` | PP_5150 | Q88CN0 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Ribose-5-phosphate isomerase A (EC 5.3.1.6) (Phosphoriboisomerase A) (PRI) |
| [x] | `algC` | PP_5288 | Q88C93 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) |
| [x] | `zwf` | PP_5351 | Q88C32 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) |

## Notes

Generated UTC: 2026-07-15T14:52:59.970771+00:00

## 2026-07-15 curation notes

- Added `modules/pentose_phosphate_pathway.yaml` as a combined oxidative/non-oxidative PPP module with eight reaction leaves and no module-level MF terms.
- Attached module-level OpenScientist research supporting the two-branch PPP boundary and exclusion of ED/peripheral spillovers from the reusable module core.
- Fetched and curated first-pass reviews for `zwfA`, `zwfB`, `gntZ`, `rpe`, `rpiA`, `tktA`, and `tal`.
- Reused existing curated `zwf` and `pgl` reviews, then attached completed OpenScientist research to keep this batch consistent.
- Initial OpenScientist gene-level jobs for `gntZ`, `rpe`, `rpiA`, and `tktA` hit the provider's default 3600 s timeout; they completed after restart with provider parameter `timeout=7200`.
- The pathway/taxon OpenScientist report supports treating KEGG ppu00030 as over-broad: ED, peripheral glucose oxidation, PRPP synthesis, and gluconeogenic/reductive spillovers should not be counted as PPP holes.
