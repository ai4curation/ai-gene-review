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

## Second pass — mining the publications corpus

`ASSAY_TO_FUNCTION/mine_papers.py` does what the first pass showed was needed:
the unit of analysis is now *(annotation, readout-class-used-in-the-source-paper)*.
For each PMID-backed annotation it resolves the cached `publications/PMID_*.md`,
detects which readout classes that paper uses, attaches the GO **aspect**
(MF/BP/CC, from the GOA TSVs), and flags **thematic alignment** — whether the
annotation's GO term is actually *about* the process the readout reports
(GO id in `commonly_overmapped_to`, or label matches `aligned_label_regex`).

```bash
uv run python projects/ASSAY_TO_FUNCTION/mine_papers.py
```

Coverage: **75,931 annotations; 36,660 PMID-backed; 36,449 papers resolved**
(129 PMIDs not cached). 16,682 paper-level readout matches; **722 thematically
aligned** (the high-precision subset where the readout plausibly *drove* the
annotation).

Performance note: detection is a two-stage filter — a cheap literal substring
*screen* (`SCREEN` in the script, a necessary superset per class) gates the
expensive `IGNORECASE` regex, which runs only on the rare screen hits. Screens
were validated to lose zero matches vs. regex-only on a 350-paper sample
(including the 50 largest). Detection is memoized per unique PMID.

### Headline result: the aspect constraint holds

For **thematically aligned** annotations, what GO aspect does each hub readout
license?

| readout_class | aspect distribution (aligned) |
|---|---|
| APOPTOSIS_CASPASE | **BP 68, MF 0** |
| OXIDATIVE_STRESS_ROS | **BP 10, MF 0** |
| VIABILITY_PROLIFERATION | **BP 87**, CC 3 |
| AUTOPHAGY_FLUX | **BP 109**, CC 15 |
| UPR_ER_STRESS | **BP 17**, MF 2 |
| CALCIUM_FLUX | **BP 20**, MF 2 |
| MITO_MEMBRANE_POTENTIAL | **CC 139**, BP 26 |
| TRANSCRIPTIONAL_REPORTER | BP 143, **MF 71**, CC 1 |

This directly supports the core hypothesis: phenotypic-hub readouts almost
never license **MF** annotations. Caspase, ROS, autophagy, viability, and UPR
readouts produce BP terms (ΔΨm probes produce mostly CC = mitochondrion
localization). **The one exception is transcriptional reporters (MF 71)** — but
inspecting those rows, they are bona fide TF-activity terms (`DNA-binding
transcription factor activity`, `transcription cis-regulatory region binding`)
on genuine transcription factors, mostly `ACCEPT`ed. A luciferase reporter
legitimately supports MF *for a TF*; it is not over-annotation there.

### The real over-annotation mode: correct-but-non-core, not wrong

Action breakdown for aligned annotations (the strong-link subset):

| readout_class | reviewed | ACCEPT | NON_CORE | rm/OA% | anyDn% |
|---|--:|--:|--:|--:|--:|
| VIABILITY_PROLIFERATION | 90 | 21 | **58** | 9% | **74%** |
| APOPTOSIS_CASPASE | 63 | 25 | **34** | 3% | 59% |
| OXIDATIVE_STRESS_ROS | 10 | 3 | 4 | 30% | 70% |
| CALCIUM_FLUX | 22 | 10 | 7 | 18% | 50% |
| MITO_MEMBRANE_POTENTIAL | 165 | 98 | 20 | **21%** | 38% |
| UPR_ER_STRESS | 19 | 9 | 5 | 11% | 37% |
| TRANSCRIPTIONAL_REPORTER | 207 | 146 | 36 | 7% | 28% |
| AUTOPHAGY_FLUX | 124 | 80 | 20 | 5% | 24% |

The key correction to the first-pass intuition: hub readouts are **not removed
more often** than molecular evidence (hard `rm/OA%` is comparable — molecular
controls run ~27% in the weak-link view). Instead their characteristic failure
mode is **demotion to non-core**: viability/proliferation (58/90 → NON_CORE)
and apoptosis (34/63) annotations are rarely *wrong*, but are overwhelmingly
judged peripheral. That is the precise, defensible sense in which these
readouts "over-annotate": they inflate the annotation set with correct-but-
peripheral process terms rather than producing outright errors.

Mitochondrial-membrane-potential readouts are the exception with a genuinely
elevated *hard* downgrade rate (21%), often via `MODIFY` (31/165) — ΔΨm is a
non-specific organelle-health readout that gets refined to more proximal terms.

### Caveats

- **Weak link.** A paper using assay R does not prove the *specific* annotation
  was based on R. Thematic alignment mitigates this (722 high-precision rows)
  but cannot fully establish causation.
- The `any-downgrade` rate is high (40-60%) for *every* class including
  molecular controls, because it is dominated by `KEEP_AS_NON_CORE`/`MODIFY`,
  which are refinements, not errors. The hard `rm/OA%` and the aspect/non-core
  breakdowns are the discriminating signals, not the raw downgrade rate.

## The rubric (deliverable)

The grounded, curator-facing rubric is in [`ASSAY_TO_FUNCTION/RUBRIC.md`](ASSAY_TO_FUNCTION/RUBRIC.md)
(narrative + decision procedure + worked corpus contrasts) with a
machine-readable companion in [`ASSAY_TO_FUNCTION/rubric.yaml`](ASSAY_TO_FUNCTION/rubric.yaml).

