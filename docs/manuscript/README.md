---
title: "AUGR framework manuscript"
---

# AUGR manuscript

LaTeX source for the umbrella paper describing **AUGR** (Assessment via Unified
Gene-evidence Review) — the agentic, evidence-grounded framework underpinning the
`ai-gene-review` project.

This is the *framework* / *platform* paper. It is broader than, and complementary
to, the focused application paper in
[`projects/BIOREASON_COMPARISON/article/`](../../projects/BIOREASON_COMPARISON/article/),
which evaluates the BioReason-Pro predictor using one of AUGR's pipelines. The
BioReason paper is used here as a running example and source of background.

## Files

| File | Description |
|------|-------------|
| `manuscript.tex` | Canonical full manuscript source. |
| `references.bib` | Bibliography. |
| `justfile` | Build recipes. |

## Building

Requires a TeX distribution with `latexmk`, `xelatex`, and `bibtex`:

```bash
cd docs/manuscript
just pdf      # build manuscript.pdf
just wc       # word count
just clean    # remove build artifacts
```

The PDF is not committed (see `.gitignore`); `manuscript.tex` is the source of
truth.

## Scope and provenance of numbers

Corpus statistics in the Results section (review counts, organism count, action
distribution) are derived directly from the committed `genes/**/*-ai-review.yaml`
files and `rules/`, `publications/`, `reactome/` caches at the time of writing.
They should be recomputed from the repository before submission rather than taken
as fixed. The author list is a placeholder pending finalization.
