# ECOLI argB annotation audit

## Scope and source provenance

All 10 normally seeded original annotation rows were reviewed. Original term, reference, evidence, relationship and supporting-entity payloads are retained. No NEW rows were added.

Native E. coli kinase assays and structures support catalysis and ATP binding. PMID:11967071 is an abstract-only global mitomycin-C expression study; retain the curator-attributed IEP response as contextual, not a direct DNA-repair function. Do not transfer the parallel aspartokinase III regulatory results in PMID:14623187 to ArgB.

## Evidence and access

- PMID:10393305: N-Acetyl-L-glutamate kinase from Escherichia coli: cloning of the gene, purification and crystallization of the recombinant enzyme and preliminary X-ray analysis of the free and ligand-bound forms. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.
- PMID:14623187: Site-directed mutagenesis of Escherichia coli acetylglutamate kinase and aspartokinase III probes the catalytic and substrate-binding mechanisms of these amino acid kinase family enzymes and allows three-dimensional modelling of aspartokinase. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.
- PMID:17651682: Continuous spectrophotometric assays for three regulatory enzymes of the arginine biosynthetic pathway. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.
- PMID:12875848: The course of phosphorus in the reaction of N-acetyl-L-glutamate kinase, determined from the structures of crystalline complexes, including a complex with an AlF(4)(-) transition state mimic. Access: cached abstract or bibliographic record only; detailed claims limited accordingly.

Curated UniProt CC reaction, pathway, localization, cofactor and HAMAP/domain evidence was read independently; no GOA, DE label, keyword or ARBA-only prediction is used as biological support.

## Research tooling

Normal Falcon research with perplexity-lite fallback was attempted alongside publication caching. Falcon authentication failed (403); fallback failed with quota error (401). No synthetic provider report was written. FEBA lookup was attempted; no reachable data source/usable organism dataset was returned, so no fitness result is claimed. Exact tool output is in `.cache/module-audit-logs/arginine-ECOLI-argB-{deep,fitness,pmids}.log`.
