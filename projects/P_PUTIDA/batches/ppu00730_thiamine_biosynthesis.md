---
title: "PSEPK ppu00730 Thiamine metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00730: Thiamine metabolism

- Module seed: `thiamine_biosynthesis`
- Candidate genes from membership table: 13
- Primary bucket genes: 13
- Existing review files: 13
- Curated review files: 13
- Existing Asta research files: 13

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
| [x] | `thiL` | PP_0519 | Q88QH4 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Thiamine-monophosphate kinase (TMP kinase) (Thiamine-phosphate kinase) (EC 2.7.4.16) |
| [x] | `dxs` | PP_0527 | Q88QG7 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | 1-deoxy-D-xylulose-5-phosphate synthase (EC 2.2.1.7) (1-deoxyxylulose-5-phosphate synthase) (DXP synthase) (DXPS) |
| [x] | `thiO` | PP_0612 | Q88Q83 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Glycine oxidase (GO) (EC 1.4.3.19) |
| [x] | `iscS` | PP_0842 | Q88PK8 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Cysteine desulfurase IscS (EC 2.8.1.7) |
| [x] | `adk` | PP_1506 | P0A136 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Adenylate kinase (AK) (EC 2.7.4.3) (ATP-AMP transphosphorylase) (ATP:AMP phosphotransferase) (Adenylate monophosphate ki |
| [x] | `iscS-II` | PP_2435 | Q88K56 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | cysteine desulfurase (EC 2.8.1.7) |
| [x] | `PP_3186` | PP_3186 | Q88I16 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Aminopyrimidine aminohydrolase (EC 3.5.99.2) |
| [x] | `thiD` | PP_4782 | Q88DP2 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | hydroxymethylpyrimidine kinase (EC 2.7.1.49) |
| [x] | `thiE` | PP_4783 | Q88DP1 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Thiamine-phosphate synthase (TP synthase) (TPS) (EC 2.5.1.3) (Thiamine-phosphate pyrophosphorylase) (TMP pyrophosphoryla |
| [x] | `rsgA` | PP_4903 | Q88DC4 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Small ribosomal subunit biogenesis GTPase RsgA (EC 3.6.1.-) |
| [x] | `thiC` | PP_4922 | Q88DA5 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Phosphomethylpyrimidine synthase (EC 4.1.99.17) (Hydroxymethylpyrimidine phosphate synthase) (HMP-P synthase) (HMP-phosp |
| [x] | `thiI` | PP_5045 | Q88CY4 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | tRNA sulfurtransferase (EC 2.8.1.4) (Sulfur carrier protein ThiS sulfurtransferase) (Thiamine biosynthesis protein ThiI) |
| [x] | `thiG` | PP_5104 | Q88CS6 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | Thiazole synthase (EC 2.8.1.10) |

## Promoted Context Genes

| Done | Gene | Locus | UniProt | Basis | Review | Notes |
|---|---|---|---|---|---|---|
| [x] | `pet` | PP_3185 | Q88I17 | UniPathway UPA00060 / TenA-family salvage context | CURATED | Neighbor of PP_3186; aminopyrimidine aminohydrolase/thiamine salvage rather than de novo core. |
| [x] | `PP_5105` | PP_5105 | Q88CS5 | Falcon/module gap-fill plus local UniProt ThiS family metadata | CURATED | ThiS sulfur carrier promoted into the module; absent from KEGG ppu00730 membership. |

## Notes

Generated UTC: 2026-07-07T09:30:40.824179+00:00

Manual update 2026-07-07 PDT:

- Created and validated `modules/thiamine_biosynthesis.yaml`.
- Falcon generic module report:
  `modules/thiamine_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway report:
  `projects/P_PUTIDA/deep-research/PSEPK__thiamine_biosynthesis__ppu00730-deep-research-falcon.md`.
- Curated and validated all 13 KEGG candidate gene reviews plus promoted context
  genes `pet` and `PP_5105`.
- Main module decision: strict de novo thiamine diphosphate biosynthesis is
  covered by `dxs`, `thiC`, `thiD`, `thiO`, `thiG`, `thiE`, and `thiL`; `iscS`
  and `thiI` are shared sulfur-relay support; `PP_3186`/`pet` are salvage; `adk`
  and `rsgA` are KEGG side nodes, not thiamine-specific enzymes.
- Falcon flagged ThiF as an expected sulfur-relay component. Local PSEPK metadata
  has no unambiguous `thiF` product or symbol; `PP_5105` is the local ThiS
  candidate, while PP_0735/`moeB` was not promoted to ThiF without additional
  evidence.
