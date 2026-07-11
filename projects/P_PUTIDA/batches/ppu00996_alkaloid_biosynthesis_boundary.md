---
title: "PSEPK ppu00996 Biosynthesis of various alkaloids batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00996: Biosynthesis of various alkaloids

- Module seed: `alkaloid_biosynthesis_boundary`
- Candidate genes from membership table: 1
- Primary bucket genes: 1
- Existing review files: 1
- Curated review files: 1
- Existing Asta research files: 1

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
| [x] | `PP_3358` | PP_3358 | Q88HJ8 | kegg:ppu00996 | PRESENT | CURATED | PRESENT | Hydroxycinnamoyl-CoA hydratase-lyase (EC 4.1.2.41, EC 4.2.1.101) |

## Notes

Generated UTC: 2026-07-08T18:13:35.616320+00:00

2026-07-11 PDT status sync: `modules/alkaloid_biosynthesis_boundary.yaml` is curated and validates with both module validators. `PP_3358` validates cleanly. This is a one-gene pathway-absence/boundary case: KEGG ppu00996 contains only PP_3358, a feruloyl-CoA hydratase/lyase side-node enzyme in hydroxycinnamate/vanillin metabolism, so no alkaloid biosynthesis process should be inferred from this bucket alone.

Real Falcon commands were run:

```bash
just module-deep-research-falcon alkaloid_biosynthesis_boundary
just module-pathway-deep-research-falcon alkaloid_biosynthesis_boundary ppu00996 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/alkaloid_biosynthesis_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__alkaloid_biosynthesis_boundary__ppu00996-deep-research-falcon.md`
