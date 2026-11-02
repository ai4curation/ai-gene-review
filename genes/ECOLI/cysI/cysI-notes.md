# cysI curation notes

## 2026-10-26 — complete E. coli annotation review

Reviewed all 18 original GOA-seeded rows; payload comparison against the pre-edit snapshot passed. No NEW annotations were added. Actions: {'ACCEPT': 14, 'MODIFY': 3, 'REMOVE': 1}.

Read the direct isolated-beta-subunit Mössbauer/EPR abstract PMID:6257697 and full cached reconstitution/structural work PMID:26088143 and PMID:40140349. CysI binds siroheme and a coupled [4Fe-4S] cluster and performs sulfite reduction, whereas CysJ has the NADPH/FAD/FMN input machinery. Remove the GO:0050661 NADP-binding IEA traced to InterPro:IPR011786: this maps a holoenzyme nucleotide requirement onto the wrong subunit. This judgment rests on positive structural/biochemical division of labor, not absence of an annotated binding feature. Propagation metadata records subunit-role conflation.

Retain the NADPH-sulfite-reductase annotation as an enzyme-level claim and use contributes_to_molecular_function in the core. Refine broad oxidoreductase activity, amino acid biosynthesis and iron-sulfur binding to existing specific terms. All siroheme/[4Fe-4S] and complex-membership rows remain accepted. PMID:4144254 is bibliographic-only, but independent same-target evidence supports the biological claims. No unsupported ferredoxin donor is inferred.

The N-terminal deletions in PMID:26088143 preserve catalytic-center function with artificial reducing systems but fail CysJ assembly and native complementation: these are different assays. PMID:40140349 studies engineered minimal dimers; neither that construct nor current UniProt alpha8beta8 language settles universal native stoichiometry. The core does not assert a stoichiometric number.

## Research provenance and access limitations

Normal Falcon deep research was attempted for this exact accession, then the configured Perplexity-lite fallback. Falcon authentication failed; the fallback returned HTTP401 insufficient quota. No provider-named research artifact was fabricated. Logs: `.cache/module-audit-logs/sulfate-ECOLI-cysI-research.log`.

Normal `just fetch-fitness ECOLI cysI` was also attempted. No local FEBA database/BarSeqR data or reachable remote data source was available; no fitness artifact was written. This is missing evidence, not a negative phenotype. Log: `.cache/module-audit-logs/sulfate-ECOLI-cysI-fitness.log`.

Sources were obtained using normal publication fetches. Abstract-only results are used only when explicit; original reference IDs and titles are preserved. GOA rows are assertions under review and are never cited as evidence. Independent annotation-reviewer consultation agreed with retaining real complex-level activities while separating subunit contributions and correcting CysI nucleotide-binding conflation. Targeted schema/evidence validation, automatic UniProt record-section backfill, HTML rendering and helper-generated provenance are run after editing.

## Validation outcome

Automatic record-section backfill completed. `just validate ECOLI cysI` passed with no warnings or errors. The complete pre-edit annotation payload comparison passed for every row. The rendered review and helper-generated history accompany this curation.
