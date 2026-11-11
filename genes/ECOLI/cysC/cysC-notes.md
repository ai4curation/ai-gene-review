# cysC curation notes

## 2026-10-26 — complete E. coli annotation review

Reviewed all 9 original GOA-seeded rows; payload comparison against the pre-edit snapshot passed. No NEW annotations were added. Actions: {'ACCEPT': 9}.

PMID:1332767 and PMID:2549047 explicitly characterize E. coli CysC APS kinase, ATP-dependent PAPS production and identical-subunit oligomers. The historical phosphorylated-enzyme model is not required to accept the kinase activity; no general protein-kinase activity is inferred. The phosphorylation process is as specific as supported without inventing a new BP term.

CysC acts in the E. coli PAPS-dependent sulfate-assimilation route. This does not imply that APS kinase in every species necessarily supplies assimilatory PAPS reductase, because plants use PAPS in sulfation while reducing APS directly. Homooligomerization is specifically supported by the purified enzyme and is retained. Both original publication caches are abstract-only; the retained conclusions are stated explicitly.

## Research provenance and access limitations

Normal Falcon deep research was attempted for this exact accession, then the configured Perplexity-lite fallback. Falcon authentication failed; the fallback returned HTTP401 insufficient quota. No provider-named research artifact was fabricated. Logs: `.cache/module-audit-logs/sulfate-ECOLI-cysC-research.log`.

Normal `just fetch-fitness ECOLI cysC` was also attempted. No local FEBA database/BarSeqR data or reachable remote data source was available; no fitness artifact was written. This is missing evidence, not a negative phenotype. Log: `.cache/module-audit-logs/sulfate-ECOLI-cysC-fitness.log`.

Sources were obtained using normal publication fetches. Abstract-only results are used only when explicit; original reference IDs and titles are preserved. GOA rows are assertions under review and are never cited as evidence. Independent annotation-reviewer consultation agreed with retaining real complex-level activities while separating subunit contributions and correcting CysI nucleotide-binding conflation. Targeted schema/evidence validation, automatic UniProt record-section backfill, HTML rendering and helper-generated provenance are run after editing.

## Validation outcome

Automatic record-section backfill completed. `just validate ECOLI cysC` passed with no warnings or errors. The complete pre-edit annotation payload comparison passed for every row. The rendered review and helper-generated history accompany this curation.
