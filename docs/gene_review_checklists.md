# Gene review checklists (pilot)

A gene review PR can carry a filled checklist for each gene review it changes. Checklists are
checked with [linkml-checklist-validator](https://github.com/ai4curation/linkml-checklist-validator)
(`lcv`) against the schema `rubrics/gene_review.yaml`. Each checklist sits next to that PR's
history record and has the same session id:
`history/genes/<org>/<GENE>/<session-id>.checklist.yaml`. Create it with
`lcv skeleton rubrics/gene_review.yaml genes/<org>/<GENE>/<GENE>-ai-review.yaml -o <path>`, fill
it in, and run `lcv check rubrics/gene_review.yaml <checklist> <review>`, which must pass before
the PR is opened. The checklist asks for evidence on each judged annotation decision, on the
references examined, on the curated UniProt and GOA lines, on validation and on the history
record's model. The
`.claude/skills/fill-gene-review-checklist` skill describes how to fill it, and
`rubrics/examples/` holds a filled example. This is a warn-only pilot. No CI job runs `lcv` until
LCV is public, and a PR without a checklist is not rejected.
