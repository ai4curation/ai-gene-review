# ppgL notes

- UniProt identifies `ppgL` (Q88LB4) as the Pseudomonas putida KT2440 protein reviewed here. [file:PSEPK/ppgL/ppgL-uniprot.txt, "SubName: Full=L-alpha-hydroxyglutaric acid gamma-lactonase {ECO:0000313|EMBL:AAN67635.1};"]
- Asta retrieval was run as the gene-level provider for this first pass; hits were treated as retrieval context, with mechanistic decisions anchored to UniProt/GOA unless direct organism-specific evidence was available. [file:PSEPK/ppgL/ppgL-deep-research-asta.md, "- **Protein Description:** SubName: Full=L-alpha-hydroxyglutaric acid gamma-lactonase {ECO:0000313|EMBL:AAN67635.1};"]
- Curation interpretation: `ppgL` is handled as a PPP-adjacent side node unless the exact enzyme reaction is one of the strict PPP steps in `modules/pentose_phosphate_pathway.yaml`.
