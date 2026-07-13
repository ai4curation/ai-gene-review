---
title: "PSEPK ppu02024 Quorum sensing partition"
maturity: DRAFT
tags: [BIOLOGY_DOMAIN, PIPELINE]
species: [PSEPK]
autolink_gene_symbols: false
---

# PSEPK ppu02024: Quorum sensing partition

KEGG ppu02024 is an umbrella map in PSEPK. The primary 60-gene set
does not define a single LuxI/LuxR quorum-sensing module; it is mostly
transport, response-regulator, efflux, and surface-context genes.

## Outputs

- Source batch: `projects/P_PUTIDA/batches/ppu02024_quorum_sensing_boundary.tsv`
- Partition table: `projects/P_PUTIDA/batches/ppu02024_quorum_sensing_partition.tsv`

## Partition Summary

| Bucket | Genes | Proposed module | Action | Example genes |
|---|---:|---|---|---|
| `fur_iron_regulation_spillover` | 1 | `iron_homeostasis_regulation_boundary` | SIDE_CONTEXT | `fur__Q88RL0` |
| `polyamine_abc_import` | 13 | `polyamine_transport_boundary` | EXISTING_OR_REUSE | `potA`, `PP_0412`, `PP_0413`, `PP_0414`, `ydcV`, `ydcU`, `ydcT`, `ydcS` |
| `branched_chain_amino_acid_abc_import` | 25 | `branched_chain_amino_acid_abc_import_boundary` | EXISTING_OR_REUSE | `PP_0615`, `PP_0616`, `PP_0617`, `PP_0618`, `PP_0619`, `livF-I`, `livG`, `livM` |
| `surface_adhesion_singleton` | 1 | `surface_adhesion_boundary` | DEFER | `PP_0806` |
| `phosphonate_abc_import` | 4 | `phosphonate_phosphinate_metabolism` | EXISTING_OR_REUSE | `PP_1722`, `PP_1723`, `PP_1724`, `PP_1726` |
| `rnd_multidrug_efflux` | 2 | `rnd_multidrug_efflux_boundary` | NEW_SUBMODULE | `PP_2064`, `PP_2065` |
| `qsebc_like_two_component_regulation` | 5 | `qsebc_like_two_component_regulation_boundary` | NEW_SUBMODULE | `PP_2713`, `PP_2714`, `kdpE`, `PP_4224`, `qseB` |
| `peptide_opine_glutathione_abc_import` | 8 | `peptide_opine_glutathione_abc_import_boundary` | NEW_SUBMODULE | `PP_3220`, `PP_3221`, `PP_3222`, `PP_3223`, `gsiA`, `PP_4454`, `gsiC`, `PP_4458` |
| `dmt_transporter_singleton` | 1 | `dmt_transporter_boundary` | DEFER | `PP_3609` |

## Working Decisions

- Do not curate all 60 primary genes as one quorum-sensing PR.
- The largest component is branched-chain amino-acid ABC import, already
  represented by a transport submodule; keep it out of a quorum-sensing
  core module.
- Polyamine import is biologically adjacent to signaling and biofilm
  behavior, but should still be curated as transport unless direct
  regulatory evidence changes the module boundary.
- The clearest signaling sub-batch is the QseBC-like two-component group
  (`PP_2713`, `PP_2714`, `kdpE`, `PP_4224`, `qseB`).
- Fur, DMT transporter, surface adhesion, RND efflux, phosphonate import,
  and peptide/opine/glutathione import are side/boundary contexts.

## Completed Sub-batches

- `rnd_multidrug_efflux`: two genes present, Asta-backed,
  first-pass curated, validated, and rendered; new module
  `modules/rnd_multidrug_efflux_boundary.yaml` created, validated,
  and rendered. PP_2064 is treated as the membrane-fusion/adaptor
  component that contributes to pump-level efflux activity, while
  PP_2065 is retained as the inner-membrane RND xenobiotic
  transporter.
- `qsebc_like_two_component_regulation`: five genes present,
  Asta-backed, first-pass curated, validated, and rendered; new
  module `modules/qsebc_like_two_component_regulation_boundary.yaml`
  created, validated, and rendered. PP_2714-PP_2713 and
  PP_4224-qseB are treated as predicted local sensor kinase/response
  regulator pairs, while kdpE remains an unresolved KdpE-like
  response activator side branch.
- `phosphonate_abc_import`: four genes present, Asta-backed,
  first-pass curated, validated, and rendered; existing module
  `modules/phosphonate_phosphinate_metabolism.yaml` extended,
  validated, and rendered. PP_1722-PP_1726 are treated as a
  second AEP/phosphonate ABC import candidate with substrate
  range and direct PhnW handoff left as a knowledge gap.
- `peptide_opine_glutathione_abc_import`: eight genes present,
  Asta-backed, first-pass curated, validated, and rendered; new
  module `modules/peptide_opine_glutathione_abc_import_boundary.yaml`
  created, validated, and rendered. PP_3220-PP_3223 are treated
  as a dipeptide-like ABC importer, while gsiA/PP_4454/gsiC/
  PP_4458 are treated as a mixed Gsi/opine-like ABC import
  boundary with substrate range unresolved.
- `polyamine_abc_import`: thirteen genes present, Asta-backed,
  first-pass curated, validated, and rendered; existing module
  `modules/polyamine_transport_boundary.yaml` extended,
  validated, and rendered. PP_0411-PP_0414, ydcV/ydcU/ydcT/
  ydcS, and PP_3814-PP_3817 are treated as polyamine ABC
  import candidates, while PP_2870 remains a binding-protein
  singleton with unresolved transporter partners.
- `fur_iron_regulation_spillover`: one gene present,
  Asta-backed, first-pass curated, validated, and rendered;
  new module `modules/iron_homeostasis_regulation_boundary.yaml`
  created, validated, and rendered. PP_0119/fur__Q88RL0 is
  treated as a Fur-family iron-homeostasis transcription
  regulator side context, distinct from direct quorum sensing.
- `surface_adhesion_singleton`: one gene present, Asta-backed,
  first-pass curated, validated, and rendered; new module
  `modules/surface_adhesion_boundary.yaml` created, validated,
  and rendered. PP_0806 is treated as a large BapA/Bap-like
  surface-adhesion/biofilm-boundary protein.
- `dmt_transporter_singleton`: one gene present, Asta-backed,
  first-pass curated, validated, and rendered; new module
  `modules/dmt_transporter_boundary.yaml` created, validated,
  and rendered. PP_3609 is treated as a DMT/YdcZ-family
  membrane transporter with unresolved substrate.

## Next Steps

- The ppu02024 partition is first-pass complete at 60/60 primary
  review folders and 60/60 Asta reports. Do not curate ppu02024
  as one satisfiable quorum-sensing module; maintain the nine
  boundary buckets instead.
- Run real Falcon module/pathway commands only after a concrete submodule
  is selected; current Edison Falcon access failure mode is HTTP 402.
