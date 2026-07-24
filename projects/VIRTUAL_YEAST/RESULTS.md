# Workstream #3 — Prediction-vs-review benchmarks (yeast + pombe)

Scripts (all reproducible, nothing hardcoded):
[`score_predictions.py`](score_predictions.py) ·
[`aspect_stratified.py`](aspect_stratified.py) ·
[`interpro2go_novelty.py`](interpro2go_novelty.py)
Data: [`annotation_review_outcomes.tsv`](annotation_review_outcomes.tsv)

Uses this repo's curated reviews as a gold standard to evaluate GO annotations/predictions
— the prediction-vs-truth evaluation the "virtual yeast" Perspective (Nature 655, 2026)
never supplies for its foundation-model function predictors (Evo, ESM, PANTHER/IBA).

---

## 1. Retention: computational vs experimental annotations

Over all reviewed *S. cerevisiae* genes (123 genes, 3,926 reviewed annotations):

| evidence class | n | retained % | over-annotated / removed % |
|---|---|---|---|
| experimental (IDA/IMP/IPI…) | 2,458 | 76.7 | 22.4 |
| computational (IBA/IEA/ISS…) | 1,342 | **92.5** | 6.9 |

"Retained" = `ACCEPT`+`KEEP_AS_NON_CORE`+`MODIFY`; "rejected" = `MARK_AS_OVER_ANNOTATED`+`REMOVE`.
Computational annotations survive expert review *more* often than experimental ones —
because the computational bucket is dominated by GO's conservative **IBA** phylogenetic
pipeline, while experimental is inflated by uninformative `IPI` "protein binding" (800 calls).

## 2. Where the over-annotation lives: evidence class × GO aspect

Stratifying by GO aspect (`aspect_stratified.py`, aspect joined from each gene's GOA TSV)
**localizes** the rejection almost entirely to **molecular function**:

**S. cerevisiae** (n=3,926)

| evidence class | aspect | n | retained % | over-annot/removed % |
|---|---|---|---|---|
| experimental | **MF** | 1,145 | **54.7** | **45.2** |
| experimental | BP | 795 | 97.5 | 2.0 |
| experimental | CC | 505 | 95.8 | 3.4 |
| computational | MF | 524 | 92.0 | 7.6 |
| computational | BP | 412 | 90.8 | 9.2 |
| computational | CC | 402 | 96.0 | 3.7 |

**S. pombe** (independent PomBase-curated set; 72 genes, 2,519 annotations) — same pattern, milder:

| evidence class | aspect | n | retained % | over-annot/removed % |
|---|---|---|---|---|
| experimental | **MF** | 550 | **77.3** | **22.5** |
| experimental | BP | 535 | 98.9 | 0.6 |
| experimental | CC | 601 | 98.7 | 1.2 |
| computational | MF | 248 | 79.8 | 18.1 |
| computational | BP | 243 | 83.1 | 14.8 |
| computational | CC | 248 | 94.0 | 5.6 |

**Key result:** the annotation noise is concentrated in **molecular function**. Experimental
**BP and CC annotations are ~96–99% trustworthy** in both organisms; experimental **MF is
where over-annotation lives** (45% flagged in yeast, 22% in pombe), driven by
uninformative/over-general `protein binding`. This directly validates this repo's own
curation guideline (avoid bare `protein binding`) and gives a concrete, actionable rule for
AIVC priors: **trust curated BP/CC as priors; treat the experimental MF layer as noisy and
require a more informative MF term.**

## 3. Novelty: InterPro2GO predictions vs GOA

`interpro2go_novelty.py` reads each gene's **real** InterPro domains (cached UniProt record),
maps them through the InterPro2GO table (`rules/arba/_interpro2go.txt`), and compares
predicted GO terms to the gene's GOA. (Exact-id match is a conservative novelty proxy; it
does not resolve ontology subsumption.)

| organism | genes w/ prediction | unique predictions | already in GOA (CNN) | novel |
|---|---|---|---|---|
| S. cerevisiae | 98 | 271 | **255 (94.1%)** | 16 (5.9%) |
| S. pombe | 59 | 193 | **172 (89.1%)** | 21 (10.9%) |

**Key result:** on well-characterized genes, domain-based prediction is **~90–94%
redundant** with existing curation (Correct-but-Not-Novel). This is the CNN /
training-data-contamination phenomenon from the de Crécy-Lagard taxonomy quantified: a
predictor scored on curated genes mostly re-derives what is already known. The top novel
term in yeast, `GO:0140662` (ATP-dependent protein folding chaperone), is predicted for 9
Hsp70-family genes — a natural test of paralog discrimination (below).

## 4. Worked example: PredictionReview of a paralog over-annotation

The same InterPro2GO prediction, `GO:0140662` (ATP-dependent protein folding chaperone),
lands differently across three Hsp70 paralogs — exactly the paralog-subfamily failure mode
a domain- or foundation-model predictor commits:

| gene | role | assessment |
|---|---|---|
| SSA1 | canonical cytosolic Hsp70 foldase | correct (function well known) |
| SSQ1 | mitochondrial, ATP-dependent Fe-S transfer | correct (more precise) |
| **SSZ1** | atypical RAC Hsp70; **binds ATP but does not hydrolyze it; ATPase dispensable in vivo** | **PLI — paralog over-annotation** |

