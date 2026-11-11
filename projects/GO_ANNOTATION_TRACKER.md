---
title: GO Annotation Tracker Shadowing
maturity: IN_PROGRESS
tags: [EVALUATION]
autolink_gene_symbols: false
---

# GO Annotation Tracker Shadowing

**Bottom line:** GO curators raise and resolve about 500 annotation issues a
year on the go-annotation tracker. Each one is a small, real curation problem
with a curator-made answer. We mirror the tracker into `issues/go-annotation/`,
do our own work on the issues that are annotation work, and have a separate
rater compare our answer with the curators'. Prospective issues are the real
evaluation: our work is committed before the curators resolve them. The
retrospective backfill (issues created since 2024-11-10) is mostly a
confirmation study, and that is fine.

We never notify the curators. See [No upstream notifications](#no-upstream-notifications).

## Layout

`issues/<tracker>/` holds one folder per upstream issue. The layout allows other
trackers to be shadowed later.

| File | Owner | Content |
|---|---|---|
| `tracker.yaml` | curated | upstream repo, `backfill_since`, `prospective_since`, label → kind hints |
| `sync-state.yaml` | sync | cursor (newest upstream `updated_at` stored) |
| `<N>/source.yaml` | sync | current upstream state: title, state, labels, linked repos |
| `<N>/thread.jsonl` | sync | append-only opening post, comments and events; an edit adds a new version |
| `<N>/issue.yaml` | curated | `ShadowIssue`: study, triage, shadow work, upstream resolution, prior work |
| `<N>/shadow.md` | curated | the worker's free-text log (optional) |
| `<N>/self-rating.yaml` | curated | `SelfRating`: the worker's confidence, kept apart so the rater can read the record without it |
| `<N>/rating.yaml` | curated | `ShadowRating` from an independent rater (optional) |
| `<N>/report.md` | curated | the rater's write-up of the approach and how well it did; required beside `rating.yaml` |
| `<N>/rating-<label>.yaml`, `report-<label>.md` | curated | further ratings of the same work, for comparing raters; `rating.yaml` is the primary (most independent) one |

The sync creates `issue.yaml` once, as a stub, and never rewrites curated files.
The schema is `src/ai_gene_review/schema/shadow_issue.yaml`.

## Workflow

1. **Sync.** The `shadow-issues-sync` workflow runs daily and opens or refreshes
   one PR with new stubs and thread updates. Locally: `just sync-shadow-issues`.
   It only sends GET requests.
2. **Triage.** For each `untriaged` issue, decide whether it is annotation work
   and set `triage.kind`, `in_scope` and `rationale`, reading only the
   opening post. For prospective issues the sync adds a `suggested_kind` from
   the labels, as a hint. Retrospective stubs get none, and
   `show --opening-only` prints no labels: a backfilled issue's labels were set
   while it was resolved and can give the disposition away.
3. **Shadow work.** For each issue in `needs_shadow`, do the work here as
   for any other task: gene reviews, family reviews, curated rules, proposed
   terms. Record `shadow.diagnosis` with quote-checked `supported_by`,
   `proposed_actions` (subject, term, replacement; `FLAG_FOR_CHECK` for a
   suspicion not established), `work_products`, `worker_run` and
   `saw_prior_work` in `issue.yaml`, and the worker's confidence in
   `self-rating.yaml`. Unfinished work is `IN_PROGRESS` and sits in the
   `in_progress` queue until a later run resumes it. Read the thread with
   `just show-shadow-issue N --as-of <time>` (or `--opening-only` for BLIND)
   and record that time as `thread_snapshot_at`. Before changing anything,
   record any existing review of an affected gene, family, rule or term as
   `prior_work` with `relation: COVERS_SUBJECT`.
4. **Rating.** Once upstream closes the issue, a different agent or person
   fills `resolution` and writes `rating.yaml`. The `shadow-issues-rater`
   workflow does this daily on a different model (`claude-sonnet-5`) from the
   worker (`claude-opus-5`). Each rating records `rater_model`, `rater_run` and
   `independence`. `self_rating_seen` records whether the rater saw
   `self-rating.yaml`, and when (it should be `NEVER`). Many threads end in "fixed, thanks", so
   the rater should check the released artifacts (GOA, interpro2go, ARBA and
   PAINT releases, linked ontology PRs) rather than rely on the thread alone,
   and date each check (`checked_at`). If upstream has acted but the change is
   not yet released, score `downstream: PENDING_RELEASE` and re-rate after the
   next release.
5. **Report.** At the end, the rater writes `report.md` beside `rating.yaml`,
   describing the approach taken and how well it did. It is the committed,
   diffable record, and validation fails without it. In an interactive
   session the rater may also publish it as a Claude artifact and record the
   link as `report_url`, an optional mirror. The procedure for steps 4 and 5
   is the `shadow-issue-rater` skill (`.claude/skills/shadow-issue-rater/`).

`just outstanding-shadow-issues` lists the four queues (`untriaged`,
`in_progress`, `needs_shadow`, `needs_rating`), prospective issues and newest
issues first. `just shadow-ratings` prints the table of all ratings, generated
from the `rating.yaml` files.

Throughput is one shadowed issue a day and one rating a day. Only issues that
have been shadowed can be rated, so the 837 closed backfilled issues are rated
as the worker reaches them, not all at once.

### Kinds of issue

| `IssueKindEnum` | Typical issue | Our work product |
|---|---|---|
| `PAINT_IBA` | an IBA from a PANTHER node is wrong for some members | family review, IBA rows in gene reviews |
| `TERM_WIDE_REVIEW` | review all annotations to a term before obsoletion | per-gene dispositions (as in [MEVALONATE_PATHWAY_OBSOLETION](MEVALONATE_PATHWAY_OBSOLETION.md)) |
| `MAPPING_RULE` | an InterPro2GO, ARBA, keyword or UniRule mapping misfires | `rules/curated` rule, rule review |
| `GENE_ANNOTATION` | specific annotations on a few gene products | gene review |
| `NEW_ANNOTATION_REQUEST` | annotate a complex or CC term | NEW rows |
| `OUT_OF_SCOPE` | pipeline, technical, guideline or process issue | triage only |

For term-wide reviews, the unit of comparison is the per-gene disposition,
with the issue as parent.

### Study and blinding

`study` is fixed at stub creation: `PROSPECTIVE` if the issue was created on or
after `prospective_since` (2026-11-10), otherwise `RETROSPECTIVE`.
`shadow.blinding` records what the worker saw: `BLIND` (opening post only),
`PARTIAL` (the thread up to `thread_snapshot_at`) or `UNBLINDED`. For
prospective work, git commit times show that our work came before the upstream
resolution.

Retrospective issues are often only partly blind: the repo's GOA files and the
ontology already reflect the fix, the model may have seen the thread in
training, and the repo may already hold work on the issue. `prior_work` records
two kinds: `NAMES_ISSUE`, a commit message names the issue (75 issues in the
backfill, found from git history; the natural first confirmation batch), and
`COVERS_SUBJECT`, an existing review of an affected gene or family made for
another reason. Only the first unblinds the thread, but both make the shadow
work less independent, and the rater should say so.

Agent worktrees can start from an older commit than the coordinator's branch.
A worker whose checkout has no `issues/go-annotation/tracker.yaml` must stop
rather than work without the mirror.

## No upstream notifications

GitHub turns an issue URL, the `org/repo#N` shorthand and an at-mention, written
in a commit message, PR title or body, issue or comment, into a cross-reference
or notification on the curators' side. Before this project, PRs made from the
go-annotation scanner prompts did exactly that (for example on go-annotation
6591, 6632 and 6414). The rules:

- Name an upstream issue as `issues/go-annotation/N` or "go-annotation N",
  never as a URL or `geneontology/<repo>#N` (any geneontology repo).
- Never at-mention anyone except cmungall.
- Text inside committed files creates no cross-reference, so mirrored threads
  keep their URLs and handles. Never paste mirrored text into a PR body.

Enforcement, all built on `src/ai_gene_review/shadow_issues/guard.py`:

- a Claude Code `PreToolUse` Bash hook (`.claude/hooks/upstream_notification_hook.py`)
  blocks `git commit`, `gh pr|issue ...` and `gh api -f/-F` commands whose text
  or body file contains a hazard;
- a `commit-msg` pre-commit hook (`pre-commit install --hook-type commit-msg`);
- the `upstream-notification-guard` workflow checks PR titles, bodies and commit
  messages. It cannot undo a cross-reference GitHub has already made, but it
  stops the squash commit from repeating it on main;
- `just check-upstream-refs FILE` checks a body before you use it.

## Status

- 2026-11-10: tracker, schema, sync, guard and queues built. Backfilled 1,109
  issues (go-annotation 5516–6649, created 2024-11-10 onward): 837 closed, 272
  open, all `RETROSPECTIVE` and `UNTRIAGED`. Label hints: 397 PAINT_IBA, 311
  TERM_WIDE_REVIEW, 248 MAPPING_RULE, 27 GENE_ANNOTATION, 9
  NEW_ANNOTATION_REQUEST, 5 OUT_OF_SCOPE, 112 unlabeled.

- 2026-11-10: the `go-annotation-scanner` workflow, which read the upstream
  tracker directly and cross-referenced curators' issues from its PRs, is
  replaced by `shadow-issues-worker`. The worker reads only the mirror. Each
  run triages a batch, or shadows one issue under the blinding protocol above,
  and opens one PR. Priority: prospective untriaged, prospective needs_shadow,
  retrospective needs_shadow, then retrospective untriaged (25 per run, issues
  with `prior_work` and open issues first). It runs daily in the `medium` and
  `fast` cron profiles and weekly in `slow`.
- 2026-11-10: first experiment, go-annotation 6596 (a PAINT IBA of GDP-forming
  succinate-CoA ligase on yeast LSC1). A blind worker agreed with the curator
  and traced the error to the term's placement at the root of the
  alpha-subunit family PTHR11117, although the beta subunit sets nucleotide
  specificity; it proposed a NOT at the Fungi node and found that the
  issue's *S. pombe* precedent named the beta, not the alpha, subunit. An
  independent rater scored it CONCORDANT (actions PARTIAL, downstream
  PENDING_RELEASE, added value SOME, harm NONE). Confound: the LSC1 review
  already removed the row (COVERS_SUBJECT prior work). The run led to five
  protocol fixes: `self-rating.yaml` split out of `issue.yaml`,
  `PENDING_RELEASE`, `checked_at`, `COVERS_SUBJECT` prior work, and the
  worktree preflight. The rater's report is
  `issues/go-annotation/6596/report.md`; writing that report is now step 5 of
  the protocol.
- 2026-11-11: changes after PR review. Rating integrity: `self_rating_seen`
  (NEVER, BEFORE_SCORING, AFTER_SCORING) replaces a boolean that could
  contradict the summary; `rater_model`, `rater_run` and `independence`
  make separation from the worker a recorded fact; a rater workflow on a
  different model runs the `needs_rating` queue; and `report.md` is
  committed. 6596 is recorded honestly as `SAME_MODEL_SEPARATE_RUN`,
  self-rating seen `AFTER_SCORING`. Blinding: no label hints or labels for
  retrospective issues. Evidence: `supported_by` quotes in `issue.yaml` are
  now checked by `just validate-quotes`. Robustness: an `in_progress` queue,
  a sync that skips incomplete timeline items, a one-hour cursor overlap, CI
  validation of `issues/**`, and the notification hook extended to GitHub
  MCP tools and every `gh api` field form. The PTHR11117 verdict is now
  enforced (a GO:0004776 term assessment with LSC1 and SPAC16E8.17c as
  member exceptions), and the SPAC16E8.17c row is REMOVE. NAMES_ISSUE prior
  work is derived by `shadow-issues backfill-prior-work`, which drops bulk
  commits naming many issues.

- 2026-11-11: go-annotation 6596 re-rated on a different model
  (`claude-sonnet-5`, `DIFFERENT_MODEL`). The first rater's files and
  resolution were set aside before the run, and the new rater saw neither
  them nor the self-rating (`self_rating_seen: NEVER`). The Sonnet rating is
  now the primary `rating.yaml`; the first is kept as
  `rating-same-model.yaml`. The raters agree on triage, diagnosis, actions and
  harm, and disagree on three dimensions:

  | Dimension | Same model (Opus) | Different model (Sonnet) |
  |---|---|---|
  | Outcome | CONCORDANT | PARTIAL |
  | Downstream | PENDING_RELEASE | PARTIAL |
  | Added value | SOME | SUBSTANTIAL |

  Both raters found the same facts: the curator's fix was a primary NOT on
  P53598, nothing is released yet, and the *S. pombe* alpha subunit O13750
  still carries the IBA. They weigh them differently. Sonnet reads the
  worker's family-wide proposal (a Fungi-node NOT reaching about 18 other
  fungal recipients) as more than the curator did, which lowers agreement and
  raises added value. Opus counted only what the thread establishes. Two
  points in the Sonnet rating overreach. It treats the absence of a Fungi-node
  NOT as established, though the thread does not say either way. And it scores
  `downstream: PARTIAL` although nothing upstream has reached released data,
  which the definitions call `PENDING_RELEASE`. A single issue cannot settle
  which rater is better calibrated, but it shows the rating depends on the
  rater. That argues for rating a sample of issues twice and reporting
  agreement, not one score.

## Next steps

- Let the worker triage the backfill, starting with the 75 issues that have
  `prior_work` (confirmation batch) and the 272 open issues.
- Re-rate PENDING_RELEASE issues after each PANTHER/GO release.
- Rate a sample of shadowed issues with two raters on different models, and
  report inter-rater agreement per dimension.
- Tighten the rater skill: an absence the thread does not state is unknown,
  and `downstream` is `PENDING_RELEASE` whenever nothing upstream is released.
