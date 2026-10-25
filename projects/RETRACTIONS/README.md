---
title: "Retraction check — supporting material"
---

# Retraction check — supporting material

Supporting material for the [Retracted Literature project](../RETRACTIONS.md).

## Contents

- `check_retractions.py` — the checker. Walks every `genes/*/*/*-ai-review.yaml`,
  collects each `PMID:` citation **with its citation site** (`reference`,
  `annotation` = an annotation's `original_reference_id`, or `supporting_text` =
  a `supported_by[].reference_id`), queries PubMed in batches of 200 through NCBI
  E-utilities `efetch`, and reads the `PublicationType` list and the
  `CommentsCorrections` `RefType`s. Records that are themselves retraction /
  expression-of-concern / erratum **notices** are excluded — citing the notice is
  good practice, not a defect.
- `retraction-check.tsv` — **generated**: one row per flagged PMID, with severity,
  the raw PubMed signals, the notice PMID(s), which genes cite it, how they cite
  it, and whether the review already records `is_invalid: true`.
- `retraction-check.json` — **generated**: the same data plus run totals and the
  PMIDs PubMed did not resolve.
- `retraction-register.md` — **generated** register (do not edit by hand):
  retractions first, then expressions of concern, then errata in a quiet
  informational section.

## Regenerate

```bash
uv run --no-dev python projects/RETRACTIONS/check_retractions.py
```

A full pass is ~126 `efetch` requests over ~25,000 PMIDs and takes the better part
of an hour; set `NCBI_API_KEY` to raise the rate limit. Useful variants:

```bash
# check specific PMIDs (still reports where they are cited in the reviews).
# A partial run needs its own --out-dir so it cannot overwrite the full-scan
# reports with a handful of rows; --pmids also accepts a comma-separated list.
uv run --no-dev python projects/RETRACTIONS/check_retractions.py \
    --pmids 19225519,16616141 --out-dir /tmp/spot

# rebuild the register from the last run, no network
uv run --no-dev python projects/RETRACTIONS/check_retractions.py \
    --from-json projects/RETRACTIONS/retraction-check.json
```

## Severity tiers

| Tier | PubMed signal | Weight |
|---|---|---|
| `RETRACTED` | `Retracted Publication` publication type, or a `RetractionIn` reference | Actionable — the source is withdrawn |
| `EXPRESSION_OF_CONCERN` | `Expression of Concern` publication type, or an `ExpressionOfConcernIn` reference | Read the notice; not grounds for removing an annotation |
| `ERRATUM` | An `ErratumIn` reference | **Usually benign** — most errata are an author name, an affiliation or a figure legend |

The `citation_sites` column is what makes a row actionable: a retracted paper in a
`references:` list is bibliographic cleanup, whereas the same paper as an
annotation's `original_reference_id` is a curation question.

## PubPeer check (prototype)

- `check_pubpeer.py` — asks PubPeer which cited PMIDs have comments. It reuses
  `check_retractions.py`'s citation harvest, so rows carry the same
  `citation_sites`. It then re-asks PubMed about each PubPeer hit, so every
  row has a current PubMed severity and the register can pick out the papers
  that are discussed but carry no formal notice.
- `pubpeer-check.tsv` / `pubpeer-check.json` — **generated**: one row per cited
  PMID with PubPeer comments (count, latest comment date, thread URL, publisher
  updates PubPeer relays, PubMed severity, citing genes, and the review actions
  on any annotation resting on the paper).
- `pubpeer-register.md` — **generated** register: PubPeer-only formal notices
  first, then discussed papers behind GO annotations with no PubMed notice.

```bash
uv run --no-dev python projects/RETRACTIONS/check_pubpeer.py
uv run --no-dev python projects/RETRACTIONS/check_pubpeer.py --pmids 19225519 --out-dir /tmp/pp
uv run --no-dev python projects/RETRACTIONS/check_pubpeer.py --from-json projects/RETRACTIONS/pubpeer-check.json
```

Endpoint caveats, all found by probing it:

- It uses `https://pubpeer.com/v3/publications`, the endpoint PubPeer's browser
  extensions call, with the extension's public `devkey`. That is fine for a
  prototype but is not a documented bulk API; get a PubPeer key before
  scheduling this, and pass it as `PUBPEER_DEVKEY`.
- **At most 10 publications are returned per request**, however many PMIDs are
  sent, and only PMIDs with a PubPeer page come back. A 100-PMID batch found 10
  hits where the same PMIDs asked 10 at a time found 27. The checker splits any
  batch whose response is full until each answer is provably complete.
- The default `python-requests`/`urllib` user agents get a 403.
- **Matching is not strictly by PMID**: asked about PMID 13760, PubPeer
  returns PMID:27926515, an unrelated 2016 Oncotarget paper. Entries for PMIDs
  that were not asked for are dropped.
- It rate-limits at ~3 requests/second (429). Requests are spaced 1 s apart and
  back off on 429; a full pass takes roughly half an hour.
- PubPeer's relayed notices are incomplete. It showed no update for one PubMed
  retraction (PMID:16616141) and only an erratum for another (PMID:29371969),
  so PubMed stays the authority on severity.

A comment count is not a verdict: a thread can be an image-duplication report
or a request for a reagent. The register ranks and lists; reading the thread is
the curator's step.
