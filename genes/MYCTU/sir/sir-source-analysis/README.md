# Sir reaction localization in Reactome

Source: [Reactome R-MTU-936703](https://reactome.org/content/detail/R-MTU-936703).
Reproduce: `uv run python genes/MYCTU/sir/sir-source-analysis/fetch_reactome_location.py`.
The adjacent JSON is the unmodified ContentService response, retrieved on
2026-10-26. The repository's ordinary Reactome summary cache omits these fields.

The reaction compartment displayName is:

> cytosol

Its catalystActivity displayName is:

> sulfite reductase (ferredoxin) activity of Sir holoenzyme [cytosol]

This is a curated pathway location, not a direct localization experiment.
It supports retention of the TAS cytosol annotation without treating a soluble
crystal structure as evidence of cellular localization.
