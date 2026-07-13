# PP_3236 notes

2026-07-10: First-pass named lipoprotein-family curation.
PP_3236 encodes an OprI-named lipoprotein paralog in Pseudomonas putida KT2440. Because the fetched GOA file has no annotations and UniProt lacks domain signatures beyond lipoprotein/coiled-coil metadata, this pass records only conservative membrane lipoprotein context.

Primary provenance: UniProt product/domain/keyword evidence [file:PSEPK/PP_3236/PP_3236-uniprot.txt "DE   SubName: Full=Lipoprotein OprI {ECO:0000313|EMBL:AAN68843.1};"; file:PSEPK/PP_3236/PP_3236-uniprot.txt "KW   Lipoprotein {ECO:0000313|EMBL:AAN68843.1};"; file:PSEPK/PP_3236/PP_3236-uniprot.txt "KW   Signal {ECO:0000256|SAM:SignalP}."]. Asta retrieval mainly confirmed the same metadata-level identity [file:PSEPK/PP_3236/PP_3236-deep-research-asta.md "- **Protein Description:** SubName: Full=Lipoprotein OprI {ECO:0000313|EMBL:AAN68843.1};"].

Decision: OprI-named membrane lipoprotein paralog with unresolved localization specificity and function.

Localization caution: this pass adds only broad membrane context, not a cell-outer-membrane annotation, because the local evidence is lipoprotein metadata without a direct subcellular-location line.
