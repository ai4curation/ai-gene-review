# tatB-I evidence notes

## 2026-08-11

This DRAFT first pass uses the exact KT2440 UniProt and GOA records plus
conserved TatB topology and family evidence. No direct KT2440 TatB-I experiment
was consulted; substrate specificity relative to the second Tat locus remains
an explicit question.

## 2026-09-01 annotation-reviewer pass

Reviewed all five GOA rows against the fetched UniProt record, TatB-specific
InterPro assignment, locus context, and reusable Tat module. Tat-complex
membership and the Tat-specific process are retained; the isolated-subunit
transporter MF and broad protein-transport parent are kept as correct non-core
annotations. The generic membrane row is retained as MODIFY to the
bacterial plasma membrane. No row remains PENDING or UNDECIDED.

## 2026-11-10 harmonization pass

Re-reviewed alongside the newly reviewed E. coli tatA/tatB/tatC so that rows
sharing a term get the same action in every Tat subunit review. Changes from the
earlier pass: transporter-activity rows (GO:0008320, GO:0009977) are
MARK_AS_OVER_ANNOTATED with a WRONG_QUALIFIER source defect for all three
subunits, because the activity belongs to the assembled TatABC complex (the earlier pass mixed ACCEPT, KEEP_AS_NON_CORE and
MARK_AS_OVER_ANNOTATED across siblings); GO:0065002 and GO:0015031 are MODIFY to
GO:0043953; GO:0016020 is MODIFY to GO:0005886. TatB/TatC-family members get a
NEW ISS GO:0005048 signal sequence receptor activity row matching the E. coli
IDA proposal. No provider deep research was generated; the review uses the
UniProt/HAMAP record, PMID:23530902 for the KT2440 systems, and E. coli
literature for the conserved subunit roles.
