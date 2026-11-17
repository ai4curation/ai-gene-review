# Corynebacterium glutamicum leuA (P42455) curation notes

Provider deep research was not run for this gene. These notes record the
literature read for the review (cached abstracts under `publications/`).

- Cloning by complementation, leucine feedback inhibition (Ki 0.4 mM),
  attenuation-like leader, and leuA inactivation raising lysine yield
  [PMID:8117072 "The first enzyme of the pathway is inhibited by leucine (Ki = 0.4 mM)"].
- Feedback-resistant R529H/G532D variant used for leucine overproduction
  [PMID:24333966 "We identified a feedback-resistant IMPS variant, which carries two amino acid exchanges (R529H, G532D)."].
- Ortholog structure (M. tuberculosis LeuA): C-terminal regulatory domain is
  the leucine feedback site; active-site zinc [PMID:15159544]. UniProt's
  Mg2+ cofactor for P42455 is a HAMAP rule assignment, not measured.
- No GOA row records leucine binding or feedback regulation; a NEW L-leucine
  binding (GO:0070728) annotation was considered but not proposed because
  direct binding has not been measured for this protein (inhibition only).
  Recorded as a suggested question and experiment instead.
- Actions aligned with PSEPK leuA (GO:0003985 REMOVE) and yeast LEU4/LEU9 /
  S. pombe leu3 (GO:0003824 MODIFY to GO:0003852; GO:0046912 TOO_GENERAL).
