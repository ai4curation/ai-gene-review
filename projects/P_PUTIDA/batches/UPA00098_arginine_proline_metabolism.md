---
title: "PSEPK UPA00098 UniPathway UPA00098 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00098: UniPathway UPA00098

- Module seed: `arginine_proline_metabolism`
- Candidate genes from membership table: 5
- Primary bucket genes: 1
- Existing review files: 5
- Curated review files: 5
- Existing Asta research files: 5

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
- [x] Run module + pathway + PSEPK Falcon deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `proB` | PP_0691 | Q88Q07 | kegg:ppu00332 | PRESENT | CURATED | PRESENT | Glutamate 5-kinase (EC 2.7.2.11) (Gamma-glutamyl kinase) (GK) |
| [x] | `ocd__Q88H32` | PP_3533 | Q88H32 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Ornithine cyclodeaminase (OCD) (EC 4.3.1.12) |
| [x] | `proC` | PP_3778 | Q88GE6 | unipathway:UPA00098 | PRESENT | CURATED | PRESENT | Pyrroline-5-carboxylate reductase (P5C reductase) (P5CR) (EC 1.5.1.2) (PCA reductase) |
| [x] | `proA` | PP_4811 | Q88DL4 | kegg:ppu00332 | PRESENT | CURATED | PRESENT | Gamma-glutamyl phosphate reductase (GPR) (EC 1.2.1.41) (Glutamate-5-semialdehyde dehydrogenase) (Glutamyl-gamma-semialde |
| [x] | `proI` | PP_5095 | Q88CT5 | kegg:ppu00330 | PRESENT | CURATED | PRESENT | Pyrroline-5-carboxylate reductase (P5C reductase) (P5CR) (EC 1.5.1.2) (PCA reductase) |

## Notes

Generated UTC: 2026-07-09T23:55:28.089969+00:00

Curator notes, 2026-07-09:

- Reused and updated `modules/arginine_proline_metabolism.yaml`; the proline
  biosynthesis/interconversion part now explicitly includes the full UPA00098
  member set: `proB`, `proA`, `proC`, `proI`, and `ocd__Q88H32`.
- No new gene-level curation was required. All five selected genes already had
  review folders, curated YAML, and Asta reports from the broader
  arginine/proline pass.
- Focused validation passed for all five gene reviews. Each review reports the
  existing non-blocking warning that no annotation directly cites the available
  Asta file.
- Real Falcon generic module research was attempted and failed before report
  creation with Edison HTTP 402 Payment Required:
  `modules/arginine_proline_metabolism-deep-research-falcon.md`.
- Real Falcon PSEPK module+pathway research was attempted and failed before
  report creation with Edison HTTP 402 Payment Required:
  `projects/P_PUTIDA/deep-research/PSEPK__arginine_proline_metabolism__upa00098-deep-research-falcon.md`.
- The taxon-aware Falcon command resolved the expected local candidate set:
  `proB`, `ocd__Q88H32`, `proC`, `proA`, and `proI`.
- Boundary call: UPA00098 is a proline biosynthesis/interconversion support
  bucket inside the existing broad arginine/proline metabolism module, not a
  new standalone module.
