# ECOLI argE annotation audit

## Scope and source provenance

All 14 normally seeded original annotation rows were reviewed. Original term, reference, evidence, relationship and supporting-entity payloads are retained. No NEW rows were added.

PMID:10684608 directly reports broad N-acyl-amino-acid hydrolysis, including acetyl/formyl-methionine with higher activity than acetylornithine, one Zn per purified monomer, and activation by added Zn or Co. Preserve cobalt binding as a measured biochemical capability, non-core; do not infer physiological cobalt occupancy. Broad deacetylase/amidohydrolase claims are genuine multi-substrate functions, not evidence of peptide or DapE activity.

## Evidence and access

- PMID:10684608: Mechanistic analysis of the argE-encoded N-acetylornithine deacetylase. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.
- PMID:1551850: Structural and biochemical characterization of the Escherichia coli argE gene product. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.

Curated UniProt CC reaction, pathway, localization, cofactor and HAMAP/domain evidence was read independently; no GOA, DE label, keyword or ARBA-only prediction is used as biological support.

## Research tooling

Normal Falcon research with perplexity-lite fallback was attempted alongside publication caching. Falcon authentication failed (403); fallback failed with quota error (401). No synthetic provider report was written. FEBA lookup was attempted; no reachable data source/usable organism dataset was returned, so no fitness result is claimed. Exact tool output is in `.cache/module-audit-logs/arginine-ECOLI-argE-{deep,fitness,pmids}.log`.
