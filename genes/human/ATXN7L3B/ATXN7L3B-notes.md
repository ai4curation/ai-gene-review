# ATXN7L3B notes

## 2026-10-05 review (PAINT, affinage)

- ENY2 competitor/sequesterer [PMID:27601583 "In vitro, ATXN7L3B competes with ATXN7L3 to bind ENY2, and in vivo, knockdown of ATXN7L3B leads to concomitant loss of ENY2."]. The source is abstract-only; the sequestration wording comes from UniProt's curation of the same paper.
- ENY2 IPI → GO:0140311 protein sequestering activity (core MF); USP22 IPI → GO:1990381.
- Added NEW GO:0090086 negative regulation of protein deubiquitination (IDA): overexpression raises H2Bub1, and the ATXN7L3B-containing complex is a poor DUB.
- Regulation of gene expression: both rows non-core (round 1 changed the IEP row from over-annotated; see below).

## 2026-10-05 revision (reviewer round 1)

- GO:0010468: both rows are now KEEP_AS_NON_CORE. IEP is the wrong code for perturbation data, but that is a code issue, not over-annotation of the term, and the IBA node is partly seeded by this row.
- The NEW row now states the basis for its IDA code. The UniProt protein-stability arm (ATXN7L3 destabilization) is raised as a suggested question.
