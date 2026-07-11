---
title: "PSEPK UPA00286 alginate biosynthesis boundary batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00286: alginate biosynthesis boundary

- Module seed: `alginate_biosynthesis_boundary`
- Candidate genes from membership table: 11
- Primary bucket genes: 2
- Existing review files: 11
- Curated review files: 11
- Existing Asta research files: 11

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `algB` | PP_0133 | Q88RJ6 | kegg:ppu02020 | PRESENT | CURATED | PRESENT | Alginate biosynthesis transcriptional regulatory protein AlgB |
| [x] | `algF` | PP_1278 | Q88ND4 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Alginate biosynthesis protein AlgF |
| [x] | `algJ` | PP_1279 | Q88ND3 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Probable alginate O-acetylase AlgJ (EC 2.3.1.-) (Alginate biosynthesis protein AlgJ) |
| [x] | `algI` | PP_1280 | Q88ND2 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Probable alginate O-acetylase AlgI (EC 2.3.1.-) (Alginate biosynthesis protein AlgI) |
| [x] | `algX` | PP_1282 | Q88ND0 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Alginate biosynthesis protein AlgX (Probable alginate O-acetyltransferase AlgX) (EC 2.3.1.-) |
| [x] | `algG` | PP_1283 | Q88NC9 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | Mannuronan C5-epimerase (EC 5.1.3.37) (Poly(beta-D-mannuronate) C5 epimerase) |
| [x] | `algE` | PP_1284 | Q88NC8 | unipathway:UPA00286 | PRESENT | CURATED | PRESENT | Alginate production protein AlgE |
| [x] | `algK` | PP_1285 | Q88NC7 | unipathway:UPA00286 | PRESENT | CURATED | PRESENT | Alginate biosynthesis protein AlgK |
| [x] | `alg44` | PP_1286 | Q88NC6 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Alginate biosynthesis protein Alg44 |
| [x] | `alg8` | PP_1287 | Q88NC5 | kegg:ppu00543 | PRESENT | CURATED | PRESENT | Glycosyltransferase alg8 (EC 2.4.-.-) |
| [x] | `algD` | PP_1288 | Q88NC4 | kegg:ppu00051 | PRESENT | CURATED | PRESENT | GDP-mannose 6-dehydrogenase (GMD) (EC 1.1.1.132) |

## Notes

Generated UTC: 2026-07-10T00:53:36.924620+00:00

2026-07-09 PDT:

- Created and validated `modules/alginate_biosynthesis_boundary.yaml` as a
  dedicated UniPathway UPA00286 coverage module.
- All 11 UniPathway UPA00286 members have curated review YAMLs and Asta reports;
  this pass added missing Asta retrieval reports for the two UniPathway-primary
  export/scaffold genes `algE` and `algK`.
- The module consolidates alginate biology split across existing pathway
  batches: `algD` precursor formation from `ppu00051`, `alg8`/`alg44` and
  `algF`/`algJ`/`algI`/`algX` polymerization/modification context from
  `ppu00543`, `algB` regulatory context from `ppu02020`, and the UniPathway-only
  `algE`/`algK` export/scaffold context.
- Falcon generic module research was attempted with
  `just module-deep-research-falcon alginate_biosynthesis_boundary` and failed
  before report generation with Edison HTTP 402 Payment Required. Expected
  output remains queued:
  `modules/alginate_biosynthesis_boundary-deep-research-falcon.md`.
- Falcon PSEPK module+pathway research was attempted with
  `just module-pathway-deep-research-falcon alginate_biosynthesis_boundary UPA00286 PSEPK`
  and failed before report generation with Edison HTTP 402 Payment Required.
  Expected output remains queued:
  `projects/P_PUTIDA/deep-research/PSEPK__alginate_biosynthesis_boundary__upa00286-deep-research-falcon.md`.
