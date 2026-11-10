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
| `<N>/rating.yaml` | curated | `ShadowRating` from an independent rater (optional) |

The sync creates `issue.yaml` once, as a stub, and never rewrites curated files.
The schema is `src/ai_gene_review/schema/shadow_issue.yaml`.

## Workflow

1. **Sync.** The `shadow-issues-sync` workflow runs daily and opens or refreshes
   one PR with new stubs and thread updates. Locally: `just sync-shadow-issues`.
   It only sends GET requests.
2. **Triage.** For each `untriaged` issue, decide whether it is annotation work
   and set `triage.kind`, `in_scope` and `rationale`. The sync's
   `suggested_kind` (from labels) is only a hint.
3. **Shadow work.** For each issue in `needs_shadow`, do the work here as
   for any other task: gene reviews, family reviews, curated rules, proposed
   terms. Record `shadow.diagnosis`, `proposed_actions` (subject, term,
   replacement) and `work_products`, plus a self-rating. Read the thread with
   `just show-shadow-issue N --as-of <time>` (or `--opening-only` for BLIND)
   and record that time as `thread_snapshot_at`.
4. **Rating.** Once upstream closes the issue, a different agent or person
   fills `resolution` and writes `rating.yaml`. The rater should not read the
   worker's self-rating first. Many threads end in "fixed, thanks", so the
   rater should check the released artifacts (GOA, interpro2go, ARBA and PAINT
   releases, linked ontology PRs) rather than rely on the thread alone.

`just outstanding-shadow-issues` lists the three queues (`untriaged`,
`needs_shadow`, `needs_rating`), prospective issues and newest issues first.

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
training, and 75 issues in the window already have earlier work in this repo.
That earlier work is recorded as `prior_work` on each issue. These 75 are the
natural first confirmation batch.

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

## Next steps

- Let the worker triage the backfill, starting with the 75 issues that have
  `prior_work` (confirmation batch) and the 272 open issues.
- Write the rater prompt (a separate agent, not the worker) and a summary
  report over `rating.yaml` files.
