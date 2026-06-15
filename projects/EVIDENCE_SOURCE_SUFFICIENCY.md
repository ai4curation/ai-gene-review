# EVIDENCE_SOURCE_SUFFICIENCY

**Which lower-effort evidence sources are *sufficient* to support an ACCEPT decision for an existing GO annotation — review papers, abstracts alone, or deep-research reports?**

## Motivation

Reviewing an existing GO annotation costs curator (or agent) effort, and that
cost is dominated by *which document you have to read*. Reading a full-text
primary paper is expensive; reading an abstract, a narrative review, or a
pre-synthesized deep-research report is cheap. If cheap sources are routinely
*sufficient* to confirm an annotation, the review pipeline can be made much
faster and cheaper — especially for the modal action, **ACCEPT**.

This project tests four hypotheses about evidence-source sufficiency:

- **H-a (reviews):** For ACCEPT, a published *review* article is usually
  sufficient — and reviews tend to carry the phylogenetic / comparative
  reasoning that justifies a conserved-function call.
- **H-b (abstracts):** For ACCEPT, the *abstract alone* is often sufficient.
- **H-c (deep research):** A *deep-research* report has sufficient depth to
  support ACCEPT.
- **H-d (narrative sections):** The *background* (Introduction / Literature
  Review) and *Discussion / Conclusions* sections are a rich but under-used
  vein of supporting text.

### Why ACCEPT

ACCEPT is both the modal action and the one where cheap confirmation is most
plausible: confirming an already-asserted function is easier than overturning
or refining it. The opposite end (REMOVE / MODIFY) plausibly *needs* deeper,
primary evidence, and the baseline census below already hints at this
(REMOVE support is 92.8% primary research and only 16.7% abstract-only). So the
payoff of "cheap sources suffice" is concentrated in ACCEPT, and that is where
we scope the question.

## The key methodological pitfall: usage ≠ sufficiency

The corpus records **what curators cited**, not **what was required**. This is a
census of *observed usage*, and it is confounded by habit and ordering:

> **Absence of review (or deep-research) support in a review does NOT mean a
> review was *unable* to support the annotation.** A curator who reaches for a
> primary paper first, and stops once the annotation is justified, leaves no
> trace that a review would have served equally well.

Therefore the census can only ever give a **lower bound** on how often a source
*could* suffice, and it cannot establish sufficiency or necessity on its own.
Any real test of H-a–H-d needs an **ablation / counterfactual** design (below),
not just a tally of the existing `supported_by` blocks.

## What has been built

A reusable measurement layer (PR on branch
`claude/go-annotation-sources-rqwmfl`):

- **`Reference.publication_type`** (`PublicationTypeEnum`: `PRIMARY_RESEARCH`,
  `REVIEW`, `SYSTEMATIC_REVIEW`, `META_ANALYSIS`, `DEEP_RESEARCH`, `DATABASE`,
  `BIOINFORMATICS`, …). For PMIDs it is inferred from PubMed's MEDLINE `PT`
  metadata; for `GO_REF` / `Reactome` / `file:` refs from the identifier scheme.
- **`ai-gene-review analyze-evidence-sources`** — cross-tabulates
  `publication_type × reference_section_type × review.action` across an
  organism and writes `reports/evidence_sources/<organism>_evidence_sources.md`
  plus per-snippet / per-annotation / per-reference TSVs.
- The existing **`reference_section_type`** slot on every supporting-text
  snippet already records which manuscript section a quote came from
  (TITLE / ABSTRACT / INTRODUCTION / RESULTS / DISCUSSION / CONCLUSIONS / …).

## Baseline census (human, 933 reviews) — and its caveats

From the first run (30.8k references, 70.2k evidence snippets, 52.6k reviewed
annotations):

| Hypothesis | Census signal | Read with caveat |
|---|---|---|
| H-a reviews | Reviews are cited rarely: 1.5% of refs; ≤3.8% of annotations have any review support; primary research dominates every action. Phylogenetic reasoning enters via the **IBA / `GO_REF:0000033`** pipeline, not narrative reviews. | Usage ≠ ability. Says nothing about whether a review *could* support ACCEPT. PubMed under-tags reviews, so REVIEW is a lower bound. |
| H-b abstracts | Of section-tagged snippets, 61.5% are title/abstract. **Abstract-only support by action: ACCEPT 70.8%, MARK_AS_OVER_ANNOTATED 81.2%** vs MODIFY 46.9%, REMOVE 16.7%. | Strongest result, and it points the right way for ACCEPT — but measured on the ~5% of snippets that carry a section tag. |
| H-c deep research | 723 deep-research refs across 556 genes support **6,914 annotations** — far more used than reviews. | Heavy *use* ≠ sufficient *depth*; depth/correctness not yet scored. |
| H-d narrative | Narrative sections (Intro / Lit-review / Discussion / Conclusions) are only **5.1%** of tagged snippets; CONCLUSIONS appears in **2**. Abstract (59%) + Results (23%) dominate. | Either an untapped vein or evidence it isn't needed — cannot tell from a usage census. |

