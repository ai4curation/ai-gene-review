# paaJ curation notes

- UniProt accession Q88HS3 names the target
  `3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase`
  [file:PSEPK/paaJ/paaJ-uniprot.txt,
  "SubName: Full=3-oxoadipyl-CoA/3-oxo-5,6-dehydrosuberyl-CoA thiolase"].
- UniProt records the reaction
  `succinyl-CoA + acetyl-CoA = 3-oxoadipyl-CoA + CoA`
  [file:PSEPK/paaJ/paaJ-uniprot.txt,
  "Reaction=succinyl-CoA + acetyl-CoA = 3-oxoadipyl-CoA + CoA;"].
- The exact 3-oxoadipyl-CoA thiolase term is retained. Generic acyltransferase
  parents are replaced by it, while acetyl-CoA C-acetyltransferase is marked
  over-annotated because it specifies the wrong second substrate.
- Phenylacetate catabolism is modeled as the principal paa-locus role.
  The pathway-level paralog analysis identifies the
  3,4-dihydroxybenzoate-process annotation as over-propagation from
  PcaF/PP_1377, so it is marked over-annotated rather than retained as a
  secondary PaaJ role.
