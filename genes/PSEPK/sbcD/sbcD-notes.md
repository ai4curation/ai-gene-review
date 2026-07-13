# sbcD notes

2026-07-10: First-pass repair-helicase/recombination split curation.
sbcD encodes the nuclease subunit of the SbcCD DNA-structure-processing complex in Pseudomonas putida KT2440. UniProt and GOA support endonuclease and 3'-to-5' exonuclease activities in DNA metabolic/recombination contexts.

Primary provenance:
- [file:PSEPK/sbcD/sbcD-goa.tsv "UniProtKB	Q88LB0	sbcD	enables	GO:0008408	3'-5' exonuclease activity	molecular_function	ECO:0000256	IEA	GO_REF:0000002	InterPro:IPR004593	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	InterPro	Nuclease SbcCD subunit D	20260706"]
- [file:PSEPK/sbcD/sbcD-uniprot.txt "DE   RecName: Full=Nuclease SbcCD subunit D {ECO:0000256|ARBA:ARBA00013365, ECO:0000256|RuleBase:RU363069};"]
- [file:PSEPK/sbcD/sbcD-uniprot.txt "DR   GO; GO:0008408; F:3'-5' exonuclease activity; IEA:InterPro."]
- [file:PSEPK/sbcD/sbcD-uniprot.txt "CC   -!- FUNCTION: SbcCD cleaves DNA hairpin structures. These structures can"]
- [file:PSEPK/sbcD/sbcD-uniprot.txt "CC   -!- SIMILARITY: Belongs to the SbcD family. {ECO:0000256|ARBA:ARBA00010555,"]
- [file:PSEPK/sbcD/sbcD-uniprot.txt "DR   PANTHER; PTHR30337; COMPONENT OF ATP-DEPENDENT DSDNA EXONUCLEASE; 1."]
- [file:PSEPK/sbcD/sbcD-uniprot.txt "DR   Pfam; PF00149; Metallophos; 1."]
- [file:PSEPK/sbcD/sbcD-uniprot.txt "KW   DNA recombination {ECO:0000256|RuleBase:RU363069};"]
- [file:PSEPK/sbcD/sbcD-uniprot.txt "FT   DOMAIN          1..232"]
- [file:PSEPK/sbcD/sbcD-uniprot.txt "DR   InterPro; IPR004843; Calcineurin-like_PHP."]

Decision: curate conservatively inside the repair-helicase/recombination boundary; do not promote ProtNLM-only names to GO functions.
