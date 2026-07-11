---
title: "PSEPK UPA00664 bacterial lipoprotein maturation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00664: bacterial lipoprotein maturation, Lgt step

- Module seed: `bacterial_lipoprotein_maturation`
- Candidate genes from membership table: 3
- Primary bucket genes: 1
- Existing review files: 3
- Curated review files: 3
- Existing Asta research files: 3

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Attempt module-level Falcon deep research; Edison returned HTTP 402 before creating a task, so no Falcon report file was produced.
- [x] Attempt module + pathway + PSEPK Falcon deep research for UPA00664; Edison returned HTTP 402 before creating a task, so no taxon/pathway Falcon report file was produced.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `lspA` | PP_0604 | Q88Q91 | kegg:ppu03060 | PRESENT | CURATED | PRESENT | Lipoprotein signal peptidase (EC 3.4.23.36) (Prolipoprotein signal peptidase) (Signal peptidase II) (SPase II) |
| [x] | `lnt` | PP_4790 | Q88DN4 | unipathway:UPA00666 | PRESENT | CURATED | PRESENT | Apolipoprotein N-acyltransferase (ALP N-acyltransferase) (EC 2.3.1.269) |
| [x] | `lgt` | PP_5142 | Q88CN8 | unipathway:UPA00664 | PRESENT | CURATED | PRESENT | Phosphatidylglycerol--prolipoprotein diacylglyceryl transferase (EC 2.5.1.145) |

## Notes

Generated UTC: 2026-07-10T00:23:58.750263+00:00

2026-07-09 PDT:

- Completed first-pass curation for `lgt` and reused already-curated `lspA` plus newly curated `lnt` as complete Lgt-LspA-Lnt lipoprotein maturation context.
- `lgt` is treated as the inner-membrane phosphatidylglycerol--prolipoprotein diacylglyceryl transferase first step.
- `lspA` is already curated in the `bacterial_protein_export` batch as signal peptidase II and is included here as middle-step context.
- `lnt` is treated as the inner-membrane apolipoprotein N-acyltransferase final step; its broad GOA acyltransferase term is modified to `GO:0016410` N-acyltransferase activity.
- Falcon module and UPA00664 taxon/pathway runs were attempted with the real commands and both failed immediately with Edison HTTP 402 Payment Required. No placeholder deep-research files were created.
