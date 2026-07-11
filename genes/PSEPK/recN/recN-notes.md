# recN notes

2026-07-10: First-pass repair-helicase/recombination split curation.
recN encodes a RecN-family SMC-like DNA repair/recombination protein in Pseudomonas putida KT2440. UniProt/PANTHER evidence supports recombinational repair of damaged DNA and bacterial-nucleoid localization, while ATP binding is the only current molecular-function row.

Primary provenance:
- [file:PSEPK/recN/recN-goa.tsv "UniProtKB	Q88DU0	recN	involved_in	GO:0006310	DNA recombination	biological_process	ECO:0000256	IEA	GO_REF:0000002	InterPro:IPR004604	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	InterPro	DNA repair protein RecN	20260706"]
- [file:PSEPK/recN/recN-uniprot.txt "DE   RecName: Full=DNA repair protein RecN {ECO:0000256|ARBA:ARBA00021315, ECO:0000256|PIRNR:PIRNR003128};"]
- [file:PSEPK/recN/recN-uniprot.txt "DR   GO; GO:0006310; P:DNA recombination; IEA:InterPro."]
- [file:PSEPK/recN/recN-uniprot.txt "CC   -!- FUNCTION: May be involved in recombinational repair of damaged DNA."]
- [file:PSEPK/recN/recN-uniprot.txt "CC   -!- SIMILARITY: Belongs to the RecN family. {ECO:0000256|ARBA:ARBA00009441,"]
- [file:PSEPK/recN/recN-uniprot.txt "DR   PANTHER; PTHR11059; DNA REPAIR PROTEIN RECN; 1."]
- [file:PSEPK/recN/recN-uniprot.txt "DR   Pfam; PF02463; SMC_N; 1."]
- [file:PSEPK/recN/recN-uniprot.txt "KW   ATP-binding {ECO:0000256|ARBA:ARBA00022840};"]
- [file:PSEPK/recN/recN-uniprot.txt "FT   DOMAIN          5..512"]
- [file:PSEPK/recN/recN-uniprot.txt "DR   InterPro; IPR004604; DNA_recomb/repair_RecN."]

Decision: curate conservatively inside the repair-helicase/recombination boundary; do not promote ProtNLM-only names to GO functions.
