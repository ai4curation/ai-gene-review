---
title: "PSEPK cell-envelope/division functional-bucket partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK cell-envelope/division functional-bucket partition

The `module:cell_envelope_division` bucket is a UniProt
name/keyword umbrella. It mixes Lpt/LPS outer-membrane assembly,
lipid-A/LPS-core biosynthesis, peptidoglycan turnover, cell-division
regulatory spillovers, VacJ/MlaA phospholipid-asymmetry context,
ApbE-like envelope flavinylation, outer-membrane barrels/channels,
and many domain-resolved or generic lipoprotein spillovers.

## Outputs

- Source table: `projects/P_PUTIDA/data/psepk_pathway_partition.tsv`
- Full partition table: `projects/P_PUTIDA/batches/module_cell_envelope_division_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Status | Example genes |
|---|---:|---|---|---|---|
| `lpt_outer_membrane_lps_transport_context` | 2 | `lpt_lps_transport_boundary` | EXISTING_OR_REUSE | CURATED | `lptD`, `lptE` |
| `lps_core_lipid_a_biosynthesis_context` | 2 | `lipopolysaccharide_biosynthesis` | NEXT_SUBMODULE | CURATED | `PP_3016`, `PP_3134` |
| `maltose_acetyltransferase_lipid_a_keyword_spillover` | 1 | `(none)` | COMPLETED_REASSIGN_OR_KEEP_OUT | CURATED | `maa` |
| `peptidoglycan_turnover_remodeling_candidates` | 11 | `peptidoglycan_biosynthesis` | EXISTING_OR_REUSE | CURATED | `amiD`, `ampD`, `rlpA__Q88PC1`, `mltF`, `PP_1325`, `PP_2147`, `PP_3562`, `pbpG` |
| `cell_division_regulatory_spillovers` | 3 | `divisome_z_ring_septation_boundary` | EXISTING_OR_REUSE | CURATED | `sulA`, `PP_2199`, `PP_2352` |
| `vacj_phospholipid_asymmetry_context` | 1 | `mla_phospholipid_transport_boundary` | EXISTING_OR_REUSE | CURATED | `vacJ` |
| `apbe_fmn_transferase_spillover` | 1 | `ccm_heme_export_cytochrome_c_maturation_boundary` | EXISTING_OR_REUSE | CURATED | `PP_2150` |
| `outer_membrane_barrel_channel_autotransporter_context` | 8 | `transport_envelope_spillover_boundary` | NEW_OR_REUSE_BOUNDARY | CURATED | `yiaD`, `PP_1121`, `PP_1122`, `PP_1880`, `PP_3069`, `PP_3449`, `PP_4291`, `PP_4293` |
| `named_outer_membrane_lipoprotein_families` | 9 | `transport_envelope_spillover_boundary` | NEW_OR_REUSE_BOUNDARY | CURATED | `uxpA`, `slyB`, `oprI`, `PP_3236`, `yaiW`, `PP_4032`, `PP_4855`, `PP_5037` |
| `domain_resolved_lipoprotein_spillovers` | 30 | `transport_envelope_spillover_boundary` | NEW_OR_REUSE_BOUNDARY | CURATED | `PP_0116`, `PP_0139`, `PP_0512`, `PP_0549`, `PP_0576`, `PP_0753`, `PP_1115`, `PP_1146` |
| `generic_lipoprotein_signal_spillovers` | 30 | `transport_envelope_spillover_boundary` | NEW_OR_REUSE_BOUNDARY | CURATED | `PP_0091`, `PP_0092`, `PP_0277`, `PP_0677`, `PP_1204`, `PP_1498`, `PP_2197`, `PP_2252` |

## Working Decisions

- Do not curate the 98-gene functional bucket as one satisfiable module.
- Treat LptD/LptE as already curated Lpt/LPS-transport context.
- The first follow-up batch is the LPS-core/lipid-A split: PP_3016
  and PP_3134 connect to the existing `lipopolysaccharide_biosynthesis`
  module, while maa is recorded separately as a lipid-A-keyword spillover
  whose first-pass review supports maltose O-acetyltransferase activity.
- The cell-division regulatory spillover split is complete: sulA,
  PP_2199, and PP_2352 connect to the existing
  `divisome_z_ring_septation_boundary` module as SulA regulatory
  context and candidate ZapE-like ATPases.
- The VacJ/MlaA singleton split is complete: vacJ connects to the
  existing `mla_phospholipid_transport_boundary` module as MlaA-family
  lipoprotein context for intermembrane phospholipid transfer.
- The ApbE/FMNylylation singleton split is complete: PP_2150 connects
  to the existing `ccm_heme_export_cytochrome_c_maturation_boundary`
  module as related envelope flavoprotein maturation context rather
  than as a CcmABCD heme-export component.
- The peptidoglycan turnover/remodeling split is complete: amiD,
  ampD, rlpA/Q88PC1, mltF, PP_1325, PP_2147, PP_3562, pbpG,
  rlpA/Q88DM1, PP_4971, and PP_5354 connect to the existing
  `peptidoglycan_biosynthesis` module as turnover, remodeling,
  binding, or cell-wall assembly candidates.
- The outer-membrane barrel/channel/autotransporter, named
  lipoprotein-family, domain-resolved lipoprotein, and generic
  lipoprotein/signal-peptide splits are complete and represented in
  the existing `transport_envelope_spillover_boundary` module.
- The generic lipoprotein/signal-peptide set remains low-specificity
  in the module: all 30 entries are broad membrane/envelope candidates
  without pathway, partner, or molecular-function assignments.
