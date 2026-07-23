# paaD curation notes

- UniProt accession Q88HS8 conservatively names the target
  `Subunit of phenylacetate degradation enzyme`
  [file:PSEPK/paaD/paaD-uniprot.txt,
  "SubName: Full=Subunit of phenylacetate degradation enzyme"].
- The protein has a PaaD-like family assignment and MIP18-like/PaaD
  zinc-ribbon domains, but no EC number and prediction-level protein evidence.
- The pathway-level OpenScientist report maps it to the PaaABCDE epoxidase by
  homology and synteny, not direct KT2440 biochemistry
  [file:projects/P_PUTIDA/deep-research/PSEPK__phenylacetate_catabolism__ppu00360-deep-research-openscientist.md,
  "| paaD | PP_3275 | Q88HS8 | epoxidase component (Fe-S) | Homology + synteny | No EC in UniProt; \"subunit of phenylacetate degradation enzyme\" |"].
- The review therefore uses `contributes_to` for the complex molecular
  function and does not assign an independent catalytic activity to PaaD.
