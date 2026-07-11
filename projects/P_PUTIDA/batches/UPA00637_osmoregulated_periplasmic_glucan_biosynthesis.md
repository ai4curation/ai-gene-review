---
title: "PSEPK UPA00637 osmoregulated periplasmic glucan biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00637: Osmoregulated Periplasmic Glucan Biosynthesis

- Module seed: `osmoregulated_periplasmic_glucan_biosynthesis`
- Candidate genes from membership table: 2
- Primary bucket genes: 2
- Existing review files: 2
- Curated review files: 2
- Existing OpenScientist research files: 4

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

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | OpenScientist research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `opgH` | PP_5025 | Q88D04 | unipathway:UPA00637 | PRESENT | DONE | PRESENT | Glucans biosynthesis glucosyltransferase H (EC 2.4.1.-) |
| [x] | `opgG` | PP_5026 | Q88D03 | unipathway:UPA00637 | PRESENT | DONE | PRESENT | Glucans biosynthesis protein G |

## Notes

Curated scope: treat UPA00637 as the compact OpgH/OpgG osmoregulated periplasmic glucan backbone module. OpgH supplies UDP-glucose-dependent inner-membrane glucosyltransferase activity; OpgG is curated as a Sec-exported periplasmic GH186 beta-1,2-glucanase inferred from characterized orthologs. Generic carbohydrate/glucan GO process terms are modified to the specific OPG biosynthesis term where supported. Accessory OPG decoration, chain-length-control, Ndv/Chv cyclic-glucan routes, and the distinct BcsA-like cyclic beta-1,3-glucan system are kept outside this module.

Generated UTC: 2026-07-11T22:11:45.660422+00:00
