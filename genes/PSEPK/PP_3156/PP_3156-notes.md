# PP_3156 notes

2026-07-10: First-pass universal-stress-protein stress-bucket curation.
PP_3156 encodes a cytoplasmic tandem-domain Universal Stress Protein A-family protein in Pseudomonas putida KT2440. UniProt transfers a DNA-damaging-agent resistance comment by similarity, but this first pass treats that as context rather than a gene-specific GO process annotation.

Primary provenance:
- [file:PSEPK/PP_3156/PP_3156-goa.tsv "UniProtKB	Q88I45	PP_3156	located_in	GO:0005737	cytoplasm	cellular_component	ECO:0007322	IEA	GO_REF:0000044	UniProtKB-SubCell:SL-0086	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	UniProt	UspA domain-containing protein	20260706"]
- [file:PSEPK/PP_3156/PP_3156-uniprot.txt "DE   SubName: Full=Universal stress protein family {ECO:0000313|EMBL:AAN68764.1};"]
- [file:PSEPK/PP_3156/PP_3156-uniprot.txt "DR   GO; GO:0005737; C:cytoplasm; IEA:UniProtKB-SubCell."]
- [file:PSEPK/PP_3156/PP_3156-uniprot.txt "CC   -!- FUNCTION: Required for resistance to DNA-damaging agents."]
- [file:PSEPK/PP_3156/PP_3156-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000256|ARBA:ARBA00004496}."]
- [file:PSEPK/PP_3156/PP_3156-uniprot.txt "CC   -!- SIMILARITY: Belongs to the universal stress protein A family."]

Decision: keep the assignment conservative. The records support USP-family/domain context and, for most genes, cytoplasmic localization. They do not support a specific molecular function, substrate, ATP-binding claim, or stress-response GO process in this first pass.
