# rep notes

2026-07-10: First-pass replication-accessory/polymerase split curation.
rep encodes an ATP-dependent Rep/UvrD-subfamily DNA helicase. UniProt/HAMAP and GOA support a single-stranded DNA-dependent 3'-5' helicase acting in DNA replication, with recombinational repair retained as shared repair context.

Primary provenance:
- [file:PSEPK/rep/rep-goa.tsv "UniProtKB	Q88CB7	rep	enables	GO:0043138	3'-5' DNA helicase activity	molecular_function	ECO:0000501	IEA	GO_REF:0000120	EC:5.6.2.4|PANTHER:PTN002253357|UniRule:UR000161582	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	UniProt	ATP-dependent DNA helicase Rep	20260706"]
- [file:PSEPK/rep/rep-uniprot.txt "DE   RecName: Full=ATP-dependent DNA helicase Rep {ECO:0000256|HAMAP-Rule:MF_01920};"]
- [file:PSEPK/rep/rep-uniprot.txt "DR   GO; GO:0043138; F:3'-5' DNA helicase activity; IEA:UniProtKB-UniRule."]
- [file:PSEPK/rep/rep-uniprot.txt "CC   -!- FUNCTION: Rep helicase is a single-stranded DNA-dependent ATPase"]
- [file:PSEPK/rep/rep-uniprot.txt "CC   -!- CATALYTIC ACTIVITY:"]
- [file:PSEPK/rep/rep-uniprot.txt "DR   PANTHER; PTHR11070:SF64; ATP-DEPENDENT DNA HELICASE REP; 1."]
- [file:PSEPK/rep/rep-uniprot.txt "DR   Pfam; PF00580; UvrD-helicase; 1."]
- [file:PSEPK/rep/rep-uniprot.txt "KW   ATP-binding {ECO:0000256|ARBA:ARBA00022840, ECO:0000256|HAMAP-"]
- [file:PSEPK/rep/rep-uniprot.txt "FT   DOMAIN          2..280"]
- [file:PSEPK/rep/rep-uniprot.txt "DR   InterPro; IPR013986; DExx_box_DNA_helicase_dom_sf."]

Decision: route as replication accessory/polymerase boundary context; do not over-promote weak product names.
