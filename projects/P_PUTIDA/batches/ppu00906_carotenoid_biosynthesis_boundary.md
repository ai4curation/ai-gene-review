---
title: "PSEPK ppu00906 Carotenoid biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00906: Carotenoid biosynthesis

- Module seed: `carotenoid_biosynthesis_boundary`
- Candidate genes from membership table: 1
- Primary bucket genes: 1
- Existing review files: 1
- Curated review files: 1
- Existing Asta research files: 1

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted 2026-07-11 PDT; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted 2026-07-11 PDT; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `crtZ` | PP_3246 | Q88HV7 | kegg:ppu00906 | PRESENT | CURATED | PRESENT | Beta-carotene hydroxylase (EC 1.-.-.-) |

## Notes

Generated UTC: 2026-07-08T16:19:52.736026+00:00

2026-07-11 PDT status sync: `modules/carotenoid_biosynthesis_boundary.yaml`
is curated and validates with both module validators. `crtZ` validates as a
one-gene beta-carotene 3-hydroxylase/xanthophyll-biosynthesis boundary case;
the only gene-level warning is the non-blocking note that the Asta file is not
cited in annotation decisions.

Real Falcon commands were run:

```bash
just module-deep-research-falcon carotenoid_biosynthesis_boundary
just module-pathway-deep-research-falcon carotenoid_biosynthesis_boundary ppu00906 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no
Falcon reports were written. Expected output paths remain:

- `modules/carotenoid_biosynthesis_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__carotenoid_biosynthesis_boundary__ppu00906-deep-research-falcon.md`
