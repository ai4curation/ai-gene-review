# RETREG2 (FAM134A) — review notes

UniProt: Q8NC44. Gene: RETREG2 (synonym FAM134A). Human. Member of the FAM134/RETREG family (RETREG1/FAM134B, RETREG2/FAM134A, RETREG3/FAM134C).

## Domain architecture
- Multi-pass ER membrane protein: three transmembrane segments forming a reticulon-homology domain (RHD; InterPro IPR055257 RETR2_RHD; Pfam PF24456) that shapes/curves ER membranes.
- C-terminal LIR motif (MOTIF 490-495) that binds ATG8/LC3 family proteins.
[file:human/RETREG2/RETREG2-uniprot.txt FT TRANSMEM/MOTIF; DR CDD RETR2_RHD]

## Core function (synthesized)
RETREG2/FAM134A is an ER-anchored selective-autophagy (ER-phagy / reticulophagy) receptor. It exists in an inactive state under basal conditions and is activated upon cellular stress; when activated it induces ER fragmentation and delivers ER fragments into lysosomes by sequestration into autophagosomes via interaction with ATG8-family proteins (LC3/GABARAP) through its LIR motif. As an RHD-containing reticulon-family protein it also shapes ER membranes. It is required for collagen quality control (in a LIR-independent manner, by similarity).
[file:human/RETREG2/RETREG2-uniprot.txt "Endoplasmic reticulum (ER)-anchored autophagy regulator which exists in an inactive state under basal conditions but is activated following cellular stress (PubMed:34338405). When activated, induces ER fragmentation and mediates ER delivery into lysosomes through sequestration into autophagosomes via interaction with ATG8 family proteins"]
[PMID:34338405 "Role of FAM134 paralogues in endoplasmic reticulum remodeling, ER-phagy, and Collagen quality control"]
[PMID:26040720 "Regulation of endoplasmic reticulum turnover by selective autophagy" — foundational ER-phagy / FAM134 family paper]

## Interactions
- ATG8 family modifiers (MAP1LC3A/B, GABARAP family) via LIR motif.
[file:human/RETREG2/RETREG2-uniprot.txt "Interacts with ATG8 family modifier proteins MAP1LC3A..."]
- PMID:21900206 = directed protein interaction network (high-throughput); PMID:26040720 ER-phagy context.

## Localization
ER membrane (multi-pass). [file:human/RETREG2/RETREG2-uniprot.txt SUBCELLULAR LOCATION]

## Annotation judgments
- Core ACCEPT: ER membrane localization (GO:0005789 IEA and EXP), endoplasmic reticulum-autophagosome adaptor activity (GO:0140506 IEA — the ER-phagy receptor MF), substrate localization to autophagosome (GO:0061753 — ER delivery to autophagosome).
- KEEP_AS_NON_CORE: membrane (GO:0016020 IBA — generic parent of ER membrane); endoplasmic reticulum (GO:0005783 IEA — generic parent of ER membrane).
- protein binding (GO:0005515) — KEEP_AS_NON_CORE (uninformative bare; 21900206 high-throughput, 26040720 ER-phagy).
- All annotations are biologically consistent; nothing to REMOVE.
