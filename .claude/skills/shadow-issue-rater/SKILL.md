---
name: shadow-issue-rater
description: >
  Independently rate our shadow work on a mirrored upstream issue
  (issues/<tracker>/<N>/), compare it with what the curators actually did, write
  rating.yaml and the resolution block, and publish a Claude artifact reporting the
  approach taken and how well it did. Use after a shadow worker has finished an
  issue that upstream has closed, or when asked to rate or report on shadow work.
---

# Shadow Issue Rater

You are the independent rater for one shadow issue. You must not be the agent that
did the shadow work. The protocol is in `projects/GO_ANNOTATION_TRACKER.md`; the
record formats are `ShadowIssue`, `ShadowRating` and `SelfRating` in
`src/ai_gene_review/schema/shadow_issue.yaml`.

## Never notify upstream

Never write an upstream issue URL or `geneontology/<repo>#N` in a commit message,
PR, issue or comment, and never at-mention anyone except cmungall. Do not push, open
PRs, or comment unless the coordinator asks. Name an upstream issue as
`issues/go-annotation/N` or "go-annotation N". In the report artifact, refer to
curators by role ("the PAINT curator", "an SGD curator"), not by name or handle,
and use they/them for them.

## 1. Read the shadow work without the self-rating

Do not open `self-rating.yaml` until you have scored. Read `issue.yaml` (triage,
shadow, prior_work), `shadow.md`, and the diff of the work products listed in
`shadow.work_products`.

## 2. Establish what upstream did

You may read everything: `just show-shadow-issue N` (full thread),
`thread.jsonl`, `source.yaml`. Many threads end in "fixed", so also check
downstream reality with read-only queries: the gene product's current annotations
(QuickGO or GO API), interpro2go, ARBA or PAINT releases, linked ontology changes.
Compare with the repo's cached `GENE-goa.tsv`. A fix not yet visible is usually
release lag; say so, do not guess.

Fill `resolution` in `issue.yaml`: `status`, `resolved_at`, `summary`, and
`evidence` (`kind`, `ref` such as `comment:<id>`, `checked_at` for every downstream
check, `note`). Do not touch `triage` or `shadow`.

## 3. Score

Write `rating.yaml`: `tracker`, `number`, `rater`, `rated_at`,
`saw_self_rating: false` (true if you saw it before scoring, and say how in
`summary`), `outcome`, and the dimensions `triage`, `diagnosis`, `actions`,
`downstream` (`PENDING_RELEASE` when upstream acted but the change is not yet
released), `added_value`, `harm`, and `summary`.

Judge term by term. Credit added value only after verifying it. Spot-check two or
three of the worker's key factual claims and quotes. Name every confound in
`summary`, especially `prior_work` (NAMES_ISSUE unblinds the thread;
COVERS_SUBJECT means the repo already held a conclusion).

Run `just validate-shadow-issues <tracker>`.

## 4. Publish the report artifact

As the last step, publish a Claude artifact (Artifact tool, a plain HTML page)
that a reader who has not seen the files can follow. It covers:

- the issue in one paragraph (the claim and what kind of issue it is);
- the approach taken: blinding and what the worker could see, prior work, what
  the worker investigated and produced, with file paths;
- what upstream did, with the evidence and the dates checked;
- the rating: outcome and each dimension, with the reason for each;
- what the worker got right, what it missed, and any claim that was refuted;
- confounds, and lessons for the protocol or tooling;
- cost where known (tokens, wall time).

Title it with the tracker and number, e.g. "go-annotation 6596 shadow". Record the
URL as `report_url` in `rating.yaml`, then validate again. The coordinator adds
the link to the PR description.

## 5. Commit

Commit locally with a message like "Rate shadow work on go-annotation N", checked
with `python3 src/ai_gene_review/shadow_issues/guard.py --commit-msg FILE`.
