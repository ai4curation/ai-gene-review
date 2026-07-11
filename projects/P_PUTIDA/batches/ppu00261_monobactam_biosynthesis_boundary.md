---
title: "PSEPK ppu00261 Monobactam biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00261: Monobactam biosynthesis

- Module seed: `monobactam_biosynthesis_boundary`
- Candidate genes from membership table: 9
- Primary bucket genes: 9
- Existing review files: 9
- Curated review files: 9
- Existing Asta research files: 9

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
| [x] | `dapA__Q88NH2` | PP_1237 | Q88NH2 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | 4-hydroxy-tetrahydrodipicolinate synthase (HTPA synthase) (EC 4.3.3.7) |
| [x] | `cysD` | PP_1303 | Q88NA9 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Sulfate adenylyltransferase subunit 2 (EC 2.7.7.4) (ATP-sulfurylase small subunit) (Sulfate adenylate transferase) (SAT) |
| [x] | `cysNC` | PP_1304 | Q88NA8 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Sulfate adenylyltransferase subunit 1 (EC 2.7.7.4) (ATP-sulfurylase large subunit) (Sulfate adenylate transferase) (SAT) |
| [x] | `asd__Q88LE4` | PP_1989 | Q88LE4 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Aspartate-semialdehyde dehydrogenase (ASA dehydrogenase) (ASADH) (EC 1.2.1.11) (Aspartate-beta-semialdehyde dehydrogenas |
| [x] | `PP_2036` | PP_2036 | Q88L99 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | 4-hydroxy-tetrahydrodipicolinate synthase (EC 4.3.3.7) |
| [x] | `dapA__Q88JL0` | PP_2639 | Q88JL0 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | 4-hydroxy-tetrahydrodipicolinate synthase (HTPA synthase) (EC 4.3.3.7) |
| [x] | `PP_3808` | PP_3808 | Q88GB6 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Antibiotic synthesis protein MbtH |
| [x] | `PP_4473` | PP_4473 | Q88EI9 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Aspartate kinase (EC 2.7.2.4) (Aspartokinase) |
| [x] | `dapB` | PP_4725 | Q88DU4 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | 4-hydroxy-tetrahydrodipicolinate reductase (HTPA reductase) (EC 1.17.1.8) |

## Notes

Generated UTC: 2026-07-07T18:17:16.750886+00:00

## Workflow Notes

- Created and validated `modules/monobactam_biosynthesis_boundary.yaml`.
- Registered `kegg:ppu00261` in `projects/P_PUTIDA/build_pathway_worklist.py`
  as the `monobactam_biosynthesis_boundary` module.
- Fetched the five missing review folders: `dapA__Q88NH2`, `PP_2036`,
  `dapA__Q88JL0`, `PP_3808`, and `dapB`.
- Collision-safe names such as `dapA__Q88NH2` cannot be resolved directly by
  `just fetch-gene`; fetch these with the CLI using `--uniprot-id` and `--alias`.
- Ran Asta for the five newly fetched genes and validated all 9 batch reviews.
- Rendered all 9 gene pages.
- 2026-07-11 status sync: ran `just module-deep-research-falcon monobactam_biosynthesis_boundary`
  and `just module-pathway-deep-research-falcon monobactam_biosynthesis_boundary ppu00261 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/monobactam_biosynthesis_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__monobactam_biosynthesis_boundary__ppu00261-deep-research-falcon.md`.

## Curation Notes

- Treat this as a KEGG boundary/absence batch, not evidence that KT2440 has a
  complete monobactam route.
- `dapA__Q88NH2`, `dapA__Q88JL0`, `PP_2036`, `PP_4473`, `asd__Q88LE4`, and
  `dapB` are aspartate-family / diaminopimelate / L-lysine precursor context.
- `cysD` and `cysNC` are sulfate adenylyltransferase subunits in sulfate
  assimilation and should remain sulfate-activation side-node context.
- `PP_3808` is an MbtH-like accessory protein; the current first-pass support is
  siderophore/NRPS context, not monobactam-specific biosynthesis.
- No `PENDING` actions remain in the newly curated ppu00261 reviews.
