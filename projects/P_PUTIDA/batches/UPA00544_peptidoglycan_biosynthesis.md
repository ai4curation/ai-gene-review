---
title: "PSEPK UPA00544 UniPathway UPA00544 batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK UPA00544: UniPathway UPA00544

- Module seed: `peptidoglycan_biosynthesis`
- Candidate genes from membership table: 6
- Primary bucket genes: 1
- Existing review files: 6
- Curated review files: 6
- Existing Asta research files: 6

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `amgK` | PP_0405 | Q88QT3 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | N-acetylmuramate/N-acetylglucosamine kinase (MurNAc/GlcNAc kinase) (EC 2.7.1.221) (Anomeric sugar kinase) |
| [x] | `murU` | PP_0406 | Q88QT2 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | N-acetylmuramate alpha-1-phosphate uridylyltransferase (MurNAc-1P uridylyltransferase) (MurNAc-alpha-1P uridylyltransfer |
| [x] | `anmK` | PP_0434 | Q88QQ4 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | Anhydro-N-acetylmuramic acid kinase (EC 2.7.1.170) (AnhMurNAc kinase) |
| [x] | `mpl` | PP_0547 | Q88QE7 | unipathway:UPA00544 | PRESENT | CURATED | PRESENT | UDP-N-acetylmuramate--L-alanyl-gamma-D-glutamyl-meso-2,6-diaminoheptandioate ligase (EC 6.3.2.45) (Murein peptide ligase |
| [x] | `mupP` | PP_1764 | Q88M11 | kegg:ppu00520 | PRESENT | CURATED | PRESENT | N-acetylmuramic acid 6-phosphate phosphatase (MurNAc 6-phosphate phosphatase) (MurNAc-6P phosphatase) (EC 3.1.3.105) |
| [x] | `nagZ` | PP_2145 | Q88KZ4 | kegg:ppu01501 | PRESENT | CURATED | PRESENT | Beta-hexosaminidase (EC 3.2.1.52) (Beta-N-acetylhexosaminidase) (N-acetyl-beta-glucosaminidase) |

## Notes

Generated UTC: 2026-07-10T02:08:03.133850+00:00

Completed first-pass curation for UPA00544 on 2026-07-09 PDT. The missing
UniPathway-primary member `mpl` was fetched by accession alias Q88QE7, Asta was
run, and `genes/PSEPK/mpl/mpl-ai-review.yaml` was curated and validated. The
other five members (`amgK`, `murU`, `anmK`, `mupP`, `nagZ`) were reused from
existing curated reviews.

`modules/peptidoglycan_biosynthesis.yaml` now includes UniPathway UPA00544 as a
peptidoglycan recycling/salvage support view. The new module part separates
NagZ/AnmK/MupP/AmgK/MurU/Mpl recycling and salvage from de novo MurA/MurB/MurC-F
precursor synthesis while keeping both arms inside the peptidoglycan module.

Both real Falcon commands were attempted and failed before report generation
with Edison HTTP 402 Payment Required. The queued report paths are:

- `modules/peptidoglycan_biosynthesis-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__peptidoglycan_biosynthesis__upa00544-deep-research-falcon.md`

The taxon-aware Falcon command resolved the expected six-gene candidate set:
`amgK`, `murU`, `anmK`, `mpl`, `mupP`, and `nagZ`.
