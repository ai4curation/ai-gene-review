# cdc-14 review notes

## Session 1 (2026-10-26)

- Fetched with `just fetch-gene worm cdc-14`; UniProt P81299 (CDC14_CAEEL), 44 GOA rows.
- No deep-research API keys; literature summary written by hand in
  `cdc-14-deep-research-manual.md`. Full text available for PMID:12213836 and
  PMID:21723944; PMID:15247923 and PMID:15282614 are abstract-only.
- Key judgement: the cytokinesis/central-spindle IMP rows (PMID:12213836, RNAi) are
  contradicted by null alleles he118/he141 (PMID:15247923, PMID:21723944)
  [PMID:21723944 "we find no evidence supporting a role for cdc-14 function during mitosis"].
  These IMP process rows are REMOVEd; the corresponding IBA rows inherited from
  yeast Cdc14/Clp1 (mitotic exit, cytokinesis, MT organisation) are marked
  over-annotated because the worm null shows the inherited mitotic role is not
  detectable.
- Localisation rows (spindle, midzone, midbody, centrosome, nucleolus) kept as
  non-core; nucleus and cytoplasm accepted because nucleocytoplasmic shuttling of
  CDC-14C is part of how its quiescence activity is regulated (PMID:21723944).
- Core function: CDC14-family phosphatase that maintains developmental G1
  quiescence upstream of CKI-1 and in parallel with LIN-35 (PMID:15247923,
  PMID:21723944).
- No NEW terms proposed. Substrate-level question (does CDC-14 directly
  dephosphorylate CKI-1?) recorded as a suggested question/experiment.
