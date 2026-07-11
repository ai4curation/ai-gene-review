---
title: "PSEPK ppu02025 Biofilm formation - Pseudomonas aeruginosa batch"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu02025: Biofilm formation - Pseudomonas aeruginosa

- Module seed: `biofilm_formation_pseudomonas_boundary`
- Candidate genes from membership table: 43
- Primary bucket genes: 43
- Existing review files: 43
- Curated review files: 43
- Existing Asta research files: 43

## Required Workflow

- [x] Curate or update the species-neutral module.
- [ ] Run module-level Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [ ] Run module + pathway + PSEPK Falcon deep research. Attempted before 2026-07-11 status normalization; blocked by Edison HTTP 402 before report generation.
- [x] Fetch all selected genes with `just fetch-gene PSEPK <gene>`.
- [x] Run Asta deep research for selected genes.
- [x] Curate each selected gene review.
- [x] Validate module and gene reviews.
- [ ] Open one PR for this module/pathway.
- [ ] Shepherd PR through review, CI, and merge readiness.

## Candidate Genes

| Done | Gene | Locus | UniProt | Primary bucket | Existing review | Curation | Asta research | Protein |
|---|---|---|---|---|---|---|---|---|
| [x] | `crp` | PP_0424 | Q88QR4 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | DNA-binding transcriptional dual regulator |
| [x] | `PP_0914` | PP_0914 | Q88PD6 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | cyclic-guanylate-specific phosphodiesterase (EC 3.1.4.52) |
| [x] | `PP_1488` | PP_1488 | Q88MT0 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Methyl-accepting chemotaxis transducer |
| [x] | `PP_1489` | PP_1489 | Q88MS9 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | CheW domain protein |
| [x] | `PP_1491` | PP_1491 | Q88MS7 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Chemotaxis protein CheW |
| [x] | `PP_1492` | PP_1492 | Q88MS6 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Chemotaxis protein CheA (EC 2.7.13.3) |
| [x] | `cheB3` | PP_1493 | Q88MS5 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Protein-glutamate methylesterase/protein-glutamine glutaminase of group 3 operon (EC 3.1.1.61) (EC 3.5.1.44) |
| [x] | `PP_1494` | PP_1494 | Q88MS4 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | diguanylate cyclase (EC 2.7.7.65) |
| [x] | `gacS` | PP_1650 | Q88MC3 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `csrA__Q88M29` | PP_1746 | Q88M29 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Translational regulator CsrA (Carbon storage regulator) |
| [x] | `PP_1875` | PP_1875 | Q88LQ4 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `PP_2617` | PP_2617 | Q88JN2 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Type VI secretion system baseplate subunit TssK |
| [x] | `PP_2620` | PP_2620 | Q88JM9 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Type VI secretion system baseplate subunit TssG |
| [x] | `PP_2623` | PP_2623 | Q88JM6 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Type VI secretion system contractile sheath large subunit |
| [x] | `PP_2624` | PP_2624 | Q88JM5 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Type VI secretion system contractile sheath small subunit |
| [x] | `PP_2664` | PP_2664 | Q88JI5 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Sensor histidine kinase PP_2664 (EC 2.7.13.3) |
| [x] | `PP_3088` | PP_3088 | Q88IB1 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | ImpA N-terminal domain-containing protein |
| [x] | `PP_3093` | PP_3093 | Q88IA6 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Type VI secretion system baseplate subunit TssK |
| [x] | `PP_3096` | PP_3096 | Q88IA3 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Type VI secretion system baseplate subunit TssG |
| [x] | `puuD` | PP_3099 | Q88IA0 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Uricase/urate oxidase (EC 1.7.3.3) |
| [x] | `PP_3100` | PP_3100 | Q88I99 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Type VI secretion protein |
| [x] | `PP_3581` | PP_3581 | Q88GY4 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | cyclic-guanylate-specific phosphodiesterase (EC 3.1.4.52) |
| [x] | `csrA__Q88G93` | PP_3832 | Q88G93 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Translational regulator CsrA (Carbon storage regulator) |
| [x] | `PP_4074` | PP_4074 | Q88FL5 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Type VI secretion system contractile sheath small subunit |
| [x] | `PP_4078` | PP_4078 | Q88FL2 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Type VI secretion system baseplate subunit TssG |
| [x] | `PP_4080` | PP_4080 | Q88FL0 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Type VI secretion system baseplate subunit TssK |
| [x] | `uvrY` | PP_4099 | Q88FJ6 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Response regulator GacA (Global activator) |
| [x] | `PP_4173` | PP_4173 | Q88FC5 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Sensory/regulatory protein RpfC (EC 2.7.13.3) |
| [x] | `PP_4362` | PP_4362 | Q88EU1 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | HPt domain-containing protein |
| [x] | `PP_4363` | PP_4363 | Q88EU0 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Sensor histidine kinase/response regulator |
| [x] | `PP_4364` | PP_4364 | Q88ET9 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Anti-sigma F factor antagonist |
| [x] | `csrA__Q88EJ0` | PP_4472 | Q88EJ0 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Translational regulator CsrA (Carbon storage regulator) |
| [x] | `TpbB` | PP_4670 | Q88DZ8 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Diguanylate cyclase (EC 2.7.7.65) |
| [x] | `PP_4781` | PP_4781 | Q88DP3 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `PP_4824` | PP_4824 | Q88DK1 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | histidine kinase (EC 2.7.13.3) |
| [x] | `pde` | PP_4917 | Q88DB0 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | 3',5'-cyclic-nucleotide phosphodiesterase (EC 3.1.4.17) |
| [x] | `PP_4987` | PP_4987 | Q88D41 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Chemotaxis protein |
| [x] | `PP_4988` | PP_4988 | Q88D40 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Chemotaxis protein CheA (EC 2.7.13.3) |
| [x] | `pilJ` | PP_4989 | Q88D39 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Protein PilJ |
| [x] | `pilI` | PP_4990 | Q88D38 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Protein PilI |
| [x] | `pilH` | PP_4991 | Q88D37 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Protein PilH |
| [x] | `pilG` | PP_4992 | Q88D36 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Protein PilG |
| [x] | `PP_5561` | PP_5561 | A0A140FWB4 | kegg:ppu02025 | PRESENT | CURATED | PRESENT | Type VI secretion system-associated protein TagF |

