---
title: "PSEPK ppu00051 Fructose and mannose metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00051: Fructose and mannose metabolism

- Module seed: `fructose_mannose_metabolism`
- Candidate genes from membership table: 18
- Primary bucket genes: 8
- Existing review files: 18
- Curated review files: 18
- Existing Asta research files: 18

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
| [x] | `fruK` | PP_0794 | Q88PQ4 | kegg:ppu02060 | PRESENT | CURATED | PRESENT | Phosphofructokinase |
| [x] | `fruA` | PP_0795 | Q88PQ3 | kegg:ppu02060 | PRESENT | CURATED | PRESENT | protein-N(pi)-phosphohistidine--D-fructose phosphotransferase (EC 2.7.1.202) |
| [x] | `algA` | PP_1277 | Q88ND5 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | Alginate biosynthesis protein AlgA [Includes: Mannose-6-phosphate isomerase (EC 5.3.1.8) (Phosphohexomutase) (Phosphoman |
| [x] | `algL` | PP_1281 | Q88ND1 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | Alginate lyase (EC 4.2.2.3) (Poly(beta-D-mannuronate) lyase) |
| [x] | `algG` | PP_1283 | Q88NC9 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | Mannuronan C5-epimerase (EC 5.1.3.37) (Poly(beta-D-mannuronate) C5 epimerase) |
| [x] | `alg44` | PP_1286 | Q88NC6 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Alginate biosynthesis protein Alg44 |
| [x] | `alg8` | PP_1287 | Q88NC5 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Glycosyltransferase alg8 (EC 2.4.-.-) |
| [x] | `algD` | PP_1288 | Q88NC4 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | GDP-mannose 6-dehydrogenase (GMD) (EC 1.1.1.132) |
| [x] | `PP_1776` | PP_1776 | Q88M00 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | Alginate biosynthesis protein AlgA (EC 2.7.7.13) (EC 5.3.1.8) |
| [x] | `cpsG` | PP_1777 | Q88LZ9 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | phosphomannomutase (EC 5.4.2.8) |
| [x] | `gmd` | PP_1799 | Q88LX8 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | GDP-mannose 4,6-dehydratase (EC 4.2.1.47) (GDP-D-mannose dehydratase) |
| [x] | `rmd` | PP_1800 | Q88LX7 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | Oxidoreductase Rmd |
| [x] | `PP_2037` | PP_2037 | Q88L98 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | Aldolase |
| [x] | `fucD` | PP_2831 | Q88J18 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | L-fuconate dehydratase (EC 4.2.1.68) |
| [x] | `tpiA` | PP_4715 | Q88DV4 | kegg:ppu00562 | PRESENT | CURATED | PRESENT | Triosephosphate isomerase (TIM) (TPI) (EC 5.3.1.1) (Triose-phosphate isomerase) |
| [x] | `fba` | PP_4960 | Q88D67 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC 4.1.2.13) |
| [x] | `fbp` | PP_5040 | Q88CY9 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class |
| [x] | `algC` | PP_5288 | Q88C93 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) |

## Falcon-Promoted Genes

| Done | Gene | Locus | UniProt | Source bucket | Review | Asta research | Reason |
|---|---|---|---|---|---|---|---|
| [x] | `fruB` | PP_0793 | Q88PQ5 | kegg:ppu02060 | CURATED | PRESENT | Falcon identified FruB as the missing PEP-dependent PTS phosphorelay component required with FruA for fructose import/phosphorylation. |

## Notes

Generated UTC: 2026-07-07T04:25:21.130853+00:00

- Falcon module research: `modules/fructose_mannose_metabolism-deep-research-falcon.md`.
- Falcon PSEPK pathway research: `projects/P_PUTIDA/deep-research/PSEPK__fructose_mannose_metabolism__ppu00051-deep-research-falcon.md`.
- Main lesson: KEGG `ppu00051` conflates fructose PTS entry, alginate precursor synthesis, alginate polymer handling, and the PP_1776/gmd/rmd LPS/O-antigen GDP-D-rhamnose branch.
- Review corrections after Falcon: added `fruB`; removed the false PP_1776 alginate-core interpretation; changed `gmd` and `rmd` to GDP-D-rhamnose/LPS branch context; kept `PP_2037` unresolved as a likely KEGG spillover artifact.
