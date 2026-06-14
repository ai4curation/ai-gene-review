---
title: "Projects"
---

# Projects

Each project is a curation/analysis effort tracked in this directory.

## Folder structure

A project is a top-level markdown file `FOO.md`, optionally accompanied by a
same-named folder `FOO/` that holds its supporting material:

```
projects/
  FOO.md            # the project page (overview, status, findings)
  FOO/              # supporting material for FOO (optional)
    FOO-pathway.md  # sub-pages: pathway summaries, recommendations, sub-analyses
    notes.md        # working notes
    data/           # data files
    *.py            # analysis scripts
    ...
```

Guidelines:

- The **project page** is always the top-level `FOO.md`. Keep the high-level
  overview, status, and conclusions here.
- Put **supporting material** — pathway summaries, curation-recommendation docs,
  per-organism or per-topic sub-analyses, data files, scripts, reports — inside
  `FOO/`. Do **not** leave them as loose `FOO-*.md` siblings at the top level.
- Link between a project page and its sub-pages with ordinary relative links:
  `[pathway](FOO/FOO-pathway.md)` from `FOO.md`, and
  `[parent project](../FOO.md)` from a file inside `FOO/`.
- Every authored project markdown file must start with a YAML frontmatter block
  defining at least a `title:` (enforced by `tests/test_project_frontmatter.py`).
  Auto-generated `*-deep-research-*.md` and `*.citations.md` artifacts are exempt.

### Known exceptions

A few folders predate this convention and do not yet have a matching top-level
`FOO.md` (their content lives entirely inside the folder): `PANTHER_IBA_REVIEW/`,
`QUANTUM_SENSING/`, `TRANSCRIPTION_FACTORS/`, and `paint/`. These are migration
targets — when touched, promote a top-level `FOO.md` overview page for them.

## Rendering

`just render-projects` (or `ai-gene-review render-projects ...`) renders the
whole `projects/` tree recursively to `pages/projects/`, **mirroring the
subfolder structure**: `projects/FOO/bar.md` → `pages/projects/FOO/bar.html`.
Relative `.md` links are rewritten to `.html` with their path preserved, so the
links above resolve in both the source tree and the rendered site.

The project **index** (`pages/projects/index.html`) is **manually maintained** —
add a `<div class="project-card">` entry when you add a project. `render-projects`
does not update the index.
