# pcaF (Acinetobacter baylyi ADP1, Q43974) notes

## Provenance

- Deep research: `just deep-research ACIAD pcaF --provider falcon` was attempted
  on 2026-10-23 and failed with "Failed to authenticate"; no provider report
  exists. This review was written from the Swiss-Prot record and cached
  publications.
- Added as the non-Pseudomonas exemplar of the PcaF thiolase in
  `modules/beta_ketoadipate_lower_pathway.yaml`.

## Evidence

- Swiss-Prot curated function (no automatic evidence tag): "Catalyzes thiolytic
  cleavage of beta-ketoadipyl-CoA to succinyl-CoA and acetyl-CoA."
  [file:ACIAD/pcaF/pcaF-uniprot.txt]; PE level 1 from N-terminal protein
  sequencing in PMID:8063101.
- pcaF is the third gene of the pcaIJFBDKCHG operon encoding the six
  protocatechuate-to-succinate/acetyl-CoA enzymes [PMID:8063101].
- Orthologous CatF of Pseudomonas sp. B13 was shown to have 3-oxoadipyl-CoA
  thiolase activity when expressed [PMID:11741863 "codes for a protein of 401
  amino acid residues with a predicted mass of 41,678 Da with 3-oxoadipyl-CoA
  thiolase activity"].
- Broad parents GO:0003988, GO:0016746, GO:0016747 are is_a ancestors of
  GO:0033812 (checked with runoak against go.db) and are reviewed TOO_GENERAL.
