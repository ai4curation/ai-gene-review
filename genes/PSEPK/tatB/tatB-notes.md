# tatB evidence notes

## 2026-08-11

This DRAFT first pass uses the exact KT2440 UniProt and GOA records plus
conserved TatB family evidence. PMID:23530902 provides organism-specific
evidence that both complete P. putida Tat systems can transport UxpB. Because
the paper reports at system level, the TatB-specific receptor role remains an
inference from family assignment and membership in the PP_5016-PP_5018 locus.

UniProt names PP_5017 `tatB`; that authoritative symbol is retained. The
provider-generated protein-export report's suggestion to relabel it `tatB-II`
is a non-authoritative consistency proposal and is not adopted.

## 2026-09-01 annotation-reviewer pass

Reviewed all six GOA rows against the fetched UniProt/HAMAP record,
PMID:23530902, and the reusable Tat module. Tat-complex membership,
plasma-membrane localization, and the Tat-specific process are retained. The
whole-transporter MF and generic protein-transport parent are kept as correct
non-core annotations, while generic membrane remains an over-annotation. The publication supports
transport by the complete second Tat system, not an isolated TatB activity. No
row remains PENDING or UNDECIDED.

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
