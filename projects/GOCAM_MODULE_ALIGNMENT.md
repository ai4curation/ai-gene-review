---
title: "GO-CAM review and module alignment"
description: "Review cached production GO-CAMs and align them with reusable modules"
maturity: IN_PROGRESS
tags: [PIPELINE]
species: [human]
index_group: CROSS_CUTTING
---

# GO-CAM review and module alignment

## Scope

This lane reviews production GO-CAM snapshots cached under `gocams/` and aligns them with
reusable `modules/` records. GO-CAM source snapshots are read-only; curation goes into
`gocams/<model>/<model>-review.yaml`, and reusable pathway structure goes into module YAML.

For each reviewed model:

- assess molecular-function typing, `has_input` usage, causal edges, complexes, cellular/process
  context, evidence, and consistency with the relevant gene reviews
- find the module or modules that cover the same biology and compare parts, annotons, activities,
  and causal structure
- fix the module when it is missing a reusable step that the GO-CAM gets right
- record GO-CAM-only issues in the `GoCamReview` rather than editing the cached source snapshot
- note any needed gene-review repair in the `GoCamReview` and leave the gene review for its owner

## Current Cache Survey

- As of 2026-11-22, 2,037 GO-CAM source snapshots are cached: 2,036 production
  snapshots plus `671ae02600002832`, a `status: development` model.
- 45 `GoCamReview` files currently exist.
- 877 top-level module YAML files currently exist.
- 189 modules contain structured `gocam_associations`.
- Those module associations cite 559 cached GO-CAM models.
- 29 reviewed GO-CAM models are already cited by at least one module.
- 16 reviewed GO-CAM models are not yet cited by any module.

The 559 module-cited GO-CAM models include the development model
`671ae02600002832`, which is already cited by `modules/glycopeptide_resistance_depsipeptide.yaml`;
the lane should decide explicitly whether to review such non-production edge cases. Module
associations also use both allowed model spellings: most store `model: gomodel:<id>`, while a
few store bare local ids, so survey queries need to normalize both forms.

This leaves a large backlog of cached, unreviewed models that already overlap at least one
module. The first pass should prefer small human models with existing module associations and
high gene-review coverage, while skipping work already owned by open PRs or adjacent lanes such as
TNF/nSMase, cGAS-STING, integrated stress response, ribosome quality control, yeast or fungal
families, nematode pathogens, and broad human-family review. GO-CAM compartment-edge repair
remains in `GOCAM_COMPARTMENTS`, while module taxon scoping remains in `MODULE_TAXON_AUDIT`;
this lane should reuse those joins when they explain a reviewed model's structure.

## First Batch

The first content PRs are one model each. A GO-CAM review and a small correction to its matching
module can travel together when both are about the same model.

| PR | GO-CAM | Module | Why first |
| --- | --- | --- | --- |
| 1 | `67c10cc400009089`, EGF signaling pathway | `egfr_signaling` | compact receptor-to-MAPK chain with five activities, all five human genes already reviewed, and a direct module overlap |
| 2 | `69d8496c00003152`, FBXO42-mediated p53 degradation | `p53_signaling` | four-activity ubiquitin-ligase model with complete local gene-review coverage and an existing activity pin in the p53 module |
| 3 | `62b4ffe300001804`, CASP3 and CASP7 cleavage of PARP1 during apoptosis | `apoptotic_execution_phase` | four-activity caspase substrate model with complete local gene-review coverage, an existing execution-phase module association, and a likely CASP7 RNA-binding term issue |

After these land, continue down the same queue: choose unreviewed human GO-CAMs with explicit
module overlap, avoid modules already in active PRs, and create a new generic module only when the
GO-CAM covers a reusable motif that no existing module can absorb.
