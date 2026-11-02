# NOSS1 argC2 annotation audit

## Scope and source provenance

All 5 normally seeded original annotation rows were reviewed. Original term, reference, evidence, relationship and supporting-entity payloads are retained. No NEW rows were added.

The 322-aa cloned historical argC sequence corresponds to P54894/all2498, current argC2 nomenclature; do not confuse it with the other paralog. Native and E. coli complementation support biosynthetic participation (PMID:1406250). NADPH chemistry and type-2 assignment use curated HAMAP MF_01110; the abstract does not itself report cofactor kinetics. GO:0051287 specifically means unphosphorylated NAD, so refine to the NADP reaction partner rather than claim NADH utilization.

## Evidence and access

- PMID:1406250: Isolation of arginine auxotrophs, cloning by mutant complementation, and sequence analysis of the argC gene from the cyanobacterium Anabaena species PCC 7120. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.
- PMID:7929012: Analysis of expression of the argC and argD genes in the cyanobacterium Anabaena sp. strain PCC 7120. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.

Curated UniProt CC reaction, pathway, localization, cofactor and HAMAP/domain evidence was read independently; no GOA, DE label, keyword or ARBA-only prediction is used as biological support.

## Research tooling

Normal Falcon research with perplexity-lite fallback was attempted alongside publication caching. Falcon authentication failed (403); fallback failed with quota error (401). No synthetic provider report was written. FEBA lookup was attempted; no reachable data source/usable organism dataset was returned, so no fitness result is claimed. Exact tool output is in `.cache/module-audit-logs/arginine-NOSS1-argC2-{deep,fitness,pmids}.log`.

The local ontology snapshot retains the shorter label for GO:0003942 while live QuickGO includes “(NADP+)”. Author-supplied core/replacement labels follow the local validator vocabulary; original machine-sourced labels remain unchanged. The identifier and reaction are identical.
