# SYNY3 argG annotation audit

## Scope and source provenance

All 11 normally seeded original annotation rows were reviewed. Original term, reference, evidence, relationship and supporting-entity payloads are retained. No NEW rows were added.

PMID:38478146 full text provides recombinant assays and native overexpression: growth advantage occurs with nitrate but not supplied arginine. Avoid universal rate-limiting or direct redox-regulation claims. Two bare protein-binding rows are removed as uninformative under policy, retaining the TrxA trapping observations here; this is not a denial of interaction. Historical urea-cycle interpretation (PMID:10648527) must be distinguished from the later ArgZ ornithine-ammonia cycle (PMID:29632414,31914412): the latter releases ammonia, not urea. Leave urea-cycle propagation unresolved pending evidence for a parallel urea-producing route; do not infer it solely from shared ArgG chemistry.

## Evidence and access

- PMID:38478146: Arginine inhibits the arginine biosynthesis rate-limiting enzyme and leads to the accumulation of intracellular aspartate in Synechocystis sp. PCC 6803. Access: cached full text.
- PMID:14673118: Thioredoxin-linked processes in cyanobacteria are as numerous as in chloroplasts, but targets are different. Access: cached full text.
- PMID:16526092: Selecting thioredoxins for disulphide proteomics: target proteomes of three thioredoxins from the cyanobacterium Synechocystis sp. PCC 6803. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.
- PMID:10648527: Arginine catabolism in the cyanobacterium Synechocystis sp. Strain PCC 6803 involves the urea cycle and arginase pathway. Access: cached full text.
- PMID:29632414: The cyanobacterial ornithine-ammonia cycle involves an arginine dihydrolase. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.
- PMID:31914412: Crystal structures and biochemical analyses of the bacterial arginine dihydrolase ArgZ suggests a "bond rotation" catalytic mechanism. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.

Curated UniProt CC reaction, pathway, localization, cofactor and HAMAP/domain evidence was read independently; no GOA, DE label, keyword or ARBA-only prediction is used as biological support.

## Research tooling

Normal Falcon research with perplexity-lite fallback was attempted alongside publication caching. Falcon authentication failed (403); fallback failed with quota error (401). No synthetic provider report was written. FEBA lookup was attempted; no reachable data source/usable organism dataset was returned, so no fitness result is claimed. Exact tool output is in `.cache/module-audit-logs/arginine-SYNY3-argG-{deep,fitness,pmids}.log`.
