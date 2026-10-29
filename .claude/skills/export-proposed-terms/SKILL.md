---
name: export-proposed-terms
description: Export top-level ai-gene-review `proposed_new_terms` entries to a deterministic TSV table.
---

# Export Proposed Terms

Use this skill when the user asks for a TSV or tabular extract of ontology term
requests recorded in gene review YAML files.

Run the helper from the repository root:

```bash
uv run python src/ai_gene_review/tools/export_proposed_terms.py -o reports/proposed_new_terms.tsv
```

Pass files or directories after the options to restrict the export. With no
inputs, the helper scans `genes/**/*-ai-review.yaml`.

The TSV defaults to `reports/proposed_new_terms.tsv`. It has one row per
top-level `proposed_new_terms` entry and skips reviews where
`proposed_new_terms` is empty. It includes:

- source review fields: `source_path`, `organism`, `gene_directory`,
  `review_id`, `gene_symbol`, `taxon_id`, `taxon_label`
- proposal fields: `term_index`, `proposed_name`, `proposed_definition`,
  `justification`, `proposed_parent_id`, `proposed_parent_label`
- structured evidence fields serialized as JSON: `proposed_mappings`,
  `supported_by`

The exporter intentionally ignores `knowledge_gaps[].proposed_terms`; those are
nested gap-specific proposals, not the review's top-level ontology request list.
If the user explicitly asks for gap proposals too, write a separate ad hoc
extract with a column that distinguishes top-level terms from gap terms.

For custom column order, filtering, or aggregation, treat the generated TSV as a
staging table and post-process it with Python's `csv` module or pandas. Preserve
TSV safety by keeping embedded tabs and newlines out of scalar cells.

Treat the TSV as a read-only reporting view, not a round-trip editing source.
Scalar columns are whitespace-normalized for tabular readability; nested
`proposed_mappings` and `supported_by` values are compact JSON for inspection.
When updating a review, copy exact `supporting_text` from the source YAML or
publication cache, not from a TSV extract.
