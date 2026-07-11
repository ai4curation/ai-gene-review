---
title: "PSEPK ppu00040 Pentose and glucuronate interconversions batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00040: Pentose and glucuronate interconversions

- Module seed: `pentose_glucuronate_interconversions`
- Candidate genes from membership table: 8
- Primary bucket genes: 8
- Existing review files: 8
- Curated review files: 8
- Existing Asta research files: 8

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
| [x] | `rpe` | PP_0415 | Q88QS3 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | Ribulose-phosphate 3-epimerase (EC 5.1.3.1) |
| [x] | `PP_1256` | PP_1256 | Q88NF5 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) |
| [x] | `PP_2037` | PP_2037 | Q88L98 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | Aldolase |
| [x] | `PP_2585` | PP_2585 | Q88JR4 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) |
| [x] | `PP_2694` | PP_2694 | Q88JF5 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | Aldehyde dehydrogenase family protein |
| [x] | `udg` | PP_2926 | Q88IS3 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | UDP-glucose 6-dehydrogenase (EC 1.1.1.22) |
| [x] | `PP_3602` | PP_3602 | Q88GW5 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | 2,5-dioxovalerate dehydrogenase (EC 1.2.1.26) |
| [x] | `galU` | PP_3821 | Q88GA4 | kegg:ppu00040 | PRESENT | CURATED | PRESENT | UTP--glucose-1-phosphate uridylyltransferase (EC 2.7.7.9) (UDP-glucose pyrophosphorylase) |

## Promoted Gap-Fill Genes

These genes are absent from the eight-gene KEGG membership batch but were
promoted by the PSEPK Falcon pathway report as stronger oxidative-hexuronate
arm candidates than several KEGG side nodes.

| Done | Gene | Locus | UniProt | Source | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|
| [x] | `gnl` | PP_1170 | Q88NN7 | Falcon gap-fill | CURATED | PRESENT | SMP-30/Gluconolactonase/LRE-like candidate lactonase |
| [x] | `udh` | PP_1171 | Q88NN6 | Falcon gap-fill | CURATED | PRESENT | Uronate dehydrogenase (EC 1.1.1.203) |

## Notes

Generated UTC: 2026-07-07T02:43:13.021889+00:00
