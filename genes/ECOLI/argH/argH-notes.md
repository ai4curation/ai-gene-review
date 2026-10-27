# ECOLI argH annotation audit

## Scope and source provenance

All 8 normally seeded original annotation rows were reviewed. Original term, reference, evidence, relationship and supporting-entity payloads are retained. No NEW rows were added.

The cell-free argH expression study uses radiolabeled argininosuccinate cleavage as the assay. Arginase and urease are downstream coupling enzymes in that assay, not additional activities of ArgH. Do not import the ArgH(A) acetyltransferase fusion architecture of other bacterial lineages into E. coli ArgH.

## Evidence and access

- PMID:6762207: The determination by radiochemical assay of argininosuccinase produced in an Escherichia coli system in vitro. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.

Curated UniProt CC reaction, pathway, localization, cofactor and HAMAP/domain evidence was read independently; no GOA, DE label, keyword or ARBA-only prediction is used as biological support.

## Research tooling

Normal Falcon research with perplexity-lite fallback was attempted alongside publication caching. Falcon authentication failed (403); fallback failed with quota error (401). No synthetic provider report was written. FEBA lookup was attempted; no reachable data source/usable organism dataset was returned, so no fitness result is claimed. Exact tool output is in `.cache/module-audit-logs/arginine-ECOLI-argH-{deep,fitness,pmids}.log`.
