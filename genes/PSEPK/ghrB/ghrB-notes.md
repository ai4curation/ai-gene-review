# ghrB notes

- UniProt identifies `ghrB` (Q88NF1) as the Pseudomonas putida KT2440 protein reviewed here. [file:PSEPK/ghrB/ghrB-uniprot.txt, "SubName: Full=2-ketoaldonate reductase / hydroxypyruvate/glyoxylate reductase {ECO:0000313|EMBL:AAN66885.1};"]
- Asta retrieval was run as the gene-level provider for this first pass; hits were treated as retrieval context, with mechanistic decisions anchored to UniProt/GOA unless direct organism-specific evidence was available. [file:PSEPK/ghrB/ghrB-deep-research-asta.md, "- **Protein Description:** SubName: Full=2-ketoaldonate reductase / hydroxypyruvate/glyoxylate reductase {ECO:0000313|EMBL:AAN66885.1}; EC=1.1.1.215 {ECO:0000313|EMBL:AAN66885.1}; EC=1.1.1.79 {ECO:0000313|EMBL:AAN66885.1}; EC=1.1.1.81 {ECO:0000313|EMBL:AAN66885.1};"]
- Curation interpretation: `ghrB` is handled as a PPP-adjacent side node unless the exact enzyme reaction is one of the strict PPP steps in `modules/pentose_phosphate_pathway.yaml`.
