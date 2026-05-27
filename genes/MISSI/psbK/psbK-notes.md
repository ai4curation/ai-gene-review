## Curation notes

- QuickGO export is header-only; therefore no UniProt DR/HAMAP-derived terms are listed as `existing_annotations` or proposed as `NEW`.
- UniProt has a generic ARBA cytoplasm IEA, but the reviewed core function uses thylakoid membrane localization from HAMAP and plastid/chloroplast context.
- Addressed PR review by using GO:0042549 for PSII stabilization rather than assigning the more specific PSII electron-transport process directly to this small structural subunit.
