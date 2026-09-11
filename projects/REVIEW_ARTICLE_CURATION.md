---
title: "Review-Article Curation"
maturity: SCOPING
tags: [PIPELINE, EVALUATION]
---

# REVIEW_ARTICLE_CURATION

**Does a review article carry as much curatable information as the primary
literature it summarizes — and is it cheaper to curate from? Test it at the
granularity a review is actually written at (family, complex, pathway), not at
the single gene.**

## Motivation: the existing result measures mismatch, not information

[`EVIDENCE_SOURCE_SUFFICIENCY`](EVIDENCE_SOURCE_SUFFICIENCY.md) already ran a
blind ablation of its H-a ("a review is usually sufficient for ACCEPT") and got a
discouraging number: **P(ACCEPT | REVIEW_ONLY, available) = 14.3%**, far below
abstract-only (85.7%). Taken at face value that kills the idea.

But the failure modes say something different. Of the 29 REVIEW_ONLY assignments
in `EVIDENCE_SOURCE_SUFFICIENCY/sample/blind_ablation_assignments.tsv`, **22 had
no review available at all**, and of the 7 that did, the blinded reviewer's stated
reason was a *granularity* complaint in 4:

| Gene | Term | Verdict | Blinded reviewer's reason |
|---|---|---|---|
| ATP6AP1 | GO:0048388 | UNDECIDED | "Review describes V-ATPases … but does not mention ATP6AP1 specifically" |
| ATP6V1E1 | GO:0033178 | UNDECIDED | "never mentions ATP6V1E1 or the E subunit specifically" |
| SRP19 | GO:0048500 | UNDECIDED | "describes the signal recognition particle as a six-protein, one-RNA … complex but does not specifically identify SRP19 as a component" |
| CYB5D2 | GO:0007399 | UNDECIDED | "lists 'neural functions' … spread across four MAPR proteins collectively, not specifically attributed to CYB5D2" |

