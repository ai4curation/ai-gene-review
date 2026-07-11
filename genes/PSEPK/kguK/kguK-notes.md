# kguK notes

- UniProt identifies `kguK` (Q88HH9) as the Pseudomonas putida KT2440 protein reviewed here. [file:PSEPK/kguK/kguK-uniprot.txt, "SubName: Full=2-ketogluconokinase {ECO:0000313|EMBL:AAN68982.1};"]
- Asta retrieval was run as the gene-level provider for this first pass; hits were treated as retrieval context, with mechanistic decisions anchored to UniProt/GOA unless direct organism-specific evidence was available. [file:PSEPK/kguK/kguK-deep-research-asta.md, "- **Protein Description:** SubName: Full=2-ketogluconokinase {ECO:0000313|EMBL:AAN68982.1}; EC=2.7.1.13 {ECO:0000313|EMBL:AAN68982.1};"]
- Curation interpretation: `kguK` is handled as a PPP-adjacent side node unless the exact enzyme reaction is one of the strict PPP steps in `modules/pentose_phosphate_pathway.yaml`.
