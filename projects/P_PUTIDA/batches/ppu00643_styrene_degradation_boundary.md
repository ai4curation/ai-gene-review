---
title: "PSEPK ppu00643 Styrene degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00643: Styrene degradation

- Module seed: `styrene_degradation_boundary`
- Candidate genes from membership table: 5
- Primary bucket genes: 5
- Existing review files: 5
- Curated review files: 5
- Existing Asta research files: 5

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
| [x] | `PP_2932` | PP_2932 | Q88IR7 | kegg:ppu00643 | PRESENT | CURATED | PRESENT | Amidase family protein |
| [x] | `peaE` | PP_3463 | Q88H97 | kegg:ppu00643 | PRESENT | CURATED | PRESENT | Phenylacetaldehyde dehydrogenase (EC 1.2.1.39) |
| [x] | `hmgC` | PP_4619 | Q88E49 | kegg:ppu00643 | PRESENT | CURATED | PRESENT | Maleylacetoacetate isomerase (EC 5.2.1.2) |
| [x] | `hmgB` | PP_4620 | Q88E48 | kegg:ppu00643 | PRESENT | CURATED | PRESENT | fumarylacetoacetase (EC 3.7.1.2) |
| [x] | `hmgA` | PP_4621 | Q88E47 | kegg:ppu00643 | PRESENT | CURATED | PRESENT | Homogentisate 1,2-dioxygenase (HGDO) (EC 1.13.11.5) (Homogentisate oxygenase) (Homogentisic acid oxidase) (Homogentisica |

## Notes

Generated UTC: 2026-07-08T13:51:09.525448+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon styrene_degradation_boundary`
  and `just module-pathway-deep-research-falcon styrene_degradation_boundary ppu00643 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/styrene_degradation_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__styrene_degradation_boundary__ppu00643-deep-research-falcon.md`.
