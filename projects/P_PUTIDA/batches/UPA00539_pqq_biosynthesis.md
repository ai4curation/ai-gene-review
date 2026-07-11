---
title: "PSEPK UPA00539 UniPathway UPA00539 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00539: UniPathway UPA00539

- Module seed: `pqq_biosynthesis`
- Candidate genes from membership table: 7
- Primary bucket genes: 7
- Existing review files: 7
- Curated review files: 7
- Existing Asta research files: 7

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research. Attempted 2026-07-09; Edison rejected task creation with HTTP 402 before report generation.
- [x] Run module + pathway + PSEPK Falcon deep research. Attempted 2026-07-09; Edison rejected task creation with HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `pqqE` | PP_0376 | Q88QV8 | unipathway:UPA00539 | PRESENT | CURATED | PRESENT | PqqA peptide cyclase (EC 1.21.98.4) (Coenzyme PQQ synthesis protein E) (Pyrroloquinoline quinone biosynthesis protein E) |
| [x] | `pqqD1` | PP_0377 | Q88QV7 | unipathway:UPA00539 | PRESENT | CURATED | PRESENT | PqqA binding protein 1 (Coenzyme PQQ synthesis protein D 1) (Pyrroloquinoline quinone biosynthesis protein D 1) |
| [x] | `pqqC` | PP_0378 | Q88QV6 | unipathway:UPA00539 | PRESENT | CURATED | PRESENT | Pyrroloquinoline-quinone synthase (EC 1.3.3.11) (Coenzyme PQQ synthesis protein C) (Pyrroloquinoline quinone biosynthesi |
| [x] | `pqqB` | PP_0379 | Q88QV5 | unipathway:UPA00539 | PRESENT | CURATED | PRESENT | Coenzyme PQQ synthesis protein B (Pyrroloquinoline quinone biosynthesis protein B) |
| [x] | `pqqA` | PP_0380 | Q88QV4 | unipathway:UPA00539 | PRESENT | CURATED | PRESENT | Coenzyme PQQ synthesis protein A (Pyrroloquinoline quinone biosynthesis protein A) |
| [x] | `pqqF` | PP_0381 | Q88QV3 | unipathway:UPA00539 | PRESENT | CURATED | PRESENT | Coenzyme PQQ synthesis protein F (EC 3.4.24.-) (Pyrroloquinoline quinone biosynthesis protein F) |
| [x] | `pqqD2` | PP_2681 | Q88JG8 | unipathway:UPA00539 | PRESENT | CURATED | PRESENT | PqqA binding protein 2 (Coenzyme PQQ synthesis protein D 2) (Pyrroloquinoline quinone biosynthesis protein D 2) |

## Notes

Generated UTC: 2026-07-09T23:18:04.620542+00:00
