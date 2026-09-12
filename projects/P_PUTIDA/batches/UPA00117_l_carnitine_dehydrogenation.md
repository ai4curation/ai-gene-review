---
title: "PSEPK UPA00117 UniPathway UPA00117 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00117: UniPathway UPA00117

- Pathway seed: `l_carnitine_dehydrogenation` (single-step; no standalone module retained)
- Candidate genes from membership table: 1
- Primary bucket genes: 1
- Existing review files: 1
- Curated review files: 1
- Existing OpenScientist research files: 1

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

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `lcdH` | PP_0302 | Q88R32 | unipathway:UPA00117 | PRESENT | CURATED | PRESENT | L-carnitine dehydrogenase (CDH) (L-CDH) (EC 1.1.1.108) |

## Notes

Generated UTC: 2026-07-11T21:08:35.324367+00:00

- Retired the previous `modules/l_carnitine_dehydrogenation.yaml` seed:
  UPA00117 is a single LcdH oxidation step and should not be represented as a
  standalone one-part module. Reintroduce it only inside a broader multi-part
  carnitine-utilization module.
- OpenScientist gene-level research completed:
  `genes/PSEPK/lcdH/lcdH-deep-research-openscientist.md`.
- OpenScientist generic retrieval completed:
  `modules/l_carnitine_dehydrogenation-deep-research-openscientist.md`.
- OpenScientist PSEPK module+pathway research completed:
  `projects/P_PUTIDA/deep-research/PSEPK__l_carnitine_dehydrogenation__upa00117-deep-research-openscientist.md`.
- Curation decision: UPA00117 is covered by the single KT2440 candidate
  `lcdH` / PP_0302 / Q88R32 for NAD(+)-dependent L-carnitine oxidation to
  3-dehydrocarnitine.
- Boundary call: PP_0301, PP_0303, PP_0304, PP_0305 are adjacent
  carnitine-utilization context, not members of this single-step UniPathway
  bucket.
- Quality-control call: the OpenScientist reports mention GO:0008859 as
  carnitine 3-dehydrogenase activity, but OAK/GO lookup shows GO:0008859 is
  exoribonuclease II activity. The correct fetched GOA term retained here is
  GO:0047728.
