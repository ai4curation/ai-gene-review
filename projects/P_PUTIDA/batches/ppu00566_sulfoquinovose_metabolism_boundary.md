---
title: "PSEPK ppu00566 Sulfoquinovose metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00566: Sulfoquinovose metabolism

- Module seed: `sulfoquinovose_metabolism_boundary`
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
| [x] | `mdh` | PP_0654 | Q88Q44 | kegg:ppu00566 | PRESENT | CURATED | PRESENT | Probable malate dehydrogenase (EC 1.1.1.37) |
| [x] | `yihS` | PP_1014 | Q88P39 | kegg:ppu00566 | PRESENT | CURATED | PRESENT | Aldose-ketose isomerase (EC 5.3.1.7) |

## Notes

Generated UTC: 2026-07-08T11:29:04.413352+00:00

First-pass conclusion: `ppu00566` is a two-gene boundary/absence map rather
than a complete sulfoquinovose degradation pathway in KT2440. `mdh` is
central-carbon malate dehydrogenase spillover. `yihS` carries the actionable
specificity conflict: KEGG assigns sulfoquinovose isomerase K18479/EC 5.3.1.31,
whereas UniProt/GOA currently assign mannose isomerase EC 5.3.1.7/GO:0050089.
The review records the KEGG sulfoquinovose-isomerase call as a `NEW` candidate
lead and leaves the specific substrate unresolved.

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon sulfoquinovose_metabolism_boundary`
  and `just module-pathway-deep-research-falcon sulfoquinovose_metabolism_boundary ppu00566 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/sulfoquinovose_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__sulfoquinovose_metabolism_boundary__ppu00566-deep-research-falcon.md`.
