# tatA-II evidence notes

## 2026-09-01 annotation-reviewer pass

Reviewed all seven GOA rows against the fetched UniProt/HAMAP record,
PMID:23530902, the existing OpenScientist gene report, and the reusable Tat
module. Tat-complex membership, plasma-membrane localization, and the
Tat-specific and parent transmembrane-transport processes plus TatA transporter
activity are retained. Broad protein transport is kept as non-core, while
generic membrane is marked as an over-annotation. PMID:23530902 supports
transport by both complete PSEPK Tat systems. No row remains PENDING or
UNDECIDED.

## 2026-11-10 harmonization pass

Re-reviewed alongside the newly reviewed E. coli tatA/tatB/tatC so that rows
sharing a term get the same action in every Tat subunit review. Changes from the
earlier pass: transporter-activity rows (GO:0008320, GO:0009977) are ACCEPT or
MODIFY to GO:0009977 for TatA, which performs translocation, and
MARK_AS_OVER_ANNOTATED with a WRONG_QUALIFIER source defect for the receptor
subunits TatB and TatC (the earlier pass mixed ACCEPT, KEEP_AS_NON_CORE and
MARK_AS_OVER_ANNOTATED across siblings); GO:0065002 and GO:0015031 are MODIFY to
GO:0043953; GO:0016020 is MODIFY to GO:0005886. TatB/TatC-family members get a
NEW ISS GO:0005048 signal sequence receptor activity row matching the E. coli
IDA proposal. No provider deep research was generated; the review uses the
UniProt/HAMAP record, PMID:23530902 for the KT2440 systems, and E. coli
literature for the conserved subunit roles.
