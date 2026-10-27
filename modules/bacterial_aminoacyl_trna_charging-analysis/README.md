# Reproducible module checks

Run from the repository root:

```
uv run python modules/bacterial_aminoacyl_trna_charging-analysis/check_module.py
uv run python modules/bacterial_aminoacyl_trna_charging-analysis/check_routes.py
```

`members.json` lists the exact 42 reviewed products and their source strain identifiers. The module checker independently reads each unedited UniProt record, validates accession/taxon and PANTHER membership, then calls the production module validator. `family-membership-evidence.json` preserves the cross-reference snapshot; official family names are validated by the normal ontology-backed validator. It is not a new inferred family classification.

`go-term-snapshot.json` is an unedited normal QuickGO JSON response from the 2026-10-26 audit. It records the live author-supplied molecular functions and process terms. Raw source provenance for the archived bacterial cysteine proteins is in `genes/9BACT/A0A0S7X285/A0A0S7X285-source-analysis/`.

The route checker calls the production Boolean compiler with an explicit organism and assembly-aware predicate. Species identity and complex subunit completeness are predicate responsibilities, not automatic properties of the compiler. Its partial-route tests establish modeled chemical capability, not measured native flux. `route-results.json` records the exact input inventories and expected/observed outcomes. `validation-results.json` records production validation results and honest family-review coverage advisories.