## Limitations to fix before drawing conclusions

1. **PubMed under-tags reviews.** The MEDLINE `PT` field misses many review
   articles (e.g. PMID:24268103, a KCTD review, is only "Journal Article"). Add
   journal-name heuristics (Nat Rev, Trends, Annu Rev, WIREs, Curr Opin, "…
   Reviews"), MeSH, and/or a lightweight content classifier; backfill
   `publication_type`. Until then REVIEW counts are a floor.
2. **Section tagging is ~5% populated.** H-b and H-d are measured on a small,
   possibly biased subset. Raise coverage (validator nudge and/or a backfill
   pass that assigns `reference_section_type` to existing snippets) before
   trusting the section distribution.
3. **Cited ≠ required.** The census measures observed usage. It cannot, by
   itself, answer the sufficiency/necessity questions H-a–H-d pose.

## Proposed methodology: ablation re-review (the real test)

To move from "what was cited" to "what suffices", run a counterfactual on a
sample of **ACCEPT** annotations that today carry full-text / primary support:

1. **Build restricted evidence bundles** per annotation:
   (i) abstract-only, (ii) review-only, (iii) deep-research-only.
2. **Re-review under each restriction**, blinded to the original decision, and
   record whether ACCEPT is still reached *with adequate justification*.
3. **Sufficiency estimate** = agreement rate with the original ACCEPT under each
   restricted bundle. High agreement ⇒ that source class is sufficient for ACCEPT
   in that stratum.
4. **Necessity probe** (complementary): where primary/full-text was cited, judge
   whether an abstract or review conveys the same fact — LLM-assisted with human
   spot-check.

Stratify by aspect (MF / BP / CC) and by whether the term is a conserved /
phylogenetically-inferred function (where H-a's "reviews carry the phylogenetic
reasoning" should bite hardest).

A pre-registered protocol operationalizing this for ACCEPT decisions is in
[`EVIDENCE_SOURCE_SUFFICIENCY/PROTOCOL.md`](EVIDENCE_SOURCE_SUFFICIENCY/PROTOCOL.md);
the reproducible stratified sample (30 genes, 484 ACCEPT annotations, seed
`20260614`) is produced by `EVIDENCE_SOURCE_SUFFICIENCY/sample/sample_genes.py`.

## Status

- [x] `publication_type` schema field + PubMed-PT inference + cache
- [x] `analyze-evidence-sources` CLI and first human census report
- [x] Pre-registered study protocol + reproducible stratified-by-aspect sampler
- [x] Scoring harness (`sample/../score.py`): estimands + gene-clustered bootstrap CIs + blind calibration
- [x] Objective auto-labeling pass (`autolabel.py`, cited-snippet provenance) + [preliminary results](EVIDENCE_SOURCE_SUFFICIENCY/RESULTS.md): for ACCEPT annotations citing a full-text-cached pub, the justifying quote is in the **abstract 90.6%** of the time (artifact-free fair test)
- [x] Blind-ablation validation (`build_blind_bundles.py` + blinded reviewers): conditional on availability, **abstract 85.7% ≫ deep research 40% > review-alone 14.3%**; retrospective abstract number is optimistic by only +7 pts
- [ ] Full-text reading pass (fixes H-d; upgrades fact_in_abstract to semantic)
- [ ] Broaden REVIEW_ONLY bundle + scale sample to tighten blind CIs
- [ ] Better review detection (journal/MeSH heuristics) + `publication_type` backfill
- [ ] Raise `reference_section_type` coverage above the current ~5%
- [ ] Ablation re-review harness for ACCEPT annotations (sufficiency test)
- [ ] Deep-research depth scoring (H-c)

## Next steps

1. Improve review detection so H-a is tested against a real review set, not a
   PubMed-PT floor.
2. Backfill section tags so the H-b / H-d distributions are representative.
3. Stand up the ablation re-review harness on a pilot of ACCEPT annotations,
   starting with MF terms where abstract-level confirmation looks strongest.

## Relationship to existing projects

- **`ASSAY_TO_FUNCTION.md`** — complementary axis: that project asks *which
  experimental readouts* license an annotation; this one asks *which document
  sources* are enough to confirm one.
- **`AD_HOC_BIOINFORMATICS.md`** — bioinformatics analyses are themselves a
  `publication_type: BIOINFORMATICS` evidence source tracked by this analysis.
