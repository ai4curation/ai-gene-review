# yaiW notes

2026-07-10: First-pass named lipoprotein-family curation.
yaiW (PP_3805) encodes a DUF1615 lipoprotein annotated as required for swarming in Pseudomonas putida KT2440. The current metadata supports a membrane lipoprotein and swarming-associated candidate, but does not establish the molecular mechanism or a GO biological-process annotation for motility.

Primary provenance: UniProt product/domain/keyword evidence [file:PSEPK/yaiW/yaiW-uniprot.txt "DE   SubName: Full=Lipoprotein required for swarming {ECO:0000313|EMBL:AAN69399.1};"; file:PSEPK/yaiW/yaiW-uniprot.txt "DR   InterPro; IPR011673; DUF1615."; file:PSEPK/yaiW/yaiW-uniprot.txt "KW   Lipoprotein {ECO:0000313|EMBL:AAN69399.1};"]. Asta retrieval mainly confirmed the same metadata-level identity [file:PSEPK/yaiW/yaiW-deep-research-asta.md "- **Protein Description:** SubName: Full=Lipoprotein required for swarming {ECO:0000313|EMBL:AAN69399.1};"].

Decision: DUF1615 membrane lipoprotein candidate associated by product name with swarming.

Localization caution: this pass adds only broad membrane context, not a cell-outer-membrane annotation, because the local evidence is lipoprotein metadata without a direct subcellular-location line.
