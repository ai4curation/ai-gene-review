# BTK ortholog-source trace

`rat-donor-annotation-trace.json` is the normal QuickGO annotation-search response for UniProtKB:A0A0G2K6M9 (retrieved 2026-10-26). It identifies primary publications behind rat BTK claims transferred to mouse/human. The response is provenance, not functional evidence and is never used in a `supported_by` entry. Reproduce with GET `https://www.ebi.ac.uk/QuickGO/services/annotation/search?geneProductId=UniProtKB:A0A0G2K6M9&limit=200`, Accept application/json. Primary papers were fetched normally into `publications/` and assessed independently.
