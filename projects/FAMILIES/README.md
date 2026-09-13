---
title: "Family catalog — rendering and sources"
autolink_gene_symbols: false
---

Supporting documentation for the [family catalog](../FAMILIES.md).

The catalog reads authored `*-review.yaml` and `*-review.md` files under
`interpro/<database>/<entry>/`. It merges structured and prose reviews for the
same entry. Metadata and research reports alone do not create catalog rows.
PANTHER functional coherence and Pfam-associated InterPro mapping viability are
separate assessments and are displayed separately.

## Rendering

The source page selects the catalog through `template: family_index` in its YAML
frontmatter. The filename is arbitrary; sources must be under `projects/`, or the
renderer must receive an explicit `projects_dir`. Unknown template names fail with
an error.

```bash
uv run ai-gene-review render-projects projects/FAMILIES.md -o pages/projects
```

## PR previews

Published source links default to the repository's `main` branch. To preview files
that exist only on a PR branch, pass `--source-ref` while rendering to a
separate output directory:

```bash
uv run ai-gene-review render-projects projects/FAMILIES.md --source-ref cmungall/gr-pages -o /tmp/family-preview
```

The revision can be a branch or commit. It affects GitHub source links; links to
other rendered site pages still require the corresponding site tree. Keep the
default `main` links in committed production pages.

The CLI also accepts `AI_GENE_REVIEW_SOURCE_REF` as a fallback; an explicit
`--source-ref` takes precedence. Python render functions accept `source_ref`
directly and do not read the environment. The selected revision applies to
catalog links, related source links, and the footer.
