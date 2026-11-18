# PP_5147 (Q88CN3) - Pseudomonas putida KT2440 curation notes

- New deep research could not be generated in this session (no provider API keys); the existing
  OpenScientist report was used as secondary triage. Its 67.7% identity claim was reproduced locally.
- 2026-11-10: resolved the UNDECIDED activity row with `PP_5147-bioinformatics/holpase_orthology.py`
  (output `PP_5147-bioinformatics/RESULTS.md`; run from repo root with `--cache-dir <dir>`).
  - NCBIfam NF052360 (HolPasePseu, equivalog built on PMID:31862725, TC 280): PP_5147 is the only
    KT2440 member above TC; PA0335 is the only PAO1 member.
  - phmmer reciprocal best hits PA0335 <-> PP_5147; 0.677 identity over 217 columns; HAD Asp7, Asp9
    and Asp179 conserved.
- Added NEW GO:0000105 (ISS) because the GOA set has only the activity row.
- The OpenScientist recommendation to treat PP_5147 as "the principal" HolPase ignores PP_3157 (a
  TIGR02067 HisN member); not adopted. Both are retained as HolPases; in-vivo flux sharing unknown.
- 2026-11-18: added substrate-specificity evidence with
  `PP_5147-bioinformatics/holpase_fingerprint.py` (output `FINGERPRINT.md`). The catalytic Asp
  residues above are HAD motif I and Mg2+ ligands, shared with phosphoserine phosphatases, so they do
  not separate the two reactions. Kinateder et al. 2024 did, by alanine scanning PA0335
  [PMID:38284491 "Taken together, the residues D16 and D18 form a DxD motif, which is indicative for
  a HolPase, whereas an ExI motif indicates a PSPase."]; Y47 is the third required residue, and Y57
  and T113 support the call. PP_5147 carries all five. It is also below the noise cutoff of both
  SerB-type PSPase models (TIGR00338.1, NF008350.0), as PA0335 is, while M. jannaschii SerB shows the
  reverse. Neither PA0335 nor PP_5147 passes the second HolPase model NF052359.1, presumably another
  HolPase lineage.
