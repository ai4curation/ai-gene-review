---
title: "PSEPK ppu00622 Xylene degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00622: Xylene degradation

- Module seed: `benzoate_upper_pathway`
- Candidate genes from membership table: 6
- Primary bucket genes: 4
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
| [x] | `PP_1791` | PP_1791 | Q88LY5 | kegg:ppu00621 | PRESENT | CURATED | PRESENT | Aldolase/synthase |
| [x] | `PP_2504` | PP_2504 | Q88JY9 | kegg:ppu00621 | PRESENT | CURATED | PRESENT | 2-hydroxymuconate tautomerase (EC 5.3.2.6) (4-oxalocrotonate tautomerase) |
| [x] | `benA` | PP_3161 | Q88I40 | kegg:ppu00622 | PRESENT | CURATED | PRESENT | Benzoate 1,2-dioxygenase subunit alpha (EC 1.14.12.10) |
| [x] | `benB` | PP_3162 | Q88I39 | kegg:ppu00622 | PRESENT | CURATED | PRESENT | Benzoate 1,2-dioxygenase subunit beta (EC 1.14.12.10) |
| [x] | `benC` | PP_3163 | Q88I38 | kegg:ppu00622 | PRESENT | CURATED | PRESENT | Benzoate 1,2-dioxygenase electron transfer component (EC 1.14.12.10, EC 1.18.1.3) |
| [x] | `benD` | PP_3164 | Q88I37 | kegg:ppu00622 | PRESENT | CURATED | PRESENT | 1,6-dihydroxycyclohexa-2,4-diene-1-carboxylate dehydrogenase (EC 1.3.1.25) |

## Notes

Generated UTC: 2026-07-06T22:36:20.775793+00:00
