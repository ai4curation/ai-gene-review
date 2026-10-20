---
title: ProtNLM2 evaluation archive (superseded)
---
# Archive: superseded ProtNLM2 bootstrap files

[← back to ProtNLM2 Evaluation](../../PROTNLM_EVALUATION.md)

These files are kept only as a record of how the first ARGO-ProtNLM-50 prediction reviews were
seeded, plus the first slide deck. **They are superseded. Do not run or cite them as current results.** Archived on 2026-09-27.

| File | What it was | Why it is archived |
|------|-------------|--------------------|
| `generate_prediction_reviews.py` | One-time script that wrote `genes/<ORG>/<GENE>/<GENE>-protnlm-predictions-review.yaml` from the bench50 CSVs | It hardcodes per-accession verdicts that contradict the current curated YAMLs, and by default it overwrites existing YAMLs (only `--only-missing` skipped them). Its `__main__` now exits with an error instead of running. |
| `bench50_novel_review.csv` | Early agent triage of 32 "novel" ARGO-50 predictions, with its own labels (e.g. `TRIVIALLY_DERIVABLE`, `PHMMER_TRANSFER_PLAUSIBLE`) | Its labels are not the VDCL categories, and many of its judgments were later revised in the per-gene reviews. |
| `protnlm_evaluation_slides.md`, `_embedded.md`, `.html`, `.pptx` | First slide deck, built from the pre-release XML export and the early ARGO-50 triage | Its counts and several case-study verdicts (e.g. "trivially correct" for the wheat patatin, now NPI) predate the current reviews. Replaced on 2026-10-19 by an HTML slide deck ([claude.ai artifact](https://claude.ai/artifact/MSLGF5gr1jNJiecx3SwhCg)) whose figures are generated from `benchmark-funnel.json`. Its image links (`slides_figures/...`) were written for the old location and no longer resolve from `archive/`. |

The calls of record are the per-gene `*-protnlm-predictions-review.yaml` files. Current totals come
from [`build_benchmark_summary.py`](../build_benchmark_summary.py) and are reported in the
[cross-cohort results](../benchmark-results.md).
