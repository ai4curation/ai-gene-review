# trxB notes

- UniProt identifies `trxB` (Q88PR2) as the Pseudomonas putida KT2440 protein reviewed here. [file:PSEPK/trxB/trxB-uniprot.txt, "RecName: Full=Thioredoxin reductase {ECO:0000256|RuleBase:RU003880};"]
- Asta retrieval was run as the gene-level provider for this first pass; hits were treated as retrieval context, with mechanistic decisions anchored to UniProt/GOA unless direct organism-specific evidence was available. [file:PSEPK/trxB/trxB-deep-research-asta.md, "- **Protein Description:** RecName: Full=Thioredoxin reductase {ECO:0000256|RuleBase:RU003880}; EC=1.8.1.9 {ECO:0000256|RuleBase:RU003880};"]
- Curation interpretation: `trxB` is handled as a PPP-adjacent side node unless the exact enzyme reaction is one of the strict PPP steps in `modules/pentose_phosphate_pathway.yaml`.
