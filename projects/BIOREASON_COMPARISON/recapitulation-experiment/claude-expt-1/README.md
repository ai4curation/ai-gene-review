---
title: "ESR-ECOLI-DET-Mini Recap Results"
autolink_gene_symbols: false
benchmark_id: ESR-ECOLI-DET-Mini
benchmark_alias: ESR-ECOLI-DET-7
dataset_id: 10.5281/zenodo.20751016
dataset_url: https://doi.org/10.5281/zenodo.20751016
---

# ESR-ECOLI-DET-Mini Recap Results

Archived result bundle from PR #1535:

- PR: <https://github.com/ai4curation/ai-gene-review/pull/1535>
- PR title: `DO NOT MERGE Independent reviews of 7 E. coli genes + DeepECTF prediction assessments (claude-expt-1)`
- Source head commit: `9ce787b0daddbf03d6bc1b5164682f7e0000e7cd`
- Dataset ID: `10.5281/zenodo.20751016`
- Benchmark ID: `ESR-ECOLI-DET-Mini` (alias: `ESR-ECOLI-DET-7`)

These files are preserved here as project experiment outputs only. They should not be treated as production updates to `genes/ECOLI/`.

## Contents

- `genes/ECOLI/DET-PREDICTION-REVIEW-SUMMARY.md` — original experiment summary.
- `genes/ECOLI/<gene>/<gene>-det-predictions-review.yaml` — DeepECTF prediction review outputs.
- `genes/ECOLI/<gene>/<gene>-ai-review.yaml` — independently recreated gene reviews from the experiment.
- `genes/ECOLI/yciO/yciO-bioinformatics/` — YciO/TsaC alignment artifacts used by the experiment.
- `publications/PMID_*.md` — supporting publication caches added by the experiment branch.

## ESR-ECOLI-DET-Mini Verdicts

| Gene | DeepECTF prediction | Experiment verdict | Error type |
|---|---|---|---|
| fepE | EC:2.7.13.3 histidine kinase | REP | FREQUENCY_BIAS |
| yciO | EC:2.7.7.87 TC-AMP synthase | PLI | PARALOG_OVERANNOTATION |
| yegV | EC:2.7.1.92 5-dehydro-2-deoxygluconokinase | UNC | |
| ygfF | EC:1.1.1.47 glucose 1-dehydrogenase | UNC | |
| yjdM | EC:3.11.1.2 phosphonoacetate hydrolase | NPI | IN_VITRO_NOT_IN_VIVO |
| yjhQ | EC:2.3.1.189 mycothiol synthase | NPI | PATHWAY_CONTEXT_IGNORED |
| yrhB | EC:4.1.2.50 6-carboxytetrahydropterin synthase | NPI | PATHWAY_CONTEXT_IGNORED |

Relative to the published de Crécy-Lagard expert labels, this experiment is an exact class match for fepE, yciO, yjhQ, and yrhB, and differs for yegV, ygfF, and yjdM. It is therefore a 4/7 exact-label Expert Synthetic Review recap, not a 7/7 replication.
