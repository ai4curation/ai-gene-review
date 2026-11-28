# SIRT4 notes

## 2026-11-27

The automated deep-research providers available in this checkout did not include the requested Falcon/Perplexity routes, so `just deep-research-falcon human SIRT4 --fallback perplexity-lite` failed before creating provider output. This review used the cached GOA publications, the UniProtKB Swiss-Prot record, Reactome event summaries cached by `just fetch-gene`, and the existing PANTHER PTHR11085 PAINT table.

SIRT4 is a mitochondrial matrix sirtuin whose clearest human molecular functions are NAD-dependent delipoylation of the DLAT lipoyl cofactor and mono-ADP-ribosylation of GLUD1. Several electronic rows still follow generic sirtuin deacetylase, histone-deacetylase, and chromatin-remodeling edges that fit nuclear sirtuins rather than SIRT4.
