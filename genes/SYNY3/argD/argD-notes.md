# SYNY3 argD annotation audit

## Scope and source provenance

All 10 normally seeded original annotation rows were reviewed. Original term, reference, evidence, relationship and supporting-entity payloads are retained. No NEW rows were added.

Read PMID:36982927 full text: acetylornithine efficiency is 2500-fold higher than ornithine and 10,700-fold higher than GABA (the order matters). PMID:24989231 abstract reports native mutant, isotope and flux evidence for the GABA shunt. Preserve that role rather than dismiss it on Km alone. No redundant NEW activity is added: the existing broad transaminase row can cover multiple measured reactions. DapC-like lysine-pathway activity is only a curated "may" inference and is not promoted to a new assertion.

## Evidence and access

- PMID:36982927: Kinetic Characterization and Catalytic Mechanism of N-Acetylornithine Aminotransferase Encoded by slr1022 Gene from Synechocystis sp. PCC6803. Access: cached full text.
- PMID:24989231: The γ-aminobutyric acid shunt contributes to closing the tricarboxylic acid cycle in Synechocystis sp. PCC 6803. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.

Curated UniProt CC reaction, pathway, localization, cofactor and HAMAP/domain evidence was read independently; no GOA, DE label, keyword or ARBA-only prediction is used as biological support.

## Research tooling

Normal Falcon research with perplexity-lite fallback was attempted alongside publication caching. Falcon authentication failed (403); fallback failed with quota error (401). No synthetic provider report was written. FEBA lookup was attempted; no reachable data source/usable organism dataset was returned, so no fitness result is claimed. Exact tool output is in `.cache/module-audit-logs/arginine-SYNY3-argD-{deep,fitness,pmids}.log`.
