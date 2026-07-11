---
title: "PSEPK transport ion/metal sub-bucket partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK transport ion/metal sub-bucket partition

The parent `ion_metal_transporters_and_antiporters` split contains true
cation homeostasis systems plus metal-binding redox proteins, proteases,
and membrane enzyme side nodes. This deeper partition separates those
contexts before first-pass curation.

## Outputs

- Source table: `projects/P_PUTIDA/batches/module_transport_membrane_efflux_ion_metal_transporters_and_antiporters.tsv`
- Full partition table: `projects/P_PUTIDA/batches/module_transport_membrane_efflux_ion_metal_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Status | Example genes |
|---|---:|---|---|---|---|
| `monovalent_cation_antiporters_potassium_systems` | 26 | `monovalent_cation_antiporter_boundary` | COMPLETED_SUBMODULE | CURATED | `trkA`, `kefB-I`, `PP_0928`, `nhaA1`, `kup`, `PP_1467`, `PP_1587`, `mrpG` |
| `p_type_metal_atpases` | 5 | `p_type_metal_atpase_transport_boundary` | COMPLETED_SUBMODULE | CURATED | `cadA-I`, `cadA-II`, `mgtA`, `PP_4261`, `cadA-III` |
| `transition_metal_magnesium_cobalt_transporters` | 15 | `transition_metal_magnesium_cobalt_transport_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0026`, `PP_0629`, `PP_0683`, `PP_0947`, `PP_1227`, `PP_1836`, `PP_1843`, `cmaX` |
| `chromate_fluoride_and_other_inorganic_channels` | 3 | `inorganic_ion_channel_resistance_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_2556`, `fluC`, `PP_4986` |
| `sodium_solute_symporters_and_mate_efflux` | 14 | `sodium_solute_symporter_mate_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0496`, `PP_0569`, `PP_0670`, `gltS`, `arcD-I`, `arcD-II`, `actP-I`, `actP-II` |
| `membrane_redox_electron_transfer_spillovers` | 25 | `membrane_redox_electron_transfer_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0111`, `PP_0125`, `cc`, `PP_0180`, `hmp`, `cumA`, `PP_1083`, `fdxA` |
| `membrane_metalloenzymes_and_envelope_side_nodes` | 14 | `transport_membrane_enzyme_spillover_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0093`, `PP_0144`, `PP_1124`, `PP_1526`, `rseP`, `wbpL`, `PP_1838`, `htpX` |

## Working Decisions

- Do not curate the 102-gene ion/metal bucket as one satisfiable module.
- The monovalent cation antiporter and potassium-system split is complete
  and represented in `modules/monovalent_cation_antiporter_boundary.yaml`.
- The P-type metal ATPase split is complete and represented in
  `modules/p_type_metal_atpase_transport_boundary.yaml`.
- The chromate/fluoride/inorganic-channel split is complete and represented in
  `modules/inorganic_ion_channel_resistance_boundary.yaml`.
- The transition-metal/Mg/Co transporter split is complete and represented in
  `modules/transition_metal_magnesium_cobalt_transport_boundary.yaml`.
- The membrane redox/electron-transfer spillover split is complete and represented in
  `modules/membrane_redox_electron_transfer_boundary.yaml`.
- Route cytochromes, heme proteins, ferredoxins, and Ccm proteins toward
  membrane redox/electron-transfer context rather than ion transport.
- Treat metalloproteases, metal-dependent transferases/sulfatases, TamB,
  and phospholipid-modification entries as membrane/enzyme side nodes.
