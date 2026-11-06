# cysK curation notes

## 2026-08-11 first-pass synthesis

- Q88E95 is the KT2440 CysK-family enzyme (IPR005859). Its exact record assigns
  O-acetyl-L-serine + hydrogen sulfide to L-cysteine + acetate and identifies
  pyridoxal 5'-phosphate as cofactor [UniProtKB:Q88E95,
  "Reaction=O-acetyl-L-serine + hydrogen sulfide = L-cysteine + acetate;"].
- GO:0004124 is therefore core; generic catalytic and transferase terms are
  retained only as non-core parents. Broad GO:0019344 remains correct, while
  live route-specific GO:0006535 is used for the authored core process.
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

## 2026-09-27 correction: GO:0006535 is retired

- The 2026-08-11 entry above says the live route-specific GO:0006535 is used for
  the authored core process. That was wrong: GO retired the term (obsolete no
  later than release 2026-03-25, replaced_by GO:0019344). A reviewed label alias
  in conf/oak_config.yaml and stale committed term caches had kept it
  validating. The NEW proposal is removed and the authored core process is
  GO:0019344; the O-acetylserine route is carried by the
  bacterial_cysteine_biosynthesis_via_o_acetylserine module. UniProt's
  `DR GO; GO:0006535` line is a stale cross-reference, not support for a new
  term (PR #3105).

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

All five original payloads, including the inherited PLP-binding NEW, preserved. Strengthened the specific synthase rationale with the target NCBIfam cysK model and RuleBase-backed reaction; S-313 extract activity is species-level and PAO1 assays are comparative. The genuine OpenScientist report and PDF/HTML artifacts are unchanged. Its conclusion asserting endogenous CSC formation and CDI toxin activation overreaches its evidence, and its reference review now explicitly flags that defect. The PAO1 negative CysE-peptide result argues against generic CSC assumptions but is not a direct negative experiment on Q88E95. No moonlighting or thiosulfate activity is transferred.

Existing genuine OpenScientist research and its artifacts were used as secondary evidence and preserved byte-for-byte.

Original GOA payloads, raw UniProt/GOA files and inherited authored proposals are preserved. Current GO checks distinguish the active cysteine synthase MF from obsolete route-specific BP terms GO:0006535 and GO:0019345. Focused gene and helper-history validations are recorded in the audit manifest.
