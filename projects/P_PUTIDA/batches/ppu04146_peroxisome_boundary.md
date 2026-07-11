---
title: "PSEPK ppu04146 Peroxisome batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu04146: Peroxisome

- Module seed: `peroxisome_boundary`
- Candidate genes from membership table: 12
- Primary bucket genes: 10
- Existing review files: 12
- Curated review files: 12
- Existing Asta research files: 12

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted on 2026-07-09; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted on 2026-07-09; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `katE` | PP_0115 | Q88RL4 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Catalase (EC 1.11.1.6) |
| [x] | `katA` | PP_0481 | Q88QK9 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Catalase (EC 1.11.1.6) |
| [x] | `sodB` | PP_0915 | Q88PD5 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Superoxide dismutase [Fe] (EC 1.15.1.1) |
| [x] | `sodA` | PP_0946 | Q88PA4 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Superoxide dismutase (EC 1.15.1.1) |
| [x] | `PP_2887` | PP_2887 | Q88IW2 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Catalase-related peroxidase (EC 1.11.1.-) |
| [x] | `PP_3394` | PP_3394 | Q88HG4 | kegg:ppu00907 | PRESENT | CURATED | PRESENT | 3-hydroxy-3-methylglutaryl-CoA lyase |
| [x] | `mvaB` | PP_3540 | Q88H25 | kegg:ppu00907 | PRESENT | CURATED | PRESENT | hydroxymethylglutaryl-CoA lyase (EC 4.1.3.4) |
| [x] | `icd` | PP_4011 | Q88FS2 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Isocitrate dehydrogenase [NADP] (EC 1.1.1.42) |
| [x] | `idh` | PP_4012 | Q88FS1 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Isocitrate dehydrogenase [NADP] (EC 1.1.1.42) (Oxalosuccinate decarboxylase) |
| [x] | `nudC` | PP_4029 | Q88FQ8 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | NAD-capped RNA hydrolase NudC (DeNADding enzyme NudC) (EC 3.6.1.-) (NADH pyrophosphatase) (EC 3.6.1.22) |
| [x] | `fadD-I` | PP_4549 | Q88EB7 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) |
| [x] | `fadD-II` | PP_4550 | Q88EB6 | kegg:ppu04146 | PRESENT | CURATED | PRESENT | Long-chain-fatty-acid--CoA ligase (EC 6.2.1.3) (Long-chain acyl-CoA synthetase) |

## Notes

Generated UTC: 2026-07-09T08:39:37.999975+00:00

- 2026-07-09: Created and validated `modules/peroxisome_boundary.yaml`.
- 2026-07-09: Attempted `just module-deep-research-falcon peroxisome_boundary`; Edison returned HTTP 402 Payment Required at task creation, so no Falcon module output was written.
- 2026-07-09: Attempted `just module-pathway-deep-research-falcon peroxisome_boundary ppu04146 PSEPK`; Edison returned HTTP 402 Payment Required at task creation, so no Falcon pathway+taxon output was written.
