# adhB notes

- UniProt identifies `adhB` (Q88GU4) as the Pseudomonas putida KT2440 protein reviewed here. [file:PSEPK/adhB/adhB-uniprot.txt, "SubName: Full=Alcohol dehydrogenase cytochrome c subunit {ECO:0000313|EMBL:AAN69223.1};"]
- Asta retrieval was run as the gene-level provider for this first pass; hits were treated as retrieval context, with mechanistic decisions anchored to UniProt/GOA unless direct organism-specific evidence was available. [file:PSEPK/adhB/adhB-deep-research-asta.md, "- **Protein Description:** SubName: Full=Alcohol dehydrogenase cytochrome c subunit {ECO:0000313|EMBL:AAN69223.1};"]
- Curation interpretation: `adhB` is handled as a PPP-adjacent side node unless the exact enzyme reaction is one of the strict PPP steps in `modules/pentose_phosphate_pathway.yaml`.
