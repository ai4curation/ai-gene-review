---
title: "PSEPK ppu02025 Biofilm formation partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu02025: Biofilm formation partition

KEGG ppu02025 is a Pseudomonas aeruginosa biofilm-formation umbrella.
The PSEPK primary set mixes regulatory, chemotaxis, c-di-GMP, type IV
pilus, and T6SS context rather than a single linear pathway.

## Outputs

- Source batch: `projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_boundary.tsv`
- Partition table: `projects/P_PUTIDA/batches/ppu02025_biofilm_formation_pseudomonas_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Status | Example genes |
|---|---:|---|---|---|---|
| `global_gac_csr_crp_biofilm_regulation` | 6 | `global_biofilm_regulation_boundary` | NEW_SUBMODULE | CURATED | `crp`, `gacS`, `uvrY`, `csrA__Q88M29`, `csrA__Q88G93`, `csrA__Q88EJ0` |
| `wsp_chemotaxis_c_di_gmp_cluster` | 6 | `wsp_surface_sensing_c_di_gmp_boundary` | NEW_SUBMODULE | CURATED | `PP_1488`, `PP_1489`, `PP_1491`, `PP_1492`, `cheB3`, `PP_1494` |
| `c_di_gmp_turnover` | 4 | `c_di_gmp_turnover_boundary` | NEW_SUBMODULE | CURATED | `PP_0914`, `PP_3581`, `TpbB`, `pde` |
| `t6ss_biofilm_context` | 13 | `bacterial_secretion_system_boundary` | EXISTING_OR_REUSE | CURATED | `PP_2617`, `PP_2620`, `PP_2623`, `PP_2624`, `PP_3088`, `PP_3093`, `PP_3096`, `puuD` |
| `orphan_biofilm_regulatory_sensors` | 8 | `orphan_biofilm_regulatory_sensors_boundary` | NEW_SUBMODULE | CURATED | `PP_1875`, `PP_2664`, `PP_4173`, `PP_4362`, `PP_4363`, `PP_4364`, `PP_4781`, `PP_4824` |
| `pil_chp_twitching_regulation` | 6 | `pil_chp_twitching_motility_boundary` | NEW_SUBMODULE | CURATED | `PP_4987`, `PP_4988`, `pilJ`, `pilI`, `pilH`, `pilG` |

## Working Decisions

- Do not curate all 43 primary genes as one biofilm-formation PR.
- Reuse the bacterial secretion-system boundary for T6SS apparatus
  genes instead of creating a biofilm-specific T6SS module.
- The strongest new biofilm-specific batches are Wsp-like surface sensing,
  c-di-GMP turnover, Gac/Csr/Crp global regulation, and Pil/Chp
  twitching regulation.
- The orphan histidine kinase/Hpt/anti-sigma entries are captured as a
  conservative unresolved regulatory-sensor boundary rather than direct
  per-gene biofilm-output assertions.

## Completed Sub-batches

- `wsp_chemotaxis_c_di_gmp_cluster`: first-pass gene reviews, Asta gene
  research, and `modules/wsp_surface_sensing_c_di_gmp_boundary.yaml`
  are complete for PP_1488, PP_1489, PP_1491, PP_1492, cheB3, and
  PP_1494, with already curated wspC/PP_1490 included as local cluster
  context.
- Falcon taxon-aware module/pathway research for
  `wsp_surface_sensing_c_di_gmp_boundary` + `ppu02025` + PSEPK was
  attempted with the real command and failed with HTTP 402, so no
  Falcon report is cited for this sub-batch.
- `c_di_gmp_turnover`: first-pass gene reviews, Asta gene research,
  and `modules/c_di_gmp_turnover_boundary.yaml` are complete for
  PP_0914, PP_3581, TpbB, and pde.
- Falcon taxon-aware module/pathway research for
  `c_di_gmp_turnover_boundary` + `ppu02025` + PSEPK was attempted
  with the real command and failed with HTTP 402, so no Falcon
  report is cited for this sub-batch.
- `pil_chp_twitching_regulation`: first-pass gene reviews, Asta
  gene research, and `modules/pil_chp_twitching_motility_boundary.yaml`
  are complete for PP_4987, PP_4988, pilJ, pilI, pilH, and pilG.
- Falcon taxon-aware module/pathway research for
  `pil_chp_twitching_motility_boundary` + `ppu02025` + PSEPK was
  attempted with the real command and failed with HTTP 402, so no
  Falcon report is cited for this sub-batch.
- `global_gac_csr_crp_biofilm_regulation`: first-pass gene reviews,
  Asta gene research, and `modules/global_biofilm_regulation_boundary.yaml`
  are complete for crp, gacS, uvrY/gacA, csrA__Q88M29,
  csrA__Q88G93, and csrA__Q88EJ0.
- Falcon taxon-aware module/pathway research for
  `global_biofilm_regulation_boundary` + `ppu02025` + PSEPK was
  attempted with the real command and failed with HTTP 402, so no
  Falcon report is cited for this sub-batch.
- `t6ss_biofilm_context`: first-pass gene reviews and Asta
  gene research are complete for PP_2617, PP_2620, PP_2623,
  PP_2624, PP_3088, PP_3093, PP_3096, puuD, PP_3100,
  PP_4074, PP_4078, PP_4080, and PP_5561. This bucket reuses
  `modules/bacterial_secretion_system_boundary.yaml`; puuD/PP_3099
  is interpreted as a likely TssC/VipB-family sheath protein and
  its EC-derived urate oxidase activity annotation is marked for
  removal.
- `orphan_biofilm_regulatory_sensors`: first-pass gene reviews,
  Asta gene research, and
  `modules/orphan_biofilm_regulatory_sensors_boundary.yaml` are
  complete for PP_1875, PP_2664, PP_4173, PP_4362, PP_4363,
  PP_4364, PP_4781, and PP_4824/retS.

## Next Steps

- Register ppu02025 as `PARTITIONED` in the pathway worklist.
- Treat all six ppu02025 sub-buckets as first-pass complete: Wsp-like
  surface sensing, c-di-GMP turnover, Pil/Chp twitching regulation,
  Gac/Csr/Crp global regulation, T6SS context via the secretion
  boundary module, and orphan regulatory sensors.
- Run real Falcon module/pathway commands only after a concrete submodule
  is selected; current Edison Falcon access failure mode is HTTP 402.
