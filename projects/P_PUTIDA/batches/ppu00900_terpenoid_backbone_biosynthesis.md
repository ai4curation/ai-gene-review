---
title: "PSEPK ppu00900 Terpenoid backbone biosynthesis batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00900: Terpenoid backbone biosynthesis

- Module seed: `terpenoid_backbone_biosynthesis`
- Candidate genes from membership table: 17
- Primary bucket genes: 14
- Existing review files: 17
- Curated review files: 17
- Existing Asta research files: 17

## Required Workflow

- [x] Curate or update the species-neutral module.
- [x] Run module-level Falcon deep research.
- [x] Run module + pathway + PSEPK Falcon deep research.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `dxs` | PP_0527 | Q88QG7 | kegg:ppu00730 | PRESENT | CURATED | PRESENT | 1-deoxy-D-xylulose-5-phosphate synthase (EC 2.2.1.7) (1-deoxyxylulose-5-phosphate synthase) (DXP synthase) (DXPS) |
| [x] | `ispA` | PP_0528 | Q88QG6 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Farnesyl diphosphate synthase (EC 2.5.1.1, EC 2.5.1.10) |
| [x] | `ubiX` | PP_0548 | Q88QE6 | kegg:ppu00627 | PRESENT | CURATED | PRESENT | Flavin prenyltransferase UbiX (EC 2.5.1.129) |
| [x] | `PP_0582` | PP_0582 | Q88QB2 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Thiolase family protein |
| [x] | `ispH` | PP_0606 | Q88Q89 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | 4-hydroxy-3-methylbut-2-enyl diphosphate reductase (HMBPP reductase) (EC 1.17.7.4) |
| [x] | `ispB` | PP_0687 | Q88Q11 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Octaprenyl diphosphate synthase (EC 2.5.1.90) (All-trans-octaprenyl-diphosphate synthase) (Octaprenyl pyrophosphate synt |
| [x] | `ispE` | PP_0723 | Q88PX5 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | 4-diphosphocytidyl-2-C-methyl-D-erythritol kinase (CMK) (EC 2.7.1.148) (4-(cytidine-5'-diphospho)-2-C-methyl-D-erythrito |
| [x] | `ispG` | PP_0853 | Q88PJ7 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | 4-hydroxy-3-methylbut-2-en-1-yl diphosphate synthase (flavodoxin) (EC 1.17.7.3) (1-hydroxy-2-methyl-2-(E)-butenyl 4-diph |
| [x] | `uppS` | PP_1595 | Q88MH6 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Ditrans,polycis-undecaprenyl-diphosphate synthase ((2E,6E)-farnesyl-diphosphate specific) (EC 2.5.1.31) (Ditrans,polycis |
| [x] | `dxr` | PP_1597 | Q88MH4 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | 1-deoxy-D-xylulose 5-phosphate reductoisomerase (DXP reductoisomerase) (EC 1.1.1.267) (1-deoxyxylulose-5-phosphate reduc |
| [x] | `ispD` | PP_1614 | Q88MF7 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | 2-C-methyl-D-erythritol 4-phosphate cytidylyltransferase (EC 2.7.7.60) (4-diphosphocytidyl-2C-methyl-D-erythritol syntha |
| [x] | `ispF` | PP_1618 | Q88MF3 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | 2-C-methyl-D-erythritol 2,4-cyclodiphosphate synthase (MECDP-synthase) (MECPP-synthase) (MECPS) (EC 4.6.1.12) |
| [x] | `fadA__Q88L84` | PP_2051 | Q88L84 | kegg:ppu00592 | PRESENT | CURATED | PRESENT | 3-ketoacyl-CoA thiolase (Thiolase I) (EC 2.3.1.16) |
| [x] | `PP_2215` | PP_2215 | Q88KS4 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |
| [x] | `PP_3355` | PP_3355 | Q88HK1 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase |
| [x] | `bktB` | PP_3754 | Q88GH0 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Beta-ketothiolase BktB (EC 2.3.1.16, EC 2.3.1.9) |
| [x] | `yqeF` | PP_4636 | Q88E32 | kegg:ppu00900 | PRESENT | CURATED | PRESENT | Acetyl-CoA acetyltransferase (EC 2.3.1.9) |

## Notes

Generated UTC: 2026-07-07T08:44:17.676672+00:00

## Curation Checkpoint

Status as of 2026-07-07:

- Created and validated `modules/terpenoid_backbone_biosynthesis.yaml`.
- Falcon generic module report complete:
  `modules/terpenoid_backbone_biosynthesis-deep-research-falcon.md`.
- Falcon PSEPK module+pathway report complete:
  `projects/P_PUTIDA/deep-research/PSEPK__terpenoid_backbone_biosynthesis__ppu00900-deep-research-falcon.md`.
- 17/17 candidate rows now have review files, Asta retrieval files, curated
  review actions, and successful `just validate PSEPK <gene>` checks.
- Core KT2440 backbone coverage is the MEP/DOXP route plus prenyl-diphosphate
  extension: `dxs`, `dxr`, `ispD`, `ispE`, `ispF`, `ispG`, `ispH`, `ispA`,
  `ispB`, and `uppS`.
- `ubiX` is retained as a ubiquinone-biosynthesis boundary enzyme, not a strict
  terpenoid-backbone step.
- Thiolase and acetyl-CoA acetyltransferase entries (`PP_0582`,
  `fadA__Q88L84`, `PP_2215`, `PP_3355`, `bktB`, `yqeF`) are KEGG composite-map
  spillovers from mevalonate-like chemistry or fatty-acid metabolism; they do
  not establish a native KT2440 mevalonate pathway.
- The PSEPK Falcon report suggested adding `idi`/PP_0854, but this was rejected
  after verification: local UniProt metadata and live UniProt REST identify
  PP_0854 as `hisS`/histidyl-tRNA synthetase, and no UP000000556
  IDI/EC 5.3.3.2 entry was found.

Validation commands run:

```bash
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C ModuleReview modules/terpenoid_backbone_biosynthesis.yaml
uv run python -m ai_gene_review.validation.module_validator modules/terpenoid_backbone_biosynthesis.yaml
for gene in dxs ispA ubiX PP_0582 ispH ispB ispE ispG uppS dxr ispD ispF fadA__Q88L84 PP_2215 PP_3355 bktB yqeF; do just validate PSEPK "$gene"; done
```
