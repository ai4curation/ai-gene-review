---
title: "PSEPK ppu00592 alpha-Linolenic acid metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00592: alpha-Linolenic acid metabolism

- Module seed: `alpha_linolenic_acid_metabolism_boundary`
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
| [x] | `fadA__Q88L84` | PP_2051 | Q88L84 | kegg:ppu00592 | PRESENT | CURATED | PRESENT | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) |
| [x] | `fadA__Q88L01` | PP_2137 | Q88L01 | kegg:ppu00592 | PRESENT | CURATED | PRESENT | 3-ketoacyl-CoA thiolase (EC 2.3.1.16) (Acetyl-CoA acyltransferase) (Beta-ketothiolase) (Fatty acid oxidation complex sub |

## Notes

Generated UTC: 2026-07-08T11:32:18.701347+00:00

First-pass conclusion: `ppu00592` is a two-gene boundary/absence map, not a
complete alpha-linolenic-acid-specific pathway in KT2440. Both candidates are
FadA-like 3-ketoacyl-CoA thiolases already curated as generic fatty-acid
beta-oxidation enzymes.

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon alpha_linolenic_acid_metabolism_boundary`
  and `just module-pathway-deep-research-falcon alpha_linolenic_acid_metabolism_boundary ppu00592 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/alpha_linolenic_acid_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__alpha_linolenic_acid_metabolism_boundary__ppu00592-deep-research-falcon.md`.
