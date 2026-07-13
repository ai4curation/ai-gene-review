# dinG notes

2026-07-10: First-pass repair-helicase/recombination split curation.
dinG encodes a DinG/Rad3-like ATP-dependent DNA helicase in Pseudomonas putida KT2440. HAMAP/UniProt evidence supports DNA-dependent ATPase and 5'-to-3' DNA helicase activity on D-loops, R-loops, forked DNA, and G-quadruplex DNA, with an iron-sulfur cluster.

Primary provenance:
- [file:PSEPK/dinG/dinG-goa.tsv "UniProtKB	Q88NS9	dinG	enables	GO:0043139	5'-3' DNA helicase activity	molecular_function	ECO:0000501	IEA	GO_REF:0000120	EC:5.6.2.3|UniRule:UR000804393	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	UniProt	ATP-dependent DNA helicase DinG	20260706"]
- [file:PSEPK/dinG/dinG-uniprot.txt "DE   RecName: Full=ATP-dependent DNA helicase DinG {ECO:0000256|HAMAP-Rule:MF_02205};"]
- [file:PSEPK/dinG/dinG-uniprot.txt "DR   GO; GO:0043139; F:5'-3' DNA helicase activity; IEA:UniProtKB-UniRule."]
- [file:PSEPK/dinG/dinG-uniprot.txt "CC   -!- FUNCTION: DNA-dependent ATPase and 5'-3' DNA helicase. Unwinds D-loops,"]
- [file:PSEPK/dinG/dinG-uniprot.txt "CC   -!- CATALYTIC ACTIVITY:"]
- [file:PSEPK/dinG/dinG-uniprot.txt "CC   -!- COFACTOR:"]
- [file:PSEPK/dinG/dinG-uniprot.txt "CC   -!- SIMILARITY: Belongs to the helicase family. DinG subfamily. Type 1 sub-"]
- [file:PSEPK/dinG/dinG-uniprot.txt "DR   PANTHER; PTHR11472:SF59; ATP-DEPENDENT DNA HELICASE DING; 1."]
- [file:PSEPK/dinG/dinG-uniprot.txt "DR   Pfam; PF00270; DEAD; 1."]
- [file:PSEPK/dinG/dinG-uniprot.txt "KW   4Fe-4S {ECO:0000256|ARBA:ARBA00022485, ECO:0000256|HAMAP-Rule:MF_02205};"]

Decision: curate conservatively inside the repair-helicase/recombination boundary; do not promote ProtNLM-only names to GO functions.
