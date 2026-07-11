# copA-I notes

2026-07-10: First-pass arsenic/copper metal-resistance stress-bucket curation.
copA-I encodes a periplasmic copper-resistance protein A in Pseudomonas putida KT2440. The multicopper oxidase/CopA domain architecture and GOA support copper ion binding, broad oxidoreductase activity, and periplasmic localization; this first pass does not assign a narrower physiological copper-oxidation reaction.

Primary provenance:
- [file:PSEPK/copA-I/copA-I-goa.tsv "UniProtKB	Q88KT4	copA-I	enables	GO:0016491	oxidoreductase activity	molecular_function	ECO:0000501	IEA	GO_REF:0000120	InterPro:IPR011706|PANTHER:PTN002270456	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	UniProt	Copper resistance protein A	20260706"]
- [file:PSEPK/copA-I/copA-I-uniprot.txt "DE   SubName: Full=Copper resistance protein A {ECO:0000313|EMBL:AAN67818.1};"]
- [file:PSEPK/copA-I/copA-I-uniprot.txt "DR   GO; GO:0016491; F:oxidoreductase activity; IEA:UniProtKB-KW."]
- [file:PSEPK/copA-I/copA-I-uniprot.txt "DR   InterPro; IPR011707; Cu-oxidase-like_N."]
- [file:PSEPK/copA-I/copA-I-uniprot.txt "DR   Pfam; PF00394; Cu-oxidase; 1."]
- [file:PSEPK/copA-I/copA-I-deep-research-asta.md "  protein_description: 'SubName: Full=Copper resistance protein A {ECO:0000313|EMBL:AAN67818.1};'"]

Decision: keep the assignment conservative. ArsH proteins are curated to FMN reductase activity; arsenate reductase candidates get broad oxidoreductase plus arsenic-response context because the fetched GOA has no exact MF rows; CopAB proteins are represented as copper-binding/homeostasis or broad oxidoreductase cell-envelope copper-resistance proteins.
