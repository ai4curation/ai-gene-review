---
title: "PSEPK regulation/signal-transduction functional-bucket partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK regulation/signal-transduction functional-bucket partition

The `module:regulation_signal_transduction` bucket is a UniProt
name/domain umbrella. It mixes hundreds of transcription factors,
two-component-system proteins, sigma-factor regulators, phage-like
regulatory proteins, toxin-antitoxin components, and low-information
DNA-binding proteins. It is not satisfiable as one biological module.

## Outputs

- Source table: `projects/P_PUTIDA/data/psepk_pathway_partition.tsv`
- Full partition table: `projects/P_PUTIDA/batches/module_regulation_signal_transduction_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Status | Example genes |
|---|---:|---|---|---|---|
| `lysr_transcriptional_regulators` | 107 | `lysr_transcriptional_regulator_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0036`, `PP_0055`, `PP_0079`, `trpI`, `gcdR`, `PP_0371`, `PP_0595`, `PP_0661` |
| `two_component_sensors_response_regulators` | 48 | `orphan_two_component_regulators_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0215`, `PP_0270`, `gltR-I`, `PP_0355`, `PP_0409`, `PP_0768`, `PP_0769`, `colR` |
| `low_information_or_named_transcriptional_regulators` | 32 | `transcriptional_regulator_spillover_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0017`, `PP_0175`, `PP_0274`, `PP_0357`, `nrdR`, `PP_0537`, `hexR`, `PP_1057` |
| `arac_xyls_transcriptional_regulators` | 40 | `arac_xyls_transcriptional_regulator_boundary` | COMPLETED_SUBMODULE | CURATED | `gbdR`, `cdhR`, `PP_0583`, `ada`, `PP_0876`, `PP_1313`, `PP_1395`, `PP_1711` |
| `gntr_transcriptional_regulators` | 29 | `gntr_transcriptional_regulator_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0163`, `PP_0204`, `PP_0486`, `PP_0620`, `PP_0969`, `PP_1109`, `PP_1697`, `PP_1727` |
| `merr_arsr_marr_metal_redox_regulators` | 25 | `metal_redox_stress_transcription_regulator_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0585`, `PP_0590`, `PP_0740`, `PP_0921`, `PP_1253`, `PP_1578`, `PP_1683`, `arsR1` |
| `tetr_acrr_transcriptional_regulators` | 25 | `tetr_acrr_transcriptional_regulator_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0242`, `PP_0594`, `ttgR`, `PP_1497`, `PP_1515`, `PP_1968`, `PP_1978`, `PP_2144` |
| `small_family_metabolic_transcriptional_regulators` | 21 | `metabolic_transcriptional_regulator_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0384`, `PP_0663`, `glpR`, `PP_1307`, `rbsR`, `PP_2601`, `PP_2609`, `fnrB` |
| `xre_cro_phage_toxin_antitoxin_regulators` | 28 | `phage_regulation_toxin_antitoxin_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0276`, `PP_0497`, `PP_0852`, `PP_1198`, `PP_1549`, `PP_1550`, `PP_1716`, `PP_1935` |
| `sigma54_enhancer_binding_regulators` | 16 | `sigma54_enhancer_binding_regulator_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0051`, `PP_0546`, `PP_0767`, `PP_2259`, `PP_2587`, `PP_2771`, `PP_3075`, `PP_3467` |
| `sigma_anti_sigma_and_sigma_factors` | 16 | `sigma_anti_sigma_regulation_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0865`, `PP_0994`, `PP_1008`, `rpoE`, `mucA`, `mucB`, `rpoS`, `PP_2088` |

## Working Decisions

- Do not curate the 387-gene functional bucket as one satisfiable module.
- Treat most rows as transcription-factor family batches until gene-level
  evidence supports a pathway-specific regulon assignment.
- Reuse existing boundary modules for ECF sigma/anti-sigma regulators,
  orphan two-component regulators, phage/toxin-antitoxin regulators,
  and metal/redox/stress regulators where the gene-level evidence fits.
- Use the small-family metabolic-regulator split as the first follow-up
  batch because it is compact and contains several named metabolic
  regulators while still exercising the same GOA-overannotation pattern
  seen in the larger LysR/AraC/GntR/TetR expansions. This split is now
  complete and represented in `modules/metabolic_transcriptional_regulator_boundary.yaml`.
- For generic transcription-factor paralogs, broad DNA-binding or
  transcription-regulator terms can be core, but broad parent biological
  process terms such as `DNA-templated transcription` should usually be
  non-core or over-annotated unless there is gene-specific evidence.
