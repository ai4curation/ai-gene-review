# Source-record defects for REACTOME

1 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9BQ52 involved_in GO:0016078 tRNA decay (TAS, Reactome:R-HSA-9708296)
- **Field:** GO TERM
- **Change:** GO:0016078 → GO:0042780 (tRNA 3'-end processing)
- **Recorded in:** `genes/human/ELAC2/ELAC2-ai-review.yaml`

The enclosing ELAC2 annotation, assigned by Reactome with R-HSA-9708296, maps the gene to tRNA decay. The current pathway describes tRNA-derived small RNA biogenesis, and its target-resolved ELAC2 child R-HSA-9708812 removes a pre-tRNA 3′ trailer. PMID:19933153 supports that precursor-processing step, not destruction of mature tRNA. Repoint this ELAC2 GO association to GO:0042780. This is a lateral correction of the modeled process, not an ontology descendant refinement or a request to remove the valid Reactome reaction.
