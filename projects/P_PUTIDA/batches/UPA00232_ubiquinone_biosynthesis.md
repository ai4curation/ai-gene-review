---
title: "PSEPK UPA00232 ubiquinone biosynthesis support batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00232: ubiquinone biosynthesis support

- Module seed: `ubiquinone_biosynthesis`
- Candidate genes from membership table: 11
- Primary bucket genes: 3
- Existing review files: 11
- Curated review files: 11
- Existing Asta research files: 11

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Reuse completed module-level Falcon deep research from the `ppu00130` ubiquinone biosynthesis checkpoint.
- [x] Reuse completed module + pathway + PSEPK Falcon deep research from the `ppu00130` ubiquinone biosynthesis checkpoint; the report explicitly covers the UbiB/UbiJ/UbiK accessory context promoted through UniPathway UPA00232.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `coq7` | PP_0427 | Q88QR1 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | 3-demethoxyubiquinol 3-hydroxylase (DMQ hydroxylase) (EC 1.14.99.60) (2-nonaprenyl-3-methyl-6-methoxy-1,4-benzoquinol hy |
| [x] | `ubiG` | PP_1765 | Q88M10 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | Ubiquinone biosynthesis O-methyltransferase (2-polyprenyl-6-hydroxyphenol methylase) (EC 2.1.1.222) (3-demethylubiquinon |
| [x] | `ubiE` | PP_5011 | Q88D17 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | Ubiquinone/menaquinone biosynthesis C-methyltransferase UbiE (EC 2.1.1.163) (EC 2.1.1.201) (2-methoxy-6-polyprenyl-1,4-b |
| [x] | `ubiJ` | PP_5012 | Q88D16 | unipathway:UPA00232 | PRESENT | CURATED | PRESENT | Ubiquinone biosynthesis accessory factor UbiJ |
| [x] | `ubiB` | PP_5013 | A0A140FWS4 | unipathway:UPA00232 | PRESENT | CURATED | PRESENT | Probable protein kinase UbiB (EC 2.7.-.-) (Ubiquinone biosynthesis protein UbiB) |
| [x] | `visC` | PP_5197 | Q88CI4 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | Oxidoreductase involved in anerobic synthesis of ubiquinone, FAD/NAD(P)-binding domain |
| [x] | `ubiH` | PP_5199 | Q88CI2 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | 2-octaprenyl-6-methoxyphenyl hydroxylase |
| [x] | `ubiD` | PP_5213 | Q88CG8 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | 3-octaprenyl-4-hydroxybenzoate carboxy-lyase (EC 4.1.1.98) (Polyprenyl p-hydroxybenzoate decarboxylase) |
| [x] | `ubiK` | PP_5235 | Q88CE6 | unipathway:UPA00232 | PRESENT | CURATED | PRESENT | Ubiquinone biosynthesis accessory factor UbiK |
| [x] | `ubiC` | PP_5317 | Q88C66 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | Probable chorismate pyruvate-lyase (CL) (CPL) (EC 4.1.3.40) |
| [x] | `ubiA` | PP_5318 | Q88C65 | kegg:ppu00130 | PRESENT | CURATED | PRESENT | 4-hydroxybenzoate octaprenyltransferase (EC 2.5.1.39) (4-HB polyprenyltransferase) |

## Notes

Generated UTC: 2026-07-10T00:30:31.541439+00:00

2026-07-09 PDT:

- Completed the UPA00232 support-bucket registration for the existing `ubiquinone_biosynthesis` module.
- All 11 UniPathway UPA00232 members already have curated review YAMLs and Asta reports.
- The strict module was already created during `ppu00130`; this support batch documents the full UniPathway cross-reference, including the three UniPathway-primary accessory genes `ubiJ`, `ubiB`, and `ubiK`.
- Falcon generic and PSEPK-specific module research were already completed for the `ppu00130` ubiquinone checkpoint and are reused here rather than rerun as a duplicate provider job.
