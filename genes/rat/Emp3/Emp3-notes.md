# Emp3 (rat) review notes

- 2026-10-28: fetched; UniProt Q9QYW5 confirmed (GeneID 81505, RGD:621094). 8 GOA rows,
  all IBA/IEA/ISO; no rat experimental annotations.
- PMID:19473976 supplied as a "key experimental paper" is an MCT1/embigin paper with no
  EMP3 content (grep of full text: no EMP/PMP22/bleb hits). Not used as evidence; listed
  in references with reference_review relevance NONE.
- Human-derived BP rows (apoptotic process, bleb assembly) trace to overexpression in
  HEK-293 [PMID:12107182], where all four EMPs gave the same phenotype. Overexpression of a
  tetraspan family member causing blebbing/death is not evidence that endogenous Emp3
  participates in apoptosis or bleb assembly -> MARK_AS_OVER_ANNOTATED.
- Location: plasma membrane is supported (tetraspan topology, N-glycosylated extracellular
  loop; human EMP3 at PM and in endosomal compartments [PMID:37936247]; MAM antigen on red
  cell surface [PMID:36789459]). Generic "membrane" -> MODIFY to plasma membrane.
- No molecular function is established for any EMP3; best-supported mechanistic role (in
  human GBM cells) is regulating trafficking/stability of EGFR. Not asserted as NEW
  (single-system cancer cell evidence, not rat).
