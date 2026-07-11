---
title: "PSEPK motility, chemotaxis, pili, and biofilm functional-bucket partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK motility, chemotaxis, pili, and biofilm functional-bucket partition

The `module:motility_chemotaxis_biofilm` bucket is a UniProt
name/keyword umbrella. It mixes type IV pilus biogenesis, fimbrial
surface-adhesion subunits, alginate envelope/export side candidates,
orphan MCP receptors, a sensory c-di-GMP phosphodiesterase spillover,
a DNA-binding response-regulator spillover, CheY-like/membrane
accessory spillovers, outer-membrane flagellation-name spillover,
flagellar export/localization/accessory spillovers, and c-di-GMP
flagellar brake context.

## Outputs

- Source table: `projects/P_PUTIDA/data/psepk_pathway_partition.tsv`
- Full partition table: `projects/P_PUTIDA/batches/module_motility_chemotaxis_biofilm_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Status | Example genes |
|---|---:|---|---|---|---|
| `type_iv_pilus_biogenesis_boundary` | 12 | `type_iv_pilus_biogenesis_boundary` | NEW_SUBMODULE | CURATED | `PP_0608`, `PP_0609`, `PP_0610`, `pilE`, `pilC`, `pilF`, `PP_3480`, `PP_3481` |
| `fimbrial_type1_surface_adhesion_extension` | 2 | `pili_surface_adhesion_boundary` | EXISTING_OR_REUSE | CURATED | `PP_1888`, `fimI` |
| `hcp_t6ss_product_name_spillover` | 1 | `bacterial_secretion_system_boundary` | EXISTING_OR_REUSE | CURATED | `PP_0655` |
| `alginate_envelope_and_lyase_context` | 5 | `alginate_biosynthesis_boundary` | EXISTING_OR_REUSE | CURATED | `glmP`, `PP_1754`, `PP_3350`, `PP_3464`, `PP_3774` |
| `orphan_mcp_chemotaxis_receptor_candidates` | 3 | `orphan_mcp_aerotaxis_receptors_boundary` | EXISTING_OR_REUSE | CURATED | `PP_2310`, `PP_3950`, `PP_4888` |
| `sensory_c_di_gmp_pde_spillover` | 1 | `c_di_gmp_turnover_boundary` | EXISTING_OR_REUSE | CURATED | `PP_2599` |
| `dna_binding_response_regulator_spillover` | 1 | `orphan_two_component_regulators_boundary` | EXISTING_OR_REUSE | CURATED | `PP_2403` |
| `chey_like_membrane_accessory_spillovers` | 3 | `chemotaxis_adaptation_accessory_boundary` | EXISTING_OR_REUSE | CURATED | `PP_3757`, `PP_3771`, `PP_4331` |
| `outer_membrane_flagellation_name_spillover` | 1 | `transport_envelope_spillover_boundary` | EXISTING_OR_REUSE | CURATED | `ycfJ` |
| `flagellar_export_localization_accessory_spillovers` | 5 | `flagellar_export_assembly_boundary` | EXISTING_OR_REUSE | CURATED | `PP_4328`, `PP_4329`, `PP_4342`, `flhF`, `PP_4377` |
| `c_di_gmp_flagellar_brake_spillover` | 1 | `flagellar_motor_switch_stator_boundary` | EXISTING_OR_REUSE | CURATED | `ycgR` |

## Working Decisions

- Do not curate the 35-gene functional bucket as one satisfiable module.
- Reuse completed chemotaxis, flagellar, alginate, and pili/surface-adhesion modules where the functional bucket is a keyword spillover.
- Completed `type_iv_pilus_biogenesis_boundary`: the 12-gene T4P assembly set is curated into `modules/type_iv_pilus_biogenesis_boundary.yaml`, with pilD and pilT retained as explicit hole-filling gaps.
- Completed `fimbrial_type1_surface_adhesion_extension`: PP_1888 and fimI extend the existing FimD/PP_1890 chaperone-usher context in `modules/pili_surface_adhesion_boundary.yaml`.
- Completed `hcp_t6ss_product_name_spillover`: PP_0655 was initially pulled in by a generic fimbrial-protein-related product name, but its Hcp/T6SS domains route it to `modules/bacterial_secretion_system_boundary.yaml`.
- Completed `alginate_envelope_and_lyase_context`: glmP, PP_1754, PP_3350, PP_3464, and PP_3774 are curated into `modules/alginate_biosynthesis_boundary.yaml` as alginate efficiency, export-domain, and lyase-domain boundary context.
- Completed `orphan_mcp_chemotaxis_receptor_candidates`: PP_2310, PP_3950, and PP_4888 are curated into `modules/orphan_mcp_aerotaxis_receptors_boundary.yaml` as ligand-unresolved MCP receptor/transducer candidates.
- Completed `sensory_c_di_gmp_pde_spillover`: PP_2599 was initially pulled in by a chemotaxis sensory-transducer product name, but HD-GYP/HD-PDEase/cyclic-di-GMP phosphodiesterase-family evidence routes it to `modules/c_di_gmp_turnover_boundary.yaml`.
- Completed `dna_binding_response_regulator_spillover`: PP_2403 was initially pulled in by a CheY-like product name, but OmpR/PhoB DNA-binding response-regulator evidence routes it to `modules/orphan_two_component_regulators_boundary.yaml`.
- Completed `chey_like_membrane_accessory_spillovers`: PP_3757, PP_3771, and PP_4331 are curated into `modules/chemotaxis_adaptation_accessory_boundary.yaml` as one compact CheY-like response-regulator candidate and two conservative membrane accessory candidates.
- Completed `outer_membrane_flagellation_name_spillover`: ycfJ is routed to `modules/transport_envelope_spillover_boundary.yaml` as an outer-membrane lipoprotein/surface-antigen-family protein.
- Completed `flagellar_export_localization_accessory_spillovers`: PP_4328, PP_4329, PP_4342, flhF, and PP_4377 are curated into `modules/flagellar_export_assembly_boundary.yaml` as hook-control, export-gate, FlhG/FleN-family, FlhF, and FlaG accessory context.
- Completed `c_di_gmp_flagellar_brake_spillover`: ycgR is routed to `modules/flagellar_motor_switch_stator_boundary.yaml` as a PilZ-domain c-di-GMP-dependent motor brake.
- All 35 motility/chemotaxis/biofilm functional-bucket genes are now first-pass curated.
- Run real Falcon module/pathway commands only after selecting a concrete module; current Edison Falcon access failure mode is HTTP 402.
