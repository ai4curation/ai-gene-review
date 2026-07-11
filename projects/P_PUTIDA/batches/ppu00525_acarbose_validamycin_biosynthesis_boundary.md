---
title: "PSEPK ppu00525 Acarbose and validamycin biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00525: Acarbose and validamycin biosynthesis

- Module seed: `acarbose_validamycin_biosynthesis_boundary`
- Candidate genes from membership table: 2
- Primary bucket genes: 2
- Existing review files: 2
- Curated review files: 2
- Existing Asta research files: 2

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
| [x] | `rfbA` | PP_1783 | Q88LZ3 | kegg:ppu00525 | PRESENT | CURATED | PRESENT | Glucose-1-phosphate thymidylyltransferase (EC 2.7.7.24) |
| [x] | `rffG` | PP_1785 | Q88LZ1 | kegg:ppu00525 | PRESENT | CURATED | PRESENT | dTDP-glucose 4,6-dehydratase (EC 4.2.1.46) |

## Notes

Generated UTC: 2026-07-08T00:28:23.190345+00:00

Completed first-pass curation on 2026-07-07 PDT / 2026-07-08 UTC.

Validation and rendering completed:

- `uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/acarbose_validamycin_biosynthesis_boundary.yaml`
- `uv run python -m ai_gene_review.validation.module_validator modules/acarbose_validamycin_biosynthesis_boundary.yaml`
- `just validate PSEPK rfbA`
- `just validate PSEPK rffG`
- `just render PSEPK rfbA`
- `just render PSEPK rffG`

Main curation conclusions:

- Treat KEGG `ppu00525` as a boundary/absence map. KT2440 has only two shared
  dTDP-sugar precursor enzymes from this KEGG pathway, not a satisfiable
  acarbose, validamycin, or aminocyclitol antibiotic biosynthesis pathway.
- `rfbA` supplies glucose-1-phosphate thymidylyltransferase activity to make
  dTDP-glucose.
- `rffG` supplies dTDP-glucose 4,6-dehydratase activity in deoxy-sugar
  nucleotide metabolism.
- No additional gene-level edits were needed for this batch because both genes
  were already curated in the adjacent `ppu00520`/`ppu00523` nucleotide-sugar
  work.

- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon acarbose_validamycin_biosynthesis_boundary` and
  `just module-pathway-deep-research-falcon acarbose_validamycin_biosynthesis_boundary ppu00525 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/acarbose_validamycin_biosynthesis_boundary-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__acarbose_validamycin_biosynthesis_boundary__ppu00525-deep-research-falcon.md`.
