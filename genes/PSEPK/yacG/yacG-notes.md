# yacG notes

2026-07-10: First-pass DNA topology/topoisomerase sub-batch curation.
yacG (PP_0630) encodes DNA gyrase inhibitor YacG, a small zinc-binding protein in Pseudomonas putida KT2440. UniProt/HAMAP metadata supports a YacG-family protein that binds the GyrB C-terminal domain and inhibits DNA gyrase by preventing productive DNA interaction. In this first pass it is curated as a DNA-topology regulatory side node, not as a general transcription regulator.

Primary provenance:
- [file:PSEPK/yacG/yacG-goa.tsv "UniProtKB	Q88Q66	yacG	enables	GO:0008657	DNA topoisomerase type II (double strand cut, ATP-hydrolyzing) inhibitor activity	molecular_function	ECO:0000256	IEA	GO_REF:0000104	UniRule:UR000098286	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	UniProt	DNA gyrase inhibitor YacG	20260706"]
- [file:PSEPK/yacG/yacG-uniprot.txt "DE   RecName: Full=DNA gyrase inhibitor YacG {ECO:0000255|HAMAP-Rule:MF_00649};"]
- [file:PSEPK/yacG/yacG-uniprot.txt "DR   GO; GO:0008657; F:DNA topoisomerase type II (double strand cut, ATP-hydrolyzing) inhibitor activity; IEA:UniProtKB-UniRule."]
- [file:PSEPK/yacG/yacG-uniprot.txt "CC   -!- FUNCTION: Inhibits all the catalytic activities of DNA gyrase by"]
- [file:PSEPK/yacG/yacG-uniprot.txt "CC   -!- COFACTOR:"]
- [file:PSEPK/yacG/yacG-uniprot.txt "CC   -!- SUBUNIT: Interacts with GyrB. {ECO:0000255|HAMAP-Rule:MF_00649}."]
- [file:PSEPK/yacG/yacG-uniprot.txt "CC   -!- SIMILARITY: Belongs to the DNA gyrase inhibitor YacG family."]
- [file:PSEPK/yacG/yacG-uniprot.txt "DR   PANTHER; PTHR36150; DNA GYRASE INHIBITOR YACG; 1."]
- [file:PSEPK/yacG/yacG-uniprot.txt "DR   Pfam; PF03884; YacG; 1."]
- [file:PSEPK/yacG/yacG-uniprot.txt "DR   InterPro; IPR005584; DNA_gyrase_inhibitor_YacG."]
- Decision: curate as part of the DNA-topology/topoisomerase boundary module.
