# Reading & reviewing GO-CAM activities (best practice)

This is a distilled rubric for **reading** cached GO-CAM activities (annotons)
and judging whether they hold up — for QC of a model, for checking an activity
against a gene's annotation review, and for grounding `modules/` in real models.

It is adapted from the GO Consortium GO-CAM documentation and the
[`geneontology/gocam-agent`](https://github.com/geneontology/gocam-agent)
`gocam-best-practice` and `validate-claims` skills. Unlike that workspace, this
project is **read-only**: we never edit or upload models. We cache them
(`gocams/<id>/<id>-src.yaml`) and assess them
(`gocams/<id>/<id>-review.yaml`, schema class `GoCamReview`).

## What an activity (annoton) is

Each GO-CAM activity couples:

- `enabled_by` — the **gene product** that carries the activity,
- `molecular_function` — the GO MF term,
- optionally `part_of` — the **biological process** the activity contributes to,
- optionally `occurs_in` — the **cellular component** it happens in,
- `causal_associations` — directed edges to **downstream** activities.

In the cached YAML these are the fields of each entry under `activities:`, and
they are flattened into `gocams/index.tsv` (one row per activity).

## How to read each field (and how it goes wrong)

These map 1:1 to `GoCamQcFlagEnum` in the schema, so a `GoCamActivityReview` can
record exactly which issue applies.

- **Molecular function specificity.** Prefer the most specific MF term; a generic
  parent where a child applies is `GENERIC_MF`.
- **Binding is not a function.** A bare `protein binding`-type MF with no
  functional consequence is `BINDING_AS_FUNCTION`. Look for the real role:
  catalytic (kinase/phosphatase/…), receptor activity, molecular **adaptor**
  activity (connector/linker), or **sequestering** activity (capture/localize).
  Co-IP / pull-down / Y2H prove *interaction only* — they do not license an
  "activates" claim without a mechanistic shift.
- **`has input`** names what an activity targets/transforms, and is easy to
  misread (`HAS_INPUT_MISUSE`):
  - enzyme → the **substrate** modified;
  - transcription factor → the **target gene** (not the DNA);
  - receptor → the **downstream effector** activated (not the ligand — the ligand
    is a causal upstream regulator);
  - transporter → the **cargo**.
- **Direct vs indirect causal edges.** `directly_*_regulates` (e.g. `RO:0002413`)
  is a single step (kinase phosphorylates substrate); `*_regulates` /
  `indirectly_*` (e.g. `RO:0002407`) is multi-step (TF → expression → new
  activity). The wrong choice is `DIRECT_VS_INDIRECT_CAUSAL`; a reversed
  subject→object edge is `INCORRECT_DIRECTIONALITY`.
- **Context.** A missing `occurs_in` is `MISSING_LOCATION`; an activity not tied
  into a process via `part_of` is `MISSING_PROCESS`; an activity with no causal
  edges at all is `ORPHAN_ACTIVITY`.
- **Evidence.** Every activity/edge should carry an ECO code + reference; absence
  is `MISSING_EVIDENCE`. Mechanism ≠ phenotype: a knockout phenotype does not by
  itself license a *direct* regulation edge.
- **Complexes.** Represent the specific **active subunit** when its activity is
  known; use the complex term only when attribution is unclear; represent all
  contributing subunits when the activity is shared. A mismatch is
  `COMPLEX_SUBUNIT_REPRESENTATION`.

## Verdict scale

Record an overall `verdict` per activity (`GoCamClaimVerdictEnum`), mirroring the
forensic claim-validation scale:

- **OK** — well supported and best-practice-compliant.
- **UNCERTAIN** — defensible but imprecise or under-supported (needs a caveat).
- **WRONG** — contradicts the evidence or breaks a hard rule (binding-as-function,
  reversed causality, etc.).

Anchor every non-trivial verdict in **verbatim** `supporting_text` from a cited
reference (the same discipline as gene-review `supporting_text`). Biological
plausibility alone is not evidence.

## Consistency with gene reviews

The point of caching GO-CAMs here is to cross-check them against our annotation
reviews. For each activity, set `consistency` (`GoCamConsistencyEnum`) relative
to the gene's `genes/**/<gene>-ai-review.yaml`:

`CONSISTENT` · `MORE_SPECIFIC` · `MORE_GENERAL` · `RELATED` · `CONFLICT`
(the review removed/negated/over-annotated this function) · `NOT_IN_REVIEW`
(a candidate gap) · `NO_GENE_REVIEW`.

Join on `gene_product` via `gocams/index.tsv`. `CONFLICT` and `NOT_IN_REVIEW`
are the signals worth surfacing.

## Quick checklist

- [ ] MF is the most specific correct term (not generic, not bare binding).
- [ ] `has input` names the substrate/target-gene/effector/cargo — not a ligand or raw DNA.
- [ ] Causal edges are direct/indirect as the mechanism warrants, pointing subject→object.
- [ ] `occurs_in` and `part_of` are present where known.
- [ ] Every activity/edge has an ECO code + reference; claims have verbatim support.
- [ ] Complex activities attributed to the right subunit(s).
- [ ] Consistency with the gene review recorded (watch for CONFLICT / NOT_IN_REVIEW).

## Attribution

Adapted from the GO Consortium GO-CAM annotation guidelines and the
`gocam-best-practice` / `validate-claims` skills in
[`geneontology/gocam-agent`](https://github.com/geneontology/gocam-agent).
