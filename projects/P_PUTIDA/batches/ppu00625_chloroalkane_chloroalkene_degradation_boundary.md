---
title: "PSEPK ppu00625 Chloroalkane and chloroalkene degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00625: Chloroalkane and chloroalkene degradation

- Module seed: `chloroalkane_chloroalkene_degradation_boundary`
- Candidate genes from membership table: 5
- Primary bucket genes: 3
- Existing review files: 5
- Curated review files: 5
- Existing Asta research files: 5

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
| [x] | `fdhA` | PP_0328 | Q88R06 | kegg:ppu00625 | PRESENT | CURATED | PRESENT | Formaldehyde dehydrogenase (EC 1.2.1.46) |
| [x] | `frmA` | PP_1616 | Q88MF5 | kegg:ppu00626 | PRESENT | CURATED | PRESENT | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrog |
| [x] | `pedE` | PP_2674 | Q88JH5 | kegg:ppu00625 | PRESENT | CURATED | PRESENT | Quinoprotein alcohol dehydrogenase PedE (EC 1.1.2.8) (Ca(2+)-dependent pyrroloquinoline quinone-dependent alcohol dehydr |
| [x] | `pedH` | PP_2679 | Q88JH0 | kegg:ppu00625 | PRESENT | CURATED | PRESENT | Quinoprotein alcohol dehydrogenase PedH (EC 1.1.2.-) (Lanthanide-dependent pyrroloquinoline quinone-dependent alcohol de |
| [x] | `adhP` | PP_3839 | Q88G86 | kegg:ppu00626 | PRESENT | CURATED | PRESENT | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) |

## Notes

Generated UTC: 2026-07-08T12:14:36.398054+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon chloroalkane_chloroalkene_degradation_boundary`
  and `just module-pathway-deep-research-falcon chloroalkane_chloroalkene_degradation_boundary ppu00625 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/chloroalkane_chloroalkene_degradation_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__chloroalkane_chloroalkene_degradation_boundary__ppu00625-deep-research-falcon.md`.
