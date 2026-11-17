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


## Comparative cysteine-route audit (2026-11-06)

All five original payloads, including the inherited PLP-binding NEW, preserved. The specific cysM NCBIfam model and RuleBase-backed sulfide reaction support OAS-dependent cysteine synthesis. PMID10482527 measures P.putida S-313 extracts without distinguishing this KT2440 locus. PAO1 CysM thiosulfate preference is useful comparative evidence, but direct S-sulfocysteine synthesis and native substrate preference remain unresolved for Q88MC0; no additional activity is asserted.

Default Falcon research was attempted normally with --provider falcon and failed with HTTP403. No provider report was fabricated; this section records manual review.

Original GOA payloads, raw UniProt/GOA files and inherited authored proposals are preserved. Current GO checks distinguish the active cysteine synthase MF from obsolete route-specific BP terms GO:0006535 and GO:0019345. Focused gene and helper-history validations are recorded in the audit manifest.
