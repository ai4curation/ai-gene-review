---
title: "PSEPK UPA00191 UniPathway UPA00191 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00191: UniPathway UPA00191

- Module seed: `rubredoxin_electron_transfer`
- Candidate genes from membership table: 1
- Primary bucket genes: 1
- Existing review files: 1
- Curated review files: 1
- Existing OpenScientist research files: 3

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `rubA` | PP_5315 | Q88C68 | unipathway:UPA00191 | PRESENT | CURATED | PRESENT | Rubredoxin |

## Notes

OpenScientist species-aware research indicates that RubA covers a rubredoxin electron-carrier step, but UPA00191 as an alkane-degradation pathway is not satisfiable in KT2440 because a true alkane 1-monooxygenase is absent; the GO:0043448 annotation is marked over-annotated in the gene review.

Generated UTC: 2026-07-11T21:42:36.011565+00:00
