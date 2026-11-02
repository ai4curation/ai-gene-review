# ANKRD46 notes

- 228 aa: four N-terminal ANK repeats and one predicted C-terminal TM helix (190-210), i.e. a probable tail-anchored protein. PE1; low tissue specificity; Pharos Tbio. PAN-GO 0.
- GOA: one row, membrane (IEA, SubCell, ECO:0000305) → ACCEPT.
- **OpenCell** (cell line 1394, endogenous N-terminal tag, HEK293T): er_3 (Prominent), vesicles_1. Added NEW GO:0005783 endoplasmic reticulum (HDA, PMID:35271311), backed by ANKRD46-bioinformatics/opencell_localization.py. GO:0005783 is not a descendant of membrane (ancestors checked in OLS4), so it is not redundant.
- Interactions: IntAct 121 and BioGRID 138, mostly membrane-protein Y2H partners of isoform 2; none validated and none in GOA.
- Literature: ANKRD46 appears only as a miRNA target (miR-21, miR-451, miR-25-3p) and in marker studies. No function.
- **PAINT oddity:** the PTHR22677 PAINT slice contains only node PTN001193669, seeded by ANKRD45 (Q5TZF3), the same node that appears in the PTHR24201 slice. Current PANTHER places ANKRD45 in PTHR24201:SF15, so the node seems to be listed under two families. It does not reach ANKRD46.
- knowledge_gaps: MF_DARK (ER location known).
