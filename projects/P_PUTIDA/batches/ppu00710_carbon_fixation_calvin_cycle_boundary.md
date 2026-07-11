---
title: "PSEPK ppu00710 Carbon fixation by Calvin cycle batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00710: Carbon fixation by Calvin cycle

- Module seed: `carbon_fixation_calvin_cycle_boundary`
- Candidate genes from membership table: 13
- Primary bucket genes: 10
- Existing review files: 13
- Curated review files: 13
- Existing Asta research files: 13

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted on 2026-07-11; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted on 2026-07-11; blocked by Edison HTTP 402 before report generation.
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
| [x] | `mdh` | PP_0654 | Q88Q44 | kegg:ppu00566 | PRESENT | CURATED | PRESENT | Probable malate dehydrogenase (EC 1.1.1.37) |
| [x] | `gapA` | PP_1009 | Q88P44 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Glyceraldehyde-3-phosphate dehydrogenase (EC 1.2.1.-) |
| [x] | `ppc` | PP_1505 | Q88MR4 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Phosphoenolpyruvate carboxylase (PEPC) (PEPCase) (EC 4.1.1.31) |
| [x] | `gapB` | PP_2149 | Q88KZ0 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Glyceraldehyde-3-phosphate dehydrogenase (EC 1.2.1.-) |
| [x] | `tal` | PP_2168 | Q88KX1 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Transaldolase (EC 2.2.1.2) |
| [x] | `tpiA` | PP_4715 | Q88DV4 | kegg:ppu00562 | PRESENT | CURATED | PRESENT | Triosephosphate isomerase (TIM) (TPI) (EC 5.3.1.1) (Triose-phosphate isomerase) |
| [x] | `fba` | PP_4960 | Q88D67 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Fructose-1,6-bisphosphate aldolase (FBP aldolase) (EC 4.1.2.13) |
| [x] | `pgk` | PP_4963 | Q88D64 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Phosphoglycerate kinase (EC 2.7.2.3) |
| [x] | `tktA` | PP_4965 | Q88D62 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Transketolase (EC 2.2.1.1) |
| [x] | `fbp` | PP_5040 | Q88CY9 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Fructose-1,6-bisphosphatase class 1 (FBPase class 1) (EC 3.1.3.11) (D-fructose-1,6-bisphosphate 1-phosphohydrolase class |
| [x] | `maeB` | PP_5085 | Q88CU5 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | NADP-dependent malic enzyme (EC 1.1.1.40) |
| [x] | `rpiA` | PP_5150 | Q88CN0 | kegg:ppu00710 | PRESENT | CURATED | PRESENT | Ribose-5-phosphate isomerase A (EC 5.3.1.6) (Phosphoriboisomerase A) (PRI) |

## Notes

Generated UTC: 2026-07-08T14:42:26.761964+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon carbon_fixation_calvin_cycle_boundary`
  and `just module-pathway-deep-research-falcon carbon_fixation_calvin_cycle_boundary ppu00710 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/carbon_fixation_calvin_cycle_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__carbon_fixation_calvin_cycle_boundary__ppu00710-deep-research-falcon.md`.
