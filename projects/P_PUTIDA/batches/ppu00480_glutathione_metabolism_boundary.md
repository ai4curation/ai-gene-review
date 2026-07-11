---
title: "PSEPK ppu00480 Glutathione metabolism batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu00480: Glutathione metabolism

- Module seed: `glutathione_metabolism_boundary`
- Candidate genes from membership table: 31
- Primary bucket genes: 24
- Existing review files: 31
- Curated review files: 31
- Existing Asta research files: 31

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
| [x] | `PP_0183` | PP_0183 | Q88RE7 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glutathione S-transferase (EC 2.5.1.18) |
| [x] | `gshA` | PP_0243 | Q88R90 | kegg:ppu00340 | PRESENT | CURATED | PRESENT | Glutamate--cysteine ligase (EC 6.3.2.2) (Gamma-ECS) (GCS) (Gamma-glutamylcysteine synthetase) |
| [x] | `PP_0777` | PP_0777 | Q88PS1 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glutathione peroxidase |
| [x] | `speC` | PP_0864 | Q88PI6 | kegg:ppu04148 | PRESENT | CURATED | PRESENT | ornithine decarboxylase (EC 4.1.1.17) |
| [x] | `pepA` | PP_0980 | Q88P73 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Probable cytosol aminopeptidase (EC 3.4.11.1) (Leucine aminopeptidase) (LAP) (EC 3.4.11.10) (Leucyl aminopeptidase) |
| [x] | `zwfA` | PP_1022 | Q88P31 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) |
| [x] | `gstA` | PP_1162 | Q88NP5 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Protein GstA |
| [x] | `PP_1347` | PP_1347 | Q88N68 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glutathione S-transferase family protein |
| [x] | `PP_1686` | PP_1686 | Q88M88 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glutathione peroxidase |
| [x] | `PP_1821` | PP_1821 | Q88LV6 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glutathione S-transferase family protein |
| [x] | `gpx` | PP_1874 | Q88LQ5 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glutathione peroxidase |
| [x] | `gstB` | PP_1894 | Q88LN5 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glutathione S-transferase reducing arsenate to arsenite |
| [x] | `pepN` | PP_2017 | Q88LB8 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Aminopeptidase N (EC 3.4.11.2) |
| [x] | `PP_2474` | PP_2474 | Q88K19 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glutathione S-transferase family protein |
| [x] | `PP_2536` | PP_2536 | Q88JW1 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glutathione S-transferase family protein |
| [x] | `PP_2700` | PP_2700 | Q88JE9 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glutathione-dependent peroxiredoxin (EC 1.11.1.27) |
| [x] | `pxpA1` | PP_2920 | Q88IS9 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | 5-oxoprolinase subunit A 1 (5-OPase subunit A 1) (EC 3.5.2.9) (5-oxoprolinase (ATP-hydrolyzing) subunit A 1) |
| [x] | `PP_3253` | PP_3253 | Q88HV0 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Putative glutamate--cysteine ligase 2 (EC 6.3.2.2) (Gamma-glutamylcysteine synthetase 2) (GCS 2) (Gamma-GCS 2) |
| [x] | `ptxD` | PP_3376 | Q88HI1 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Phosphonate dehydrogenase (EC 1.20.1.1) |
| [x] | `PP_3535` | PP_3535 | Q88H30 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | Glutathione hydrolase proenzyme (EC 2.3.2.2) (EC 3.4.19.13) [Cleaved into: Glutathione hydrolase large chain; Glutathion |
| [x] | `gor` | PP_3819 | Q88GA5 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glutathione reductase (GRase) (EC 1.8.1.7) |
| [x] | `icd` | PP_4011 | Q88FS2 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Isocitrate dehydrogenase [NADP] (EC 1.1.1.42) |
| [x] | `idh` | PP_4012 | Q88FS1 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Isocitrate dehydrogenase [NADP] (EC 1.1.1.42) (Oxalosuccinate decarboxylase) |
| [x] | `zwfB` | PP_4042 | Q88FP7 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) |
| [x] | `gntZ` | PP_4043 | Q88FP6 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | 6-phosphogluconate dehydrogenase, decarboxylating (EC 1.1.1.44) |
| [x] | `ybgJ` | PP_4576 | Q88E90 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Allophanate hydrolase subunit (EC 3.5.1.54) |
| [x] | `pxpA2` | PP_4577 | Q88E89 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | 5-oxoprolinase subunit A 2 (5-OPase subunit A 2) (EC 3.5.2.9) (5-oxoprolinase (ATP-hydrolyzing) subunit A 2) |
| [x] | `ggt` | PP_4659 | Q88E09 | kegg:ppu00430 | PRESENT | CURATED | PRESENT | Glutathione hydrolase proenzyme (EC 2.3.2.2) (EC 3.4.19.13) [Cleaved into: Glutathione hydrolase large chain; Glutathion |
| [x] | `gshB` | PP_4993 | Q88D35 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glutathione synthetase (EC 6.3.2.3) (GSH synthetase) (GSH-S) (GSHase) (Glutathione synthase) |
| [x] | `PP_5211` | PP_5211 | Q88CH0 | kegg:ppu04156 | PRESENT | CURATED | PRESENT | glutathione-specific gamma-glutamylcyclotransferase (EC 4.3.2.7) |
| [x] | `zwf` | PP_5351 | Q88C32 | kegg:ppu00480 | PRESENT | CURATED | PRESENT | Glucose-6-phosphate 1-dehydrogenase (G6PD) (EC 1.1.1.49) |

## Notes

Generated UTC: 2026-07-07T23:31:32.691723+00:00

## Completion Notes

- Completed 2026-07-07: all 31 KEGG `ppu00480` membership genes have review folders, Asta reports, curated review YAMLs, validation, and rendered gene pages.
- Created and validated `modules/glutathione_metabolism_boundary.yaml`.
- 2026-07-11 PDT status sync: ran the real Falcon commands
  `just module-deep-research-falcon glutathione_metabolism_boundary` and
  `just module-pathway-deep-research-falcon glutathione_metabolism_boundary ppu00480 PSEPK`.
  Both reached Edison task creation and failed with HTTP 402 Payment Required,
  so no Falcon reports were written. Expected output paths remain
  `modules/glutathione_metabolism_boundary-deep-research-falcon.md` and
  `projects/P_PUTIDA/deep-research/PSEPK__glutathione_metabolism_boundary__ppu00480-deep-research-falcon.md`.
- Boundary decision: strict glutathione biosynthesis/recycling/turnover nodes are separated from GST/peroxidase detoxification, NADPH-supply enzymes, aminopeptidases, allophanate/5-oxoproline side context, and unrelated SpeC/PtxD spillovers.
- First-pass fixes include removing carbohydrate-metabolism spillover from `pxpA1`/`pxpA2`, narrowing broad catalytic/ligase terms for `gshB` and `PP_3253`, representing PP_2700 as glutathione-dependent peroxidase chemistry rather than accepting thioredoxin-specific substrate wording, and keeping cofactor/localization annotations non-core.
