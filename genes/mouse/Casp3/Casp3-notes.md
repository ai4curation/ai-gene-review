# Casp3 notes

## 2026-09-30 APOPTOSIS GOA refresh

Fetched current mouse Casp3 GOA and UniProt snapshots and reviewed 15 newly surfaced rows on the completed draft. The refresh carried forward existing actions for duplicate human-ortholog nucleus, cytosol, cytoplasm, pyroptotic-inflammatory-response, peptidase, regulation-of-protein-localization, protein-maturation, and execution-phase rows. A new `PMID:19759058` IntAct `GO:0005515 protein binding` row for ribosomal protein S18 was removed as generic substrate-screen binding evidence while retaining the same paper's direct cysteine-type endopeptidase activity row.

The new `PMID:24378336` broad `GO:0006915 apoptotic process` row was accepted with exact evidence from the BDNF/NT4 gustatory-development paper. The new `PMID:16183742` `GO:0097190 apoptotic signaling pathway` row was kept as non-core because that source places Casp3 activation in the PIDD/RAIDD apoptotic context but does not move Casp3's core function upstream of execution-phase proteolysis. Nine old electronic rows that no longer appear in the refreshed GOA snapshot were removed, including superseded ARBA rows and older Ensembl/UniProt source variants now represented by newly imported rows.

Added structured propagation reviews to 21 human- and rat-ortholog ISO rows that had already been marked for removal, narrowing, or over-annotation. The remaining mixed-action warnings are intentional source-specific cautions around abstract-only experimental papers: PMID:12970760 for a broad B-cell apoptosis row, PMID:12477715 for a cytoplasm row, and PMID:17544522 for a cysteine-type peptidase row. Each term is otherwise supported for Casp3 by stronger direct or propagated evidence.
