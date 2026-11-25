# MYCTU argF annotation audit

## Scope and source provenance

All 13 normally seeded original annotation rows were reviewed. Original term, reference, evidence, relationship and supporting-entity payloads are retained. No NEW rows were added.

PMID:1406593 explicitly studies Mycobacterium bovis BCG, not H37Rv; retain the well-supported enzyme function using native M. tuberculosis structure/chemistry (PMID:18062991) without alleging curator misattribution. Full PMID:12011001 explains that failure of citrulline rescue is compatible with polarity on downstream argG. This does not make ArgF an argininosuccinate synthetase or a direct host immune regulator. Norvaline is an inhibitor/ornithine mimic in the structure, not an alternative physiological substrate.

## Evidence and access

- PMID:18062991: The crystal structures of ornithine carbamoyltransferase from Mycobacterium tuberculosis and its ternary complex with carbamoyl phosphate and L-norvaline reveal the enzyme's catalytic mechanism. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.
- PMID:17012791: Expression, purification, crystallization and preliminary X-ray analysis of two arginine-biosynthetic enzymes from Mycobacterium tuberculosis. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.
- PMID:12011001: Construction and phenotypic characterization of an auxotrophic mutant of Mycobacterium tuberculosis defective in L-arginine biosynthesis. Access: cached full text.
- PMID:1406593: Molecular cloning, characterization and purification of ornithine carbamoyltransferase from Mycobacterium bovis BCG. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.

Curated UniProt CC reaction, pathway, localization, cofactor and HAMAP/domain evidence was read independently; no GOA, DE label, keyword or ARBA-only prediction is used as biological support.

## Research tooling

Normal Falcon research with perplexity-lite fallback was attempted alongside publication caching. Falcon authentication failed (403); fallback failed with quota error (401). No synthetic provider report was written. FEBA lookup was attempted; no reachable data source/usable organism dataset was returned, so no fitness result is claimed. Exact tool output is in `.cache/module-audit-logs/arginine-MYCTU-argF-{deep,fitness,pmids}.log`.