The remaining three: one wrong-document selection failure (LRRK2 given generic
Parkinson's review material), one genuine depth failure (NFE2L2), one success
(CRISP3).

In every mismatch row the review *did* know the system — the V-ATPase, the SRP,
the MAPR family — and was marked insufficient because it did not descend to a
per-gene, per-term claim. Combined with the 22/29 availability failures (reviews
about single genes barely exist), the 14.3% is best read as: **we asked a
family-level document to fill a gene-level artefact.** That is a measurement
artifact of the evaluation unit, not a fact about review articles.

So: re-run the comparison with the artefact and the document matched in
granularity, and make granularity an experimental variable rather than a nuisance.

## The reframe: pick the document first, derive the unit from it

| Tier | Document that exists | Artefact class in this repo | Review availability |
|---|---|---|---|
| Gene | single-gene review (rare) | `GeneReview` (`genes/<org>/<G>/<G>-ai-review.yaml`) | poor — the negative control |
| Family | family/superfamily review | `FamilyReview` (`interpro/panther/<PTHR>/<PTHR>-review.yaml`, 14 curated) | good |
| Complex / pathway / module | complex or pathway review | `ModuleReview` (`modules/*.yaml`, 317 already curated) | good |

The repo is already set up for the two upper tiers: `ModuleReview` decomposes
into `parts`, `variant_sets`, `annotons`, and `connections`, each carrying
`EvidenceItem`s — which is the level a good pathway review actually writes at.
`FamilyReview` decomposes into `subfamilies`, `node_assessments`, `term_assessments`,
and `residue_sites` — subfamily-level functional divergence and IBD node placement,
which is exactly the level a family review writes at. The gene tier is retained
deliberately, as the condition we expect reviews to lose, to confirm the mismatch
diagnosis rather than assume it.

`FamilyReview.residue_sites` is a bonus for this experiment specifically: a residue
claim is anchored to a reference protein's native numbering and can be **checked
against the actual sequence automatically**, giving a fabrication metric that needs
no adjudicator at all.

## Two questions, kept separate

- **Q1 — information content.** Does review-only curation recover the same nodes,
  terms, topology, and specificity as primary-only curation?
- **Q2 — cost.** Is it cheaper per unit of curated output (documents read, tokens,
  turns, wall-clock, rework)?

Do not collapse them. A source can lose on Q1 and still win decisively on
cost-per-recovered-node, which is the operationally interesting answer: reviews
as a cheap first pass that primary literature then refines.

## Design

### Sampling frame — anchor on the review, not on the gene

The prior study sampled genes and asked whether a review existed; that guarantees
a thin, biased review arm. Invert it:

1. Define a frame of candidate review articles with pre-registered inclusion
   criteria (e.g. PubMed `PT=Review` plus journal heuristics — Annu Rev, Nat Rev,
   Trends, Curr Opin, WIREs — published in the last N years, full text cacheable).
2. Keep reviews whose scope maps onto a **nameable unit**: a PANTHER family, a
   protein complex, or a pathway/module we can express as a `ModuleReview`.
3. Stratify the sample across the three granularity tiers and across
   well-studied vs obscure units (the latter matters for leakage, below).

Roughly half of the 317 existing modules should be matchable to a pathway or
complex review; that is the sampling pool for the module tier.

### Defining the matched primary corpus (the "cone")

Two defensible definitions, and they are not equivalent:

- **Review-bibliography cone** — the primary papers the review itself cites.
  Clean pairing, but *circular*: the review is guaranteed to cover exactly this
  literature, so it inflates the review arm.
- **Independent cone** (recommended as the primary analysis) — the primary
  references cited in GOA/UniProt for the members of the unit, assembled without
  reference to the review. The review is then free to miss things, which is the
  question being asked.

Run both; the gap between them is itself a result (how much of the relevant
literature a review omits).

### Arms

All arms receive the same scaffolding (UniProt records, GOA tables, sequence,
schema, prompt, validation loop) and differ **only** in the narrative bundle:

| Arm | Bundle | Purpose |
|---|---|---|
| **0 — floor** | scaffolding only, no narrative text | measures what the curating model produces from parametric memory. **Essential**; without it, agreement between R and P may just be memorization. |
| **R** | the review article, full text | the treatment |
| **P** | the independent cone, full text, review withheld | the comparator |
| **P-matched** | random subset of the cone truncated to the review's token count | fair per-token comparison; controls the volume confound |
| **R+P** | both | ceiling / headroom estimate |

Arms are curated independently and blind to each other by separate agent
sessions; outputs are relabeled before adjudication.

### Gold standard

Primary: **union adjudication.** A third, unblinded adjudicator with all arms plus
unrestricted retrieval builds the reference artefact; each arm is then scored
against it. This avoids depending on a pre-existing curation and is symmetric
between arms. Human spot-check on a subsample.

Secondary: the **existing curated module/family artefact**, where one exists *and*
its provenance is review-free — otherwise the review arm is scored against a
target partly derived from reviews.

### Metrics

Because both arms emit schema-validated YAML with grounded identifiers, scoring
is structural rather than free-text:

**Q1 — content**

- **Node recall** — fraction of gold `parts` / `annotons` / family members recovered.
- **Term recall, ontology-aware** — per gold descriptor, classify the arm's term as
  EXACT / ANCESTOR / DESCENDANT / SIBLING / UNRELATED / ABSENT. (Reuse the
  exact-core-MF-match metric from [`AFFINAGE_EVALUATION`](AFFINAGE_EVALUATION.md),
  which already found "stops at a general parent" to be the dominant failure of a
  narrative-derived grounding.)
- **Specificity** — mean information content / depth of asserted MF terms, and the
  signed delta to gold. Directly quantifies "the review stops at the parent".
- **Precision / fabrication** — asserted nodes and terms absent from gold *and*
  unsupported by that arm's own bundle.
- **Groundedness** — fraction of assertions whose `supporting_text` passes the
  repo's existing verbatim-substring reference validator. Free and fully objective.
- **Topology** — `connections`, `variant_sets`, and module-boundary decisions
  recovered. Predicted review strength.
- **Fine-grained claims** — residue claims, negative/NOT results, taxon distribution,
  `knowledge_gaps`. Predicted review weakness. At the family tier, `residue_sites`
  additionally give a *sequence-checkable* fabrication rate, independent of gold.

**Q2 — cost**

Documents opened, tokens read, curator turns, tool calls, wall-clock, first-pass
`just validate` failure count, and post-adjudication rework edits. Derived headline:
**gold nodes recovered per 1k tokens read.**

### Confounds and controls

1. **Volume asymmetry** — one review vs 60 papers confounds information with
   reading budget. → `P-matched` arm.
2. **Staleness** — a review is stale by construction. → record the review's
   publication year, and report recall both overall and against the *recoverable
   subset* (gold nodes whose supporting evidence predates the review). This
   separates "reviews lose because they are old" from "reviews lose because they
   are shallow", and only the second is an argument against the approach.
3. **Parametric leakage** — the curating model already knows TP53. → Arm 0 as the
   floor, verbatim-`supporting_text` enforcement on every assertion, and
   deliberate oversampling of obscure families/modules.
4. **Review quality variance** — → pre-registered frame and inclusion criteria;
   record journal and citation count as covariates. The LRRK2 row above shows what
   an off-target review does to the numbers.
5. **Cone circularity** — → independent cone as the primary analysis (above).
6. **Adjudicator bias** — → arms anonymized and presented in randomized order.

### Predictions (state before running)

Pre-registering these makes the study falsifiable rather than confirmatory:

- Review recall rises monotonically with tier: gene < family < module. *(If it does
  not, the granularity-mismatch diagnosis above is wrong.)*
- Reviews win on module topology, boundary setting, and variant sets.
- Reviews lose on residue-level claims, negative results, and MF term specificity
  (systematic ANCESTOR bias).
- Reviews win Q2 decisively — several-fold more gold nodes per 1k tokens read.
- Arm 0 is well below both R and P at the module tier, and uncomfortably close to
  them at the gene tier for famous genes.

### Pilot sizing

Pilot: **6 units** (2 gene, 2 family, 2 module) × arms {0, R, P} = 18 curation runs,
to shake out the instrument, the scoring code, and the adjudication rubric. Then
scale to ~30 units with the full five arms, bootstrapping CIs clustered by unit
(same approach as `EVIDENCE_SOURCE_SUFFICIENCY/score.py`).

## Status

- [ ] Lock the design and pre-register it as `REVIEW_ARTICLE_CURATION/PROTOCOL.md`
- [ ] Build the review frame + unit matcher over `modules/` and PANTHER families
- [ ] Bundle builder (scaffolding / review / cone / budget-matched cone)
- [ ] Structural scorer (node recall, ontology-aware term match, specificity delta)
- [ ] Pilot n=6 × 3 arms
- [ ] Scale to n=30, unit-clustered bootstrap CIs

## Relationship to existing projects

- [`EVIDENCE_SOURCE_SUFFICIENCY`](EVIDENCE_SOURCE_SUFFICIENCY.md) — the parent.
  This project is its H-a, re-specified so the evaluation unit does not prejudge
  the answer. H-b (abstracts) and H-c (deep research) stay there.
- [`AFFINAGE_EVALUATION`](AFFINAGE_EVALUATION.md) — supplies the ontology-aware
  grounding metrics and a prior on narrative-derived groundings being
  parent-biased.
- [`ASSAY_TO_FUNCTION`](ASSAY_TO_FUNCTION.md) — orthogonal axis: which experimental
  readouts license an annotation, rather than which document type carries it.
