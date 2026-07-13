---
title: "PSEPK chromosome/cell-cycle functional-bucket partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK chromosome/cell-cycle functional-bucket partition

The `module:chromosome_partition_cell_cycle` bucket is a functional
umbrella assembled from UniProt names and keywords. It mixes chromosome
partition/condensation proteins, divisome/septation proteins, the MinCDE
septum-site-selection system, Tol-Pal envelope/division coordination,
DNA dimer resolution/translocation, and two broad keyword spillovers.

## Outputs

- Source table: `projects/P_PUTIDA/data/psepk_pathway_partition.tsv`
- Full partition table: `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_partition.tsv`
- Completed Min-system batch: `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_min_system.tsv`
- Completed divisome/Z-ring batch: `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_divisome.tsv`
- Completed Xer/FtsK batch: `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_xer_ftsk.tsv`
- Completed Tol-Pal batch: `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_tol_pal.tsv`
- Completed chromosome partition/condensation batch: `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_partition_condensation.tsv`
- Completed broad spillover batch: `projects/P_PUTIDA/batches/module_chromosome_partition_cell_cycle_spillovers.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Example genes |
|---|---:|---|---|---|
| `chromosome_partition_condensation_boundary` | 11 | `chromosome_partition_condensation_boundary` | COMPLETED_SUBMODULE | `parB`, `PP_0693`, `PP_0694`, `PP_2161`, `PP_2412`, `PP_3700`, `smc`, `PP_4334` |
| `chromosome_dimer_resolution_and_dna_translocation_boundary` | 4 | `chromosome_dimer_resolution_dna_translocation_boundary` | COMPLETED_SUBMODULE | `xerD`, `PP_2841`, `ftsK`, `xerC` |
| `divisome_z_ring_and_septation_boundary` | 12 | `divisome_z_ring_septation_boundary` | COMPLETED_SUBMODULE | `engB`, `PP_1309`, `zapE`, `ftsL`, `ftsQ`, `ftsA`, `ftsZ`, `ftsB` |
| `min_system_septum_site_selection_boundary` | 3 | `min_system_septum_site_selection_boundary` | COMPLETED_SUBMODULE | `minE`, `minD`, `minC` |
| `tol_pal_cell_division_envelope_coordination_boundary` | 5 | `tol_pal_cell_division_envelope_coordination_boundary` | COMPLETED_SUBMODULE | `tolQ`, `tolR`, `tolB`, `pal`, `cpoB` |
| `side_spillover_general_cell_cycle_terms` | 2 | `(none)` | COMPLETED_REASSIGN_OR_KEEP_OUT | `PP_1105`, `tig` |

## Working Decisions

- Do not curate the 37-gene functional bucket as one satisfiable module.
- Treat MinCDE as the first completed sub-batch because minC, minD,
  and minE are adjacent, coherent, Asta-backed, and have direct
  septum-site-selection GO evidence.
- Keep Tol-Pal, divisome/Z-ring, chromosome partition/condensation,
  and Xer/FtsK DNA-resolution/translocation as separate sub-batches.
- Keep PP_1105 and tig out of this module unless future evidence ties
  them directly to a cell-cycle mechanism beyond broad keyword context.

## Completed Sub-batches

- `min_system_septum_site_selection_boundary`: minC, minD, and minE
  are fetched, Asta-backed, first-pass curated, validated, and
  represented in `modules/min_system_septum_site_selection_boundary.yaml`.
- `divisome_z_ring_and_septation_boundary`: engB, PP_1309, zapE,
  ftsL, ftsQ, ftsA, ftsZ, ftsB, dedD, zipA, PP_5090, and PP_5202
  are fetched or reused, Asta-backed, first-pass curated, validated,
  and represented in `modules/divisome_z_ring_septation_boundary.yaml`.
- `chromosome_dimer_resolution_dna_translocation_boundary`: xerC,
  xerD, ftsK, and PP_2841 are fetched, Asta-backed, first-pass
  curated, validated, and represented in
  `modules/chromosome_dimer_resolution_dna_translocation_boundary.yaml`.
- `tol_pal_cell_division_envelope_coordination_boundary`: tolQ,
  tolR, tolA, tolB, pal, and cpoB are fetched, Asta-backed,
  first-pass curated, validated, and represented in
  `modules/tol_pal_cell_division_envelope_coordination_boundary.yaml`.
- `chromosome_partition_condensation_boundary`: parB, PP_0002,
  PP_0693, PP_0694, PP_2161, PP_2412, PP_3700, smc, PP_4334,
  PP_4497, scpA, and PP_5070 are fetched, Asta-backed,
  first-pass curated, validated, and represented in
  `modules/chromosome_partition_condensation_boundary.yaml`.
- `side_spillover_general_cell_cycle_terms`: PP_1105 and tig are
  fetched or reused, Asta-backed, first-pass curated, validated,
  and intentionally kept outside a chromosome/cell-cycle module.

## Next Steps

- No primary genes remain in this functional bucket for first-pass
  curation; future work should revisit unresolved candidate roles
  only as deeper biology questions.
