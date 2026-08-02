---
title: "Spatial Omics & Cell–Cell Communication Predictions"
maturity: SCOPING
tags: [PIPELINE, ML_PREDICTIONS]
species: [human]
---

# Spatial Omics & Cell–Cell Communication Predictions

## Overview

This project scopes whether predictions from **spatial transcriptomics foundation
models** — specifically gene-pair and cell–cell communication (CCC) calls — can be
turned into reviewable annotation evidence under the existing
[`PredictionReview`](../src/ai_gene_review/schema/gene_review.yaml) machinery.

Before this project, the repository had **no** spatial-omics or CCC project. CCC
biology is curated at the module level (see below), and the terms `CellPhoneDB`,
`Xenium`, `Visium`, `MERFISH`, `NicheNet` appeared nowhere in `projects/` — the sole
repository-wide mention of CellPhoneDB is a passive one inside a cached publication's
methods section, where it is cited as a database from which *false positives had to be
manually removed*.

## Motivating method: SpatialFormer

Wang, Huang & Winther (2026), *Nature Computational Science*,
[10.1038/s43588-026-01016-7](https://doi.org/10.1038/s43588-026-01016-7).

A SqueezeFormer (convolution + transformer) model pretrained on 700M cell pairs from
17M spatially resolved cells across 71 Xenium slides. Relevant to us because of one
capability: **iterative gene pair perturbation (IGP)**, which knocks out gene pairs in
a paired-cell forward pass and ranks them by their effect on the predicted
co-localization logit. In the paper this produced 684 significant gene pairs in a
pulmonary-fibrosis granuloma region.

The interesting property for GO curation is that IGP is **not restricted to a curated
ligand–receptor database**. The paper's framing: *"there is currently no communication
score computed from the covariant factors that takes into account the integrated
factors in the cellular niches, including all genes rather than only ligands and
receptors."* That makes its output a genuine *prediction* to be adjudicated, rather
than a lookup of already-curated interactions.

### Availability

| Asset | Location |
|---|---|
| Source | [github.com/TerminatorJ/Spatialformer](https://github.com/TerminatorJ/Spatialformer) (MIT) |
| Package | PyPI `spatialformer` v0.1.8 (2026-03-24), Python >= 3.10 |
| Archive | Zenodo [10.5281/zenodo.20476938](https://doi.org/10.5281/zenodo.20476938) |
| Checkpoints | **Figshare** (paired- and single-input, 13 tissues / 71 slides; LoRA variants for lung, breast, colon) |
| Pretraining data | HuggingFace `xenium_5k_pandavid_dataset_v2` ([10.57967/hf/8988](https://doi.org/10.57967/hf/8988)) |

There is **no hosted API or REST endpoint** — it is a local Python package. Entry
point is `sp.tl.embed_data(...)`, which is AnnData/scanpy-native and writes embeddings
to `adata.obsm["X_SpaF"]`. Note the split that is easy to misread in the paper: the
Data availability statement's "all processed pretraining datasets are available at
HuggingFace" refers to **data**; the **weights** are on Figshare.

## Compute profile

The cost is extremely non-uniform across tasks, which determines what is worth
attempting.

| Task | Cost | Notes |
|---|---|---|
| Pretraining | 64 AMD MI250 GPUs, 8 nodes, 14 days, bf16, batch 1024, 175k steps | Not reproducible here or anywhere we have; irrelevant, we use the checkpoint |
| `embed_data(mode="single")` | One forward pass per cell, frozen model | Cheap; CPU-viable for small n |
| `embed_data(mode="pair")` | O(n²) in cells | The authors themselves subsample: *"it is computationally unrealistic to perform inference across all cellular combinations to obtain binary predictions; therefore, we randomly selected 500 cells for evaluation"* |
| **IGP** | **L₁×L₂ forward passes per cell pair**, over >= 100 cell pairs per cell-type category | With the 343-gene PF panel that is ~118k forwards per cell pair, ~1.2e7 total. Does not fit a 2h budget |
| LoRA fine-tune | 10k–100k cells, adapters only, base frozen | Modest, GPU |

**Consequence for scoping:** a faithful reproduction of the paper's Fig. 4 IGP screen is
out of reach on any single-GPU budget we have. A *bounded* IGP — one cell-type contact,
one region, a restricted gene panel on each side, subsampled cell pairs — is tractable
and still yields a reviewable ranked gene-pair list.

## Where the work can run

The AIGR session container has **no GPU** (4 vCPU, ~15 GB RAM, no `nvidia-smi`,
no `/dev/nvidia*`), so it can host data prep, preprocessing and schema mapping, but not
the inference itself.

Two candidate execution venues:

1. **OpenScientist** — an agentic co-scientist that can both run the analysis and
   interpret it. Whether its sandbox exposes a GPU, sufficient disk, and egress to
   Figshare/GEO is being determined empirically; see
   [environment probe](SPATIAL_OMICS/probe/environment-probe-prompt.md). Hard
   constraint either way: `OpenScientistParams.timeout` is validated `le=7200`, i.e. a
   2-hour ceiling per job, so any IGP run must be scoped to fit.
2. **Colab** — the upstream repo ships Colab notebooks for co-localization prediction
   and gene-pair perturbation; a T4/A100 handles a bounded IGP comfortably.

## Existing repository assets to build on

**CCC biology already curated as modules** (`modules/`), which is where predicted gene
pairs would be checked against curated pathway structure:

- Ligand–receptor axes: `wnt_signaling`, `notch_signaling`, `hedgehog_signaling`,
  `ephrin_receptor_signaling`, `chemokine_signaling`, `bmp_signaling`, `nodal_signaling`,
  `activin_receptor_signaling`, `tgfb_smad_signaling`, `egfr_signaling`, `erbb2_signaling`,
  `fgfr_signaling`, `pdgfr_signaling`, `vegfr_signaling`, `hgf_met_signaling`,
  `neurotrophin_trk_signaling`, `il1_signaling`, `il6_signaling`, `tnf_signaling`,
  `type_i_interferon_signaling`, `type_ii_interferon_signaling`,
  `death_receptor_apoptotic_signaling`
- Contact-dependent / immune synapse: `t_cell_receptor_signaling`,
  `b_cell_receptor_signaling`, `fc_gamma_receptor_signaling`,
  `fc_epsilon_receptor_signaling`, `integrin_fak_src_signaling`
- Direct conduits and non-metazoan CCC: `septal_junction`, `dicty_extracellular_camp_relay`,
  `dicty_cgmp_chemotaxis_arm`, `dicty_allorecognition_adhesion`,
  `dicty_sdf2_encapsulation_relay`, `dicty_counting_factor_size_control`

**A candidate experimental gold standard.** `PMID:35922511` (Shilts et al., *Nature*
2022, "A physical wiring diagram for the human immune system") is a systematic SAVEXIS
screen of human cell-surface receptor–ligand interactions with manually verified
interactions and explicitly removed database false positives. It is already cited in 10
human gene reviews (APP, CD28, CD320, CD47, CDH1, CTLA4, FAS, FGFR2, PI16, TNFRSF1A),
making it a natural benchmark against which to score predicted surface gene pairs.

**Single-cell inference precedent.** `CEPHALOPOD/CEPHALOPOD-scRNAseq-synthesis.md`
already writes down the inference pattern (gene G has MF F × G marks cell type C ×
C has role R → BP), which is the non-spatial ancestor of what this project proposes.

## Status

- **2026-08-02** — Project created. Availability, API surface, and compute profile
  established from the paper and upstream repo. Environment probe launched against
  OpenScientist to determine whether the analysis can run there. No inference run yet;
  **no predictions have been generated or reviewed.**

## Open questions

- Does the OpenScientist sandbox expose a GPU, and can it reach Figshare/GEO?
- Which tissue and cell-type contact makes the best first bounded IGP target? The PF
  granuloma (macrophage <-> T cell, GEO `GSE250346`) is the paper's own worked example
  and therefore the cheapest to sanity-check against.
- How should a predicted *gene pair* map onto the `PredictionReview` schema, which is
  built around a single term per prediction? A pair is naturally a statement about two
  gene products plus a relation, not one GO term.
- What is the right assessment vocabulary for CCC predictions? The existing
  COR/CNN/LSP/UNC/PLI/NPI/REP codes were designed for EC/GO function predictions; a
  co-expression-derived gene pair may need a different notion of "correct".
