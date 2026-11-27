# Spec choices

The class is `BenchmarkSpec` in `src/ai_gene_review/schema/benchmark.yaml`.

- **Taxon**: set `taxon.id`, `label` and `gaf_code`, the GO release species code
  (HUMAN, MOUSE, YEAST, ...).
- **Releases**: list them with
  `curl -sL https://release.geneontology.org/ | grep -o '20[0-9-]*' | sort -u`.
  `baseline_release` must be on or before `cutoff_date`. Use the newest release
  as `current_release` unless told otherwise.
- **`min_reference_date`**: a GO time split only shows that the GO record is new;
  a model may still have read the paper. Set this floor on or after the training
  cutoff of the models to be evaluated. A target passes only if all its
  supporting papers do. In the example window, 182 human proteins have such
  papers from 2025-06 or later and only 6 from 2026-06 or later,
  so report the counts before you settle on a date. A feature quota may set its
  own `min_reference_date`. When it does, say so in the spec description.
- **Aspects, `go_branches`, `evidence_codes`**: the evidence default is CAFA's EXP,
  IDA, IPI, IMP, IGI, IEP, TAS and IC.
- **`include_negated`**: set this to true whenever pseudoenzymes are requested,
  because "NOT catalytic activity" is the interesting target.
- **`max_proteins_per_reference`**: a reference that adds annotations to more
  proteins than this is treated as high-throughput, and its rows are dropped.
- **Features**: use a `PSEUDOENZYME` quota with a UniProt query (see the
  example). Its hits are candidates, not literature-checked labels.
- **Conditions**: blind (with `shuffle_control`), organism, full and
  agent-review: what a predictor may see, with no tool or model.
- **Predictors** (optional): each predictor planned for the benchmark, with its
  `model` and, only when known, its `model_training_cutoff`, so that
  `reference_recency` can say which predictors the benchmark is fair for.
- **Other fields**: `decoys_per_item` (3), `seed`, `size`, `dev_fraction`,
  `near_duplicate_threshold` (0.8).
