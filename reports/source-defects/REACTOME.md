# Source-record defects for REACTOME

2 open defect(s), generated from `source_defects` blocks in this repository's reviews. Do not edit by hand.

## 1. WRONG_TERM (CONFIRMED, NOT_REPORTED)

- **Record:** UniProtKB:Q9BQ52 involved_in GO:0016078 tRNA decay (TAS, Reactome:R-HSA-9708296)
- **Field:** GO TERM
- **Change:** GO:0016078 → GO:0042780 (tRNA 3'-end processing)
- **Recorded in:** `genes/human/ELAC2/ELAC2-ai-review.yaml`

The enclosing ELAC2 annotation, assigned by Reactome with R-HSA-9708296, maps the gene to tRNA decay. The current pathway describes tRNA-derived small RNA biogenesis, and its target-resolved ELAC2 child R-HSA-9708812 removes a pre-tRNA 3′ trailer. PMID:19933153 supports that precursor-processing step, not destruction of mature tRNA. Repoint this ELAC2 GO association to GO:0042780. This is a lateral correction of the modeled process, not an ontology descendant refinement or a request to remove the valid Reactome reaction.

## 2. OTHER (PROBABLE, NOT_REPORTED)

- **Record:** Reactome:R-HSA-8952289
- **Subject:** UniProtKB:O00255
- **Change:** check GO:0005788 (alternatives in the explanation)
- **Recorded in:** `genes/human/MEN1/MEN1-ai-review.yaml`

MEN1 (O00255) is listed as a FAM20C substrate in the ER-lumen reaction R-HSA-8952289, which propagates an endoplasmic reticulum lumen location to menin. Menin is a nuclear, non-secreted protein (PMID:9465067); either the menin entity should be removed from this secretory-pathway reaction or the location not propagated to GO.

> menin is located primarily in the nucleus
> — PMID:9465067
