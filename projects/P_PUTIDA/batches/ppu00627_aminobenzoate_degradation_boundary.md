---
title: "PSEPK ppu00627 Aminobenzoate degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00627: Aminobenzoate degradation

- Module seed: `aminobenzoate_degradation_boundary`
- Candidate genes from membership table: 12
- Primary bucket genes: 8
- Existing review files: 12
- Curated review files: 12
- Existing Asta research files: 12

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
| [x] | `ubiX` | PP_0548 | Q88QE6 | kegg:ppu00627 | PRESENT | CURATED | PRESENT | Flavin prenyltransferase UbiX (EC 2.5.1.129) |
| [x] | `PP_2217` | PP_2217 | Q88KS2 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | enoyl-CoA hydratase (EC 4.2.1.17) |
| [x] | `galA` | PP_2518 | Q88JX5 | kegg:ppu00627 | PRESENT | CURATED | PRESENT | Gallate dioxygenase (EC 1.13.11.57) (Gallate degradation protein A) |
| [x] | `PP_2805` | PP_2805 | Q88J44 | kegg:ppu00627 | PRESENT | CURATED | PRESENT | Baeyer-Villiger monooxygenase (BVMO) (EC 1.14.13.-) |
| [x] | `PP_2932` | PP_2932 | Q88IR7 | kegg:ppu00643 | PRESENT | CURATED | PRESENT | Amidase family protein |
| [x] | `paaF` | PP_3284 | Q88HR9 | kegg:ppu00930 | PRESENT | CURATED | PRESENT | Enoyl-CoA hydratase-isomerase (EC 4.2.1.17) |
| [x] | `fcs` | PP_3356 | Q88HK0 | kegg:ppu00627 | PRESENT | CURATED | PRESENT | Feruloyl-CoA-synthetase (EC 6.2.1.34) |
| [x] | `vdh` | PP_3357 | Q88HJ9 | kegg:ppu00627 | PRESENT | CURATED | PRESENT | Vanillin dehydrogenase (EC 1.2.1.67) |
| [x] | `PP_3358` | PP_3358 | Q88HJ8 | kegg:ppu00996 | PRESENT | CURATED | PRESENT | Hydroxycinnamoyl-CoA hydratase-lyase (EC 4.1.2.41, EC 4.2.1.101) |
| [x] | `PP_3657` | PP_3657 | Q88GR1 | kegg:ppu00627 | PRESENT | CURATED | PRESENT | p-nitrobenzoate reductase NfnB |
| [x] | `vanA` | PP_3736 | Q88GI6 | kegg:ppu00627 | PRESENT | CURATED | PRESENT | Vanillate O-demethylase oxygenase subunit (EC 1.14.13.82) |
| [x] | `vanB` | PP_3737 | Q88GI5 | kegg:ppu00627 | PRESENT | CURATED | PRESENT | Vanillate O-demethylase oxidoreductase (EC 1.14.13.-) |

## Notes

Generated UTC: 2026-07-08T12:31:00.697197+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon aminobenzoate_degradation_boundary`
  and `just module-pathway-deep-research-falcon aminobenzoate_degradation_boundary ppu00627 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/aminobenzoate_degradation_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__aminobenzoate_degradation_boundary__ppu00627-deep-research-falcon.md`.
