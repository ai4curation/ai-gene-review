---
title: "PSEPK UPA00060 thiamine biosynthesis support batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00060: thiamine biosynthesis support

- Module seed: `thiamine_biosynthesis`
- Candidate genes from membership table: 9
- Primary bucket genes: 1
- Existing review files: 9
- Curated review files: 9
- Existing Asta research files: 9

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Reuse completed module-level Falcon deep research from the `ppu00730` thiamine biosynthesis checkpoint.
- [x] Reuse completed module + pathway + PSEPK Falcon deep research from the `ppu00730` thiamine biosynthesis checkpoint; the report covers the thiamine salvage/context boundary that includes `pet`.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `thiL` | PP_0519 | Q88QH4 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Thiamine-monophosphate kinase (TMP kinase) (Thiamine-phosphate kinase) (EC 2.7.4.16) |
| [x] | `thiO` | PP_0612 | Q88Q83 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Glycine oxidase (GO) (EC 1.4.3.19) |
| [x] | `pet` | PP_3185 | Q88I17 | unipathway:UPA00060 | PRESENT | CURATED | PRESENT | Aminopyrimidine aminohydrolase (EC 3.5.99.2) |
| [x] | `PP_3186` | PP_3186 | Q88I16 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Aminopyrimidine aminohydrolase (EC 3.5.99.2) |
| [x] | `thiD` | PP_4782 | Q88DP2 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | hydroxymethylpyrimidine kinase (EC 2.7.1.49) |
| [x] | `thiE` | PP_4783 | Q88DP1 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Thiamine-phosphate synthase (TP synthase) (TPS) (EC 2.5.1.3) (Thiamine-phosphate pyrophosphorylase) (TMP pyrophosphoryla |
| [x] | `thiC` | PP_4922 | Q88DA5 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Phosphomethylpyrimidine synthase (EC 4.1.99.17) (Hydroxymethylpyrimidine phosphate synthase) (HMP-P synthase) (HMP-phosp |
| [x] | `thiI` | PP_5045 | Q88CY4 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | tRNA sulfurtransferase (EC 2.8.1.4) (Sulfur carrier protein ThiS sulfurtransferase) (Thiamine biosynthesis protein ThiI) |
| [x] | `thiG` | PP_5104 | Q88CS6 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Thiazole synthase (EC 2.8.1.10) |

## Notes

Generated UTC: 2026-07-10T00:37:08.467345+00:00

2026-07-09 PDT:

- Completed the UPA00060 support-bucket registration for the existing
  `thiamine_biosynthesis` module.
- All 9 UniPathway UPA00060 members already have curated review YAMLs and Asta
  reports.
- The strict module was already created during `ppu00730`; this support batch
  documents the full UniPathway cross-reference and highlights `pet`/PP_3185 as
  the only UniPathway-primary member. `pet` and PP_3186 are best treated as
  thiamine salvage/context rather than strict de novo thiamine diphosphate
  biosynthesis enzymes.
- Falcon generic and PSEPK-specific module research were already completed for
  the `ppu00730` thiamine checkpoint and are reused here rather than rerun as a
  duplicate provider job.
