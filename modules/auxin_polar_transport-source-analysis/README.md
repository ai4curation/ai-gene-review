# Polar auxin transport mechanism checks

Run from the repository root:

```
uv run python modules/auxin_polar_transport-source-analysis/check_module.py
```

This uses the real module validator, ontology resolution and gene/family conformance checks. The bounded PANTHER membership mapping is independently read from the 17 normally fetched UniProt records, so no large membership index is built. Exact official PANTHER labels remain validated normally.

The 22 route cases test the six native-context mechanisms, empty input, individual exporters/regulators, optional-only inputs, the rice sampled segment, combined bryophyte exporters and mixed-species pseudo-pairs. The checker deduplicates optional empty branches before counting six minimal two-activity mechanisms; raw enumeration also contains optional supersets. Neither availability of proteins nor a passing Boolean case establishes tissue coexpression, membrane polarity or complete native flux. The biological scope and source limits are in the adjacent module notes.

The checker writes its validation and route results under `.cache/module-audit-logs`. It does not modify curated module or gene files. PMID quote/title verification uses the production validator; an additional exact local-cache check covers the stable journal-URL quotation too; original paper caches are never edited.
