# cysN curation notes

## 2026-10-26 — complete E. coli annotation review

Reviewed all 16 original GOA-seeded rows; payload comparison against the pre-edit snapshot passed. No NEW annotations were added. Actions: {'ACCEPT': 11, 'REMOVE': 2, 'MODIFY': 3}.

PMID:1730615 explicitly assigns the GTP-binding consensus to CysN and describes GTPase-dependent activation of purified E. coli ATP sulfurylase. PMID:8003495 establishes 1:1 coupling of GTP hydrolysis to APS synthesis; PMID:2828368 assigns both complex subunits. These are explicit abstract results; their full text is unavailable in the cache.

Retain GTPase/GTP binding, sulfate assimilation and complex-level ATP sulfurylase assertions. CysN supplies GTP-dependent energy coupling; CysD provides the sulfate adenyl-transfer site. The core uses contributes_to_molecular_function for ATP sulfurylase plus a separate GTPase activity. Original machine payloads, including qualifiers, remain unchanged. Broad sulfur metabolism is refined to sulfate assimilation, with source-specific PTN metadata on the IBA refinement. Bare protein-binding rows are policy removals, not challenges to the reported CysD association.

## Research provenance and access limitations

Normal Falcon deep research was attempted for this exact accession, then the configured Perplexity-lite fallback. Falcon authentication failed; the fallback returned HTTP401 insufficient quota. No provider-named research artifact was fabricated. Logs: `.cache/module-audit-logs/sulfate-ECOLI-cysN-research.log`.

Normal `just fetch-fitness ECOLI cysN` was also attempted. No local FEBA database/BarSeqR data or reachable remote data source was available; no fitness artifact was written. This is missing evidence, not a negative phenotype. Log: `.cache/module-audit-logs/sulfate-ECOLI-cysN-fitness.log`.

Sources were obtained using normal publication fetches. Abstract-only results are used only when explicit; original reference IDs and titles are preserved. GOA rows are assertions under review and are never cited as evidence. Independent annotation-reviewer consultation agreed with retaining real complex-level activities while separating subunit contributions and correcting CysI nucleotide-binding conflation. Targeted schema/evidence validation, automatic UniProt record-section backfill, HTML rendering and helper-generated provenance are run after editing.

## Validation outcome

Automatic record-section backfill completed. `just validate ECOLI cysN` passed with no warnings or errors. The complete pre-edit annotation payload comparison passed for every row. The rendered review and helper-generated history accompany this curation.
