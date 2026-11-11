# cysD curation notes

## 2026-10-26 — complete E. coli annotation review

Reviewed all 16 original GOA-seeded rows; payload comparison against the pre-edit snapshot passed. No NEW annotations were added. Actions: {'ACCEPT': 10, 'MODIFY': 3, 'REMOVE': 2, 'KEEP_AS_NON_CORE': 1}.

PMID:2828368 explicitly assigns the two purified ATP sulfurylase subunits to cysD/cysN; PMID:8003495 establishes 1:1 GTP hydrolysis/APS synthesis. These caches are abstract-only but the relevant experimental conclusions are explicit. Sulfate assimilation, ATP sulfurylase membership and activity are retained. Broad catalytic activity and sulfur metabolism are refined to the existing specific function/process.

Read the full PMID:24580753 results around cysD: the deletion is peroxide-sensitive, has increased cellular ROS and reduced NADPH, and NADPH pretreatment rescues sensitivity. Retain cellular oxidative-stress response as a contextual non-core role and refine the broader response row to it. Do not infer direct peroxide-reductase chemistry or a dedicated antioxidant protein. Both generic interaction rows are removed under the bare GO:0005515 policy; neither interaction is called false.

## Research provenance and access limitations

Normal Falcon deep research was attempted for this exact accession, then the configured Perplexity-lite fallback. Falcon authentication failed; the fallback returned HTTP401 insufficient quota. No provider-named research artifact was fabricated. Logs: `.cache/module-audit-logs/sulfate-ECOLI-cysD-research.log`.

Normal `just fetch-fitness ECOLI cysD` was also attempted. No local FEBA database/BarSeqR data or reachable remote data source was available; no fitness artifact was written. This is missing evidence, not a negative phenotype. Log: `.cache/module-audit-logs/sulfate-ECOLI-cysD-fitness.log`.

Sources were obtained using normal publication fetches. Abstract-only results are used only when explicit; original reference IDs and titles are preserved. GOA rows are assertions under review and are never cited as evidence. Independent annotation-reviewer consultation agreed with retaining real complex-level activities while separating subunit contributions and correcting CysI nucleotide-binding conflation. Targeted schema/evidence validation, automatic UniProt record-section backfill, HTML rendering and helper-generated provenance are run after editing.

## Validation outcome

Automatic record-section backfill completed. `just validate ECOLI cysD` passed with no warnings or errors. The complete pre-edit annotation payload comparison passed for every row. The rendered review and helper-generated history accompany this curation.
