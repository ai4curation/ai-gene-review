---
title: "PSEPK ppu00930 Caprolactam degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00930: Caprolactam degradation

- Module seed: `caprolactam_degradation_boundary`
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
| [x] | `fadB` | PP_2136 | Q88L02 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomeras |
| [x] | `PP_2217` | PP_2217 | Q88KS2 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | enoyl-CoA hydratase (EC 4.2.1.17) |
| [x] | `paaF` | PP_3284 | Q88HR9 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) |

## Notes

Generated UTC: 2026-07-08T17:05:10.982163+00:00

2026-07-11 PDT status sync: `modules/caprolactam_degradation_boundary.yaml` is curated and validates with both module validators. `fadB`, `PP_2217`, and `paaF` all validate; `PP_2217` and `paaF` have only the existing warning that their Asta reports are not cited in annotation-level reviews. This is a route-absence/boundary case: KEGG ppu00930 contains shared CoA-thioester hydratase/isomerase and beta-oxidation side enzymes, but lacks route-defining caprolactam lactamase, 6-aminohexanoate, adipate, or semialdehyde upper-pathway enzymes.

Real Falcon commands were run:

```bash
just module-deep-research-falcon caprolactam_degradation_boundary
just module-pathway-deep-research-falcon caprolactam_degradation_boundary ppu00930 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/caprolactam_degradation_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__caprolactam_degradation_boundary__ppu00930-deep-research-falcon.md`
