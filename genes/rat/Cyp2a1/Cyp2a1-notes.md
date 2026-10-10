# Cyp2a1 review notes

## Re-review 2026-10-04

- GOA refresh (commit a3cf70b6d): no new rows and no retired rows; WITH/FROM and qualifiers
  backfilled on the 17 existing rows. 0 PENDING.
- All 17 rows re-audited. No actions changed (ACCEPT 11, KEEP_AS_NON_CORE 2, MODIFY 2,
  MARK_AS_OVER_ANNOTATED 2). No protein-binding rows.
- Positive support added where ACCEPT rested on unrelated text: the three heme binding rows
  (IBA, IEA, ISO) and iron ion binding (IEA) previously quoted only the steroid
  7-alpha-hydroxylation FUNCTION line; they now also quote the UniProt COFACTOR line
  "Name=heme; Xref=ChEBI:CHEBI:30413" [UniProtKB:P11711].
- GO:0008395 steroid hydroxylase activity (IDA, PMID:3818621, abstract-only) gained an
  abstract quote: yeast-expressed P-450a cDNA gave microsomes containing "testosterone
  7 alpha-hydroxylase activity" [PMID:3818621].
- The two arachidonate epoxygenase IBA rows (GO:0008392, GO:0019373) stay
  MARK_AS_OVER_ANNOTATED; the argument is node placement (sole seed rat Cyp2b12, RGD:620088,
  at PTN002549507), which is the allowed way to challenge an IBA.
- The two PMID:12162851 rows keep their caveat that the paper is a molecular-modelling study
  ("a molecular modelling evaluation of CYP2A interactions", title) although coded IDA; the
  coumarin process is still accepted and oxidoreductase activity still MODIFY.
- Open questions are unchanged (see suggested_questions in the review).
