---
title: "PSEPK ppu01320 Sulfur cycle batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu01320: Sulfur cycle

- Module seed: `sulfur_metabolism_boundary`
- Candidate genes from membership table: 9
- Primary bucket genes: 7
- Existing review files: 9
- Curated review files: 9
- Existing Asta research files: 9

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
| [x] | `PP_0860` | PP_0860 | Q88PJ0 | kegg:ppu01320 | PRESENT | CURATED | PRESENT | Sulfite reductase, flavoprotein component |
| [x] | `cysD` | PP_1303 | Q88NA9 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Sulfate adenylyltransferase subunit 2 (EC 2.7.7.4) (ATP-sulfurylase small subunit) (Sulfate adenylate transferase) (SAT) |
| [x] | `cysNC` | PP_1304 | Q88NA8 | kegg:ppu00261 | PRESENT | CURATED | PRESENT | Sulfate adenylyltransferase subunit 1 (EC 2.7.7.4) (ATP-sulfurylase large subunit) (Sulfate adenylate transferase) (SAT) |
| [x] | `PP_1703` | PP_1703 | Q88M71 | kegg:ppu01320 | PRESENT | CURATED | PRESENT | Assimilatory nitrate reductase/sulfite reductase (EC 1.7.99.4) |
| [x] | `cysH` | PP_2328 | Q88KG2 | kegg:ppu01320 | PRESENT | CURATED | PRESENT | Adenosine 5'-phosphosulfate reductase (APS reductase) (EC 1.8.4.10) (5'-adenylylsulfate reductase) (Thioredoxin-dependen |
| [x] | `cysI` | PP_2371 | Q88KB9 | kegg:ppu01320 | PRESENT | CURATED | PRESENT | Sulphite reductase hemoprotein, beta subunit |
| [x] | `PP_2677` | PP_2677 | Q88JH2 | kegg:ppu01320 | PRESENT | CURATED | PRESENT | Quinoprotein dehydrogenase-associated SoxYZ-like carrier |
| [x] | `PP_3822` | PP_3822 | Q88GA3 | kegg:ppu01320 | PRESENT | CURATED | PRESENT | Cytochrome c family protein |
| [x] | `cysK` | PP_4571 | Q88E95 | kegg:ppu01320 | PRESENT | CURATED | PRESENT | Cysteine synthase (EC 2.5.1.47) |

## Notes

Generated UTC: 2026-07-08T18:45:43.289648+00:00

2026-07-11 PDT status sync: `modules/sulfur_metabolism_boundary.yaml` is curated and validates with both module validators. The ppu01320 batch is the sulfur-cycle subset of the shared sulfur boundary module, covering sulfate activation/reduction, sulfite-reductase components, SoxYZ-like/cytochrome redox side nodes, and cysteine-synthesis chemistry rather than a separate monolithic sulfur-cycle route.

Gene validation passed for all nine batch members (`PP_0860`, `cysD`, `cysNC`, `PP_1703`, `cysH`, `cysI`, `PP_2677`, `PP_3822`, `cysK`) with no warnings.

Real Falcon commands were run:

```bash
just module-deep-research-falcon sulfur_metabolism_boundary
just module-pathway-deep-research-falcon sulfur_metabolism_boundary ppu01320 PSEPK
```

Both failed at Edison task creation with HTTP 402 Payment Required, so no Falcon reports were written. Expected output paths remain:

- `modules/sulfur_metabolism_boundary-deep-research-falcon.md`
- `projects/P_PUTIDA/deep-research/PSEPK__sulfur_metabolism_boundary__ppu01320-deep-research-falcon.md`
