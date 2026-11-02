# hsd11b2 (Danio rerio) review notes

hsd11b2 encodes 11-beta-hydroxysteroid dehydrogenase type 2, an NAD(+)-dependent membrane SDR that oxidizes cortisol to inactive cortisone.

## Re-review 2026-09-29
- Completed a partially-edited review (prior run left rows for GO:0070523 IDA, GO:0034650 IDA templated and GO:0033555 IMP as PENDING).
- Rewrote GO:0070523 IDA (PMID:33387577) and GO:0034650 IDA (PMID:23042946) with specific evidence; both ACCEPT. Core activity: NAD(+)-dependent cortisol->cortisone oxidation [file:...uniprot.txt "Reaction=cortisol + NAD(+) = cortisone + NADH + H(+);"; PMID:33387577 "11beta-hydroxysteroid dehydrogenase 2 (11beta-HSD2) converts active"].
- Resolved PENDING GO:0033555 (multicellular organismal response to stress) IMP PMID:34830405 as KEEP_AS_NON_CORE, consistent with the GO:0033555 IDA row: the prolonged cortisol stress response in hsd11b2 knockouts is a downstream organismal phenotype, not participatory work [PMID:34830405 "a higher magnitude in the stress response at 10 min post stress"].
- Retained prior sound decisions: GO:0047022 7-beta-HSD (NADP+) ISS REMOVE (wrong reaction chemistry/cofactor, mis-transferred from a bacterial 7-HSD); GO:0070524 11-beta-HSD (NADP+) ISS MODIFY -> GO:0070523 (type-2 cofactor is NAD+, not NADP+).
- Added reference_review (VERIFIED) to all 5 PMIDs. Validation: 0 errors, 0 warnings.
