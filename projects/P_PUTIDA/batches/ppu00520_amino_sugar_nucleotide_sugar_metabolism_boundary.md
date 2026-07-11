---
title: "PSEPK ppu00520 Amino sugar and nucleotide sugar metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00520: Amino sugar and nucleotide sugar metabolism

- Module seed: `amino_sugar_nucleotide_sugar_metabolism_boundary`
- Candidate genes from membership table: 25
- Primary bucket genes: 8
- Existing review files: 25
- Curated review files: 25
- Existing Asta research files: 25

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
| [x] | `amgK` | PP_0405 | Q88QT3 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | N-acetylmuramate/N-acetylglucosamine kinase (MurNAc/GlcNAc kinase) (EC 2.7.1.221) (Anomeric sugar kinase) |
| [x] | `murU` | PP_0406 | Q88QT2 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | N-acetylmuramate alpha-1-phosphate uridylyltransferase (MurNAc-1P uridylyltransferase) (MurNAc-alpha-1P uridylyltransfer |
| [x] | `anmK` | PP_0434 | Q88QQ4 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | Anhydro-N-acetylmuramic acid kinase (EC 2.7.1.170) (AnhMurNAc kinase) |
| [x] | `PP_0501` | PP_0501 | Q88QJ1 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | NAD-dependent epimerase/dehydratase family protein |
| [x] | `murA` | PP_0964 | Q88P88 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | UDP-N-acetylglucosamine 1-carboxyvinyltransferase (EC 2.5.1.7) (Enoylpyruvate transferase) (UDP-N-acetylglucosamine enol |
| [x] | `glk` | PP_1011 | Q88P42 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Glucokinase (EC 2.7.1.2) (Glucose kinase) |
| [x] | `algA` | PP_1277 | Q88ND5 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | Alginate biosynthesis protein AlgA [Includes: Mannose-6-phosphate isomerase (EC 5.3.1.8) (Phosphohexomutase) (Phosphoman |
| [x] | `algD` | PP_1288 | Q88NC4 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | GDP-mannose 6-dehydrogenase (GMD) (EC 1.1.1.132) |
| [x] | `mupP` | PP_1764 | Q88M11 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | N-acetylmuramic acid 6-phosphate phosphatase (MurNAc 6-phosphate phosphatase) (MurNAc-6P phosphatase) (EC 3.1.3.105) |
| [x] | `PP_1776` | PP_1776 | Q88M00 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | Alginate biosynthesis protein AlgA (EC 2.7.7.13) (EC 5.3.1.8) |
| [x] | `cpsG` | PP_1777 | Q88LZ9 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | phosphomannomutase (EC 5.4.2.8) |
| [x] | `rfbA` | PP_1783 | Q88LZ3 | kegg:ppu00525 | PRESENT | CURATED | PRESENT | Glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24) |
| [x] | `pgi1` | PP_1808 | Q88LW9 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9) (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (P |
| [x] | `rffE` | PP_1811 | Q88LW6 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | UDP-N-acetylglucosamine 2-epimerase (EC 5.1.3.14) |
| [x] | `murB` | PP_1904 | Q88LM5 | kegg:ppu00550 | PRESENT | CURATED | PRESENT | UDP-N-acetylenolpyruvoylglucosamine reductase (EC 1.3.1.98) (UDP-N-acetylmuramate dehydrogenase) |
| [x] | `nagZ` | PP_2145 | Q88KZ4 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Beta-hexosaminidase (EC 3.2.1.52) (Beta-N-acetylhexosaminidase) (N-acetyl-beta-glucosaminidase) |
| [x] | `udg` | PP_2926 | Q88IS3 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) |
| [x] | `galE` | PP_3129 | Q88I72 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | UDP-glucose 4-epimerase (EC 5.1.3.2) |
| [x] | `pgm` | PP_3578 | Q88GY7 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Phosphoglucomutase (EC 5.4.2.2) |
| [x] | `galU` | PP_3821 | Q88GA4 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) |
| [x] | `pgi2` | PP_4701 | Q88DW7 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9) (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (P |
| [x] | `glmM` | PP_4716 | Q88DV3 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | Phosphoglucosamine mutase (EC 5.4.2.10) |
| [x] | `algC` | PP_5288 | Q88C93 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) |
| [x] | `glmS` | PP_5409 | Q88BX8 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | Glutamine--fructose-6-phosphate aminotransferase [isomerizing] (EC 2.6.1.16) (D-fructose-6-phosphate amidotransferase) ( |
| [x] | `glmU` | PP_5411 | Q88BX6 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | Bifunctional protein GlmU [Includes: UDP-N-acetylglucosamine pyrophosphorylase (EC 2.7.7.23) (N-acetylglucosamine-1-phos |

## Notes

Generated UTC: 2026-07-08T00:10:29.343786+00:00

Completed first-pass curation on 2026-07-07 PDT / 2026-07-08 UTC.

Validation and rendering completed:

- `uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/amino_sugar_nucleotide_sugar_metabolism_boundary.yaml`
- `uv run python -m ai_gene_review.validation.module_validator modules/amino_sugar_nucleotide_sugar_metabolism_boundary.yaml`
- `just validate PSEPK <gene>` for all 25 genes in this batch.
- `just render PSEPK <gene>` for all 25 genes in this batch.

Main curation conclusions:

- Treat KEGG `ppu00520` as a composite amino-sugar/nucleotide-sugar envelope
  precursor boundary map.
- Core UDP-GlcNAc branch: `glmS`, `glmM`, and `glmU`.
- De novo peptidoglycan precursor branch: `murA` and `murB`.
- MurNAc recycling branch: `nagZ`, `mupP`, `anmK`, `amgK`, and `murU`.
- Nucleotide-sugar side branches: `rfbA`, `rffE`, `galE`, `galU`, and `udg`.
- Shared carbohydrate/alginate/GDP-mannose context: `algA`, `algD`, `algC`,
  `cpsG`, `glk`, `pgi1`, `pgi2`, `pgm`, PP_0501, and PP_1776.
- First-pass fixes removed UDP-N-acetylgalactosamine process over-propagation
  from `murA`, removed phosphoglucomutase/phosphomannomutase spillovers from
  `glmM`, narrowed broad catalytic/hydrolase terms for `murA`, `rffE`, `nagZ`,
  and `glmM`, and kept cofactor/localization terms as non-core.
- `rfbA` required accession-based fetch with Q88LZ3 because symbol lookup did
  not resolve the UniProt entry.

- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon amino_sugar_nucleotide_sugar_metabolism_boundary` and
  `just module-pathway-deep-research-falcon amino_sugar_nucleotide_sugar_metabolism_boundary ppu00520 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/amino_sugar_nucleotide_sugar_metabolism_boundary-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__amino_sugar_nucleotide_sugar_metabolism_boundary__ppu00520-deep-research-falcon.md`.
