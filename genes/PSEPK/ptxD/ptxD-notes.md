# ptxD notes

## 2026-07-06

First-pass PPP-adjacent review. UniProt identifies ptxD/Q88HI1 as phosphonate dehydrogenase EC 1.20.1.1 [file:PSEPK/ptxD/ptxD-uniprot.txt "DE   SubName: Full=Phosphonate dehydrogenase {ECO:0000313|EMBL:AAN68980.1};"] and GO maps the EC-derived activity to phosphonate dehydrogenase [file:PSEPK/ptxD/ptxD-uniprot.txt "DR   GO; GO:0050609; F:phosphonate dehydrogenase activity; IEA:UniProtKB-EC."]. I accepted that activity and cytosolic localization, kept NAD binding as non-core, and removed the TreeGrafter glyoxylate/hydroxypyruvate reductase calls as conflicting family-level activity propagation.

Asta was used as a target-identity check rather than a hypothesis source [file:PSEPK/ptxD/ptxD-deep-research-asta.md "- **Protein Description:** SubName: Full=Phosphonate dehydrogenase {ECO:0000313|EMBL:AAN68980.1}; EC=1.20.1.1 {ECO:0000313|EMBL:AAN68980.1};"]. A deeper literature pass could verify PtxD biochemistry directly if this gene becomes important.
