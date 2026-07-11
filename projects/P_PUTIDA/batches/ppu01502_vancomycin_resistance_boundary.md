---
title: "PSEPK ppu01502 Vancomycin resistance batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu01502: Vancomycin resistance

- Module seed: `vancomycin_resistance_boundary`
- Candidate genes from membership table: 6
- Primary bucket genes: 6
- Existing review files: 6
- Curated review files: 6
- Existing Asta research files: 6

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
| [x] | `murF` | PP_1333 | Q88N80 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | UDP-N-acetylmuramoyl-tripeptide--D-alanyl-D-alanine ligase (EC 6.3.2.10) (D-alanyl-D-alanine-adding enzyme) |
| [x] | `mraY` | PP_1334 | Q88N79 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | Phospho-N-acetylmuramoyl-pentapeptide-transferase (EC 2.7.8.13) (UDP-MurNAc-pentapeptide phosphotransferase) |
| [x] | `murG` | PP_1337 | Q88N76 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | UDP-N-acetylglucosamine--N-acetylmuramyl-(pentapeptide) pyrophosphoryl-undecaprenol N-acetylglucosamine transferase (EC  |
| [x] | `ddlB` | PP_1339 | Q88N74 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | D-alanine--D-alanine ligase B (EC 6.3.2.4) (D-Ala-D-Ala ligase B) (D-alanylalanine synthetase B) |
| [x] | `ddlA` | PP_4346 | Q88EV6 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | D-alanine--D-alanine ligase A (EC 6.3.2.4) (D-Ala-D-Ala ligase A) (D-alanylalanine synthetase A) |
| [x] | `dadX` | PP_5269 | Q88CB2 | kegg:ppu01502 | PRESENT | CURATED | PRESENT | Alanine racemase, catabolic (EC 5.1.1.1) |

## Notes

Generated UTC: 2026-07-08T19:15:54.264646+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon vancomycin_resistance_boundary`
  and `just module-pathway-deep-research-falcon vancomycin_resistance_boundary ppu01502 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/vancomycin_resistance_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__vancomycin_resistance_boundary__ppu01502-deep-research-falcon.md`.
