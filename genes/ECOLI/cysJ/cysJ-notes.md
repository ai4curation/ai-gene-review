# cysJ curation notes

## 2026-10-26 — complete E. coli annotation review

Reviewed all 23 original GOA-seeded rows; payload comparison against the pre-edit snapshot passed. No NEW annotations were added. Actions: {'ACCEPT': 18, 'REMOVE': 2, 'MODIFY': 2, 'KEEP_AS_NON_CORE': 1}.

Read original PMID:10860732, PMID:7657631 and PMID:8360156 abstracts and full cached PMID:26088143/PMID:40140349. CysJ binds NADPH, FAD and FMN and supplies electrons to the CysI metallocenter. The 1995 paper explicitly proposes one FMN plus one FAD per alpha subunit; it is not evidence for one-flavin-only CysJ. Free-flavin reductase is a measured secondary activity, retained as non-core. NADP+ binding is supported by product inhibition as well as the pyridine-nucleotide-binding structure.

PMID:20118259 was normally fetched after an initial HTTP429 failure. Its abstract and curated UniProt show a native CysJ/YcbX role in N-hydroxylated-base detoxification independent of CysI. Electron delivery to the molybdocenter is proposed in that paper, so this is not treated as direct purified YcbX electron-transfer proof. No NEW process annotation was manufactured.

The 1973 PMID:4144254 cache is bibliographic-only. Modern same-target biochemistry independently supports its sulfate/cysteine pathway assertions; no UNDECIDED decision is manufactured solely because this older source has no abstract. The 1993 paper demonstrates free-flavin reduction by purified sulfite reductase and proposes involvement in ribonucleotide reductase activation; it does not establish this as the universal primary role.

The 2015 full text supports alpha8beta4 reconstitution. The 2025 study uses engineered minimal CysJ/CysI dimers, with stable binding and transient electron-transfer interfaces distinguished; these constructs do not justify calling the native complex a heterodimer. UniProt currently states alpha8beta8, so do not silently treat that stoichiometry as experimentally settled. The core requires CysJI but does not assert a disputed universal stoichiometry. Bare binding rows are policy removals, not rejection of the interaction screens.

## Research provenance and access limitations

Normal Falcon deep research was attempted for this exact accession, then the configured Perplexity-lite fallback. Falcon authentication failed; the fallback returned HTTP401 insufficient quota. No provider-named research artifact was fabricated. Logs: `.cache/module-audit-logs/sulfate-ECOLI-cysJ-research.log`.

Normal `just fetch-fitness ECOLI cysJ` was also attempted. No local FEBA database/BarSeqR data or reachable remote data source was available; no fitness artifact was written. This is missing evidence, not a negative phenotype. Log: `.cache/module-audit-logs/sulfate-ECOLI-cysJ-fitness.log`.

Sources were obtained using normal publication fetches. Abstract-only results are used only when explicit; original reference IDs and titles are preserved. GOA rows are assertions under review and are never cited as evidence. Independent annotation-reviewer consultation agreed with retaining real complex-level activities while separating subunit contributions and correcting CysI nucleotide-binding conflation. Targeted schema/evidence validation, automatic UniProt record-section backfill, HTML rendering and helper-generated provenance are run after editing.

## Validation outcome

Automatic record-section backfill completed. `just validate ECOLI cysJ` passed with no warnings or errors. The complete pre-edit annotation payload comparison passed for every row. The rendered review and helper-generated history accompany this curation.
