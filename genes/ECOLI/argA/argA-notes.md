# ECOLI argA annotation audit

## Scope and source provenance

All 11 normally seeded original annotation rows were reviewed. Original term, reference, evidence, relationship and supporting-entity payloads are retained. No NEW rows were added.

Live QuickGO definitions independently checked: GO:0004358 specifies acetyl-L-ornithine as donor (RHEA:15349), whereas GO:0004042 specifies acetyl-CoA (RHEA:24292). Four original 4358 rows are refined by donor correction, not discarded. PMID:17651682 explicitly assays E. coli AGS and yeast GAT as different enzymes. PMID:16890 is title-only in cache; its curated experimental UniProt reaction remains independent support, not a claim to have read unavailable full text. The N-terminal kinase-like fold does not establish kinase activity.

## Evidence and access

- PMID:17651682: Continuous spectrophotometric assays for three regulatory enzymes of the arginine biosynthetic pathway. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.
- PMID:1102931: Isolation and characterization of mutants with a feedback resistant N-acetylglutamate synthase in Escherichia coli K 12. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.
- PMID:16890: N-acetylglutamate synthase of Escherichia coli: purification, characterization, and molecular properties. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.

Curated UniProt CC reaction, pathway, localization, cofactor and HAMAP/domain evidence was read independently; no GOA, DE label, keyword or ARBA-only prediction is used as biological support.

## Research tooling

Normal Falcon research with perplexity-lite fallback was attempted alongside publication caching. Falcon authentication failed (403); fallback failed with quota error (401). No synthetic provider report was written. FEBA lookup was attempted; no reachable data source/usable organism dataset was returned, so no fitness result is claimed. Exact tool output is in `.cache/module-audit-logs/arginine-ECOLI-argA-{deep,fitness,pmids}.log`.
