# tatA (E. coli K-12) curation notes

## 2026-11-10

Reviewed as the E. coli reference member for the bacterial twin-arginine
translocation module and the PANTHER family review. No provider deep-research
file was generated for this gene; the review rests on the UniProt record, the
cached GOA publications (mostly abstract-only; PMID:29358647, PMID:20169075 and
PMID:26068441 have full text), and the PAINT IBD rows for the family.

Decisions applied consistently across all nine Tat subunit reviews (E. coli
tatA/tatB/tatC and the six P. putida KT2440 paralogs):

- Reconstitution needs TatABC plus membrane potential and no ATP
  [PMID:11350936 "requires TatABC, an intact membrane potential and the
  twin-arginine targeting motif"]. No subunit transports substrate alone, so
  for TatA, TatB and TatC alike the GO:0009977/GO:0008320 rows with 'enables'
  are MARK_AS_OVER_ANNOTATED with a WRONG_QUALIFIER source defect (should be
  contributes_to), as in the September 2026 TreeGrafter re-review of tatC-I;
  core functions record contributes_to.
- GO:0015031 MODIFY to GO:0043953; GO:0065002 MODIFY to GO:0043953 (lateral, matching
  the Sec subunit precedent GO:0065002 -> GO:0043952); GO:0016020 MODIFY to
  GO:0005886.
- Bare GO:0005515 REMOVE (policy); homo-oligomer and lipid-binding rows
  KEEP_AS_NON_CORE.
- TatB and TatC get a NEW GO:0005048 signal sequence receptor activity row
  [PMID:17212781 "This binding required the SufI signal peptide."]; the
  comparator SecY carries the same term.
- The IDA cytosol row (PMID:18644791) comes from tatABC overexpression ("only
  a 15-fold overexpression"), so it is MARK_AS_OVER_ANNOTATED.

## 2026-11-11 review follow-up (PR #6246)

The first pass accepted TatA 'enables GO:0009977' while the core function used
contributes_to. Resolved toward contributes_to: reconstituted transport needs
TatA, TatB and TatC together [PMID:11350936], and the TatA mechanism is still
hedged in the sources [UniProt "TatA could form the protein-conducting channel
of the Tat system."; PMID:16027357 "strongly supports the proposal"]. The
TatA 'enables' transporter rows are now MARK_AS_OVER_ANNOTATED with a
WRONG_QUALIFIER source defect, like TatB/TatC, and the subunit's own activity
is a proposed term, "Tat translocon conduit assembly activity" (parent
GO:0140318). Deep research was not generated for this gene (no provider run).
