# History Records

AI Gene Review history records are append-only YAML files for curation,
review, and audit sessions. They keep provenance *outside* the curated
objects themselves (gene review YAML, module YAML, GO-CAM reviews, project
pages), so the curated files stay clean while every session that touched them
remains discoverable. The mechanism — schema, layout, scaffolder, and
validation — is ported from
[dismech](https://github.com/monarch-initiative/dismech) (`docs/history.md`
and `src/dismech/schema/history.yaml` there).

Store history files under `history/`, mirroring the curated layout:

```text
history/genes/<ORGANISM>/<GENE>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/modules/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/gocams/<MODEL>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/projects/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/schema/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/other/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
```

Use UTC timestamps in filenames, for example
`2026-08-28T174412Z-claude-code-a3f9c2.yaml`. The short suffix prevents
same-second collisions when multiple sessions touch the same target.

## Creating a record

Do not hand-write the path, timestamp, or session id. Scaffold a schema-valid
skeleton with the helper, then edit the emitted `details`:

```bash
just new-history --kind gene --organism human --slug CFAP300 \
  --event CREATE --outcome changed \
  --summary "Create review: CFAP300" \
  --agent-tool claude-code --model <model-id> \
  --sections existing_annotations,core_functions \
  --pr 2500 --issue 2400 \
  --details "One-paragraph summary of what was curated and how it was validated."
```

`--kind` is `gene`, `module`, `gocam`, `project`, `schema`, or `other`
(`schema`/`other` require an explicit `--path`; `gene` requires `--organism`).
`--event` is one of `CREATE`/`EDIT`/`REVIEW`/`AUDIT`/`GENERAL`; `--outcome` is
`changed`/`no_change`/`needs_followup`/`blocked`. `--issue`/`--pr`/`--url`
accept bare numbers (expanded to repo URLs) or full URLs and repeat. Run
`just new-history --help` for the full option list. The command prints the
path it created; validate it with `just validate-history <path>` and
`git add history/`.

Target paths are derived per kind:

| kind | target path | history directory |
|------|-------------|-------------------|
| `gene` | `genes/<org>/<GENE>/<GENE>-ai-review.yaml` | `history/genes/<org>/<GENE>/` |
| `module` | `modules/<SLUG>.yaml` | `history/modules/<SLUG>/` |
| `gocam` | `gocams/<MODEL>/<MODEL>-review.yaml` | `history/gocams/<MODEL>/` |
| `project` | `projects/<SLUG>.md` | `history/projects/<SLUG>/` |
| `schema`/`other` | explicit `--path` | `history/schema/<SLUG>/`, `history/other/<SLUG>/` |

A gene target points at the `-ai-review.yaml` as the primary artifact, but a
session on any file in the gene folder (notes, pathway, bioinformatics)
belongs to the same gene target — name the touched parts in the event's
`sections`.

Any PR that creates or edits curated content should include a matching
record.

## Format

Each file records one session for one target. The session may include
multiple events, and `actors` is always a list so human and AI participants
can be recorded together.

```yaml
history_version: 1

target:
  kind: gene
  slug: CFAP300
  organism: human
  path: genes/human/CFAP300/CFAP300-ai-review.yaml

session:
  id: 2026-08-28T174412Z-claude-code-a3f9c2
  timestamp: "2026-08-28T17:44:12Z"
  actors:
    - type: ai_agent
      name: claude-code
      agent_tool: claude-code
    - type: human
      name: cjm

links:
  issues:
    - https://github.com/ai4curation/ai-gene-review/issues/2400
  prs:
    - https://github.com/ai4curation/ai-gene-review/pull/2500
  urls: []

events:
  - type: REVIEW
    outcome: no_change
    sections:
      - existing_annotations
      - core_functions
    summary: Reviewed annotation actions and found no immediate edits needed.
    details: |
      Rich free-text notes go here.

      This can include reviewer reasoning, caveats, what was checked, why no
      edit was made, future follow-up suggestions, or links in prose.
```

## Renamed or retargeted targets

History records are **append-only**: once written, a record's `target.slug`
and `target.path` describe the object as it stood during that session and are
not rewritten later. When an entry is renamed, retargeted, or merged, the
earlier records keep pointing at the pre-rename path, which no longer exists
on disk. Record the move with `target.superseded_by` instead of editing the
original fields:

```yaml
target:
  kind: module
  slug: old_module_name
  path: modules/old_module_name.yaml
  superseded_by:
    slug: new_module_name
    path: modules/new_module_name.yaml
    reason: >-
      Curation showed the old boundary duplicated new_module_name, so the
      module was merged in a later session in the same PR.
```

`slug`, `path`, and `reason` are all required inside the block — the block
turns a hard layout failure into a pass, so the justification has to be
visible in review. The record files themselves move into the successor's
directory so all sessions for one entry stay together.

**`superseded_by` may be updated in place; `target.slug`/`target.path` may
not.** `target.slug`/`target.path` record what the session did and are
frozen. `superseded_by` records *where the entry lives now*, so if the
successor is itself renamed later, repoint the existing `superseded_by` at
the new entry (and move the record files again) rather than chaining a second
block.

`tests/test_history_schema.py::test_committed_history_records_follow_layout`
enforces this: a record whose `target.path` is missing passes **only** if
`target.superseded_by.path` resolves to an existing file, so an ordinary bad
slug still fails loudly. `just new-history` also warns at authoring time when
the target path does not exist yet.

## Event Types

Use the smallest useful vocabulary:

- `GENERAL`: general, legacy, or backfilled activity that is not more
  specifically classified.
- `CREATE`: initial creation of a target.
- `EDIT`: content or metadata edit.
- `REVIEW`: review that may or may not produce edits.
- `AUDIT`: structured inspection, compliance check, or triage.

Use one of these outcomes:

- `changed`
- `no_change`
- `needs_followup`
- `blocked`

Keep `summary` short enough for listings and dashboards. Put curator
reasoning, review notes, caveats, and follow-up detail in the required
`details` field.

## Retrospective backfill from PRs

The repository predates this mechanism, so most curation sessions exist only
as merged or open PRs. `scripts/backfill_history_from_prs.py` winds that
history back into `history/`:

```bash
just backfill-history --state open --dry-run   # see what would be written
just backfill-history --state open             # backfill all open PRs
just backfill-history --pr 2613 --pr 2667      # backfill specific PRs
```

For each curated target a PR touches, it writes one record seeded from PR
metadata (title, body, author, branch, changed files), timestamped at the
PR's merge/creation time so records sort into real chronology. Backfilled
records are marked as such in `details` — they are reconstructions, not
contemporaneous session notes — and the deterministic filename shortid makes
re-runs idempotent. The script requires an authenticated `gh` CLI.

## Validation

Validate one history record:

```bash
just validate-history history/genes/human/CFAP300/2026-08-28T174412Z-claude-code-a3f9c2.yaml
```

Validate all committed history records:

```bash
just validate-history-all
```

The schema lives at `src/ai_gene_review/schema/history.yaml`.
