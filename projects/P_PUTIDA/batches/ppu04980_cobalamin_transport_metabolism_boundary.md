---
title: "PSEPK ppu04980 Cobalamin transport and metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu04980: Cobalamin transport and metabolism

- Module seed: `cobalamin_transport_metabolism_boundary`
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
| [x] | `pduO` | PP_1349 | Q88N66 | kegg:ppu04980 | PRESENT | CURATED | PRESENT | Corrinoid adenosyltransferase (EC 2.5.1.17) (Cob(II)alamin adenosyltransferase) (Cob(II)yrinic acid a,c-diamide adenosyl |
| [x] | `metH` | PP_2375 | Q88KB5 | kegg:ppu04980 | PRESENT | CURATED | PRESENT | Methionine synthase (EC 2.1.1.13) (5-methyltetrahydrofolate--homocysteine methyltransferase) |

## Notes

Generated UTC: 2026-07-09T06:49:30.507917+00:00

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon cobalamin_transport_metabolism_boundary`
  and `just module-pathway-deep-research-falcon cobalamin_transport_metabolism_boundary ppu04980 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so the
  Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected output
  paths remain `modules/cobalamin_transport_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__cobalamin_transport_metabolism_boundary__ppu04980-deep-research-falcon.md`.
