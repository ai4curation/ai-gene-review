---
title: "PSEPK UPA00028 UniPathway UPA00028 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00028: UniPathway UPA00028

- Module seed: `pantothenate_and_coa_biosynthesis`
- Candidate genes from membership table: 6
- Primary bucket genes: 0
- Existing review files: 6
- Curated review files: 6
- Existing Asta research files: 6

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
| [x] | `panE` | PP_1351 | Q88N64 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) |
| [x] | `PP_2325` | PP_2325 | Q88KG5 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) |
| [x] | `PP_2998` | PP_2998 | Q88IK1 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) |
| [x] | `PP_4452` | PP_4452 | Q88EL0 | unipathway:UPA00028 | PRESENT | CURATED | PRESENT | 2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) |
| [x] | `panB` | PP_4699 | Q88DW9 | kegg:ppu00770 | PRESENT | CURATED | PRESENT | 3-methyl-2-oxobutanoate hydroxymethyltransferase (EC 2.1.2.11) (Ketopantoate hydroxymethyltransferase) (KPHMT) |
| [x] | `panC` | PP_4700 | Q88DW8 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | Pantothenate synthetase (PS) (EC 6.3.2.1) (Pantoate--beta-alanine ligase) (Pantoate-activating enzyme) |

## Notes

- Covered by the `pantothenate_and_coa_biosynthesis` module and the PSEPK
  `ppu00770` Falcon module+pathway report. PP_4452 is the UniPathway-only
  candidate added to the KEGG ppu00770 gene set.

Generated UTC: 2026-07-07T12:18:09.533215+00:00
