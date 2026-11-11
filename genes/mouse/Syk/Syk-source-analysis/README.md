# SYK donor and ontology provenance

`human-donor-autophagy-trace.json` records the normal QuickGO annotation search for human UniProtKB:P43405 and autophagy/nutrient/TORC terms, retrieved 2026-10-26. The query did not recover every historical transfer source. It identifies current provenance only, never whether a function is true; no GOA/annotation response is cited in supported_by. Primary 25946330, 26429917, 31324720 and 34634301 were independently read.

Inspect the current donor using GET https://www.ebi.ac.uk/QuickGO/services/annotation/search with geneProductId=UniProtKB:P43405 and limit=200, then filter the relevant GO terms. The historical filtered request URL was not retained with this response, so the artifact is not claimed to be a complete unfiltered donor inventory. The retained response has one current positive-TORC record (GO:1904263, PMID:34634301); absence from this response is not absence of biological activity. Current responses can differ from this dated trace.
