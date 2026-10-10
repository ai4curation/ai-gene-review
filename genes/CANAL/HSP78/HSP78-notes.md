# HSP78 review notes

## 2026-10-09 fungal PAINT-family review

- Reviewed `CANAL/HSP78` as the C. albicans representative of the fungal
  mitochondrial Hsp78 branch of `PTHR11638`. The local PANTHER member table
  places Q96UX5 in the same mitochondrial Hsp78 subfamily as S. cerevisiae HSP78
  and S. pombe hsp78.

- Deep-research provider generation failed because `uvx` attempted to write its
  managed tool environment under read-only `~/.local/share/uv/tools`. No
  `HSP78-deep-research-*.md` provider file was hand-written. I used cached GOA
  publications plus a 2026-10-09 live newer-paper search instead.

- Recent Candida search hits mention `HSP78` in expression or proteomics
  contexts, but I did not find a newer direct C. albicans Hsp78 localization,
  deletion, or biochemical paper. The review therefore treats the CGD `ND` rows
  as non-core placeholders and relies on PAINT, InterPro, UniProt transfer, and
  Ensembl/combined orthology transfer for the positive functional assertions.

- The Hsp78-specific PAINT node `PANTHER:PTN000909045` carries
  mitochondrial-matrix localization, protein refolding, and protein unfolding.
  All three were accepted because C. albicans HSP78 is in that clade.

- The broad `PANTHER:PTN000181243` cytoplasm IBA was marked over-annotated
  because `GO:0005737` is true but too broad for the mitochondrial-matrix Hsp78
  branch. The ATP hydrolysis and cellular heat-response IBAs from the same broad
  node were accepted as functions retained on both sides of the Hsp104/Hsp78
  split.

- S. cerevisiae HSP78 provides the experimental orthology anchor for the
  Candida row set: matrix localization [PMID:8413229, "Submitochondrial
  fractionation showed that hsp78 is a soluble protein located in the
  mitochondrial matrix."], Hsp70-system-dependent substrate reactivation
  [PMID:11734006, "Studies on the chaperone activity of Hsp78 show that its
  cooperation with the mitochondrial Hsp70 system, consisting of Ssc1p, Mdj1p
  and Mge1p, is needed for the efficient reactivation of substrate proteins."],
  and ATP-dependent disaggregation [PMID:16460754, "The ATP-dependent
  disaggregation activity of Hsp78 was capable of reversing the preprotein
  import defect of a destabilized mutant form of Ssc1."].

- Added a conservative ISO-style `NEW` `GO:0140545 ATP-dependent protein
  disaggregase activity` row from SGD HSP78, because the current Candida GOA
  rows captured ATP hydrolysis, refolding, and unfolding but not the integrated
  ATP-dependent disaggregase molecular function.
