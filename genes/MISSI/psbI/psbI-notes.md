## Curation notes

- QuickGO export is header-only; therefore no UniProt DR/HAMAP-derived terms are listed as `existing_annotations` or proposed as `NEW`.
- Core function treats PsbI as a small PSII reaction-center subunit needed for complex stability or assembly.
- Addressed PR review by using GO:0042549 for PSII stabilization rather than assigning the more specific PSII electron-transport process directly to this small structural subunit.
