# BACSU argJ annotation audit

## Scope and source provenance

All 6 normally seeded original annotation rows were reviewed. Original term, reference, evidence, relationship and supporting-entity payloads are retained. No NEW rows were added.

B. subtilis bifunctionality is supported by the curated HAMAP MF_01106 classification and the explicit synthesis of complementation evidence in PMID:17347518. PMID:8025667 abstract infers the cyclical pathway from the argC-F operon and ArgJ homology, not purified two-donor kinetics. Do not describe the Geobacillus stearothermophilus assays in PMID:10931207 as direct B. subtilis experiments, and do not generalize bifunctionality to all ArgJ proteins.

## Evidence and access

- PMID:8025667: Sequence and analysis of the citrulline biosynthetic operon argC-F from Bacillus subtilis. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.
- PMID:17347518: Surprising arginine biosynthesis: a reappraisal of the enzymology and evolution of the pathway in microorganisms. Access: cached full text.

Curated UniProt CC reaction, pathway, localization, cofactor and HAMAP/domain evidence was read independently; no GOA, DE label, keyword or ARBA-only prediction is used as biological support.

## Research tooling

Normal Falcon research with perplexity-lite fallback was attempted alongside publication caching. Falcon authentication failed (403); fallback failed with quota error (401). No synthetic provider report was written. FEBA lookup was attempted; no reachable data source/usable organism dataset was returned, so no fitness result is claimed. Exact tool output is in `.cache/module-audit-logs/arginine-BACSU-argJ-{deep,fitness,pmids}.log`.
