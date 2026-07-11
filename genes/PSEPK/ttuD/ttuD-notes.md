# ttuD notes

## 2026-07-06

First-pass PPP-adjacent review. UniProt identifies ttuD/Q88F00 as hydroxypyruvate reductase EC 1.1.1.81 [file:PSEPK/ttuD/ttuD-uniprot.txt "DE   SubName: Full=Hydroxypyruvate reductase {ECO:0000313|EMBL:AAN69880.1};"] and GO maps that EC to hydroxypyruvate reductase [file:PSEPK/ttuD/ttuD-uniprot.txt "DR   GO; GO:0016618; F:hydroxypyruvate reductase [NAD(P)H] activity; IEA:UniProtKB-EC."]. The same record also carries a glycerate kinase activity call from InterPro [file:PSEPK/ttuD/ttuD-uniprot.txt "DR   GO; GO:0008887; F:glycerate kinase activity; IEA:InterPro."].

I accepted the EC-derived reductase activity but left glycerate kinase as UNDECIDED rather than removing it, because the light Asta pass did not recover direct P. putida enzymology [file:PSEPK/ttuD/ttuD-deep-research-asta.md "- **Protein Description:** SubName: Full=Hydroxypyruvate reductase {ECO:0000313|EMBL:AAN69880.1}; EC=1.1.1.81 {ECO:0000313|EMBL:AAN69880.1};"].
