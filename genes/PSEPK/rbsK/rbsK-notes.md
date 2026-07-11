# rbsK notes

- UniProt identifies `rbsK` (Q88K34) as the Pseudomonas putida KT2440 protein reviewed here. [file:PSEPK/rbsK/rbsK-uniprot.txt, "RecName: Full=Ribokinase {ECO:0000256|ARBA:ARBA00016943, ECO:0000256|HAMAP-Rule:MF_01987};"]
- Asta retrieval was run as the gene-level provider for this first pass; hits were treated as retrieval context, with mechanistic decisions anchored to UniProt/GOA unless direct organism-specific evidence was available. [file:PSEPK/rbsK/rbsK-deep-research-asta.md, "- **Protein Description:** RecName: Full=Ribokinase {ECO:0000256|ARBA:ARBA00016943, ECO:0000256|HAMAP-Rule:MF_01987}; Short=RK {ECO:0000256|HAMAP-Rule:MF_01987}; EC=2.7.1.15 {ECO:0000256|ARBA:ARBA00012035, ECO:0000256|HAMAP-Rule:MF_01987};"]
- Curation interpretation: `rbsK` is handled as a PPP-adjacent side node unless the exact enzyme reaction is one of the strict PPP steps in `modules/pentose_phosphate_pathway.yaml`.
