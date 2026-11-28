# SIRT6 notes

## 2026-11-27

The automated deep-research providers available in this checkout did not include the requested Falcon/Perplexity routes, so `just deep-research-falcon human SIRT6 --fallback perplexity-lite` failed before creating provider output. This review used the cached GOA publications, the UniProtKB Swiss-Prot record, Reactome event summaries cached by `just fetch-gene`, and the existing PANTHER PTHR11085 PAINT table.

SIRT6 is the largest review in this split because its GOA file mixes direct human chromatin/DNA-repair/deacylation evidence with many orthology transfers from mouse Sirt6. The review keeps SIRT6's direct histone deacetylase, defatty-acylase, mono-ADP-ribosyltransferase, nucleosome-binding, and DNA-break-sensing functions as central, and treats most tissue or metabolism processes as non-core consequences of those molecular activities.
