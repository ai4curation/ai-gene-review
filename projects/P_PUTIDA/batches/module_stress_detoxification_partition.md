---
title: "PSEPK stress/detoxification functional-bucket partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK stress/detoxification functional-bucket partition

The `module:stress_detoxification` bucket is a UniProt name/keyword
umbrella. It mixes peroxide detoxification enzymes, GST and thiol
detoxification candidates, metal-resistance proteins, universal stress
proteins, cold/heat-shock proteins, ThiJ/DJ-1/PfpI candidates, and
miscellaneous regulatory or low-information stress spillovers.

## Outputs

- Source table: `projects/P_PUTIDA/data/psepk_pathway_partition.tsv`
- Full partition table: `projects/P_PUTIDA/batches/module_stress_detoxification_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Status | Example genes |
|---|---:|---|---|---|---|
| `peroxide_peroxiredoxin_detoxification` | 10 | `oxidative_stress_peroxide_detoxification_boundary` | COMPLETED_SUBMODULE | CURATED | `osmC`, `PP_0235`, `tsaA`, `PP_1235`, `ohr`, `ahpC`, `PP_2943`, `PP_3248` |
| `glutathione_thiol_detoxification` | 7 | `glutathione_metabolism_boundary` | COMPLETED_REUSE_EXISTING | CURATED | `PP_0335`, `yffB`, `PP_1939`, `PP_2023`, `PP_3742`, `PP_4104`, `mnaT` |
| `arsenic_copper_metal_resistance` | 8 | `metal_resistance_detoxification_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_1927`, `PP_1928`, `copB-I`, `copA-I`, `arsH`, `PP_2716`, `copB-II`, `copA-II` |
| `universal_stress_proteins` | 11 | `universal_stress_protein_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_1269`, `PP_2132`, `PP_2187`, `PP_2326`, `PP_2648`, `PP_2745`, `PP_3156`, `PP_3237` |
| `cold_heat_shock_chaperone_spillovers` | 5 | `integrated_stress_response_boundary` | COMPLETED_REUSE_EXISTING | CURATED | `capB`, `cspA-I`, `ibpA`, `PP_3313`, `PP_3314` |
| `thij_dj1_pfpi_detoxification_candidates` | 3 | `stress_detoxification_spillover_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_2491`, `PP_2992`, `PP_3431` |
| `stress_regulatory_or_misc_spillovers` | 8 | `stress_detoxification_spillover_boundary` | COMPLETED_SUBMODULE | CURATED | `srkA`, `dps`, `PP_3269`, `paaY`, `PP_3509`, `PP_3963`, `oxyR`, `PP_5593` |

## Working Decisions

- Do not curate the 52-gene functional bucket as one satisfiable module.
- Use the peroxide/peroxiredoxin detoxification split as the first
  follow-up batch because it is biologically compact and complements
  earlier catalase/SOD oxidative-stress curation without implying
  bacterial peroxisome localization.
- Reuse the existing `glutathione_metabolism_boundary` for genes with
  supported glutathione-linked detoxification, but keep generic GST
  candidates conservative until gene-level evidence is reviewed.
- Route cold/heat-shock proteins toward bacterial proteostasis/chaperone
  context rather than eukaryotic integrated-stress-response signaling.
- Treat metal-resistance genes as arsenic/copper detoxification rather
  than as generic oxidative-stress members.
