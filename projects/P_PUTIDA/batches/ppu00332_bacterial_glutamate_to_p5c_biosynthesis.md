---
title: "PSEPK ppu00332 Carbapenem biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00332: Carbapenem biosynthesis

- Module seed: `bacterial_glutamate_to_p5c_biosynthesis`
- Candidate genes from membership table: 2
- Primary bucket genes: 2
- Existing review files: 0
- Curated review files: 0
- Existing OpenScientist research files: 2

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level OpenScientist deep research.
- [x] Run module + pathway + PSEPK OpenScientist deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [ ] Run OpenScientist deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [x] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `proB` | PP_0691 | Q88Q07 | kegg:ppu00332 | PRESENT | CURATED | FAILED_TIMEOUT | Glutamate 5-kinase (EC 2.7.2.11) (Gamma-glutamyl kinase) (GK) |
| [x] | `proA` | PP_4811 | Q88DL4 | kegg:ppu00332 | PRESENT | CURATED | FAILED_TIMEOUT | Gamma-glutamyl phosphate reductase (GPR) (EC 1.2.1.41) (Glutamate-5-semialdehyde dehydrogenase) (Glutamyl-gamma-semialde |

## Notes

Generated UTC: 2026-07-16T17:37:22.072385+00:00

2026-07-16: OpenScientist timed out after 7200s for `proB` and `proA`; no gene-level report files were produced for those runs.
