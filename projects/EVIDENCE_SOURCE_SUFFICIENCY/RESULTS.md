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

## What is NOT trustworthy from this pass

- **E-d (narrative sections):** comes out ~0% narrative / 96% abstract, but this
  is a **cache artifact** — full-text sections are mostly unlocatable in our
  cache, so Discussion/Conclusions quotes fall into the UNKNOWN bucket rather
  than being counted. H-d needs a full-text reading pass; do not cite this 0%.
- **Blind-ablation (E-a/E-b/E-c sufficiency):** intentionally left empty.
  `autolabel.py` does not fabricate blinded verdicts.

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
4. **No confirmation-bias control yet.** The blind ablation is the only unbiased
   sufficiency estimate; until it is run, the abstract-sufficiency numbers
   describe curator citation behavior, not proven sufficiency.

## Next

1. Full-text reading pass to fix H-d (where facts *first* appear) and to upgrade
   `fact_in_abstract` from cited-snippet to semantic (is the fact in the abstract
   regardless of where it was quoted).
2. Run the blind-ablation bundles (87 rows) for the unbiased sufficiency numbers
   and the retrospective-vs-blind calibration gap.
3. Improve review detection beyond PubMed PT for a real H-a denominator.

*Reproduce:* `uv run python projects/EVIDENCE_SOURCE_SUFFICIENCY/autolabel.py`
then `uv run python projects/EVIDENCE_SOURCE_SUFFICIENCY/score.py`.
