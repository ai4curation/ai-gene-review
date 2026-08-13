# cysK curation notes

## 2026-08-11 first-pass synthesis

- Q88E95 is the KT2440 CysK-family enzyme (IPR005859). Its exact record assigns
  O-acetyl-L-serine + hydrogen sulfide to L-cysteine + acetate and identifies
  pyridoxal 5'-phosphate as cofactor [UniProtKB:Q88E95,
  "Reaction=O-acetyl-L-serine + hydrogen sulfide = L-cysteine + acetate;"].
- GO:0004124 is therefore core; generic catalytic and transferase terms are
  retained only as non-core parents. GO:0019344 is retained because the former
  route-specific GO:0006535 term is obsolete.
- P. putida S-313 cell extracts directly show pathway-level cysteine synthase
  activity, but the study predates KT2440 locus assignments
  [PMID:10482527, "substantial levels of O-acetylserine sulfhydrylase
  (cysteine synthase) activity."].
- P. aeruginosa genetics and biochemistry show that its CysK is the
  sulfide-oriented isoform and that single CysK or CysM loss is buffered by the
  other enzyme [PMID:41541697, "two genes does not lead to cysteine auxotrophy,
  which is reached only with the"]. This supports the family-level variant
  model but is not direct Q88E95 evidence.
- OpenScientist independently recovered the exact Q88E95 identity and the
  CysK/CysM paralog distinction, but found no direct experimental study of the
  KT2440 enzyme. Its extrapolations of cysteine synthase-complex formation,
  cytoplasmic localization, and CDI-toxin activation were not promoted to
  target-specific annotations.
