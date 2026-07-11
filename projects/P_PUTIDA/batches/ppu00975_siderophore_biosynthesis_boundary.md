---
title: "PSEPK ppu00975 Biosynthesis of various siderophores batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00975: Biosynthesis of various siderophores

- Module seed: `siderophore_biosynthesis_boundary`
- Candidate genes from membership table: 3
- Primary bucket genes: 3
- Existing review files: 3
- Curated review files: 3
- Existing Asta research files: 3

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
| [x] | `PP_2800` | PP_2800 | Q88J49 | kegg:ppu00975 | PRESENT | CURATED | PRESENT | Diaminobutyrate-2-oxoglutarate transaminase |
| [x] | `pvdH` | PP_4223 | Q88F75 | kegg:ppu00975 | PRESENT | CURATED | PRESENT | Diaminobutyrate-2-oxoglutarate transaminase (EC 2.6.1.76) |
| [x] | `pvdY` | PP_4245 | Q88F54 | kegg:ppu00975 | PRESENT | CURATED | PRESENT | Hydroxyproline acetylase (EC 2.3.1.-) |

## Notes

Generated UTC: 2026-07-08T18:07:37.998050+00:00

2026-07-11 PDT status sync: `modules/siderophore_biosynthesis_boundary.yaml` is curated and validates with both module validators. `PP_2800`, `pvdH`, and `pvdY` all validate cleanly. This shared boundary module treats ppu00975 as selected pyoverdine/siderophore precursor and tailoring chemistry, not a complete standalone siderophore route; the main ferribactin/pyoverdine NRPS assembly context is tracked in the same module through routed PvdL/PvdI/PvdJ/PvdD spillovers.

Real Falcon commands were run for the shared module and this pathway context:

```bash
just module-deep-research-falcon siderophore_biosynthesis_boundary
just module-pathway-deep-research-falcon siderophore_biosynthesis_boundary ppu00975 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/siderophore_biosynthesis_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__siderophore_biosynthesis_boundary__ppu00975-deep-research-falcon.md`
