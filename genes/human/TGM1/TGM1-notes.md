# TGM1 notes

## Manual review notes

- `GO:0003810` is the direct, conserved acyltransferase activity and is supported by human TGM1 enzymology and by the PTHR11590 root PAINT node.
- Cytosol, plasma membrane, and cornified envelope are all useful locations for TGM1. A separate generic `membrane` row is less precise than the plasma-membrane rows and is supported by its own evidence as `GO:0005886`.
- Bare `GO:0005515` rows are all uninformative interaction rows. Keep the rows distinct because each row has a separate WITH/FROM interactor.
- PMID:26220141 supports a real effect of TGM1 genotype on HaCaT proliferation and differentiation markers, but those proliferation/cell-cycle terms are downstream of defective envelope formation and should stay non-core.
- The Reactome cornified-envelope events use a cytosolic location for soluble TGM1 and a cornified-envelope or plasma-membrane location for the membrane-anchored pool; this split is consistent with PMID:7629111 and PMID:8824274.
- The live Reactome participant lists were checked on 2026-11-26 for R-HSA-6810894, R-HSA-6810899, R-HSA-6810937, R-HSA-6811539, R-HSA-6814298, R-HSA-6814387, R-HSA-6814734, and R-HSA-6814764. They show direct TGM1 participants in the early scaffold and reinforcement events, and downstream cornified-envelope states in the lamellar-body, late-envelope, CASP14, CDSN, and plasma-membrane-resorption events; those downstream rows are kept because the location claim itself is independently supported for the same cornified-envelope pathway.
