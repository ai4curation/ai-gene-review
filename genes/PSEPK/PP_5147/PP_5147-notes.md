# PP_5147 notes

## 2026-11-11: histidinol-phosphatase row moved from UNDECIDED to ACCEPT

The earlier UNDECIDED call rested on two gaps: no reproducible local orthology
analysis, and no evidence on substrate specificity, since HAD-family homologues of
PA0335 are often annotated as phosphoserine phosphatases.

Kinateder et al. 2024 closed the specificity question for this group
[PMID:38284491 "Taken together, the residues D16 and D18 form a DxD motif, which is
indicative for a HolPase, whereas an ExI motif indicates a PSPase."]. Their alanine
scan of PA0335 defined a fingerprint (D16, D18, Y47 required; Y57, T113 supporting),
and homologues carrying it were HolPases in vitro [PMID:38284491 "we conclude that
all sequences from cluster I that contain all three fingerprint residues are
HolPases"].

`PP_5147-bioinformatics/run_holpase_checks.py` (results in `RESULTS.md`) shows:

- PP_5147 is 67.7% identical to PA0335 over its full length and carries all five
  fingerprint residues. This reproduces the identity figure in the OpenScientist
  report.
- PP_5147 passes the NCBIfam histidinol-phosphatase model NF052360.1 (351.1 against
  a trusted cutoff of 280) and is below the noise cutoff of both SerB-type
  phosphoserine phosphatase models (TIGR00338.1, NF008350.0).
- PA0335 gives the same pattern; M. jannaschii SerB (Q58989), the paper's PSPase
  reference, gives the reverse.
- Neither PA0335 nor PP_5147 passes the second HolPase model, NF052359.1, which
  presumably covers another HolPase lineage.

No KT2440 assay exists, so the activity remains inferred. The open question is flux
division with the unrelated IMPase-like candidate PP_3157 (see suggested_questions).
L-histidine biosynthetic process is recorded in core_functions but not proposed as a
NEW annotation, because PP_5147's in vivo contribution relative to PP_3157 is
untested.
