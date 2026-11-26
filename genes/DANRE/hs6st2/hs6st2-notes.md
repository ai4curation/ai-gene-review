# Notes for DANRE hs6st2

## 2026-05-09 review notes

- Core function is heparan sulfate 6-O-sulfotransferase activity in heparan sulfate proteoglycan biosynthesis [PMID:12782624 "the protein shows specific 6-O-sulfotransferase activity"].
- The generic sulfotransferase annotation was modified to GO:0017095 because the substrate and sulfate position are known [file:DANRE/hs6st2/hs6st2-uniprot.txt "N-sulfoglucosamine residue (GlcNS) of heparan sulfate"].
- Eye and vascular morphogenesis annotations are retained as non-core developmental consequences [PMID:16009360 "HS6ST-2 is required for the branching morphogenesis"].
- Golgi membrane (GO:0000139) is recorded as a curation question rather than a NEW annotation because the zebrafish source file only states membrane [file:DANRE/hs6st2/hs6st2-uniprot.txt "SUBCELLULAR LOCATION: Membrane"].

## Re-review 2026-09-29
- Resolved the two PENDING GOA rows (GO:0008146 IEA GO_REF:0000002 -> MODIFY to GO:0017095; GO:0017095 IEA GO_REF:0000120 -> ACCEPT).
- Removed two stale rows whose GO_REFs no longer match the refreshed GOA (GO:0008146 IEA GO_REF:0000120 and GO:0017095 IEA GO_REF:0000116); their content is preserved by the current GO_REF:0000002 / GO_REF:0000120 rows.
- Confirmed core function heparan sulfate 6-O-sulfotransferase activity [file:...uniprot.txt "6-O-sulfation enzyme which catalyzes the transfer of sulfate"; PMID:12782624 "the protein shows specific 6-O-sulfotransferase activity"]. Broad GO:0008146 kept as MODIFY -> GO:0017095.
- Developmental IMP rows (GO:0048048 eye morphogenesis, GO:0001569 blood-vessel branching) kept KEEP_AS_NON_CORE: these are downstream consequences of altered HS 6-O-sulfation of the matrix, not work the enzyme performs in morphogenesis [PMID:16009360 "HS6ST-2 is required for the branching morphogenesis"; PMID:17937808 "Hyaloid vasculature with scarce andoversized branches"].
- Added reference_review (VERIFIED) to PMID:12782624, PMID:16009360, PMID:17937808. Validation: 0 errors.
