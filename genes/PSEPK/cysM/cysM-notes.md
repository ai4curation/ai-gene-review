# cysM curation notes

## 2026-08-11 first-pass synthesis

- Q88MC0 is the KT2440 CysM-family enzyme (IPR005858). Its exact record assigns
  the same sulfide-dependent GO:0004124 reaction as CysK and maps the PLP
  cofactor [UniProtKB:Q88MC0, "Reaction=O-acetyl-L-serine + hydrogen sulfide =
  L-cysteine + acetate;"].
- The core review does not infer thiosulfate specificity from the gene symbol.
  That chemistry is left as a hypothesis because P. aeruginosa CysM, not
  Q88MC0, has been shown to produce S-sulfocysteine
  [PMID:41541697, "OAS-dependent S-sulfocysteine synthase activity. Deletion of
  either one of the"].
- P. putida S-313 cell extracts directly show cysteine synthase activity but do
  not resolve the contribution of CysM versus CysK
  [PMID:10482527, "substantial levels of O-acetylserine sulfhydrylase
  (cysteine synthase) activity."].

## 2026-11-03 completion pass (cysteine biosynthesis module promotion)

- Generic parent rows (catalytic, transferase, O-acetyltransferase activity)
  moved from KEEP_AS_NON_CORE to TOO_GENERAL: the review's own accepted
  reaction-specific MF entails them, so keeping them as "non-core" misdescribed
  the judgement. Actions now match the sibling E. coli and P. aeruginosa
  reviews written for the same module.
- No provider deep-research run was possible in this session (no provider API
  keys); the review rests on the UniProt record, PAINT data for the PANTHER
  family, and the cached Pseudomonas literature already cited.
- Status set to COMPLETE.
