---
title: "PSEPK ppu02040 Flagellar assembly partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu02040: Flagellar assembly partition

KEGG ppu02040 is a coherent flagellar biology map, but the PSEPK
primary set is too broad for one first-pass curation batch. It mixes
structural apparatus, export/assembly factors, motor components,
regulators, and a few nonflagellar transport/envelope side entries.

## Outputs

- Source batch: `projects/P_PUTIDA/batches/ppu02040_bacterial_flagellar_assembly_boundary.tsv`
- Partition table: `projects/P_PUTIDA/batches/ppu02040_bacterial_flagellar_assembly_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Example genes |
|---|---:|---|---|---|
| `flagellar_regulation_sigma_master_control` | 6 | `flagellar_regulation_boundary` | NEW_SUBMODULE | `rpoD`, `rpoN`, `fliA`, `atoC`, `fleQ`, `flgM` |
| `nonflagellar_transport_envelope_spillovers` | 3 | `transport_envelope_spillover_boundary` | EXISTING_OR_REUSE | `fliY`, `PP_1087`, `PP_5157` |
| `flagellar_export_assembly_chaperones` | 14 | `flagellar_export_assembly_boundary` | NEW_SUBMODULE | `flhA`, `flhB`, `fliR`, `fliQ`, `fliP`, `fliO`, `fliK`, `fliJ` |
| `flagellar_basal_body_hook_filament` | 15 | `flagellar_basal_body_hook_filament_boundary` | NEW_SUBMODULE | `fliF`, `fliE`, `fliD`, `fliC`, `flgL`, `flgK`, `flgJ`, `flgI` |
| `flagellar_motor_switch_stator` | 9 | `flagellar_motor_switch_stator_boundary` | NEW_SUBMODULE | `PP_4335`, `PP_4336`, `fliN`, `fliM`, `fliL`, `fliG`, `motB`, `motA` |

## Working Decisions

- Do not curate all 47 primary genes as one first-pass flagellar PR.
- Keep `fliY`, `PP_1087`, and `PP_5157` out of the flagellar apparatus
  core unless specific evidence ties them to flagellum assembly.
- Separate global sigma/master regulation from structural apparatus
  curation so broad transcription annotations do not dominate the module.
- The strongest flagellar-apparatus batches are export/assembly,
  basal-body/hook/filament, and motor/switch/stator.

## Completed First-Pass Sub-Batches

- `flagellar_motor_switch_stator`: 9/9 genes now have review folders,
  Asta reports, first-pass curation, rendered gene pages, and a
  validated/rendered module
  (`modules/flagellar_motor_switch_stator_boundary.yaml`). PP_4335
  and PP_4336 are treated as MotD/MotC aliases for the MotCD stator,
  while FliL paralog roles remain unresolved.
- `flagellar_export_assembly_chaperones`: 14/14 genes now have
  review folders, Asta reports, first-pass curation, rendered gene
  pages, and a validated/rendered module
  (`modules/flagellar_export_assembly_boundary.yaml`). The batch
  separates the membrane export gate, FliI/FliH/FliJ export-energy
  module, hook-length control, and late assembly/chaperone support.
- `flagellar_basal_body_hook_filament`: 15/15 genes now have
  review folders, Asta reports, first-pass curation, rendered gene
  pages, and a validated/rendered module
  (`modules/flagellar_basal_body_hook_filament_boundary.yaml`).
  The batch separates MS-ring/early basal body, rod/peptidoglycan
  clearance, P/L rings, hook/hook-filament junction, and
  filament/cap structural layers.
- `flagellar_regulation_sigma_master_control`: 6/6 genes now have
  review folders, Asta reports, first-pass curation, rendered gene
  pages, and a validated/rendered module
  (`modules/flagellar_regulation_boundary.yaml`). The batch
  separates housekeeping sigma context, RpoN/sigma-54, FliA
  sigma-28, FleQ/AtoC-like activators, and the FlgM anti-sigma
  checkpoint.
- `nonflagellar_transport_envelope_spillovers`: 3/3 genes now
  have review folders, Asta reports, first-pass curation, rendered
  gene pages, and a validated/rendered boundary module
  (`modules/transport_envelope_spillover_boundary.yaml`). The
  batch keeps fliY, PP_1087, and PP_5157 outside the flagellar
  apparatus core unless direct evidence emerges.

## Next Steps

- The ppu02040 first-pass partition is complete: all five buckets
  now have curated/researched gene reviews and validated/rendered
  modules or boundary modules.
- Keep the spillover module out of the flagellar apparatus core
  unless direct functional evidence emerges.
- Run real Falcon module/pathway commands only after a concrete submodule
  is selected; current Edison Falcon access failure mode is HTTP 402.
