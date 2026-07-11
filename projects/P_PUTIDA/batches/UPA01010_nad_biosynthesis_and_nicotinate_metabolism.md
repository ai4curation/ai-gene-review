---
title: "PSEPK UPA01010 nicotinate catabolism support batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA01010: nicotinate catabolism support

- Module seed: `nad_biosynthesis_and_nicotinate_metabolism`
- Candidate genes from membership table: 9
- Primary bucket genes: 2
- Existing review files: 9
- Curated review files: 9
- Existing Asta research files: 9

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Reuse completed module-level Falcon deep research from the `ppu00760` NAD/nicotinate checkpoint.
- [x] Reuse completed module + pathway + PSEPK Falcon deep research from the `ppu00760` NAD/nicotinate checkpoint; the report covers the aerobic nicotinate-catabolic Nic cluster.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `nicF` | PP_3941 | Q88FY5 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Maleamate amidohydrolase (EC 3.5.1.107) (Nicotinate degradation protein F) |
| [x] | `maiA` | PP_3942 | Q88FY4 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Maleate isomerase (EC 5.2.1.1) (Maleate cis-trans isomerase) (Nicotinate degradation protein E) |
| [x] | `nicD` | PP_3943 | Q88FY3 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | N-formylmaleamate deformylase (EC 3.5.1.106) (Nicotinate degradation protein D) |
| [x] | `nicC` | PP_3944 | Q88FY2 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | 6-hydroxynicotinate 3-monooxygenase (6-HNA monooxygenase) (EC 1.14.13.114) (Nicotinate degradation protein C) |
| [x] | `nicX` | PP_3945 | Q88FY1 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | 2,5-dihydroxypyridine 5,6-dioxygenase (2,5-DHP dioxygenase) (EC 1.13.11.9) (Nicotinate degradation protein X) |
| [x] | `nicR` | PP_3946 | Q88FY0 | unipathway:UPA01010 | PRESENT | CURATED | PRESENT | HTH-type transcriptional repressor NicR (Nicotinate degradation protein R) |
| [x] | `nicA` | PP_3947 | Q88FX9 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Nicotinate dehydrogenase subunit A (EC 1.17.2.1) (Nicotinate degradation protein A) (Nicotinate dehydrogenase small subu |
| [x] | `nicB` | PP_3948 | Q88FX8 | kegg:ppu00760 | PRESENT | CURATED | PRESENT | Nicotinate dehydrogenase subunit B (EC 1.17.2.1) (Nicotinate degradation protein B) (Nicotinate dehydrogenase large subu |
| [x] | `nicS` | PP_3949 | Q88FX7 | unipathway:UPA01010 | PRESENT | CURATED | PRESENT | HTH-type transcriptional repressor NicS (Nicotinate degradation protein S) |

## Notes

Generated UTC: 2026-07-10T00:44:15.563070+00:00

2026-07-09 PDT:

- Completed the UPA01010 support-bucket registration for the existing
  `nad_biosynthesis_and_nicotinate_metabolism` module.
- All 9 UniPathway UPA01010 members have curated review YAMLs and Asta reports;
  this pass added missing Asta retrieval for the two UniPathway-primary
  regulator genes `nicR` and `nicS`.
- The strict catalytic route is the NicA/NicB/NicC/NicX/NicD/NicF/MaiA aerobic
  nicotinate catabolism branch already captured in the `ppu00760` module.
  `nicR` and `nicS` are retained as adjacent transcriptional-regulator context
  rather than catalytic pathway steps.
- Falcon generic and PSEPK-specific module research were already completed for
  the `ppu00760` NAD/nicotinate checkpoint and are reused here rather than rerun
  as a duplicate provider job.
