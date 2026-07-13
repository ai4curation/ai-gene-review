---
title: "PSEPK ppu02020 Two-component system partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu02020: Two-component system partition

KEGG ppu02020 is an umbrella map, not a single satisfiable module. This
partition keeps the primary 99-gene PSEPK batch as a triage table and
splits it into curation-scale systems.

## Outputs

- Source batch: `projects/P_PUTIDA/batches/ppu02020_two_component_system_boundary.tsv`
- Partition table: `projects/P_PUTIDA/batches/ppu02020_two_component_system_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Status | Example genes |
|---|---:|---|---|---|---|
| `dna_replication_spillover` | 1 | `bacterial_dna_replication` | SIDE_CONTEXT | CURATED | `dnaA` |
| `heavy_metal_copper_zinc_response` | 13 | `metal_cation_response_efflux_boundary` | NEW_SUBMODULE | CURATED | `czcR-I`, `czrSA`, `czcR-II`, `PP_1437`, `czcR-III`, `PP_2157`, `copR-I`, `copR-II` |
| `iron_uptake_regulation` | 10 | `iron_uptake_regulation_boundary` | NEW_SUBMODULE | CURATED | `pfeS-I`, `PP_0534`, `PP_1651`, `pfeS-II`, `fepA`, `PP_3576`, `fecI`, `PP_4607` |
| `alginate_biofilm_regulation` | 6 | `alginate_biofilm_regulation_boundary` | NEW_SUBMODULE | CURATED | `kinB`, `algB`, `algR`, `wspC`, `fleS`, `PP_4696` |
| `osmotic_envelope_efflux_regulation` | 7 | `osmotic_envelope_efflux_regulation_boundary` | NEW_SUBMODULE | CURATED | `ompR`, `envZ`, `PP_2100`, `evgA`, `mdtC`, `mdtB`, `mdtA` |
| `dicarboxylate_tricarboxylate_transport_regulation` | 19 | `dicarboxylate_tricarboxylate_transport_regulation_boundary` | NEW_SUBMODULE | CURATED | `dctD-I`, `PP_0264`, `uhpA`, `dctD-II`, `PP_1067`, `PP_1167`, `PP_1168`, `dctP` |
| `ecf_sigma_anti_sigma` | 10 | `ecf_sigma_anti_sigma_boundary` | NEW_SUBMODULE | CURATED | `PP_0161`, `PP_0162`, `PP_0351`, `PP_0352`, `PP_0667`, `PP_0703`, `PP_0704`, `PP_0866` |
| `nitrogen_phosphate_potassium_homeostasis` | 10 | `inorganic_nutrient_homeostasis_regulation_boundary` | NEW_SUBMODULE | CURATED | `glnD`, `glnL`, `glnG`, `phoB`, `phoR`, `kdpD`, `kdpC`, `kdpB` |
| `pili_surface_adhesion` | 12 | `pili_surface_adhesion_boundary` | NEW_SUBMODULE | CURATED | `pilA`, `fimD`, `PP_1890`, `PP_2356`, `PP_2357`, `PP_2358`, `PP_2359`, `PP_2360` |
| `orphan_generic_tcs` | 10 | `orphan_two_component_regulators_boundary` | NEW_SUBMODULE | CURATED | `PP_0574`, `PP_0887`, `regA`, `PP_1007`, `bvgA`, `PP_1181`, `PP_1182`, `PP_2671` |
| `protein_phosphatase_spillover` | 1 | `protein_phosphorylation_boundary` | SIDE_CONTEXT | CURATED | `etp` |

## Working Decisions

- Treat `modules/two_component_relay.yaml` as the reusable motif, not as
  the PSEPK ppu02020 umbrella module.
- Do not fetch and curate all 99 genes as one PR. Create smaller boundary
  modules from the partition table, starting with high-signal paired
  systems such as Dct/Tct transport regulation, nutrient homeostasis,
  and orphan/generic TCS systems.
- Transporter, efflux, pili, and housekeeping genes should remain in the
  relevant transport/envelope/replication modules unless the local
  regulatory system needs them as boundary context.
- `dnaA` and `etp` are side-context spillovers for this KEGG map and should
  not be used as evidence for two-component signaling.

## Completed Sub-batches

- `nitrogen_phosphate_potassium_homeostasis`: first-pass gene reviews,
  Asta gene research, and
  `modules/inorganic_nutrient_homeostasis_regulation_boundary.yaml` are
  complete for GlnD/NtrB/NtrC, PhoR/PhoB, and KdpD/KdpE/KdpFABC.
- `dna_replication_spillover`: first-pass gene review and Asta gene
  research are complete for dnaA, and dnaA has been added to
  `modules/bacterial_dna_replication.yaml` as replication-origin
  recognition/initiation side context from ppu02020.
- `protein_phosphatase_spillover`: first-pass gene review, Asta gene
  research, and `modules/protein_phosphorylation_boundary.yaml` are
  complete for Etp protein tyrosine phosphatase side context.
- Falcon taxon-aware module/pathway research for
  `inorganic_nutrient_homeostasis_regulation_boundary` + `ppu02020` +
  PSEPK was attempted with the real command and failed with HTTP 402, so
  no Falcon report is cited for this sub-batch.
- `iron_uptake_regulation`: first-pass gene reviews, Asta gene
  research, and `modules/iron_uptake_regulation_boundary.yaml` are
  complete for PfeS/PfeR-like two-component regulators, FepA
  siderophore-iron uptake, and FecI/FecR-like ECF sigma regulation.
- Falcon taxon-aware module/pathway research for
  `iron_uptake_regulation_boundary` + `ppu02020` + PSEPK was
  attempted with the real command and failed with HTTP 402, so no
  Falcon report is cited for this sub-batch.
- `osmotic_envelope_efflux_regulation`: first-pass gene reviews,
  Asta gene research, and
  `modules/osmotic_envelope_efflux_regulation_boundary.yaml` are
  complete for EnvZ/OmpR, PP_2100/EvgA-like regulation, and
  MdtABC efflux-pump context.
- Falcon taxon-aware module/pathway research for
  `osmotic_envelope_efflux_regulation_boundary` + `ppu02020` +
  PSEPK was attempted with the real command and failed with HTTP 402,
  so no Falcon report is cited for this sub-batch.
- `alginate_biofilm_regulation`: first-pass gene reviews, Asta
  gene research, and
  `modules/alginate_biofilm_regulation_boundary.yaml` are
  complete for KinB/AlgB, AlgR, WspC/CheR1 biofilm control,
  FleS, and PP_4696 surface-behavior regulatory context.
- Falcon taxon-aware module/pathway research for
  `alginate_biofilm_regulation_boundary` + `ppu02020` + PSEPK
  was attempted with the real command and failed with HTTP 402,
  so no Falcon report is cited for this sub-batch.
- `ecf_sigma_anti_sigma`: first-pass gene reviews, Asta gene
  research, and `modules/ecf_sigma_anti_sigma_boundary.yaml` are
  complete for the PP_0161/PP_0162, PP_0351/PP_0352,
  PP_0703/PP_0704, and PP_3085/PP_3086 local pairs plus the
  orphan PP_0667 ECF sigma factor and PP_0866 FecR-like sensor.
- Falcon taxon-aware module/pathway research for
  `ecf_sigma_anti_sigma_boundary` + `ppu02020` + PSEPK was
  attempted with the real command and failed with HTTP 402,
  so no Falcon report is cited for this sub-batch.
- `heavy_metal_copper_zinc_response`: first-pass gene reviews,
  Asta gene research, and
  `modules/metal_cation_response_efflux_boundary.yaml` are complete
  for Czc/Cop/Cus response regulators, CztS/SilS/CopS-like sensor
  kinases, and the czcC-cusBAF copper/cation efflux locus.
- Falcon taxon-aware module/pathway research for
  `metal_cation_response_efflux_boundary` + `ppu02020` + PSEPK
  was attempted with the real command and failed with HTTP 402,
  so no Falcon report is cited for this sub-batch.
- `pili_surface_adhesion`: first-pass gene reviews, Asta gene
  research, and `modules/pili_surface_adhesion_boundary.yaml` are
  complete for PilA type IV pilin context, a FimC/FimD-like
  chaperone-usher pair, the PP_2356/PP_2357-PP_2363 Csu-like
  surface-adhesion cluster, and PP_3126 polysaccharide-export
  side context.
- Falcon taxon-aware module/pathway research for
  `pili_surface_adhesion_boundary` + `ppu02020` + PSEPK was
  attempted with the real command and failed with HTTP 402,
  so no Falcon report is cited for this sub-batch.
- `orphan_generic_tcs`: first-pass gene reviews, Asta gene
  research, and `modules/orphan_two_component_regulators_boundary.yaml`
  are complete for PP_0887/regA, PP_1182/PP_1181,
  PP_3413/PP_3412, orphan PP_0574, bvgA, PP_2671, and
  the FecR-like PP_1007 anti-sigma sensor side context.
- Falcon taxon-aware module/pathway research for
  `orphan_two_component_regulators_boundary` + `ppu02020` + PSEPK
  was attempted with the real command and failed with HTTP 402,
  so no Falcon report is cited for this sub-batch.

## Next Steps

- Keep ppu02020 registered as `PARTITIONED` in the pathway worklist rather
  than `NEEDS_MODULE_MAPPING`.
- ppu02020 now has review and Asta coverage for all 99 partition-table
  genes; continue with another pathway partition rather than reopening
  the 99-gene two-component-system umbrella.
- Run real Falcon module/pathway commands only for selected submodules; the
  current Edison Falcon access failure mode is HTTP 402.
