# YSR3 (LBP2; YKR053C, P23501) notes

## Identity and activity
- PAP2 family long-chain base 1-phosphate phosphatase, minor paralog of LCB3/YSR2 [UniProt:P23501].
- Deletion of YSR2/YSR3 accumulates DHS-1-P; ER localization [PMID:10477278 "deletion of YSR2, YSR3, or both, accumulated DHS-1-P"; "YSR2 and YSR3 had the same cellular localization to endoplasmic reticulum"].
- Lower expression than YSR2 [PMID:10477278 "YSR2 had significantly higher mRNA levels than YSR3"].
- lcb3 ysr3 mutants cannot recycle exogenous LCBs into ceramide [PMID:10856228 "We showed that mutants that are unable to dephosphorylate phosphorylated sphingoid bases were unable to incorporate exogenous DHS into ceramide"].

## Curation decisions
- Yeast lacks sphingosine (4E); "sphingosine-1-phosphate phosphatase" in yeast papers means LCB-1-P phosphatase. GO:0042392 annotations kept non-core; the IDA (PMID:10856228) modified to GO:0070780 (DHS-1-P). No GO term for PHS-1-P phosphatase.
- PMID:10531356 (human JBP1/PRMT5 paper) cited for ER IDA is apparently a mis-assigned reference; ER localization accepted on other evidence.
- RCA cytosol -> MODIFY to ER membrane. Core MF GO:0070780.
