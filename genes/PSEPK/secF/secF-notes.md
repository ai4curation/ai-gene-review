# secF research notes

## Functional assignment

SecF partners with SecD in the membrane-integrated SecDF accessory motor. The
KT2440 UniProt record assigns the same PMF-dependent late-translocation mechanism
[file:PSEPK/secF/secF-uniprot.txt "SecDF uses the proton motive force (PMF) to
complete protein translocation after the ATP-dependent function of SecA."].

SecDF can complete translocation after ATP depletion inactivates SecA
[PMID:29718185 "SecDF can complete protein translocation even if SecA function is
inactivated by ATP depletion"]. This supports contributes_to GO:0009977 and
rejects the imported protein-transporting ATPase annotation.

## Annotation-reviewer pass (2026-09-01)

Reviewed all 7 GOA-derived rows and the proposed complex-membership annotation
against the local UniProt record, SecDF literature, and the module-aware
OpenScientist report. Outcome: 3 ACCEPT, 1 KEEP_AS_NON_CORE,
2 MARK_AS_OVER_ANNOTATED, 1 MODIFY, and 1 NEW; no row remains PENDING or
UNDECIDED. The erroneous ATPase IEA remains refined to `contributes_to`
GO:0009977 rather than assigning independent catalytic activity to SecF.
