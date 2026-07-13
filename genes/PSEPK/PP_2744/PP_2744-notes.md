# PP_2744 notes

- UniProt identifies `PP_2744` (Q88JA5) as the Pseudomonas putida KT2440 protein reviewed here. [file:PSEPK/PP_2744/PP_2744-uniprot.txt, "RecName: Full=ribose-phosphate diphosphokinase {ECO:0000256|ARBA:ARBA00013247};"]
- Asta retrieval was run as the gene-level provider for this first pass; hits were treated as retrieval context, with mechanistic decisions anchored to UniProt/GOA unless direct organism-specific evidence was available. [file:PSEPK/PP_2744/PP_2744-deep-research-asta.md, "- **Protein Description:** RecName: Full=ribose-phosphate diphosphokinase {ECO:0000256|ARBA:ARBA00013247}; EC=2.7.6.1 {ECO:0000256|ARBA:ARBA00013247};"]
- Curation interpretation: `PP_2744` is handled as a PPP-adjacent side node unless the exact enzyme reaction is one of the strict PPP steps in `modules/pentose_phosphate_pathway.yaml`.
