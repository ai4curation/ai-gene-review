# SIRT3 notes

## 2026-11-27

The automated deep-research providers available in this checkout did not include the requested Falcon/Perplexity routes, so `just deep-research-falcon human SIRT3 --fallback perplexity-lite` failed before creating provider output. This review used the cached GOA publications, the UniProtKB Swiss-Prot record, Reactome event summaries cached by `just fetch-gene`, and the existing PANTHER PTHR11085 PAINT table.

SIRT3 is the mitochondrial member with robust NAD-dependent lysine deacetylase activity. The current GOA rows cleanly support mitochondrial matrix localization and deacetylation of metabolic enzymes; inherited nuclear, nucleoplasmic, and chromatin-remodeling rows appear to be family-level overpropagation from the nuclear sirtuin branches.
