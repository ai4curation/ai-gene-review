---
title: "EVIDENCE_SOURCE_SUFFICIENCY — preliminary results (objective auto-pass)"
---

# EVIDENCE_SOURCE_SUFFICIENCY — preliminary results (objective auto-pass)

**Status: PARTIAL.** These come from the *objective* auto-labeling pass
(`autolabel.py`), which locates each curator's cited justifying quote in the
cached publication / deep-research file. They answer a sharp, reproducible
question — *where does the cited justifying fact live?* — but are **a lower bound
on abstract-sufficiency**, and the unbiased blind-ablation test is **not yet
run**. Read with the caveats at the bottom.

Sample: 30 human genes, 484 ACCEPT annotations (seed 20260614). Quote located in
cached text for **373/484**; the other 111 had no cited supporting_text or a
quote not present in our cache (often full-text-only papers we don't cache).

## Headline (fair test) — H-b

The cache is abstract-heavy (13.7k abstract-only vs 5.5k full-text pubs), so for
abstract-only pubs a quote can *only* be found in the abstract. Restricting to
ACCEPT annotations that cite a **full-text-cached** pub — a genuine
abstract-vs-full-text contest — removes that artifact:

> **Among 212 ACCEPT annotations citing a full-text-cached pub, the justifying
> quote is in the abstract/title for 192 (90.6%); only 20 (9.4%) required a
> full-text-only sentence.**

So for ACCEPT, the abstract carries the cited justifying fact ~9 times in 10,
even when the full text was available.

## All-locatable estimates (gene-clustered 95% CIs)

| Estimand | Overall | MF | BP | CC |
|---|---|---|---|---|
| **E-b** abstract is minimal tier \| ACCEPT | **92.8%** [86–98] (n=373) | 98.8% | 87.2% | 88.6% |
| **E-a** a *review* was cited for the fact \| ACCEPT | 2.9% [0–6] (n=450) | 1.7% | 4.3% | 3.1% |
| **E-c** *deep research* carries the fact \| ACCEPT | 11.3% [5–21] (n=450) | 10.3% | 13.0% | 11.2% |

E-a conserved/IBA subgroup: 3.9% (n=51). Reference-level: only 15/916 references
flagged as reviews (PubMed PT + journal-name heuristic) — see caveats.

The all-locatable E-b (92.8%) and the artifact-free fair test (90.6%) agree
closely, which is reassuring: the cache bias inflates the *denominator* but not
the headline rate by much.

## Blind-ablation validation (the unbiased test)

A blinded reviewer (a separate agent, no access to the original decision or the
full text) was shown *only* one restricted bundle per annotation and asked
ACCEPT / UNDECIDED / REJECT, judging solely from that text. 29 annotations per
bundle; "available" = the bundle actually had text (many genes have no review in
their reference list, and some have no DR file).

| Bundle | Source available | **P(ACCEPT \| available)** | P(ACCEPT \| assigned) |
|---|---|---|---|
| ABSTRACT_ONLY | 21/29 | **85.7%** [65–100] (0 rejects) | 62.1% |
| DEEP_RESEARCH_ONLY | 20/29 | **40.0%** [22–59] | 27.6% |
| REVIEW_ONLY | 7/29 | **14.3%** [0–43] | 3.4% |

**Ranking (conditional on availability): abstract (86%) ≫ deep research (40%) >
review-alone (14%).** The abstract alone genuinely confirms the specific ACCEPT
annotation ~6 times in 7, with zero blind rejections — H-b survives the unbiased
test. Deep research, though heavily *used*, is insufficient on its own ~60% of
the time (tempers H-c). A review alone is both rarely available (24% of genes)
and, when available, rarely sufficient for the specific term (tempers H-a).

**Calibration:** retrospective abstract-sufficiency 92.8% vs blind ACCEPT\|abstract
85.7% — a **+7.0 pt retrospective optimism gap** (only +4.9 vs the fair 90.6%).
Small and in the expected direction, which is reassuring for the retrospective
numbers.

Caveat: the blinded reviewer was instructed to judge from the provided text only
(not parametric gene knowledge), so this measures *source* sufficiency, which is
stricter than a human curator who also brings background knowledge.

## What is NOT trustworthy from this pass

- **E-d (narrative sections):** comes out ~0% narrative / 96% abstract, but this
  is a **cache artifact** — full-text sections are mostly unlocatable in our
  cache, so Discussion/Conclusions quotes fall into the UNKNOWN bucket rather
  than being counted. H-d needs a full-text reading pass; do not cite this 0%.

## Caveats (why this is a lower bound, and where it can mislead)

1. **Cited ≠ minimal-sufficient.** We record where the curator *quoted* from. If
   a fact was quoted from Results but is *also* in the abstract, we score
   FULLTEXT — so this **understates** abstract-sufficiency. The fair test (90.6%)
   is therefore a floor.
2. **Cache composition.** Addressed for H-b by the full-text-cached stratum;
   still fatal for H-d (above).
3. **Review undertagging.** E-a counts "a review was *cited*", using PubMed PT +
   a journal-name heuristic, both of which miss reviews. It does **not** test
   "could a review have supported it" — that is what the blind REVIEW_ONLY bundle
   is for. Treat 2.9% as a floor on review *usage*, not review *ability*.
4. **Confirmation-bias control (done).** The blind ablation above is the unbiased
   estimate; it agrees with the retrospective abstract number within +7 pts.
5. **Source-only judgement.** The blind reviewer judged from the bundle text
   alone; a human curator using background knowledge might ACCEPT more often, so
   the blind numbers are a *conservative* floor on real-world sufficiency.

## Next

1. Full-text reading pass to fix H-d (where facts *first* appear) and to upgrade
   `fact_in_abstract` from cited-snippet to semantic (is the fact in the abstract
   regardless of where it was quoted).
2. Improve review detection / availability beyond PubMed PT, and broaden the
   REVIEW_ONLY bundle beyond a gene's own cited references, for a fairer H-a test.
3. Scale the sample beyond 30 genes to tighten the per-bundle blind CIs.

*Reproduce:*
```bash
uv run python projects/EVIDENCE_SOURCE_SUFFICIENCY/autolabel.py
uv run python projects/EVIDENCE_SOURCE_SUFFICIENCY/build_blind_bundles.py   # builds restricted bundles
# blinded verdicts are produced by separate reviewers and merged into
# blind_ablation_assignments.tsv
uv run python projects/EVIDENCE_SOURCE_SUFFICIENCY/score.py
```