Core rule: a convergent phenotypic readout licenses **at most** a BP (or CC)
"response to / regulation of P" term, **never MF**, defaulting to **non-core** —
promote to core only when independent evidence places the gene in P's recognized
machinery. The single MF exception is a transcriptional reporter for a bona fide
DNA-binding TF.

## The flagger (operationalized rubric)

[`ASSAY_TO_FUNCTION/flag_candidates.py`](ASSAY_TO_FUNCTION/flag_candidates.py)
applies the rubric to the mined matches and emits a prioritized re-review
worklist (`reports/flagged_candidates.tsv`). It flags only annotations that are
still *standing* (not already downgraded) and *thematically aligned* to a hub
readout, so precision stays high. Two tiers:

- **Tier 1 — MF from a hub readout** (a state readout cannot license molecular
  function). The legitimate transcriptional-reporter→TF-activity case is
  excluded.
- **Tier 2 — a core (`ACCEPT`) hub-aligned BP/CC call**, where the rubric
  default is non-core; verify the gene is in the recognized machinery.

```bash
uv run python projects/ASSAY_TO_FUNCTION/flag_candidates.py
```

Current run: **298 candidates (7 Tier 1, 291 Tier 2)**. The Tier-1 set is
precisely the reporter-driven over-annotation pattern the rubric predicts —
`transcription coactivator/corepressor activity` claimed from luciferase
reporters for coregulators that are **not** sequence-specific TFs (CTNNB1/
β-catenin, NOTCH1, SIRT1, HMGB1), plus Ca²⁺-binding MF terms (Calm2, HRC) that
should rest on EF-hand/structural evidence rather than Ca²⁺ imaging. Tier 2 is a
larger triage queue dominated by `MITO_MEMBRANE_POTENTIAL` (85, mostly generic
`mitochondrion`), `TRANSCRIPTIONAL_REPORTER` (72), and `AUTOPHAGY_FLUX` (70).

These are re-review *candidates*, not asserted errors.

### Tier-1 re-review outcome (loop closed)

All 7 original Tier-1 candidates were re-reviewed against their actual evidence
(see [`ASSAY_TO_FUNCTION/REREVIEW_TIER1.md`](ASSAY_TO_FUNCTION/REREVIEW_TIER1.md)).
Outcome: **none is a clean readout-driven over-annotation** — six KEEP, one
(SIRT1 corepressor activity) a soft non-core suggestion. Three calibration
findings fed back:

1. **Binding MF is a direct activity, not a readout consequence** — Calm2/HRC
   ("calcium … binding") were false positives. The flagger now excludes
   `*binding` MF from Tier 1 (7 → 5), and the rubric's "never MF" rule is scoped
   to *regulatory/process-like* MF, not binding/catalytic MF.
2. **Coregulator MF is legitimate for genuine coregulators** (β-catenin, NICD);
   the discriminator vs. the corpus's true over-annotation (`AIP → coactivator`)
   is machinery membership, not aspect.
3. **The standing-only filter works**: the real over-annotation (AIP) was
   already `MARK_AS_OVER_ANNOTATED`, so was correctly not re-flagged. The
   flagger's marginal value is therefore highest on *unreviewed* annotations and
   the Tier-2 queue, not on re-litigating accepted MF calls.

### Tier-2 triage + the machinery discriminator

The Tier-2 queue (core `ACCEPT` on a hub-aligned BP/CC term) is large and, on
its own, low precision: re-reviewing the top `VIABILITY_PROLIFERATION` class
showed the queue mixes genuine machinery (CDK1, MYC, RB1, TP53 — correctly core)
with indirect cases (IL21, PDGFB, VEGFA). See
[`ASSAY_TO_FUNCTION/REREVIEW_TIER2.md`](ASSAY_TO_FUNCTION/REREVIEW_TIER2.md).

The flagger now (a) ranks Tier 2 by each readout class's empirical any-downgrade
rate, and (b) adds a **machinery discriminator**: a candidate is tagged
`indirect_ligand` when the gene's own MF is a *secreted signaling ligand*
(cytokine/growth factor/hormone/chemokine), because then any cellular process it
drives is downstream of receptor signaling — the strongest computable non-core
signal. This cleanly isolates 6 high-precision non-core candidates (IL21, PDGFB,
VEGFA×2, HMGB1×2) at the top of the queue while the cell-cycle machinery sinks.

```bash
uv run python projects/ASSAY_TO_FUNCTION/flag_candidates.py --target accepted
```

## Next steps

1. **Curator triage** of the ranked `flagged_candidates.tsv`, starting with the
   `indirect_ligand` subset (highest-precision non-core candidates).
2. **Expand the catalog** with more probe vocabularies and the convergent
   *process-term* GO IDs each readout gets over-mapped to.
3. **Generalize the discriminator** beyond signaling ligands (e.g. transporters,
   structural proteins) — currently those indirect cases still need human
   judgement via the ranked queue.

## Relationship to existing projects

- `OVER_ANNOTATION_PATTERNS.md` — pattern #4 ("indirect downstream process
  annotations") is the conceptual cousin; this project quantifies the
  assay-specific version of it.
- `BIOSENSORS.md` — unrelated (plant synthetic-biology biosensors).
