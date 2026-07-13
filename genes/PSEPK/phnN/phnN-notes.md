# phnN notes

- UniProt identifies `phnN` (Q88EJ3) as the Pseudomonas putida KT2440 protein reviewed here. [file:PSEPK/phnN/phnN-uniprot.txt, "RecName: Full=Ribose 1,5-bisphosphate phosphokinase PhnN {ECO:0000256|HAMAP-Rule:MF_00836};"]
- Asta retrieval was run as the gene-level provider for this first pass; hits were treated as retrieval context, with mechanistic decisions anchored to UniProt/GOA unless direct organism-specific evidence was available. [file:PSEPK/phnN/phnN-deep-research-asta.md, "- **Protein Description:** RecName: Full=Ribose 1,5-bisphosphate phosphokinase PhnN {ECO:0000256|HAMAP-Rule:MF_00836}; EC=2.7.4.23 {ECO:0000256|HAMAP-Rule:MF_00836}; AltName: Full=Ribose 1,5-bisphosphokinase {ECO:0000256|HAMAP-Rule:MF_00836};"]
- Curation interpretation: `phnN` is handled as a PPP-adjacent side node unless the exact enzyme reaction is one of the strict PPP steps in `modules/pentose_phosphate_pathway.yaml`.
