---
title: "PSEPK ppu00523 Polyketide sugar unit biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00523: Polyketide sugar unit biosynthesis

- Module seed: `polyketide_sugar_unit_biosynthesis_boundary`
- Candidate genes from membership table: 6
- Primary bucket genes: 4
- Existing review files: 6
- Curated review files: 6
- Existing Asta research files: 6

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
| [x] | `rmlC` | PP_0265 | Q88R69 | kegg:ppu00523 | PRESENT | CURATED | PRESENT | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13) (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) |
| [x] | `PP_0500` | PP_0500 | Q88QJ2 | kegg:ppu00523 | PRESENT | CURATED | PRESENT | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) |
| [x] | `rfbC` | PP_1782 | Q88LZ4 | kegg:ppu00523 | PRESENT | CURATED | PRESENT | dTDP-4-dehydrorhamnose 3,5-epimerase (EC 5.1.3.13) (Thymidine diphospho-4-keto-rhamnose 3,5-epimerase) |
| [x] | `rfbA` | PP_1783 | Q88LZ3 | kegg:ppu00525 | PRESENT | CURATED | PRESENT | Glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24) |
| [x] | `rfbD` | PP_1784 | Q88LZ2 | kegg:ppu00523 | PRESENT | CURATED | PRESENT | dTDP-4-dehydrorhamnose reductase (EC 1.1.1.133) |
| [x] | `rffG` | PP_1785 | Q88LZ1 | kegg:ppu00525 | PRESENT | CURATED | PRESENT | dTDP-glucose 4,6-dehydratase (EC 4.2.1.46) |

## Notes

Generated UTC: 2026-07-08T00:23:20.632142+00:00

Completed first-pass curation on 2026-07-07 PDT / 2026-07-08 UTC.

Validation and rendering completed:

- `uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/polyketide_sugar_unit_biosynthesis_boundary.yaml`
- `uv run python -m ai_gene_review.validation.module_validator modules/polyketide_sugar_unit_biosynthesis_boundary.yaml`
- `just validate PSEPK <gene>` for all 6 genes in this batch.
- `just render PSEPK <gene>` for all 6 genes in this batch.

Main curation conclusions:

- Treat KEGG `ppu00523` as a dTDP-deoxy-sugar/dTDP-rhamnose boundary map, not
  as evidence for a complete polyketide natural-product sugar-unit pathway in
  KT2440.
- `rfbA` supplies glucose-1-phosphate thymidylyltransferase activity to make
  dTDP-glucose.
- `rffG` supplies dTDP-glucose 4,6-dehydratase activity upstream of the
  dTDP-4-dehydro-6-deoxyglucose intermediate.
- `rmlC` and `rfbC` are duplicate dTDP-4-dehydrorhamnose 3,5-epimerase
  candidates; `PP_0500` and `rfbD` are duplicate dTDP-4-dehydrorhamnose
  reductase candidates.
- Generic racemase/epimerase parent annotations on `rmlC` and `rfbC` were
  marked as over-annotated because the specific epimerase activity is present.
  Cytosol, broad polysaccharide, O-antigen, and nucleotide-sugar process
  annotations were kept as non-core context where appropriate.
- `rmlC` and `rfbD` required accession-based fetches with Q88R69 and Q88LZ2
  because symbol lookup did not resolve their UniProt entries.

- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon polyketide_sugar_unit_biosynthesis_boundary` and
  `just module-pathway-deep-research-falcon polyketide_sugar_unit_biosynthesis_boundary ppu00523 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/polyketide_sugar_unit_biosynthesis_boundary-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__polyketide_sugar_unit_biosynthesis_boundary__ppu00523-deep-research-falcon.md`.
