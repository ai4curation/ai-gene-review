# rps12-B notes

- Fetched with `just fetch-gene POPTR rps12-B`.
- Curated as chloroplast small ribosomal subunit protein uS12cy. Generic ribosome terms are retained as non-core where the small ribosomal subunit term is more specific; structural ribosome function, rRNA binding, chloroplast localization, and translation are core.

- Addressed PR #469 review on 2026-05-10: replaced circular rRNA-binding support from the UniProt GO cross-reference with the independent UniProt subunit statement `Part of the 30S ribosomal subunit.`

- Addressed PR #469 re-review on 2026-05-10: rRNA binding support now uses the UniProtKB-UniRule GO DR line and states explicitly that the ACCEPT is rule-based for the uS12 family, not a direct Populus rRNA-contact assay.
