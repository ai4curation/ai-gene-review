# secE research notes

## Functional assignment

SecE is the essential clamp subunit of SecYEG. UniProt describes it as an
essential subunit of the SecYEG translocation channel
[file:PSEPK/secE/secE-uniprot.txt "Essential subunit of the Sec protein
translocation channel SecYEG."]. It contributes to the assembled channel's
protein transmembrane transporter activity but does not independently enable
that activity.

Purified bacterial holo-translocon work places SecYEG together with SecDF-YajC
and YidC [PMID:24550475 "Together, they form the holo-translocon (HTL), which we
have successfully overexpressed and purified."].

## Annotation-reviewer pass (2026-09-01)

Reviewed all 8 GOA-derived rows and the proposed complex-membership annotation
against the local UniProt record, SecYEG literature, and the module-aware
OpenScientist report. Outcome: 3 ACCEPT, 2 KEEP_AS_NON_CORE,
3 MARK_AS_OVER_ANNOTATED, and 1 NEW; no row remains PENDING or UNDECIDED. The
existing `enables` channel-function row remains over-annotated because SecE is a
clamp subunit that contributes to the assembled SecYEG transporter.
