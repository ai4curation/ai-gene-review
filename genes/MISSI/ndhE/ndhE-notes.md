## Curation notes

- QuickGO export is header-only; therefore no UniProt DR/InterPro/HAMAP-derived terms are listed as `existing_annotations` or proposed as `NEW`.
- Core function treats ndhE as a plastid NDH membrane-sector subunit supporting quinone reduction coupled to proton translocation.
- PR re-review noted that GO:0050136 includes "non-electrogenic" in the term label even though UniRule catalytic text for plastid NDH implies proton movement. Retained GO:0050136 because it is the current UniRule-supported contribution term, with proton-coupled transport captured separately by GO:0015990.
