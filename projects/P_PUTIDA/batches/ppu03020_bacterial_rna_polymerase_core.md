---
title: "PSEPK ppu03020 RNA polymerase batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu03020: RNA polymerase

- Module seed: `bacterial_rna_polymerase_core`
- Candidate genes from membership table: 4
- Primary bucket genes: 4
- Existing review files: 4
- Curated review files: 4
- Existing Asta research files: 4

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
| [x] | `rpoB` | PP_0447 | Q88QP2 | kegg:ppu03020 | PRESENT | CURATED | PRESENT | DNA-directed RNA polymerase subunit beta (RNAP subunit beta) (EC 2.7.7.6) (RNA polymerase subunit beta) (Transcriptase s |
| [x] | `rpoC` | PP_0448 | Q88QP1 | kegg:ppu03020 | PRESENT | CURATED | PRESENT | DNA-directed RNA polymerase subunit beta' (RNAP subunit beta') (EC 2.7.7.6) (RNA polymerase subunit beta') (Transcriptas |
| [x] | `rpoA` | PP_0479 | Q88QL1 | kegg:ppu03020 | PRESENT | CURATED | PRESENT | DNA-directed RNA polymerase subunit alpha (RNAP subunit alpha) (EC 2.7.7.6) (RNA polymerase subunit alpha) (Transcriptas |
| [x] | `rpoZ` | PP_5301 | Q88C82 | kegg:ppu03020 | PRESENT | CURATED | PRESENT | DNA-directed RNA polymerase subunit omega (RNAP omega subunit) (EC 2.7.7.6) (RNA polymerase omega subunit) (Transcriptas |

## Notes

Generated UTC: 2026-07-09T06:29:03.732067+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon bacterial_rna_polymerase_core`
  and `just module-pathway-deep-research-falcon bacterial_rna_polymerase_core ppu03020 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/bacterial_rna_polymerase_core-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__bacterial_rna_polymerase_core__ppu03020-deep-research-falcon.md`.
