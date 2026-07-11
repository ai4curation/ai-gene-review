# gnuK notes

- UniProt identifies `gnuK` (Q88HE4) as the Pseudomonas putida KT2440 protein reviewed here. [file:PSEPK/gnuK/gnuK-uniprot.txt, "RecName: Full=Gluconokinase {ECO:0000256|ARBA:ARBA00012054, ECO:0000256|RuleBase:RU363066};"]
- Asta retrieval was run as the gene-level provider for this first pass; hits were treated as retrieval context, with mechanistic decisions anchored to UniProt/GOA unless direct organism-specific evidence was available. [file:PSEPK/gnuK/gnuK-deep-research-asta.md, "- **Protein Description:** RecName: Full=Gluconokinase {ECO:0000256|ARBA:ARBA00012054, ECO:0000256|RuleBase:RU363066}; EC=2.7.1.12 {ECO:0000256|ARBA:ARBA00012054, ECO:0000256|RuleBase:RU363066};"]
- Curation interpretation: `gnuK` is handled as a PPP-adjacent side node unless the exact enzyme reaction is one of the strict PPP steps in `modules/pentose_phosphate_pathway.yaml`.
