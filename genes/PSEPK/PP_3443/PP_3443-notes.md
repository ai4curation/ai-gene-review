# PP_3443 notes

- UniProt identifies `PP_3443` (Q88HB7) as the Pseudomonas putida KT2440 protein reviewed here. [file:PSEPK/PP_3443/PP_3443-uniprot.txt, "SubName: Full=Glyceraldehyde-3-phosphate dehydrogenase {ECO:0000313|EMBL:AAN69045.1};"]
- Asta retrieval was run as the gene-level provider for this first pass; hits were treated as retrieval context, with mechanistic decisions anchored to UniProt/GOA unless direct organism-specific evidence was available. [file:PSEPK/PP_3443/PP_3443-deep-research-asta.md, "- **Protein Description:** SubName: Full=Glyceraldehyde-3-phosphate dehydrogenase {ECO:0000313|EMBL:AAN69045.1}; EC=1.2.1.59 {ECO:0000313|EMBL:AAN69045.1};"]
- Curation interpretation: `PP_3443` is handled as a PPP-adjacent side node unless the exact enzyme reaction is one of the strict PPP steps in `modules/pentose_phosphate_pathway.yaml`.
