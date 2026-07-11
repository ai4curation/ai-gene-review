# Pilot benchmark: computational vs experimental annotations under expert review

**Script:** [`score_predictions.py`](score_predictions.py) · **Data:** [`annotation_review_outcomes.tsv`](annotation_review_outcomes.tsv)
**Run over:** all reviewed *S. cerevisiae* genes in `genes/yeast/` (123 genes, 3,926 reviewed annotations).

This is workstream #3 of the [Virtual Yeast project](../VIRTUAL_YEAST.md): use this repo's
curated reviews as a gold standard to measure how well **computational** GO annotations
(IBA/IEA/ISS…) survive expert scrutiny relative to **experimental** ones (IDA/IMP/IPI…).
The "virtual yeast" Perspective (Nature 655, 2026) leans on foundation-model function
predictors (Evo, ESM, PANTHER/IBA) but reports no accuracy for them; this is the kind of
prediction-vs-truth evaluation it lacks.

## Headline result

| evidence class | n | retained | retained % | over-annotated / removed | rejected % |
|---|---|---|---|---|---|
| experimental | 2,458 | 1,885 | **76.7** | 551 | 22.4 |
| computational | 1,342 | 1,242 | **92.5** | 93 | 6.9 |
| author (TAS/NAS/IC) | 126 | 106 | 84.1 | 17 | 13.5 |

"Retained" = `ACCEPT` + `KEEP_AS_NON_CORE` + `MODIFY`; "rejected" = `MARK_AS_OVER_ANNOTATED`
+ `REMOVE`.

**The counterintuitive finding: computational annotations were retained *more* often than
experimental ones (92.5% vs 76.7%), and were flagged as over-annotations/removed far less
(6.9% vs 22.4%).**

## Why (interpretation — read with the caveats below)

This is *not* "predictions beat experiments." It reflects **what each evidence class
contains** in the curated GO record:

- **Computational here is dominated by IBA (477) and IEA (835).** GO's **IBA phylogenetic
  pipeline is deliberately conservative** — it propagates well-conserved core functions
  across orthologs, so reviewers `ACCEPT` most of it. IBA behaves like a curated causal/
  functional prior, which is exactly the point relevant to a virtual cell.
- **Experimental is inflated by IPI (800) and over-scoped IDA/IMP calls.** The single
  largest experimental bucket is `IPI` — much of which is uninformative **"protein binding"**
  that reviewers down-scope or mark as over-annotation (per this repo's own curation
  guidance to avoid bare `protein binding`). Experimental annotations also include many
  context-specific findings later judged over-general. Hence 364 experimental
  `MARK_AS_OVER_ANNOTATED` vs only 49 computational.

So the actionable message for AIVC work is the inverse of the usual assumption: **a raw
experimental-annotation dump is noisier (for "core function") than the conservative IBA
layer.** If you feed curated priors into a virtual-yeast model, IBA/GO-CAM-grade causal
annotations are a cleaner signal than an unfiltered experimental GAF — and this repo's
review actions are precisely the filter that separates the two.

## Full action breakdown

| evidence class | ACCEPT | KEEP_AS_NON_CORE | MODIFY | MARK_AS_OVER_ANNOTATED | REMOVE | NEW | UNDECIDED |
|---|---|---|---|---|---|---|---|
| experimental | 1,323 | 423 | 139 | 364 | 187 | 13 | 9 |
| computational | 962 | 170 | 110 | 49 | 44 | 4 | 3 |
| author | 76 | 29 | 1 | 8 | 9 | 3 | 0 |

## Caveats (important — do not over-read)

1. **This measures retention of *existing* annotations, not novel-prediction accuracy.**
   It is a precision proxy for the annotation pipelines *as represented in the curated set*,
   not the COR/CNN/LSP/UNC/PLI/NPI/REP novelty taxonomy. A full workstream-#3 run should
   also score predictions **absent** from GOA using `PredictionReview`.
2. **Selection bias.** These 123 genes are not a random draw of the ~6,000-gene genome —
   the reviewed set is enriched for chaperones, chromatin factors, and metabolic enzymes,
   which skews the evidence-code and function mix.
3. **Reviewer asymmetry.** Reviewers may scrutinize experimental IPI/IDA calls harder than
   IBA calls, which partly drives the gap.
4. `status: DRAFT` on most reviews — actions may change.

## Reproduce

```bash
python3 projects/VIRTUAL_YEAST/score_predictions.py \
    --out-tsv projects/VIRTUAL_YEAST/annotation_review_outcomes.tsv
```
