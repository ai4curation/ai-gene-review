# MET15 Notes

## 2026-10-24

- Seeded `CANAL/MET15` with `just fetch-gene CANAL MET15`. Automated deep
  research could not run because no provider API key was configured, so this
  review used the fetched CGD/GOA/UniProt records, cached publications, manual
  PubMed/web search, and the cached `PTHR43797` PAINT table.
- `PMID:39548263` is the key direct-function source. Kuplinska et al. cloned
  and purified C. albicans Met15p and showed that both tagged enzymes
  "displayed an activity of O-acetyl-L-homoserine sulfhydrylase". The same
  assay directly separates C. albicans Met15p from the bifunctional yeast
  source enzymes: "no L-Cys production was detected when O-acetyl-L-serine was
  present in the reaction mixture instead of OAH".
- `PANTHER:PTN002887184` is the current PAINT source node for the fungal
  homocysteine synthase clade in `interpro/panther/PTHR43797/PTHR43797-paint.tsv`.
  The cached rows on that node assert cytoplasm, `GO:0051009`
  O-acetylhomoserine sulfhydrylase activity, and `GO:0071269`
  L-homocysteine biosynthetic process. They no longer assert `GO:0004124`
  cysteine synthase activity, matching the 2024 C. albicans substrate assay.
- The `GO:0004124` cysteine synthase activity rows were removed as stale or
  over-propagated transfers from bifunctional family members because purified
  CaMet15p did not detectably convert O-acetyl-L-serine to L-cysteine. The
  `GO:0019344` L-cysteine biosynthetic process row was kept as non-core because
  Met15p produces L-homocysteine and `PMID:42003610` places C. albicans CYS4
  and CYS3 in transsulfuration, allowing cysteine/homocysteine interconversion.
- `PMID:10992284` established the original met15-deficient strain and reported
  that growth without methionine "was severely delayed" rather than fully
  abolished. `PMID:16043373` is abstract-only in the cache and only confirms
  construction of a `met15` null mutant with the synthetic Cre-loxP system.
- `PMID:34201883` supports a peripheral extracellular-region localization from
  the hyphal secretome LC-MS/MS experiment, where "a total of 301 proteins were
  identified in both replicate batches with at least 2 peptides". This
  proteomic hit was kept as non-core and left out of the core cytosolic
  biosynthetic function.
- The newest relevant paper found was `PMID:42003610`, a 2026 study of the
  C. albicans Met32 sulfur-utilization regulon. It places `MET15` among the
  sulfur-starvation-induced sulfur-assimilation/methionine genes but does not
  change the activity review.
