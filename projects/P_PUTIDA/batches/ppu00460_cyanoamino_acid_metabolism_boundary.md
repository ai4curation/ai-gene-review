---
title: "PSEPK ppu00460 Cyanoamino acid metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00460: Cyanoamino acid metabolism

- Module seed: `cyanoamino_acid_metabolism_boundary`
- Candidate genes from membership table: 7
- Primary bucket genes: 2
- Existing review files: 7
- Curated review files: 7
- Existing Asta research files: 7

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
| [x] | `glyA1` | PP_0322 | Q88R12 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Serine hydroxymethyltransferase 1 (SHMT 1) (Serine methylase 1) (EC 2.1.2.1) |
| [x] | `ansA` | PP_0495 | Q88QJ6 | kegg:ppu00460 | PRESENT | CURATED | PRESENT | Type 1 L-asparaginase (EC 3.5.1.1) |
| [x] | `glyA2` | PP_0671 | Q88Q27 | kegg:ppu04981 | PRESENT | CURATED | PRESENT | Serine hydroxymethyltransferase 2 (SHMT 2) (Serine methylase 2) (EC 2.1.2.1) |
| [x] | `PP_1160` | PP_1160 | Q88NP7 | kegg:ppu00460 | PRESENT | CURATED | PRESENT | Asparaginase family protein |
| [x] | `bglX` | PP_1403 | Q88N13 | kegg:ppu00999 | PRESENT | CURATED | PRESENT | Periplasmic beta-glucosidase (EC 3.2.1.21) (Beta-D-glucoside glucohydrolase) (Cellobiase) (Gentiobiase) |
| [x] | `PP_3535` | PP_3535 | Q88H30 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | Glutathione hydrolase proenzyme (EC 2.3.2.2) (EC 3.4.19.13) [Cleaved into: Glutathione hydrolase large chain; Glutathion |
| [x] | `ggt` | PP_4659 | Q88E09 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | Glutathione hydrolase proenzyme (EC 2.3.2.2) (EC 3.4.19.13) [Cleaved into: Glutathione hydrolase large chain; Glutathion |

## Notes

Generated UTC: 2026-07-07T22:41:44.100345+00:00

Completed first-pass curation of `ppu00460` as a cyanoamino-acid boundary
module. The primary bucket genes are `ansA` and `PP_1160`, both curated as
asparaginase-family/asparagine metabolism enzymes. `glyA1` and `glyA2` remain
serine hydroxymethyltransferase one-carbon side context; `bglX` is a periplasmic
beta-glucosidase/glucan-catabolism side node; `PP_3535` and `ggt` are
glutathione hydrolase side nodes already covered by the taurine/glutathione
boundary context.

All seven gene reviews and the module validate. Remaining validation warnings
are non-blocking older warnings on previously curated side-node reviews
(`glyA1`, `glyA2`, `ansA`, `PP_1160`, `PP_3535`, and `ggt`) about uncited Asta
retrieval files or core-location reflection.

## Workflow Notes

- 2026-07-11 status sync: ran `just module-deep-research-falcon cyanoamino_acid_metabolism_boundary`
  and `just module-pathway-deep-research-falcon cyanoamino_acid_metabolism_boundary ppu00460 PSEPK`.
  Both Edison task creation attempts failed immediately with HTTP 402 Payment Required, so
  the Falcon workflow boxes remain unchecked and no Falcon report files were written. Expected
  output paths remain `modules/cyanoamino_acid_metabolism_boundary-deep-research-falcon.md`
  and `projects/P_PUTIDA/deep-research/PSEPK__cyanoamino_acid_metabolism_boundary__ppu00460-deep-research-falcon.md`.
