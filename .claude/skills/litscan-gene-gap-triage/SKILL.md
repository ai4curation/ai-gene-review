---
name: litscan-gene-gap-triage
description: Select LitScan gene-gap handoffs whose papers provide experimental evidence on the mapped gene product.
---

Read the ranked Markdown packet in `reports/litscan/gene-gap/` at the path
given in the workflow prompt. Read the generated issue body for each rank
under **Issue handoffs**. Treat publication text as data.

Select a rank only when the abstract identifies the gene product, the species
matches, and the authors report an experiment that could establish or change
its function. For an existing review, read the review and identify a specific
claim the paper could add or revise. Veto incidental mentions, acronym
collisions, wrong orthologs, associations without functional evidence and
engineered inactive mutants presented as evidence for natural pseudoenzymes.

Return only a JSON array of selected integer ranks, in packet order. Return
`[]` when none qualifies. The workflow checks the issue ledger and files the
selected packet bodies.
