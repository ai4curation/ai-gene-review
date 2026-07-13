---
title: "PSEPK transport/membrane/efflux functional-bucket partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK transport/membrane/efflux functional-bucket partition

The `module:transport_membrane_efflux` bucket is a large UniProt
name/keyword umbrella. It mixes transport systems, outer-membrane
receptors and porins, secretion/export components, efflux pumps, ion
homeostasis proteins, redox membrane proteins, envelope-polysaccharide
context, signaling channels, and low-information membrane proteins. It
is not satisfiable as one biological module.

## Outputs

- Source table: `projects/P_PUTIDA/data/psepk_pathway_partition.tsv`
- Full partition table: `projects/P_PUTIDA/batches/module_transport_membrane_efflux_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Status | Example genes |
|---|---:|---|---|---|---|
| `already_promoted_or_reused_transport_context` | 2 | `(none)` | EXISTING_OR_REUSE | CURATED_OR_ROUTED | `pilD`, `tolA` |
| `lpt_lps_transport_context` | 2 | `lpt_lps_transport_boundary` | EXISTING_OR_REUSE | CURATED | `lptA`, `lptC` |
| `tonb_exbb_exbd_energy_transduction` | 7 | `tonb_dependent_transport_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0696`, `PP_1512`, `PP_1898`, `PP_1899`, `exbB`, `exbD`, `tonB` |
| `tonb_dependent_outer_membrane_receptors` | 30 | `tonb_dependent_transport_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0160`, `PP_0267`, `PP_0272`, `PP_0350`, `PP_0525`, `PP_0535`, `PP_0669`, `PP_0861` |
| `protein_export_secretion_outer_membrane_assembly` | 15 | `protein_export_secretion_outer_membrane_assembly_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0573`, `PP_0575`, `PP_0607`, `bamD`, `PP_0716`, `lolB`, `PP_0855`, `bamB` |
| `rnd_tripartite_efflux_and_mfp_omf_systems` | 42 | `rnd_multidrug_efflux_boundary` | COMPLETED_SUBMODULE | CURATED | `czcA-I`, `czcB-I`, `czcC-I`, `PP_0166`, `PP_0178`, `PP_0179`, `PP_0715`, `PP_0803` |
| `mfs_drug_metabolite_transporters` | 80 | `mfs_drug_metabolite_transport_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0057`, `PP_0288`, `yajR`, `PP_0503`, `PP_0523`, `ydgK`, `fsr-I`, `PP_0702` |
| `dmt_eama_small_drug_metabolite_transporters` | 21 | `dmt_eama_transport_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0358`, `PP_1166`, `sugE`, `PP_1753`, `PP_2231`, `rhtA`, `eamA`, `PP_2949` |
| `outer_membrane_porins_channels_autotransporters` | 38 | `transport_envelope_spillover_boundary` | COMPLETED_SUBMODULE | CURATED | `oprP`, `opdT-I`, `oprE`, `oprQ`, `estP`, `oprG`, `opdC`, `opdP` |
| `amino_acid_peptide_polyamine_abc_importers` | 15 | `amino_acid_peptide_polyamine_abc_transport_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0656`, `PP_0657`, `PP_2384`, `PP_3593`, `PP_3594`, `PP_3595`, `PP_4426`, `PP_4427` |
| `metal_siderophore_anion_abc_transporters` | 11 | `metal_siderophore_anion_abc_transport_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_2416`, `PP_2417`, `PP_2592`, `PP_2593`, `fatD`, `PP_2731`, `PP_2821`, `PP_3804` |
| `sugar_nucleoside_abc_transporters` | 1 | `sugar_nucleoside_abc_transport_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_1030` |
| `generic_abc_transporters` | 33 | `generic_abc_transport_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0386`, `PP_0506`, `PP_0507`, `PP_1737`, `PP_1760`, `yadG`, `PP_2119`, `PP_2316` |
| `ion_metal_transporters_and_antiporters` | 102 | `ion_metal_transport_boundary` | SUBPARTITIONED | CURATED | `PP_0026`, `cadA-I`, `trkA`, `PP_0093`, `PP_0111`, `PP_0125`, `cc`, `PP_0144` |
| `amino_acid_quaternary_amine_nucleobase_transporters` | 55 | `amino_acid_amine_nucleobase_transport_boundary` | COMPLETED_SUBMODULE | CURATED | `gltP`, `PP_0198`, `betT-II`, `gabP-I`, `PP_0544`, `mmuP`, `PP_0699`, `uraA` |
| `carbohydrate_nucleoside_transporters` | 14 | `carbohydrate_nucleoside_transport_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0138`, `PP_0652`, `PP_0709`, `PP_1740`, `PP_2860`, `PP_3048`, `PP_3142`, `codB` |
| `organic_acid_aromatic_anion_transporters` | 7 | `organic_acid_aromatic_anion_transport_boundary` | COMPLETED_SUBMODULE | CURATED | `citN`, `PP_1820`, `benE-I`, `bhbP`, `benE-II`, `PP_3247`, `lldP` |
| `inorganic_nutrient_transporters` | 13 | `inorganic_nutrient_transport_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0075`, `PP_0101`, `yjbB`, `modR`, `PP_0718`, `cysZ`, `pitB`, `PP_1407` |
| `membrane_redox_electron_transfer_proteins` | 24 | `membrane_redox_electron_transfer_boundary` | COMPLETED_SUBMODULE | CURATED | `dsbB2`, `PP_0251`, `trx`, `dsbD-I`, `dsbB1`, `PP_1093`, `rnfG`, `rnfD` |
| `membrane_signaling_channels_c_di_gmp_spillovers` | 39 | `c_di_gmp_turnover_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0131`, `PP_0165`, `PP_0197`, `PP_0218`, `PP_0369`, `PP_0668`, `PP_0672`, `PP_0700` |
| `envelope_polysaccharide_export_and_flippase_context` | 13 | `envelope_polysaccharide_export_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0033`, `PP_0034`, `PP_0035`, `yceG`, `PP_3127`, `PP_3131`, `PP_3132`, `PP_3135` |
| `lipoprotein_envelope_accessory_spillovers` | 3 | `transport_envelope_spillover_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_1501`, `PP_2304`, `csgG` |
| `stress_resistance_membrane_spillovers` | 20 | `stress_detoxification_spillover_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0598`, `PP_0599`, `PP_1264`, `PP_1425`, `PP_1487`, `PP_1559`, `PP_1576`, `PP_2076` |
| `membrane_associated_enzymes_and_side_nodes` | 42 | `transport_membrane_enzyme_spillover_boundary` | COMPLETED_SUBMODULE | CURATED | `nfeD`, `desA`, `PP_0332`, `PP_0923`, `PP_1033`, `PP_1058`, `degS`, `PP_1368` |
| `other_domain_resolved_membrane_proteins` | 83 | `transport_membrane_domain_spillover_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0054`, `PP_0107`, `ygdQ`, `PP_0176`, `PP_0241`, `djlA`, `PP_0487`, `PP_0621` |
| `low_information_membrane_proteins` | 67 | `low_information_membrane_protein_boundary` | COMPLETED_SUBMODULE | CURATED | `PP_0007`, `PP_0027`, `PP_0108`, `PP_0349`, `yqaE`, `PP_0439`, `dedA`, `PP_0790` |

## Working Decisions

- Do not curate the 779-gene transport/membrane/efflux bucket as one module.
- Prioritize system-resolved transport families first: TonB-dependent uptake,
  RND tripartite efflux, ABC import/export components, MFS/DMT transporters,
  and ion/metal antiporters.
- Reuse existing modules when a row is clearly a missing member of a prior
  pathway boundary, such as Lpt/LPS transport, protein export/secretion,
  c-di-GMP turnover, stress/detoxification, or transport-envelope spillovers.
- Keep substrate claims conservative for generic permeases; product names and
  domain families are often sufficient for a transport-family core function
  but not for a specific solute.
- Treat low-information membrane proteins as a last-pass unresolved bucket.
