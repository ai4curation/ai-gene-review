# hsp78 review notes

## 2026-10-09 fungal PAINT-family review

- Reviewed `SCHPO/hsp78` as a phylogenetically inferred member of the fungal
  mitochondrial Hsp78 branch of `PTHR11638`. The local PAINT cache places
  matrix localization, protein refolding, and protein unfolding at
  `PANTHER:PTN000909045`; all three were accepted.

- Deep-research provider generation failed because `uvx` attempted to write its
  managed tool environment under read-only `~/.local/share/uv/tools`. No
  `hsp78-deep-research-*.md` provider file was hand-written. I used cached GOA
  publications plus a 2026-10-09 live newer-paper search instead.

- The newer-paper search did not find a direct S. pombe hsp78 biochemical,
  localization, or deletion study. The review therefore leaves no direct PMID
  evidence for this gene and relies on PomBase's ISO transfer from SGD HSP78,
  UniProt subcellular mapping, InterPro domain mapping, ARBA rows, and the
  fungal Hsp78 PAINT node.

- SGD HSP78 is the experimental source for the fungal Hsp78 clade. Its product
  is directly localized to the mitochondrial matrix [PMID:8413229,
  "Submitochondrial fractionation showed that hsp78 is a soluble protein
  located in the mitochondrial matrix."], cooperates with the mitochondrial Hsp70
  system in substrate reactivation [PMID:11734006, "Studies on the chaperone
  activity of Hsp78 show that its cooperation with the mitochondrial Hsp70
  system, consisting of Ssc1p, Mdj1p and Mge1p, is needed for the efficient
  reactivation of substrate proteins."], and has ATP-dependent disaggregation
  activity [PMID:16460754, "The ATP-dependent disaggregation activity of Hsp78
  was capable of reversing the preprotein import defect of a destabilized mutant
  form of Ssc1."].

- The broad `PANTHER:PTN000181243` rows were split by term. ATP hydrolysis and
  cellular response to heat were accepted because they apply across both Hsp104
  and Hsp78 descendants. The `cytoplasm` row was marked over-annotated because
  the matrix-specific `PANTHER:PTN000909045` placement is the right compartment
  for the mitochondrial Hsp78 paralog.

- The `GO:0006457 protein folding` ARBA row was modified to `GO:0042026 protein
  refolding`. Hsp78 acts after clients have misfolded and aggregated; it is not
  a general de novo folding chaperone.
