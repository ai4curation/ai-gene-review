# ASSAY_TO_FUNCTION

**Which experimental readouts reliably support gene-function annotation, and which drive over-annotation?**

## Motivation

Functional genomics papers infer gene function through a chain:

> perturb gene **G** → readout **R** moves → conclude **G** is "involved in" process **P**

The reliability of that final `R → P` step varies enormously, but GO evidence
codes (IDA, IMP, IGI, …) do not capture it. An IMP read out with a 5×UPRE
reporter and an IMP read out with a reconstituted enzyme assay carry the same
evidence code, yet one is a distal, convergent phenotype and the other is a
direct measurement of molecular activity. This project tries to make that
hidden axis explicit and to measure, against the curated corpus, which readout
classes are associated with annotations that curators later downgrade.

## Conceptual framework

Two independent axes govern `R → P` reliability:

1. **Proximity** — does the readout measure the gene product's *own molecular
   activity* (`molecular`) or a *downstream cellular consequence* (`phenotypic`)?
2. **Convergence** — is the readout a fairly specific signature of process P
   (`low`), or a **hub** that many upstream inputs feed into (`high`)?

Over-annotation risk is highest in the **phenotypic + high-convergence**
quadrant. Classic convergent hubs: ROS, caspase activation, the UPR,
intracellular Ca²⁺, pH, mitochondrial membrane potential. A gene that moves one
of these reporters could be a direct effector *or* anything that perturbs the
process indirectly — so a positive readout licenses, at best, a cautious
`response to` / `regulation of` **BP** term (often non-core), and should never
by itself drive an **MF** or core-function call.

### Example readouts (the seed cases that motivated this)

| Readout | Reports state of | Why it over-annotates |
|---|---|---|
| 5×UPRE | UPR / ER stress | fires for *any* ER perturbation — secretory load, trafficking, metabolic stress |
| CellROX / DCFDA / MitoSOX | oxidative stress | ROS rises under nearly every stress; massively convergent |
| CellEvent / caspase-3/7 | apoptosis | caspase activation is far downstream; many insults trigger it |
| pHrodo / pHluorin | pH / phagocytosis | |
| FeRhoNox | labile Fe²⁺ | |

The full, editable catalog lives in
[`ASSAY_TO_FUNCTION/readout_catalog.yaml`](ASSAY_TO_FUNCTION/readout_catalog.yaml).

## Method (first pass — mining the curated reviews)

`ASSAY_TO_FUNCTION/mine_readouts.py` walks all `genes/**/*-ai-review.yaml`
files. For each annotation it builds an *evidence text* from the curator's
`review.summary`, `review.reason`, and `supported_by[].supporting_text`, then
matches it against the regex patterns in the catalog. Each match becomes a row
joining the readout class to the reviewer's `action`.

Reliability is summarised two ways, over **reviewed annotations only**
(UNREVIEWED / UNDECIDED / PENDING excluded from the denominator):

- `pct_removed_or_overann` — *hard* signal: REMOVE + MARK_AS_OVER_ANNOTATED
- `pct_any_downgrade` — *soft* signal: also includes KEEP_AS_NON_CORE + MODIFY

```bash
uv run python projects/ASSAY_TO_FUNCTION/mine_readouts.py
```

Outputs land in `ASSAY_TO_FUNCTION/reports/`:
`readout_matches.tsv` (one row per match), `readout_action_crosstab.tsv`
(the table below), and `matched_string_counts.tsv` (QC).

## First-pass results

Scanned **1,971 review files / 75,931 annotations**; 1,736 readout matches.

| readout_class | prox | conv | reviewed | rm/OA% | anyDn% |
|---|---|---|--:|--:|--:|
| UPR_ER_STRESS | phenotypic | high | 29 | 0% | 24% |
| APOPTOSIS_CASPASE | phenotypic | high | 41 | 7% | **49%** |
| AUTOPHAGY_FLUX | phenotypic | high | 52 | 6% | 17% |
| MITO_MEMBRANE_POTENTIAL | phenotypic | high | 24 | 8% | **42%** |
| CALCIUM_FLUX | phenotypic | high | 7 | 29% | 57% |
| IRON_PROBE | phenotypic | high | 6 | 0% | 33% |
| TRANSCRIPTIONAL_REPORTER | phenotypic | high | 60 | 3% | 22% |
| VIABILITY_PROLIFERATION | phenotypic | high | 7 | 0% | 43% |
| IN_VITRO_ENZYME | molecular | low | 500 | 9% | 24% |
| DIRECT_BINDING | molecular | low | 988 | 6% | 18% |

### Interpretation (preliminary — under-powered)

- **Directional support, not proof.** The two phenotypic-hub classes with
  non-trivial N — apoptosis/caspase (49% any-downgrade) and mitochondrial
  membrane potential (42%) — sit well above the molecular controls
  (in-vitro enzyme 24%, direct binding 18%). But UPR, autophagy, and
  transcriptional reporters are no higher than the molecular baseline, and
  several classes have N < 10. No strong claim is warranted yet.
- **The review prose is the wrong corpus for assay names.** Curators write
  *synthesis* ("phosphorylates ACC", "crystal structure shows…"), not methods.
  Probe brand names are almost absent: CellROX/DCFDA/MitoSOX matched **zero**
  review texts. The molecular classes dominate by volume only because "crystal
  structure", "cryo-EM", and "in vitro" are phrases curators naturally use.
- Implication: to actually measure how assays are interpreted, we must mine the
  **publications** (methods sections), not the review summaries — see next steps.

### Methodology lessons (substring bugs caught in QC)

Keyword mining is treacherous; the QC dump caught three false-positive sources
that would have completely inverted the headline numbers:

- `HyPer` (H₂O₂ biosensor) matched "**hyper**-activation", "**hyper**-expressed"
  → inflated oxidative stress by ~365. Fixed with case-sensitive `(?-i:HyPer)`.
- `ERSE` (ER stress element) matched "div**erse**", "rev**erse**", "adv**erse**"
  → inflated UPR from ~29 to 609. Fixed with a left word boundary.
- `MTS` (viability dye) matched "**MTs**" (microtubules) and the
  mitochondrial-targeting-sequence abbreviation → fixed by requiring
  "MTS assay/reagent/reduction".

**Always inspect `matched_string_counts.tsv` before trusting a class total.**

## Next steps

1. **Pivot to the publications corpus.** For each annotation, take its
   `original_reference_id` (PMID), pull the cached `publications/PMID_*.md`,
   detect the assay class used in *that paper*, and join paper → annotation →
   action. ~1,517 cached publications already mention these probes — a far
   richer signal than the 1,736 review-prose matches. Unit of analysis becomes
   *(paper, annotation)*, with the assay coming from the paper.
2. **Add a GO aspect axis.** Test the core claim directly: phenotypic-hub
   readouts should rarely license MF or core-function annotations. Aspect can
   come from the per-gene `*-goa.tsv` files.
3. **Expand the catalog** with more probe vocabularies and, separately, the
   convergent *process-term* GO IDs each readout tends to get over-mapped to.
4. **Build the rubric deliverable**: per readout class, the GO annotation it
   does / does not license (MF vs BP, direct vs regulatory, core vs non-core),
   with worked examples drawn from the corpus.

## Relationship to existing projects

- `OVER_ANNOTATION_PATTERNS.md` — pattern #4 ("indirect downstream process
  annotations") is the conceptual cousin; this project quantifies the
  assay-specific version of it.
- `BIOSENSORS.md` — unrelated (plant synthetic-biology biosensors).
