# PP_3383 notes

- UniProt identifies `PP_3383` (Q88HH5) as the Pseudomonas putida KT2440 protein reviewed here. [file:PSEPK/PP_3383/PP_3383-uniprot.txt, "SubName: Full=Gluconate 2-dehydrogenase flavoprotein subunit {ECO:0000313|EMBL:AAN68987.1};"]
- Asta retrieval was run as the gene-level provider for this first pass; hits were treated as retrieval context, with mechanistic decisions anchored to UniProt/GOA unless direct organism-specific evidence was available. [file:PSEPK/PP_3383/PP_3383-deep-research-asta.md, "- **Protein Description:** SubName: Full=Gluconate 2-dehydrogenase flavoprotein subunit {ECO:0000313|EMBL:AAN68987.1}; EC=1.1.99.3 {ECO:0000313|EMBL:AAN68987.1};"]
- Curation interpretation: `PP_3383` is handled as a PPP-adjacent side node unless the exact enzyme reaction is one of the strict PPP steps in `modules/pentose_phosphate_pathway.yaml`.
