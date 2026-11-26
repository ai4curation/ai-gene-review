# TGM1 notes

## Manual review notes

- `GO:0003810` is the direct, conserved acyltransferase activity and is supported by human TGM1 enzymology and by the PTHR11590 root PAINT node.
- Cytosol, plasma membrane, and cornified envelope are all useful locations for TGM1. A separate generic `membrane` row is less precise than the plasma-membrane rows and should be marked too general.
- Bare `GO:0005515` rows are all uninformative interaction rows. Keep the rows distinct because each row has a separate WITH/FROM interactor.
- PMID:26220141 supports a real effect of TGM1 genotype on HaCaT proliferation and differentiation markers, but those proliferation/cell-cycle terms are downstream of defective envelope formation and should stay non-core.
- The Reactome cornified-envelope events use a cytosolic location for soluble TGM1 and a cornified-envelope or plasma-membrane location for the membrane-anchored pool; this split is consistent with PMID:7629111 and PMID:8824274.
