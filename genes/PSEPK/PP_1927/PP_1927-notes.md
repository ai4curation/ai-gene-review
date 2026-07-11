# PP_1927 notes

2026-07-10: First-pass arsenic/copper metal-resistance stress-bucket curation.
PP_1927 encodes an ArsH-family NADPH-dependent FMN reductase in Pseudomonas putida KT2440. The product and domain evidence support FMN reductase chemistry in arsenical-resistance operon context; this first pass does not assign a narrower organoarsenical substrate or detoxification reaction beyond the supported FMN reductase activity.

Primary provenance:
- [file:PSEPK/PP_1927/PP_1927-goa.tsv "UniProtKB	Q88LK4	PP_1927	enables	GO:0052873	FMN reductase (NADPH) activity	molecular_function	ECO:0000256	IEA	GO_REF:0000117	ARBA:ARBA00088610	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	UniProt	NADPH-dependent FMN reductase ArsH	20260706"]
- [file:PSEPK/PP_1927/PP_1927-uniprot.txt "DE   RecName: Full=NADPH-dependent FMN reductase ArsH {ECO:0000256|ARBA:ARBA00073853};"]
- [file:PSEPK/PP_1927/PP_1927-uniprot.txt "DR   GO; GO:0052873; F:FMN reductase (NADPH) activity; IEA:UniProtKB-ARBA."]
- [file:PSEPK/PP_1927/PP_1927-uniprot.txt "DE   AltName: Full=Arsenical resistance operon protein ArsH {ECO:0000256|ARBA:ARBA00081288};"]
- [file:PSEPK/PP_1927/PP_1927-uniprot.txt "CC   -!- SUBUNIT: Homotetramer. {ECO:0000256|ARBA:ARBA00011881}."]
- [file:PSEPK/PP_1927/PP_1927-uniprot.txt "CC   -!- SIMILARITY: Belongs to the ArsH family."]

Decision: keep the assignment conservative. ArsH proteins are curated to FMN reductase activity; arsenate reductase candidates get broad oxidoreductase plus arsenic-response context because the fetched GOA has no exact MF rows; CopAB proteins are represented as copper-binding/homeostasis or broad oxidoreductase cell-envelope copper-resistance proteins.
