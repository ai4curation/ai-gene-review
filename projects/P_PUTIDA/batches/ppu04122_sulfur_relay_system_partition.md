---
title: "PSEPK ppu04122 Sulfur relay system partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu04122: Sulfur relay system partition

KEGG ppu04122 is a sulfur-transfer umbrella. The PSEPK primary set
mixes molybdopterin/MoCo sulfur-carrier chemistry, Tus/MnmA tRNA
thiolation, ThiS thiamine sulfur-carrier context, and general
rhodanese/mercaptopyruvate sulfurtransferase side nodes.

## Outputs

- Source batch: `projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_boundary.tsv`
- Partition table: `projects/P_PUTIDA/batches/ppu04122_sulfur_relay_system_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Example genes |
|---|---:|---|---|---|
| `molybdopterin_moco_sulfur_relay` | 9 | `molybdopterin_biosynthesis_sulfur_relay_boundary` | NEW_SUBMODULE | `moeB`, `moaC`, `moaD`, `moaE`, `PP_1969`, `moaB-I`, `PP_2482`, `moaA` |
| `tus_mnma_trna_thiolation` | 7 | `mnma_tus_trna_thiolation_boundary` | NEW_SUBMODULE | `tusA-I`, `tusA`, `tusD`, `PP_3994`, `PP_3995`, `tusE`, `mnmA` |
| `thiamine_this_sulfur_carrier` | 1 | `thiamine_biosynthesis` | EXISTING_OR_REUSE | `PP_5105` |
| `rhodanese_mercaptopyruvate_side_nodes` | 2 | `sulfur_metabolism_boundary` | EXISTING_OR_REUSE | `rhdA`, `sseA` |

## Working Decisions

- Do not curate all 19 primary genes as one generic sulfur-relay PR.
- Keep MoaD/MoeB molybdopterin sulfur-carrier chemistry separate from
  ThiS thiamine sulfur-carrier and Tus/MnmA tRNA thiolation.
- Keep `rhdA` and `sseA` with sulfur-metabolism sulfurtransferase context
  unless a specific sulfur-relay mechanism is selected.
- `PP_5105` already belongs with the thiamine-biosynthesis ThiS gap-fill.

## Completed Sub-batches

- `tus_mnma_trna_thiolation`: seven genes fetched, Asta-backed,
  first-pass curated, validated, and rendered; new module
  `modules/mnma_tus_trna_thiolation_boundary.yaml` created and
  validated. `tusA-I` and `PP_3994` have no fetched GOA rows, so
  their inferred roles are recorded in `core_functions` and module
  knowledge gaps rather than as synthetic `existing_annotations`.
- `molybdopterin_moco_sulfur_relay`: nine genes present,
  Asta-backed, first-pass curated, and validated; new module
  `modules/molybdopterin_biosynthesis_sulfur_relay_boundary.yaml`
  created and validated. `moeB` was curated as the MoaD
  adenylyltransferase, with rhodanese/sulfotransferase
  over-propagations removed, and `moaD` was curated as the sulfur
  carrier subunit of molybdopterin synthase.

## Next Steps

- The primary ppu04122 curation gaps are now closed at first pass:
  all 19 primary genes have review folders, Asta reports, and
  curated review YAMLs.
- Keep `PP_5105` with thiamine biosynthesis and `rhdA`/`sseA` with
  sulfur-metabolism sulfurtransferase context unless a future
  sulfur-relay-specific mechanism is selected.
- Rerun real Falcon module/pathway commands only when Edison Falcon
  access is available; current failure mode is HTTP 402.
