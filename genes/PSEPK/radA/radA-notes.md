# radA notes

2026-07-10: First-pass repair-helicase/recombination split curation.
radA encodes a RadA-family DNA repair protein in Pseudomonas putida KT2440. HAMAP, NCBIfam, InterPro, and GOA support an ATP-dependent DNA damage sensor/branched-DNA-processing protein involved in recombinational repair, with damaged-DNA binding and cytosolic context.

Primary provenance:
- [file:PSEPK/radA/radA-goa.tsv "UniProtKB	Q88E24	radA	enables	GO:0140664	ATP-dependent DNA damage sensor activity	molecular_function	ECO:0000256	IEA	GO_REF:0000002	InterPro:IPR020588	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	InterPro	DNA repair protein RadA	20260706"]
- [file:PSEPK/radA/radA-uniprot.txt "DE   RecName: Full=DNA repair protein RadA {ECO:0000256|HAMAP-Rule:MF_01498, ECO:0000256|NCBIfam:TIGR00416};"]
- [file:PSEPK/radA/radA-uniprot.txt "DR   GO; GO:0140664; F:ATP-dependent DNA damage sensor activity; IEA:InterPro."]
- [file:PSEPK/radA/radA-uniprot.txt "CC   -!- FUNCTION: DNA-dependent ATPase involved in processing of recombination"]
- [file:PSEPK/radA/radA-uniprot.txt "CC   -!- SIMILARITY: Belongs to the RecA family. RadA subfamily."]
- [file:PSEPK/radA/radA-uniprot.txt "DR   PANTHER; PTHR32472; DNA REPAIR PROTEIN RADA; 1."]
- [file:PSEPK/radA/radA-uniprot.txt "DR   Pfam; PF13481; AAA_25; 1."]
- [file:PSEPK/radA/radA-uniprot.txt "KW   ATP-binding {ECO:0000256|ARBA:ARBA00022840, ECO:0000256|HAMAP-"]
- [file:PSEPK/radA/radA-uniprot.txt "FT   DOMAIN          70..218"]
- [file:PSEPK/radA/radA-uniprot.txt "DR   InterPro; IPR003593; AAA+_ATPase."]

Decision: curate conservatively inside the repair-helicase/recombination boundary; do not promote ProtNLM-only names to GO functions.
