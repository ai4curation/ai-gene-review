---
title: "PSEPK ppu00500 Starch and sucrose metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00500: Starch and sucrose metabolism

- Module seed: `starch_sucrose_metabolism_boundary`
- Candidate genes from membership table: 18
- Primary bucket genes: 12
- Existing review files: 18
- Curated review files: 18
- Existing Asta research files: 18

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
| [x] | `glk` | PP_1011 | Q88P42 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Glucokinase (EC 2.7.1.2) (Glucose kinase) |
| [x] | `bglX` | PP_1403 | Q88N13 | kegg:ppu00999 | PRESENT | CURATED | PRESENT | Periplasmic beta-glucosidase (EC 3.2.1.21) (Beta-D-glucoside glucohydrolase) (Cellobiase) (Gentiobiase) |
| [x] | `cpsG` | PP_1777 | Q88LZ9 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | phosphomannomutase (EC 5.4.2.8) |
| [x] | `pgi1` | PP_1808 | Q88LW9 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Glucose-6-phosphate isomerase 1 (GPI 1) (EC 5.3.1.9) (Phosphoglucose isomerase 1) (PGI 1) (Phosphohexose isomerase 1) (P |
| [x] | `bcsA` | PP_2635 | Q88JL4 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Cellulose synthase catalytic subunit [UDP-forming] (EC 2.4.1.12) |
| [x] | `pgm` | PP_3578 | Q88GY7 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Phosphoglucomutase (EC 5.4.2.2) |
| [x] | `galU` | PP_3821 | Q88GA4 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) |
| [x] | `glgA` | PP_4050 | Q88FN9 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Glycogen synthase (EC 2.4.1.21) (Starch [bacterial glycogen] synthase) |
| [x] | `treZ` | PP_4051 | Q88FN8 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Malto-oligosyltrehalose trehalohydrolase (MTHase) (EC 3.2.1.141) (4-alpha-D-((1->4)-alpha-D-glucano)trehalose trehalohyd |
| [x] | `malQ` | PP_4052 | Q88FN7 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | 4-alpha-glucanotransferase (EC 2.4.1.25) (Amylomaltase) (Disproportionating enzyme) |
| [x] | `treY` | PP_4053 | Q88FN6 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Maltooligosyl trehalose synthase (EC 5.4.99.15) |
| [x] | `glgX` | PP_4055 | Q88FN4 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Glycogen debranching enzyme (EC 3.2.1.33) |
| [x] | `glgB` | PP_4058 | Q88FN1 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | 1,4-alpha-glucan branching enzyme GlgB (EC 2.4.1.18) (1,4-alpha-D-glucan:1,4-alpha-D-glucan 6-glucosyl-transferase) (Alp |
| [x] | `treSB` | PP_4059 | Q88FN0 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Maltokinase (EC 2.7.1.175) (EC 5.4.99.16) (Maltose alpha-D-glucosyltransferase) (Maltose-1-phosphate synthase) |
| [x] | `glgE` | PP_4060 | Q88FM9 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Alpha-1,4-glucan:maltose-1-phosphate maltosyltransferase (GMPMT) (EC 2.4.99.16) ((1->4)-alpha-D-glucan:maltose-1-phospha |
| [x] | `pgi2` | PP_4701 | Q88DW7 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Glucose-6-phosphate isomerase 2 (GPI 2) (EC 5.3.1.9) (Phosphoglucose isomerase 2) (PGI 2) (Phosphohexose isomerase 2) (P |
| [x] | `glgP` | PP_5041 | Q88CY8 | kegg:ppu00500 | PRESENT | CURATED | PRESENT | Alpha-1,4 glucan phosphorylase (EC 2.4.1.1) |
| [x] | `algC` | PP_5288 | Q88C93 | kegg:ppu00052 | PRESENT | CURATED | PRESENT | Phosphomannomutase/phosphoglucomutase (PMM / PGM) (EC 5.4.2.2) (EC 5.4.2.8) |

## Notes

Generated UTC: 2026-07-07T23:53:57.715883+00:00

Completed first-pass curation on 2026-07-07 PDT / 2026-07-07 UTC.

Validation and rendering completed:

- `uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/starch_sucrose_metabolism_boundary.yaml`
- `uv run python -m ai_gene_review.validation.module_validator modules/starch_sucrose_metabolism_boundary.yaml`
- `just validate PSEPK <gene>` for all 18 genes in this batch.
- `just render PSEPK <gene>` for all 18 genes in this batch.

Main curation conclusions:

- Treat KEGG `ppu00500` as a bacterial glycogen/alpha-glucan boundary map, not
  a strict plant starch/sucrose pathway.
- Core glycogen and alpha-glucan nodes: `glgA`, `glgB`, `glgX`, `glgP`,
  `malQ`, `treY`, `treZ`, `treSB`, and `glgE`.
- Boundary/context nodes: `bcsA` cellulose synthesis; `glk`, `pgi1`, `pgi2`,
  `pgm`, `galU`, `algC`, and `cpsG` shared sugar-phosphate or UDP-glucose
  precursor chemistry; `bglX` beta-glucosidase/cellobiose context.
- First-pass fixes include narrowing `glgA` to ADP-glucose glycogen synthase
  chemistry, removing GH13 hydrolase over-propagation from `glgB` and `glgE`,
  and keeping broad carbohydrate, localization, and cofactor terms as non-core.

- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon starch_sucrose_metabolism_boundary` and
  `just module-pathway-deep-research-falcon starch_sucrose_metabolism_boundary ppu00500 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/starch_sucrose_metabolism_boundary-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__starch_sucrose_metabolism_boundary__ppu00500-deep-research-falcon.md`.
