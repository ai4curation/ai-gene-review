# PP_3691 notes

2026-07-10: First-pass repair-helicase/recombination split curation.
PP_3691 is a very large DNA2/NAM7-like helicase-related protein in Pseudomonas putida KT2440. The fetched GOA table supports only generic helicase activity, with additional DNA2/NAM7-like, AAA, and restriction-endonuclease-like domains but no resolved organism-specific repair step.

Primary provenance:
- [file:PSEPK/PP_3691/PP_3691-goa.tsv "UniProtKB	Q88GN0	PP_3691	enables	GO:0004386	helicase activity	molecular_function	ECO:0000256	IEA	GO_REF:0000002	InterPro:IPR041677	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	InterPro	DNA helicase-related protein	20260706"]
- [file:PSEPK/PP_3691/PP_3691-uniprot.txt "DE   SubName: Full=DNA helicase-related protein {ECO:0000313|EMBL:AAN69288.1};"]
- [file:PSEPK/PP_3691/PP_3691-uniprot.txt "DR   GO; GO:0004386; F:helicase activity; IEA:UniProtKB-KW."]
- [file:PSEPK/PP_3691/PP_3691-uniprot.txt "DR   PANTHER; PTHR10887; DNA2/NAM7 HELICASE FAMILY; 1."]
- [file:PSEPK/PP_3691/PP_3691-uniprot.txt "DR   Pfam; PF13086; AAA_11; 2."]
- [file:PSEPK/PP_3691/PP_3691-uniprot.txt "KW   ATP-binding {ECO:0000313|EMBL:AAN69288.1};"]
- [file:PSEPK/PP_3691/PP_3691-uniprot.txt "FT   DOMAIN          692..755"]
- [file:PSEPK/PP_3691/PP_3691-uniprot.txt "DR   InterPro; IPR045055; DNA2/NAM7-like."]
- [file:PSEPK/PP_3691/PP_3691-uniprot.txt "DR   InterPro; IPR041679; DNA2/NAM7-like_C."]
- [file:PSEPK/PP_3691/PP_3691-uniprot.txt "DR   InterPro; IPR041677; DNA2/NAM7_AAA_11."]

Decision: curate conservatively inside the repair-helicase/recombination boundary; do not promote ProtNLM-only names to GO functions.
