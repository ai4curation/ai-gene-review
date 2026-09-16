# AI Gene Review History Records

This directory stores append-only curation session history outside the curated
content files. The mechanism is ported from
[dismech](https://github.com/monarch-initiative/dismech). New files should
follow:

```text
history/genes/<ORGANISM>/<GENE>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/modules/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/gocams/<MODEL>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/projects/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/schema/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
history/other/<SLUG>/<TIMESTAMP>-<actor>-<shortid>.yaml
```

Do not hand-write the filename or session id — scaffold a schema-valid record
with `just new-history` (run `just new-history --help` for options):

```bash
just new-history --kind gene --organism human --slug CFAP300 \
  --event CREATE --outcome changed \
  --summary "Create review: CFAP300" --agent-tool claude-code --details "..."
```

See `docs/history.md` and `src/ai_gene_review/schema/history.yaml` for the
record format. Validate records with `just validate-history <path>` or
`just validate-history-all`. PRs that change curated content (gene reviews,
modules, GO-CAM reviews, projects) should add a matching record.

Records for pre-existing work can be backfilled from PR metadata with
`just backfill-history` (see `scripts/backfill_history_from_prs.py`);
backfilled records say so in their `details`.
