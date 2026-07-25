---
title: "PSEPK ppu00440 Phosphonate and phosphinate metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00440: Phosphonate and phosphinate metabolism

- Module seed: `phosphonoacetaldehyde_degradation`
- Candidate genes from membership table: 2
- Primary bucket genes: 2
- Existing review files: 1
- Curated review files: 1
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
| [x] | `phnX` | PP_2208 | Q88KT1 | kegg:ppu00440 | PRESENT | CURATED | FAILED_TIMEOUT | Phosphonoacetaldehyde hydrolase (Phosphonatase) (EC 3.11.1.1) (Phosphonoacetaldehyde phosphonohydrolase) |
| [x] | `phnW` | PP_2209 | Q88KT0 | kegg:ppu00440 | PRESENT | CURATED | FAILED_TIMEOUT | 2-aminoethylphosphonate--pyruvate transaminase (EC 2.6.1.37) (2-aminoethylphosphonate aminotransferase) (AEP transaminas |

## Notes

Generated UTC: 2026-07-16T17:37:22.048250+00:00

2026-07-16: OpenScientist timed out after 7200s for `phnX` and `phnW`; no gene-level report files were produced for those runs.
