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
