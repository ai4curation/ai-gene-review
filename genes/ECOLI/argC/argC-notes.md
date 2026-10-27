# ECOLI argC annotation audit

## Scope and source provenance

All 11 normally seeded original annotation rows were reviewed. Original term, reference, evidence, relationship and supporting-entity payloads are retained. No NEW rows were added.

PMID:13863980 is title-only; do not invent experimental detail. Curated HAMAP MF_00150 function and catalytic reaction independently support the canonical NADPH chemistry, corroborated by the AGPR-coupled NADPH assay in PMID:17651682. Live GO:0051287 means NAD+/NADH, not NADP; refine the cofactor claim to GO:0070401 (oxidized reaction partner/product). This correction does not claim an exhaustive negative assay against NADH.

## Evidence and access

- PMID:13863980: N-Acetyl-gamma-Ilutamokinase and N-acetylglutamic gamma-semialdehyde dehydrogenase: repressible enzymes of arginine synthesis in Escherichia coli. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.
- PMID:17651682: Continuous spectrophotometric assays for three regulatory enzymes of the arginine biosynthetic pathway. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.

Curated UniProt CC reaction, pathway, localization, cofactor and HAMAP/domain evidence was read independently; no GOA, DE label, keyword or ARBA-only prediction is used as biological support.

## Research tooling

Normal Falcon research with perplexity-lite fallback was attempted alongside publication caching. Falcon authentication failed (403); fallback failed with quota error (401). No synthetic provider report was written. FEBA lookup was attempted; no reachable data source/usable organism dataset was returned, so no fitness result is claimed. Exact tool output is in `.cache/module-audit-logs/arginine-ECOLI-argC-{deep,fitness,pmids}.log`.

The local ontology snapshot retains the shorter label for GO:0003942 while live QuickGO includes “(NADP+)”. Author-supplied core/replacement labels follow the local validator vocabulary; original machine-sourced labels remain unchanged. The identifier and reaction are identical.
