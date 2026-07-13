---
title: "PSEPK UPA00666 UniPathway UPA00666 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00666: UniPathway UPA00666

- Pathway seed: `apolipoprotein_n_acyltransferase` (single-step; no standalone module retained)
- Candidate genes from membership table: 1
- Primary bucket genes: 1
- Existing review files: 1
- Curated review files: 1
- Existing OpenScientist research files: 3

## Required Workflow

- [x] Assess module granularity and record the single-step pathway curation.
- [x] Run generic OpenScientist retrieval for the pathway seed.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate gene review; standalone module retired/deferred.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `lnt` | PP_4790 | Q88DN4 | unipathway:UPA00666 | PRESENT | CURATED | PRESENT | Apolipoprotein N-acyltransferase (ALP N-acyltransferase) (EC 2.3.1.269) |

## Notes

Generated UTC: 2026-07-11T21:36:02.996296+00:00

- Retired the previous `modules/apolipoprotein_n_acyltransferase.yaml` seed:
  UPA00666 is a single Lnt N-acylation step and should not be represented as a
  standalone one-part module. Reintroduce it only inside a broader multi-part
  bacterial lipoprotein maturation module.
