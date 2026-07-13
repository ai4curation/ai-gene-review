---
title: "PSEPK ppu00410 beta-Alanine metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00410: beta-Alanine metabolism

- Module seed: `beta_alanine_metabolism_boundary`
- Candidate genes from membership table: 15
- Primary bucket genes: 10
- Existing review files: 15
- Curated review files: 15
- Existing Asta research files: 15

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
| [x] | `PP_0596` | PP_0596 | Q88Q98 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | Omega-amino acid--pyruvate aminotransferase (EC 2.6.1.18) |
| [x] | `mmsA-I` | PP_0597 | Q88Q97 | kegg:ppu00562 | PRESENT | CURATED | PRESENT | methylmalonate-semialdehyde dehydrogenase (CoA acylating) (EC 1.2.1.27) |
| [x] | `PP_0614` | PP_0614 | Q88Q81 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 1 (EC 3.5.1.6, EC 3.5.3.9) |
| [x] | `patD` | PP_1481 | Q88MT7 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | Medium chain aldehyde dehydrogenase (EC 1.2.1.19, EC 1.2.1.54) |
| [x] | `fadB` | PP_2136 | Q88L02 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Fatty acid oxidation complex subunit alpha [Includes: Enoyl-CoA hydratase/Delta(3)-cis-Delta(2)-trans-enoyl-CoA isomeras |
| [x] | `acd` | PP_2216 | Q88KS3 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | 3-sulfinopropanoyl-CoA desulfinase (EC 1.3.8.11) (EC 3.13.1.4) (3-sulfinopropionyl coenzyme A desulfinase) (Cyclohexane- |
| [x] | `PP_2217` | PP_2217 | Q88KS2 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | enoyl-CoA hydratase (EC 4.2.1.17) |
| [x] | `prr` | PP_2801 | Q88J48 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | Gamma-aminobutyraldehyde dehydrogenase (EC 1.2.1.19) |
| [x] | `paaF` | PP_3284 | Q88HR9 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) |
| [x] | `hyuC` | PP_4034 | Q88FQ3 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | N-carbamoyl-beta-alanine amidohydrolase/allantoine amidohydrolase 2 (EC 3.5.1.6, EC 3.5.3.9) |
| [x] | `pydB` | PP_4036 | A0A140FWK2 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | D-hydantoinase/dihydropyrimidinase (EC 3.5.2.2) |
| [x] | `pydX` | PP_4037 | Q88FQ1 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) |
| [x] | `pydA` | PP_4038 | Q88FQ0 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | dihydrouracil dehydrogenase (NAD(+)) (EC 1.3.1.1) (Dihydrothymine dehydrogenase) (Dihydrouracil dehydrogenase) |
| [x] | `mmsA-II` | PP_4667 | Q88E01 | kegg:ppu00562 | PRESENT | CURATED | PRESENT | methylmalonate-semialdehyde dehydrogenase (CoA acylating) (EC 1.2.1.27) |
| [x] | `panC` | PP_4700 | Q88DW8 | kegg:ppu00410 | PRESENT | CURATED | PRESENT | Pantothenate synthetase (PS) (EC 6.3.2.1) (Pantoate--beta-alanine ligase) (Pantoate-activating enzyme) |

## Notes

Generated UTC: 2026-07-07T22:04:21.730537+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon beta_alanine_metabolism_boundary`
  and `just module-pathway-deep-research-falcon beta_alanine_metabolism_boundary ppu00410 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/beta_alanine_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__beta_alanine_metabolism_boundary__ppu00410-deep-research-falcon.md`.
