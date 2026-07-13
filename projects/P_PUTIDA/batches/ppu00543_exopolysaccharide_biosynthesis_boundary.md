---
title: "PSEPK ppu00543 Exopolysaccharide biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00543: Exopolysaccharide biosynthesis

- Module seed: `exopolysaccharide_biosynthesis_boundary`
- Candidate genes from membership table: 11
- Primary bucket genes: 11
- Existing review files: 11
- Curated review files: 11
- Existing Asta research files: 11

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
| [x] | `PP_0228` | PP_0228 | Q88RA5 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | serine O-acetyltransferase (EC 2.3.1.30) |
| [x] | `cysE` | PP_0840 | Q88PL0 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | serine O-acetyltransferase (EC 2.3.1.30) |
| [x] | `PP_1110` | PP_1110 | Q88NU4 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | serine O-acetyltransferase (EC 2.3.1.30) |
| [x] | `algF` | PP_1278 | Q88ND4 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Alginate biosynthesis protein AlgF |
| [x] | `algJ` | PP_1279 | Q88ND3 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Probable alginate O-acetylase AlgJ (EC 2.3.1.-) (Alginate biosynthesis protein AlgJ) |
| [x] | `algI` | PP_1280 | Q88ND2 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Probable alginate O-acetylase AlgI (EC 2.3.1.-) (Alginate biosynthesis protein AlgI) |
| [x] | `algX` | PP_1282 | Q88ND0 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Alginate biosynthesis protein AlgX (Probable alginate O-acetyltransferase AlgX) (EC 2.3.1.-) |
| [x] | `alg44` | PP_1286 | Q88NC6 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Alginate biosynthesis protein Alg44 |
| [x] | `alg8` | PP_1287 | Q88NC5 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Glycosyltransferase alg8 (EC 2.4.-.-) |
| [x] | `PP_2124` | PP_2124 | Q88L13 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Glycosyl transferase |
| [x] | `PP_3136` | PP_3136 | Q88I65 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Serine acetyltransferase (EC 2.3.1.30) |

## Notes

Generated UTC: 2026-07-08T09:44:18.463228+00:00

Completed first-pass curation on 2026-07-08 UTC. The species-neutral boundary
module is `modules/exopolysaccharide_biosynthesis_boundary.yaml`. All 11 KEGG
`ppu00543` membership genes have review folders, Asta retrieval reports,
curated review YAMLs, successful `just validate PSEPK <gene>` runs, and rendered
review pages. The module passed both LinkML validation and
`ai_gene_review.validation.module_validator`.

Main curation conclusions:

- `ppu00543` is an exopolysaccharide/alginate boundary map, not a single
  complete polysaccharide pathway.
- The alginate production core in this batch is represented by `alg8` alginate
  synthase and `alg44` cyclic-di-GMP-binding alginate production factor.
- Alginate O-acetylation/modification context is represented by `algF`, `algJ`,
  `algI`, and `algX`. `algJ` and `algX` received first-pass `NEW` broad
  acyltransferase annotations from UniProt because the fetched GOA block did
  not include the molecular-function line.
- `PP_2124` remains an unresolved glycosyltransferase candidate; its broad
  glycosyltransferase activity was accepted, while the TreeGrafter LPS
  biosynthetic process annotation was marked over-annotated pending substrate
  evidence.
- `PP_0228`, `cysE`, `PP_1110`, and `PP_3136` are serine
  O-acetyltransferase/cysteine-biosynthesis spillovers. Their presence in
  `ppu00543` should not be interpreted as core exopolysaccharide biosynthesis.
- `algX` initially hit a transient UniProt timeout during fetch and Asta had
  intermittent read timeouts during the batch run; retrying the affected genes
  produced the missing data/retrieval files.

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon exopolysaccharide_biosynthesis_boundary`
  and `just module-pathway-deep-research-falcon exopolysaccharide_biosynthesis_boundary ppu00543 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/exopolysaccharide_biosynthesis_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__exopolysaccharide_biosynthesis_boundary__ppu00543-deep-research-falcon.md`.
