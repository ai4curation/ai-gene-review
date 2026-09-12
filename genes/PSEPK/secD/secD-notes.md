# secD research notes

## Functional assignment

SecD is the large membrane subunit of the SecDF accessory motor. The KT2440
UniProt record states that SecDF uses proton motive force after the ATP-dependent
SecA step [file:PSEPK/secD/secD-uniprot.txt "SecDF uses the proton motive force
(PMF) to complete protein translocation after the ATP-dependent function of
SecA."].

Structural and biochemical work established an ATP-independent translocation
step requiring SecDF and PMF [PMID:21562494 "In vitro analyses identified an
ATP-independent step of protein translocation that requires both SecDF and
proton motive force."]. Thus SecD contributes to GO:0009977 at the assembled
SecDF level; it does not independently enable ATPase or transporter activity.

## Annotation-reviewer pass (2026-09-01)

Reviewed all 7 GOA-derived rows and the proposed complex-membership annotation
against the local UniProt record, SecDF literature, and the module-aware
OpenScientist report. Outcome: 3 ACCEPT, 1 KEEP_AS_NON_CORE,
2 MARK_AS_OVER_ANNOTATED, 1 MODIFY, and 1 NEW; no row remains PENDING or
UNDECIDED. The erroneous ATPase IEA remains refined to `contributes_to`
GO:0009977, preserving SecA as the ATP-driven motor.
