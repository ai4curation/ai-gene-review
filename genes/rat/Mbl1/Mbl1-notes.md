# Mbl1 (rat) review notes

## Session 1 (create review)

- Fetched with `just fetch-gene rat Mbl1`; UniProt P19999 (MBL1_RAT, MBP-A) confirmed. 29 GOA rows.
- PMID:25419660 initially failed with HTTP 429; re-fetched successfully (full text, PMC4242627).
- PMID:20118239 and PMID:22167201 cached with full text and read.
- Abstract only: PMID:10903744, 10913141, 11850428, 16272342, 3584121, 9315725.
  Tried JBC site for PMID:10913141 full text: HTTP 403.
- Added references: PMID:1436090, PMID:7704532, PMID:3009480 (structures / sequence),
  PMID:15148336 (mouse Mbl1/Mbl2 double-null, the likely basis of RGD ISO rows from MGI:96923).

### Decisions

- Core: Ca2+-dependent carbohydrate (mannose/GlcNAc, high-mannose glycan) recognition and
  MASP binding, which together initiate the lectin complement pathway
  [PMID:3584121 "the activation is initiated by the sugar binding activity of MBP"].
- Extracellular region rows (6): MODIFY to extracellular space (GO:0005615); MBP-A is a
  serum protein [PMID:3584121 "Serum mannan-binding protein (MBP)"].
- GO:0042803 protein homodimerization (IPI, PMID:10913141, with P19999): the abstract reports
  that the truncated MASPs are homodimers; MBP-A itself is a homotrimer. Cannot see full text,
  so UNDECIDED rather than REMOVE.
- IBA multivesicular body: MARK_AS_OVER_ANNOTATED; IBA surfactant homeostasis: REMOVE
  (surfactant-collectin biology; MBP-A is not a lung surfactant protein). Same decisions as
  human MBL2 review.
- No NEW rows. Pattern-recognition receptor activity would be reasonable MF but I did not add it;
  the existing carbohydrate-binding and protease-binding MF terms already capture the activity.
- Phagocytosis / anti-S. aureus ISO rows rest on mouse Mbl1/Mbl2 double knockout
  (PMID:15148336), which does not separate MBL-A from MBL-C: KEEP_AS_NON_CORE.
