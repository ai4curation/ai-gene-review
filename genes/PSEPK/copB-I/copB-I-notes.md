# copB-I notes

2026-07-10: First-pass arsenic/copper metal-resistance stress-bucket curation.
copB-I encodes an outer-membrane copper-resistance protein B in Pseudomonas putida KT2440. GOA and InterPro evidence support copper ion binding, cell outer membrane localization, and intracellular copper ion homeostasis context.

Primary provenance:
- [file:PSEPK/copB-I/copB-I-goa.tsv "UniProtKB	Q88KT5	copB-I	enables	GO:0005507	copper ion binding	molecular_function	ECO:0000256	IEA	GO_REF:0000002	InterPro:IPR007939	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	InterPro	Copper resistance protein B	20260706"]
- [file:PSEPK/copB-I/copB-I-uniprot.txt "DE   SubName: Full=Copper resistance protein B {ECO:0000313|EMBL:AAN67817.1};"]
- [file:PSEPK/copB-I/copB-I-uniprot.txt "DR   GO; GO:0005507; F:copper ion binding; IEA:InterPro."]
- [file:PSEPK/copB-I/copB-I-uniprot.txt "DR   InterPro; IPR007939; Cu-R_B_prcur."]
- [file:PSEPK/copB-I/copB-I-uniprot.txt "DR   Pfam; PF05275; CopB; 1."]
- [file:PSEPK/copB-I/copB-I-uniprot.txt "FT   SIGNAL          1..26"]

Decision: keep the assignment conservative. ArsH proteins are curated to FMN reductase activity; arsenate reductase candidates get broad oxidoreductase plus arsenic-response context because the fetched GOA has no exact MF rows; CopAB proteins are represented as copper-binding/homeostasis or broad oxidoreductase cell-envelope copper-resistance proteins.
