# SIRT7 notes

## 2026-11-27

The automated deep-research providers available in this checkout did not include the requested Falcon/Perplexity routes, so `just deep-research-falcon human SIRT7 --fallback perplexity-lite` failed before creating provider output. This review used the cached GOA publications, the UniProtKB Swiss-Prot record, Reactome event summaries cached by `just fetch-gene`, and the existing PANTHER PTHR11085 PAINT table.

SIRT7 is a nucleolar and chromatin-associated NAD-dependent deacylase. Its reviewed core functions are H3K18/H3K36 deacetylation, nucleolar deacetylation of Pol I/rRNA-processing factors, H3K122 desuccinylation during the DNA-damage response, and H4K91 deglutarylation; protein-binding rows and the historical protein-methyltransferase annotation are not informative as direct SIRT7 activities.
