# acnA-II curation notes

- UniProt accession Q88KF4 is named generically as aconitate hydratase, but its
  diagnostic InterPro assignment is
  `IPR012708; 2Me_IsoCit_deHydtase_FeS-dep.`
  [file:PSEPK/acnA-II/acnA-II-uniprot.txt,
  "InterPro; IPR012708; 2Me_IsoCit_deHydtase_FeS-dep."].
- The pathway-level OpenScientist analysis resolves PP_2336 as AcnD based on
  this family assignment and adjacency to prpF. AcnD forms a methyl-trans-
  aconitate intermediate; PrpF converts it to the cis isomer used downstream.
- `aconitate hydratase activity` is removed because GO:0003994 describes the
  canonical citrate/isocitrate reaction. The available hydro-lyase parent is
  retained, and a substrate-specific AcnD molecular-function term is proposed.
- The 4Fe-4S binding annotation present in the UniProt cross-references is
  added as an ancillary cofactor property.
