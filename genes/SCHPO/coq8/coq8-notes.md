# coq8 / abc1 (Q92338, SPBC2D10.18) review notes

## Sources

No deep-research provider output is available (no provider API keys in this
environment). The review rests on the UniProt record and the cached literature;
PMID:24911838, PMID:27499294 and PMID:38425362 were read in full.

## Literature

- No UQ-10 in the mutant [PMID:14695938 "We show here that the abc1Sp defective strain
  did not produce UQ-10 and could not grow on minimal medium."]
- Cross-species rescue [PMID:8668131 "Inactivation of the abc1Sp gene by homologous gene
  replacement causes a respiratory deficiency which is efficiently rescued by the
  expression of the S. cerevisiae ABC1 gene."] and [PMID:24911838 "Similarly, CoQ10
  production by the S. pombe Δcoq8 strain was fully recovered by expression of S. pombe
  coq8 but only moderately recovered by expression of HsCOQ8/ADCK3 (Figure 7C)."]
- Ortholog ATPase [PMID:27499294 "WT Coq8NΔ41 has ATPase activity and an A197G mutation,
  which enhances MgATP binding in vitro, increased the ATPase activity (Figures 4A and
  S4A–S4C)."]
- HDA provenance question [PMID:24911838 "These results are consistent with those of a
  previous study [44] that examined the localization of 4,431 S. pombe proteins, although
  Coq8 was not included."]

## Audit decisions (2026-11)

- Added NEW GO:0016887 ATP hydrolysis activity (ISS from S. cerevisiae Coq8,
  PMID:27499294) so the core function matches the module's Coq8 annoton and the yeast
  and human COQ8B reviews.
- GO:0004672 protein kinase TAS kept MARK_AS_OVER_ANNOTATED.
- HDA mitochondrion accepted on the location, with a suggested question on provenance.
