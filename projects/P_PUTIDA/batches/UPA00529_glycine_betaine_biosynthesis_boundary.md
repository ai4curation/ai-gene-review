---
title: "PSEPK UPA00529 UniPathway UPA00529 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00529: UniPathway UPA00529

- Module seed: `glycine_betaine_biosynthesis_boundary`
- Candidate genes from membership table: 3
- Primary bucket genes: 1
- Existing review files: 3
- Curated review files: 3
- Existing Asta research files: 3

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research. Attempted; blocked by Edison HTTP 402 before report generation.
- [x] Run module + pathway + PSEPK Falcon deep research. Attempted; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `betB` | PP_5063 | Q88CW7 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Betaine aldehyde dehydrogenase (BADH) (EC 1.2.1.8) |
| [x] | `betA` | PP_5064 | Q88CW6 | kegg:ppu00670 | PRESENT | CURATED | PRESENT | Oxygen-dependent choline dehydrogenase (CDH) (CHD) (EC 1.1.99.1) (Betaine aldehyde dehydrogenase) (BADH) (EC 1.2.1.8) |
| [x] | `betI` | PP_5719 | A0A140FWS5 | unipathway:UPA00529 | PRESENT | CURATED | PRESENT | HTH-type transcriptional regulator BetI |

## Notes

Generated UTC: 2026-07-09T23:32:21.964577+00:00

2026-07-09: Created and validated
`modules/glycine_betaine_biosynthesis_boundary.yaml`. `betA` and `betB` are
the catalytic choline-derived glycine betaine route; `betI` is retained as a
regulatory boundary component for bet gene transcription. Both Falcon commands
were run for real and failed at Edison task creation with HTTP 402 Payment
Required, so no generic module or PSEPK-specific Falcon report file was
created. The taxon-aware wrapper was fixed so UniPathway buckets prefer full
pathway-membership rows; the corrected UPA00529 prompt includes all three
members (`betA`, `betB`, `betI`).