## Notes

Generated UTC: 2026-07-09T22:40:15.318220+00:00

2026-07-11 PDT status sync: created and validated
`modules/biofilm_formation_pseudomonas_boundary.yaml` as an umbrella/index module
over the completed ppu02025 sub-batches: global Gac/Csr/Crp regulation, Wsp-like
surface sensing and c-di-GMP output, c-di-GMP turnover, Pil/Chp twitching
regulation, T6SS context via `bacterial_secretion_system_boundary`, and orphan
biofilm regulatory sensors. The parent batch and partition TSVs both show 43/43
review files present, 43/43 curated review YAMLs, and 43/43 Asta reports. Module
validation passed with `linkml-validate -C ModuleReview` and the module term-label
validator. Gene review validation passed for all 43 batch review files with `uv
run ai-gene-review validate --verbose --terms --tsv-output
reports/validation-psepk-ppu02025.tsv <43 files from the batch TSV>`. The TSV
contains four non-blocking best-practice warnings: one `gacS` warning that
available Asta/Falcon deep-research files are not referenced in annotation
reviews, and three CsrA paralog warnings where the core-function `cytosol`
location is not mirrored in `existing_annotations`.

Falcon status: ran the real module-level command
`just module-deep-research-falcon biofilm_formation_pseudomonas_boundary`; it
reached Edison and failed with HTTP 402 Payment Required, so
`modules/biofilm_formation_pseudomonas_boundary-deep-research-falcon.md` was not
created. Also ran the real module + pathway + taxon command
`just module-pathway-deep-research-falcon biofilm_formation_pseudomonas_boundary ppu02025 PSEPK`;
it reached Edison and failed with the same HTTP 402 Payment Required response, so
`projects/P_PUTIDA/deep-research/PSEPK__biofilm_formation_pseudomonas_boundary__ppu02025-deep-research-falcon.md`
was not created. The Falcon workflow boxes remain unchecked.
