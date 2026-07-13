# rdgC notes

2026-07-10: First-pass repair-helicase/recombination split curation.
rdgC encodes a recombination-associated RdgC-family protein in Pseudomonas putida KT2440. HAMAP, InterPro, Pfam, and PANTHER support a bacterial RdgC protein that binds double-stranded DNA and participates in DNA recombination regulation in the cytoplasm/nucleoid context.

Primary provenance:
- [file:PSEPK/rdgC/rdgC-goa.tsv "UniProtKB	Q88M72	rdgC	enables	GO:0003690	double-stranded DNA binding	molecular_function	ECO:0007826	IEA	GO_REF:0000118	PANTHER:PTN002445568	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	TreeGrafter	Recombination-associated protein RdgC	20260706"]
- [file:PSEPK/rdgC/rdgC-uniprot.txt "DE   RecName: Full=Recombination-associated protein RdgC {ECO:0000255|HAMAP-Rule:MF_00194};"]
- [file:PSEPK/rdgC/rdgC-uniprot.txt "DR   GO; GO:0003690; F:double-stranded DNA binding; IEA:TreeGrafter."]
- [file:PSEPK/rdgC/rdgC-uniprot.txt "CC   -!- FUNCTION: May be involved in recombination. {ECO:0000255|HAMAP-"]
- [file:PSEPK/rdgC/rdgC-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Cytoplasm, nucleoid {ECO:0000255|HAMAP-"]
- [file:PSEPK/rdgC/rdgC-uniprot.txt "CC   -!- SIMILARITY: Belongs to the RdgC family. {ECO:0000255|HAMAP-"]
- [file:PSEPK/rdgC/rdgC-uniprot.txt "DR   PANTHER; PTHR38103; RECOMBINATION-ASSOCIATED PROTEIN RDGC; 1."]
- [file:PSEPK/rdgC/rdgC-uniprot.txt "DR   Pfam; PF04381; RdgC; 1."]
- [file:PSEPK/rdgC/rdgC-uniprot.txt "DR   InterPro; IPR007476; RdgC."]
- [file:PSEPK/rdgC/rdgC-deep-research-asta.md "  uniprot_accession: Q88M72"]

Decision: curate conservatively inside the repair-helicase/recombination boundary; do not promote ProtNLM-only names to GO functions.
