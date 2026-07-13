# sbcC notes

2026-07-10: First-pass repair-helicase/recombination split curation.
sbcC encodes the ATPase/SMC-like subunit of the SbcCD nuclease complex. UniProt describes SbcCD as opening DNA hairpins and processing DNA structures that arise during replication and recombination; fetched GOA supports ATP hydrolysis and double-strand-break repair context.

Primary provenance:
- [file:PSEPK/sbcC/sbcC-goa.tsv "UniProtKB	Q88LB1	sbcC	enables	GO:0016887	ATP hydrolysis activity	molecular_function	ECO:0000256	IEA	GO_REF:0000002	InterPro:IPR038729	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	InterPro	Nuclease SbcCD subunit C	20260706"]
- [file:PSEPK/sbcC/sbcC-uniprot.txt "DE   RecName: Full=Nuclease SbcCD subunit C {ECO:0000256|ARBA:ARBA00013368};"]
- [file:PSEPK/sbcC/sbcC-uniprot.txt "DR   GO; GO:0016887; F:ATP hydrolysis activity; IEA:InterPro."]
- [file:PSEPK/sbcC/sbcC-uniprot.txt "CC   -!- FUNCTION: SbcCD cleaves DNA hairpin structures. These structures can"]
- [file:PSEPK/sbcC/sbcC-uniprot.txt "CC   -!- SIMILARITY: Belongs to the SMC family. SbcC subfamily."]
- [file:PSEPK/sbcC/sbcC-uniprot.txt "DR   PANTHER; PTHR32114; ABC TRANSPORTER ABCH.3; 1."]
- [file:PSEPK/sbcC/sbcC-uniprot.txt "DR   Pfam; PF13476; AAA_23; 1."]
- [file:PSEPK/sbcC/sbcC-uniprot.txt "KW   ATP-binding {ECO:0000256|ARBA:ARBA00022840};"]
- [file:PSEPK/sbcC/sbcC-uniprot.txt "FT   DOMAIN          6..222"]
- [file:PSEPK/sbcC/sbcC-uniprot.txt "DR   InterPro; IPR027417; P-loop_NTPase."]

Decision: curate conservatively inside the repair-helicase/recombination boundary; do not promote ProtNLM-only names to GO functions.
