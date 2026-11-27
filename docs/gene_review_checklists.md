# Gene review checklists (pilot)

A gene review PR can carry a filled checklist for each gene review it changes. Checklists are
checked with [linkml-checklist-validator](https://github.com/ai4curation/linkml-checklist-validator)
(`lcv`) against the schema `rubrics/gene_review.yaml`. Each checklist is named by the session id
of that PR's history record, mirroring the history layout but outside `history/` (whose YAML files
are all validated as history records):
`rubrics/checklists/genes/<org>/<GENE>/<session-id>.checklist.yaml`. Create it with
`lcv skeleton rubrics/gene_review.yaml genes/<org>/<GENE>/<GENE>-ai-review.yaml -o <path>`, fill
it in, and run `lcv check rubrics/gene_review.yaml <checklist> <review>`, which must pass before
the PR is opened. Annotation keys include WITH/FROM, so a `just fetch-gene` refresh can turn a
filled entry into `missing:` plus `unexpected:`; regenerate after any refetch. `lcv check` does not
verify that evidence excerpts are verbatim, and neither does `just validate-quotes` (it reads
`supporting_text`, not `excerpt`), so copy them exactly. The checklist asks for evidence on each judged annotation decision, on the
references examined, on the curated UniProt and GOA lines, on validation and on the history
record's model. The
`.claude/skills/fill-gene-review-checklist` skill describes how to fill it, and
`rubrics/examples/` holds a filled example. This is a warn-only pilot. No CI job runs `lcv` until
LCV is public, and a PR without a checklist is not rejected.
