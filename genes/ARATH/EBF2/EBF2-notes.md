# EBF2 (At5g25350, Q708Y0) curation notes

## 2026-10-06 session (ethylene_signaling module)

- Identity confirmed: EBF2_ARATH, Q708Y0, At5g25350; LRR F-box paralog of EBF1.
- No deep research file (falcon provider failing this session); review based on cached literature and UniProt.
- SCF/EIN3: [PMID:15090654 "EBF1 and -2 interact directly with ethylene insensitive 3 (EIN3)"]; [PMID:14675532 "In the absence of ethylene, EIN3 is quickly degraded through a ubiquitin/proteasome pathway mediated by two F box proteins, EBF1 and EBF2."]
- Targets: [PMID:17307926 "we show that EIN3 and EIL1 are the main targets of EBF1/2"]; temporal role [PMID:17307926 "EBF2 plays a more prominent role during the latter stages of the response and the resumption of growth following ethylene removal"].
- Feedback: [PMID:18466304 "EIN3 can bind and activate the EBF2 promoter, indicating that EIN3 modulates EBF2 gene expression in planta"].
- Translational control of EBF2 via its 3' UTR by EIN2/UPFs [PMID:26496608]; EIN2 represses EBF1/2 translation [PMID:26496607].
- Decisions: EIN3/EIL1/ASK2 protein binding -> MODIFY to GO:1990756; SRK2A (At1g10940/P43291) rows -> REMOVE with a flag that "ASK1" (SKP1A, At1g75950) was probably intended; SCF complex IPI with At1g10940 in WITH -> ACCEPT term, WITH identifier doubtful; AtSubP chloroplast -> REMOVE; NEW GO:1990756.
