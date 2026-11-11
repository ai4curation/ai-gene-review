---
name: shadow-issue-rater
description: >
  Independently rate our shadow work on a mirrored upstream issue
  (issues/<tracker>/<N>/), compare it with what the curators actually did, write
  rating.yaml, the resolution block and a committed report.md on the approach taken
  and how well it did (optionally mirrored as a Claude artifact). Use after a shadow worker has finished an
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

Write `rating.yaml`:

- `tracker`, `number`, `rated_at`;
- `rater` (who rated), `rater_model` (the model, or `human`), `rater_run` (a
  workflow run URL, or a session id and agent role), and `independence`:
  `DIFFERENT_PERSON`, `DIFFERENT_MODEL`, or `SAME_MODEL_SEPARATE_RUN` when your
  model is the worker's (`shadow.worker`). Prefer a different model; never rate
  work you did;
- `self_rating_seen`: `NEVER`, `BEFORE_SCORING` (your scores may be influenced),
  or `AFTER_SCORING`. Say how it happened in `summary` if not `NEVER`;
- `outcome`, and the dimensions `triage`, `diagnosis`, `actions`, `downstream`
  (`PENDING_RELEASE` when upstream acted but the change is not yet released),
  `added_value`, `harm`;
- `summary`.

If the issue already has a `rating.yaml`, do not read it (or its report)
before scoring; write yours as `rating-<label>.yaml` with `report-<label>.md`,
and the coordinator decides which is primary (the most independent one).

Judge term by term. Score only what the evidence shows: if the thread does not
say whether upstream made a change, that is unknown, not a "no". Score
`downstream: PENDING_RELEASE` whenever upstream acted and none of it is in
released data yet; use PARTIAL or DISAGREE only for released changes. A `FLAG_FOR_CHECK` action is a question, not a proposal: it
neither agrees nor disagrees with what was done. Credit added value only after
verifying it. Spot-check two or three of the worker's key factual claims, and run
`just validate-quotes` for its `supported_by` quotes. Name every confound in
`summary`: `prior_work` (NAMES_ISSUE unblinds the thread; COVERS_SUBJECT with
`shadow.saw_prior_work: true` means the worker started from the repo's own
conclusion), and for RETROSPECTIVE issues whether the title alone gave the kind
away.

## 4. Write the report

Write `report.md` beside `rating.yaml`. It is the committed record of the rating's
reasoning, so a reader who has not seen the other files can follow it. It covers:

- the issue in one paragraph (the claim and what kind of issue it is);
- the approach taken: blinding and what the worker could see, prior work, what
  the worker investigated and produced, with file paths;
- what upstream did, with the evidence and the dates checked;
- the rating: outcome and each dimension, with the reason for each;
- what the worker got right, what it missed, and any claim that was refuted;
- confounds, and lessons for the protocol or tooling;
- cost where known (tokens, wall time).

In an interactive session with the Artifact tool, also publish the report as a
Claude artifact (a plain HTML page titled like "go-annotation 6596 shadow") and
record its URL as `report_url`. It is an optional mirror: workflow runs have no
artifact tool and leave `report_url` unset.

Run `just validate-shadow-issues <tracker>`; it fails if `report.md` is missing.
`ai-gene-review shadow-issues ratings` prints the table of all ratings.

## 5. Commit

Commit with a message like "Rate shadow work on go-annotation N", checked with
`python3 src/ai_gene_review/shadow_issues/guard.py --commit-msg FILE`.
