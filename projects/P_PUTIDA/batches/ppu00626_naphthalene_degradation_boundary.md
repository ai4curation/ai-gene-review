---
title: "PSEPK ppu00626 Naphthalene degradation batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00626: Naphthalene degradation

- Module seed: `naphthalene_degradation_boundary`
- Candidate genes from membership table: 2
- Primary bucket genes: 2
- Existing review files: 2
- Curated review files: 2
- Existing Asta research files: 2

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
| [x] | `frmA` | PP_1616 | Q88MF5 | kegg:ppu00626 | PRESENT | CURATED | PRESENT | S-(hydroxymethyl)glutathione dehydrogenase (EC 1.1.1.1) (EC 1.1.1.284) (Alcohol dehydrogenase class-3) (Alcohol dehydrog |
| [x] | `adhP` | PP_3839 | Q88G86 | kegg:ppu00626 | PRESENT | CURATED | PRESENT | Short-chain alcohol dehydrogenase (EC 1.1.1.-, EC 1.1.1.1) |

## Notes

Generated UTC: 2026-07-08T12:19:42.724813+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon naphthalene_degradation_boundary`
  and `just module-pathway-deep-research-falcon naphthalene_degradation_boundary ppu00626 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/naphthalene_degradation_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__naphthalene_degradation_boundary__ppu00626-deep-research-falcon.md`.
