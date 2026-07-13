---
title: "PSEPK ppu00300 Lysine biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00300: Lysine biosynthesis

- Module seed: `lysine_biosynthesis`
- Candidate genes from membership table: 19
- Primary bucket genes: 12
- Existing review files: 19
- Curated review files: 19
- Existing Asta research files: 19

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
| [x] | `aruC` | PP_0372 | Q88QW2 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | Acetylornithine aminotransferase 2 (EC 2.6.1.11, EC 2.6.1.13) |
| [x] | `PP_0664` | PP_0664 | Q88Q34 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | homoserine dehydrogenase (EC 1.1.1.3) |
| [x] | `dapA__Q88NH2` | PP_1237 | Q88NH2 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | 4-hydroxy-tetrahydrodipicolinate synthase (HTPA synthase) (EC 4.3.3.7) |
| [x] | `murE` | PP_1332 | Q88N81 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | UDP-N-acetylmuramoyl-L-alanyl-D-glutamate--2,6-diaminopimelate ligase (EC 6.3.2.13) (Meso-A2pm-adding enzyme) (Meso-diam |
| [x] | `murF` | PP_1333 | Q88N80 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | UDP-N-acetylmuramoyl-tripeptide--D-alanyl-D-alanine ligase (EC 6.3.2.10) (D-alanyl-D-alanine-adding enzyme) |
| [x] | `hom` | PP_1470 | Q88MU8 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | Homoserine dehydrogenase (EC 1.1.1.3) |
| [x] | `dapE` | PP_1525 | Q88MP5 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | Succinyl-diaminopimelate desuccinylase (SDAP desuccinylase) (EC 3.5.1.18) (N-succinyl-LL-2,6-diaminoheptanedioate amidoh |
| [x] | `dapD` | PP_1530 | Q88MP1 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | 2,3,4,5-tetrahydropyridine-2,6-dicarboxylate N-succinyltransferase (EC 2.3.1.117) (Tetrahydrodipicolinate N-succinyltran |
| [x] | `dapC` | PP_1588 | Q88MI3 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | N-succinyl-L,L-diaminopimelate aminotransferase alternative (EC 2.6.1.17) |
| [x] | `asd__Q88LE4` | PP_1989 | Q88LE4 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Aspartate-semialdehyde dehydrogenase (ASA dehydrogenase) (ASADH) (EC 1.2.1.11) (Aspartate-beta-semialdehyde dehydrogenas |
| [x] | `PP_2036` | PP_2036 | Q88L99 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | 4-hydroxy-tetrahydrodipicolinate synthase (EC 4.3.3.7) |
| [x] | `lysA-I` | PP_2077 | Q88L58 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | Diaminopimelate decarboxylase (DAP decarboxylase) (DAPDC) (EC 4.1.1.20) |
| [x] | `dapA__Q88JL0` | PP_2639 | Q88JL0 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | 4-hydroxy-tetrahydrodipicolinate synthase (HTPA synthase) (EC 4.3.3.7) |
| [x] | `aspC` | PP_3786 | Q88GD8 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | Aminotransferase (EC 2.6.1.1) |
| [x] | `dapF__Q88GD4` | PP_3790 | Q88GD4 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | Diaminopimelate epimerase (DAP epimerase) (EC 5.1.1.7) (PLP-independent amino acid racemase) |
| [x] | `PP_4473` | PP_4473 | Q88EI9 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Aspartate kinase (EC 2.7.2.4) (Aspartokinase) |
| [x] | `dapB` | PP_4725 | Q88DU4 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | 4-hydroxy-tetrahydrodipicolinate reductase (HTPA reductase) (EC 1.17.1.8) |
| [x] | `lysA-II` | PP_5227 | Q88CF4 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | Diaminopimelate decarboxylase (DAP decarboxylase) (DAPDC) (EC 4.1.1.20) |
| [x] | `dapF__Q88CF3` | PP_5228 | Q88CF3 | kegg:ppu00300 | PRESENT | CURATED | PRESENT | Diaminopimelate epimerase (DAP epimerase) (EC 5.1.1.7) (PLP-independent amino acid racemase) |

## Workflow Notes

- Species-neutral module created and validated:
  `modules/lysine_biosynthesis.yaml`.
- All 19 KEGG `ppu00300` membership genes have review folders, Asta reports,
  curated YAML reviews, and rendered gene pages. `lysA-II` resolves to the
  existing accession-matched `genes/PSEPK/lysA/` review for Q88CF4.
- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon lysine_biosynthesis` and
  `just module-pathway-deep-research-falcon lysine_biosynthesis ppu00300 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/lysine_biosynthesis-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__lysine_biosynthesis__ppu00300-deep-research-falcon.md`.
- Validation passed for the module and all 19 resolved review folders. Remaining
  full-batch warnings are limited to older cross-bucket reviews with pre-existing
  Asta-citation or homoserine-process reflection warnings; the nine newly
  curated ppu00300 reviews validate cleanly.

## Curation Notes

- The strict bacterial route is the diaminopimelate branch to L-lysine:
  shared aspartate-family precursor supply (`PP_4473`, `asd__Q88LE4`), DapA-like
  HTPA synthases (`dapA__Q88NH2`, `dapA__Q88JL0`, PP_2036), `dapB`, the
  succinylated branch (`dapD`, `dapC`, `dapE`), DapF epimerases
  (`dapF__Q88GD4`, `dapF__Q88CF3`), and LysA decarboxylases (`lysA-I` and the
  existing Q88CF4 `lysA` review).
- `murE` and `murF` are peptidoglycan precursor ligases that consume
  meso-diaminopimelate; they are important ppu00300 boundary nodes but do not
  satisfy L-lysine formation.
- `hom` and PP_0664 are homoserine-branch enzymes, `aspC` is upstream aspartate
  transamination context, and `aruC` is arginine/ornithine aminotransferase
  context.
- Authored process terms should use current `GO:0009085` for L-lysine
  biosynthesis. The older route-specific `GO:0009089` and diaminopimelate
  process `GO:0019877` terms are obsolete and should remain only in provenance
  or rationale text.
- `dapE` needed first-pass cleanup: the arginine-biosynthesis transfer was
  removed, and the acetylornithine deacetylase family transfer was modified to
  the specific succinyl-diaminopimelate desuccinylase activity.

## Notes

Generated UTC: 2026-07-07T19:30:06.362586+00:00
