---
title: "PSEPK ppu00332 Carbapenem biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00332: Carbapenem biosynthesis

- Module seed: `carbapenem_biosynthesis_boundary`
- Candidate genes from membership table: 2
- Primary bucket genes: 2
- Existing review files: 2
- Curated review files: 2
- Existing Asta research files: 2

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
| [x] | `proB` | PP_0691 | Q88Q07 | kegg:ppu00332 | PRESENT | CURATED | PRESENT | Glutamate 5-kinase (EC 2.7.2.11) (Gamma-glutamyl kinase) (GK) |
| [x] | `proA` | PP_4811 | Q88DL4 | kegg:ppu00332 | PRESENT | CURATED | PRESENT | Gamma-glutamyl phosphate reductase (GPR) (EC 1.2.1.41) (Glutamate-5-semialdehyde dehydrogenase) (Glutamyl-gamma-semialde |

## Notes

Generated UTC: 2026-07-07T20:48:54.878820+00:00

2026-07-11 PDT status sync: `modules/carbapenem_biosynthesis_boundary.yaml` is curated and validates with both module validators. `proB` and `proA` validate with only the existing warning that their Asta reports are not cited in annotation-level reviews. This bucket is a pathway-absence/boundary case: KEGG ppu00332 contains only ProB and ProA, ordinary proline-biosynthesis precursor enzymes, so the module treats the map as shared precursor chemistry rather than evidence for carbapenem biosynthesis in KT2440.

Real Falcon commands were run:

```bash
just module-deep-research-falcon carbapenem_biosynthesis_boundary
just module-pathway-deep-research-falcon carbapenem_biosynthesis_boundary ppu00332 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/carbapenem_biosynthesis_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__carbapenem_biosynthesis_boundary__ppu00332-deep-research-falcon.md`
