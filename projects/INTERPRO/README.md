---
title: "InterPro mapping review — supporting material"
---

# InterPro mapping review — supporting material

Supporting material for the [InterPro Mapping Review project](../INTERPRO.md).

## Contents

- `extract_suspect_interpro_mappings.py` — reproducible extractor. Walks every
  `genes/*/*/*-ai-review.yaml`, finds the annotations sourced from InterPro2GO
  (`original_reference_id: GO_REF:0000002`), recovers the source InterPro entry id(s)
  from the matching `*-goa.tsv` (the `WITH/FROM` column), joins in the reviewer's
  action, and writes the two TSVs below.
- `suspect_interpro_mappings.tsv` — one row per reviewed InterPro2GO annotation
  (gene, InterPro id(s), GO term, action, suspect flag, proposed replacement, reason).
- `interpro_family_priorities.tsv` — one row per InterPro entry, aggregating how often
  it produced an accepted vs a suspect mapping across all reviewed genes. This is the
  ranked worklist for family-level deep research (entries that repeatedly produce
  suspect mappings first).
## Family deep research (generated process)

Family deep research is generated, not hand-written. It is wired the same way as gene
deep research:

- `templates/interpro_family_research.md` — the deep-research prompt template.
- `scripts/deep_research_interpro_family.py` — wrapper that loads the cached InterPro
  metadata as context and runs `deep-research-client`.
- `just deep-research-interpro-family <IPR> [provider]` — the recipe (in
  `project.justfile`); provider defaults to `falcon` (Edison). Output:
  `interpro/<db>/<ID>/<ID>-deep-research-<provider>.md`.

```bash
just deep-research-interpro-family IPR000719          # falcon (Edison) by default
```

## Regenerate

```bash
uv run python projects/INTERPRO/extract_suspect_interpro_mappings.py
```

An annotation is counted "suspect" when its review `action` is anything other than
`ACCEPT` (MODIFY, REMOVE, MARK_AS_OVER_ANNOTATED, KEEP_AS_NON_CORE, UNDECIDED). The TSVs
are regenerated from the current state of the reviews, so re-run after new reviews land.
