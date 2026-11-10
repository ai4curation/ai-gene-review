---
title: GO Annotation Tracker Shadowing
maturity: IN_PROGRESS
tags: [EVALUATION]
autolink_gene_symbols: false
manifest:
  artifacts:
    - href: https://claude.ai/artifact/LiT1Binow1FbQQqoQFCG5p
      title: go-annotation 6596 report
      description: AI generated
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
   replacement) and `work_products` in `issue.yaml`, and the worker's
   confidence in `self-rating.yaml`. Read the thread with
   `just show-shadow-issue N --as-of <time>` (or `--opening-only` for BLIND)
   and record that time as `thread_snapshot_at`. Before changing anything,
   record any existing review of an affected gene, family, rule or term as
   `prior_work` with `relation: COVERS_SUBJECT`.
4. **Rating.** Once upstream closes the issue, a different agent or person
   fills `resolution` and writes `rating.yaml`. The rater must not open
   `self-rating.yaml` before scoring. Many threads end in "fixed, thanks", so
   the rater should check the released artifacts (GOA, interpro2go, ARBA and
   PAINT releases, linked ontology PRs) rather than rely on the thread alone,
   and date each check (`checked_at`). If upstream has acted but the change is
   not yet released, score `downstream: PENDING_RELEASE` and re-rate after the
   next release.
5. **Report.** At the end, the rater publishes a Claude artifact describing the
   approach taken and how well it did, and records its URL as
   `rating.yaml` `report_url`. The procedure for steps 4 and 5 is the
   `shadow-issue-rater` skill (`.claude/skills/shadow-issue-rater/`).

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
  worktree preflight. The rater's report is linked in this page's manifest
  and in `rating.yaml` `report_url`; publishing that report is now step 5 of
  the protocol.

## Next steps

- Let the worker triage the backfill, starting with the 75 issues that have
  `prior_work` (confirmation batch) and the 272 open issues.
- Write the rater prompt (a separate agent, not the worker) and a summary
  report over `rating.yaml` files.
