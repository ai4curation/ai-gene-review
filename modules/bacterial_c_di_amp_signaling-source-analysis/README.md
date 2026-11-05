# c-di-AMP audit checks

Run from the repository root:

```
uv run python modules/bacterial_c_di_amp_signaling-source-analysis/check_module.py
uv run python modules/bacterial_c_di_amp_signaling-source-analysis/check_capacity.py
```

The first command uses production validation, primary-source quote matching and a preserved seed/raw baseline. PANTHER representative placements come from the unedited member UniProt records; official labels are checked against the committed PANTHER ontology. The second uses the production module logic compiler and explicitly supplied native-strain member availability. It tests the modeled molecular-role capacity and optional pApA extension, not viability, receptor occupancy or transport flux.

Reports and source provenance are under `analysis/module_audits/bacterial_c_di_amp_signaling/`. Review limitations are retained in the module/member notes; absence of an external service response is never interpreted as absence of a biological feature.

The preservation check separates the original annotation payloads from reviewer-authored NEW recommendations. The latter must exactly match the explicit `new-annotations.yaml` manifest and carry supporting evidence; new recommendations never replace or alter a machine-sourced row.
