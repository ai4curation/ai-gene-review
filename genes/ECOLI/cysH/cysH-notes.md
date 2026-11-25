# cysH curation notes

## 2026-10-26 — complete E. coli annotation review

Reviewed all 9 original GOA-seeded rows; payload comparison against the pre-edit snapshot passed. No NEW annotations were added. Actions: {'MODIFY': 3, 'ACCEPT': 6}.

PMID:7588765 explicitly studies recombinant E. coli cysH, purified PAPS reduction using thioredoxin, and loss of activity after Cys239 mutation. PMID:17352498 adds the E. coli CysH/Trx1 structure and an S-sulfocysteine/mixed-disulfide catalytic intermediate; its abstract is normally cached, and the PMC full text was additionally consulted online at https://pmc.ncbi.nlm.nih.gov/articles/PMC3109433/. The modern intermediate chemistry avoids perpetuating a simple pre-existing intramolecular CysH disulfide. No iron-sulfur or glutathione-fusion properties are transferred from APS reductases.

All PAPS-reductase rows are retained. Broad catalytic and sulfur/disulfide oxidoreductase annotations are refined to the existing PAPS reductase function; the reverse convention used for some oxidoreductase labels does not make the broad annotation false. Sulfur metabolism is refined to the existing hydrogen sulfide biosynthetic process: CysH makes sulfite and CysJI subsequently makes sulfide. Cytoplasmic location has independent curated UniProt support.

## Research provenance and access limitations

Normal Falcon deep research was attempted for this exact accession, then the configured Perplexity-lite fallback. Falcon authentication failed; the fallback returned HTTP401 insufficient quota. No provider-named research artifact was fabricated. Logs: `.cache/module-audit-logs/sulfate-ECOLI-cysH-research.log`.

Normal `just fetch-fitness ECOLI cysH` was also attempted. No local FEBA database/BarSeqR data or reachable remote data source was available; no fitness artifact was written. This is missing evidence, not a negative phenotype. Log: `.cache/module-audit-logs/sulfate-ECOLI-cysH-fitness.log`.

Sources were obtained using normal publication fetches. Abstract-only results are used only when explicit; original reference IDs and titles are preserved. GOA rows are assertions under review and are never cited as evidence. Independent annotation-reviewer consultation agreed with retaining real complex-level activities while separating subunit contributions and correcting CysI nucleotide-binding conflation. Targeted schema/evidence validation, automatic UniProt record-section backfill, HTML rendering and helper-generated provenance are run after editing.

## Validation outcome

Automatic record-section backfill completed. `just validate ECOLI cysH` passed with no warnings or errors. The complete pre-edit annotation payload comparison passed for every row. The rendered review and helper-generated history accompany this curation.
