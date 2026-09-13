# secG research notes

## Functional assignment

SecG is the small accessory subunit of SecYEG. The local record says that it
participates in an early event of protein translocation
[file:PSEPK/secG/secG-uniprot.txt "Involved in protein export. Participates in an
early event of protein translocation."]. It contributes to GO:0008320 at the
assembled-channel level and is not an ATPase.

SecYEG is the bacterial protein-conducting core that associates with SecDF-YajC
in the purified holo-translocon [PMID:24550475 "The bacterial version SecYEG
interacts with the highly conserved YidC and SecDF-YajC subcomplex, which
facilitates translocation into and across the membrane."].

## Annotation-reviewer pass (2026-09-01)

Reviewed all 6 GOA-derived rows and the proposed complex-membership annotation
against the local UniProt record, SecYEG literature, and the module-aware
OpenScientist report. Outcome: 3 ACCEPT, 1 KEEP_AS_NON_CORE,
1 MARK_AS_OVER_ANNOTATED, 1 MODIFY, and 1 NEW; no row remains PENDING or
UNDECIDED. The ATPase IEA remains refined to `contributes_to` GO:0008320 because
SecG is an accessory channel subunit and SecA supplies ATP hydrolysis.