Full curated file (validates `-C PredictionReview`, "No issues found"):
[`genes/yeast/SSZ1/SSZ1-interpro2go-predictions-review.yaml`](../../genes/yeast/SSZ1/SSZ1-interpro2go-predictions-review.yaml).
For SSZ1, `GO:0140662` is scored **PLI** (`error_type: PARALOG_OVERANNOTATION`, CS=0):
InterPro2GO propagates the Hsp70 superfamily's ancestral ATP-driven foldase MF onto a
member that has functionally diverged. GOA correctly withholds any ATP-dependent foldase
term from SSZ1 (it carries `GO:0044183` protein folding chaperone + `GO:0051083` cotranslational
folding instead). `GO:0005524` (ATP binding) for the same gene is scored **CNN** (correct,
already in GOA) — SSZ1 does bind ATP; it just doesn't hydrolyze it productively.

## 5. Full adjudication of the novel set — zero COR

All 37 novel InterPro2GO predictions (16 yeast + 21 pombe) are hand-adjudicated in
[`novel_predictions_adjudication.md`](novel_predictions_adjudication.md), grounded in each
gene's curated function:

| assessment | n |
|---|---|
| CNN (correct, already curated) | 30 |
| PLI (paralog/subfamily error) | 2 — SSZ1, aah1 |
| LSP (correct but too generic) | 3 — ACL4, cdc12, ral2 |
| UNC (unverifiable) | 2 — YGR117C, pol5 |
| **COR (correct + novel)** | **0** |

**Zero COR.** On well-characterized genes, InterPro2GO yields no correct-and-novel calls:
correct predictions are redundant with curation (CNN), and the residual novel output is
paralog error (`aah1`: GH13 α-amylase predicted for a curated 4-α-glucanotransferase),
uninformative generic terms (bare `protein binding`), or unverifiable. A second validated
paralog case joins SSZ1:
[`genes/SCHPO/aah1/…`](../../genes/SCHPO/aah1/aah1-interpro2go-predictions-review.yaml) (PLI),
alongside a clean correct call
[`genes/SCHPO/slp1/…`](../../genes/SCHPO/slp1/slp1-interpro2go-predictions-review.yaml) (CNN).

## 6. A predictor with genuinely novel output: BioReason-Pro vs InterPro2GO

InterPro2GO can only emit terms in the domain→GO table, so its novelty is structurally
capped. **BioReason-Pro (RL)** is a reasoning-LLM predictor that emits free GO calls from a
chain-of-thought over sequence + domains — genuinely un-constrained output. The repo has 23
curated pombe BioReason reviews (`genes/SCHPO/*/*-bioreason-rl-review.md`); aggregated by
[`bioreason_summary.py`](bioreason_summary.py):

| metric | value |
|---|---|
| reviews | 23 |
| mean correctness | **2.78 / 5** |
| mean completeness | 2.30 / 5 |
| reviews scoring ≤2/5 correctness | **11 / 23 (48%)** |

Dominant curator-flagged error signatures:

| n | signature | schema error type |
|---|---|---|
| 8 (35%) | localization defaulted to cytoplasm | `LOCALIZATION_DEFAULT` |
| 2 | catalytic activity overstated on a pseudo-enzyme | `PSEUDOENZYME_OVERANNOTATION` |
| 2 | function specificity overstated | — |
| 1 | repeats/reinforces an InterPro2GO error (cts2) | — |

**The contrast is the point for AIVC evaluation.** The two predictor classes fail in
opposite ways:

- **InterPro2GO (domain-based):** high precision but ~90–94% redundant; residual errors are
  paralog over-annotations (SSZ1, aah1). Safe, unoriginal.
- **BioReason (reasoning-LLM):** genuinely novel free-form output, but mean correctness only
  2.78/5 with 48% of calls ≤2/5, a **systematic localization-to-cytoplasm bias (35%)**, and
  catalytic overstatement on pseudo-enzymes — and in ≥1 case it *inherited* an InterPro2GO
  error instead of correcting it. Original, but unreliable.

This is precisely the prediction-quality characterization the virtual-yeast Perspective
never provides for its foundation-model building blocks (Evo/ESM/PANTHER). A virtual cell
that ingests raw foundation-model predictions as priors would import a strong
localization-to-cytosol bias — directly harmful for a model whose whole premise is
compartment-resolved spatial architecture.

## Caveats

1. §1–2 measure **retention of existing annotations**, not novel-prediction accuracy; §3–4
   add the novelty axis (CNN vs novel, and a hand-reviewed PLI). A fuller run would
   hand-adjudicate all 16+21 novel predictions with `PredictionReview`.
2. **Selection bias:** the reviewed gene sets are non-random (enriched for chaperones,
   chromatin, metabolic enzymes), which skews the evidence/aspect mix.
3. Exact-id novelty in §3 ignores ontology subsumption (over-counts novelty).
4. Most reviews are `status: DRAFT`; actions may change.

## Reproduce

```bash
python3 projects/VIRTUAL_YEAST/score_predictions.py --out-tsv projects/VIRTUAL_YEAST/annotation_review_outcomes.tsv
python3 projects/VIRTUAL_YEAST/aspect_stratified.py --genes-dir genes/yeast --genes-dir genes/SCHPO
python3 projects/VIRTUAL_YEAST/interpro2go_novelty.py --genes-dir genes/yeast
uv run linkml-validate -s src/ai_gene_review/schema/gene_review.yaml -C PredictionReview \
    genes/yeast/SSZ1/SSZ1-interpro2go-predictions-review.yaml
```
