# uup notes

2026-07-10: First-pass repair-helicase/recombination split curation.
uup encodes an ABCF-family ATPase in Pseudomonas putida KT2440. HAMAP supports ATPase, DNA-binding, ribosome-binding, and cytoplasmic localization, with a probable role in ribosome function and possible involvement in resolving branched DNA intermediates from postreplication gaps.

Primary provenance:
- [file:PSEPK/uup/uup-goa.tsv "UniProtKB	Q88L06	uup	enables	GO:0016887	ATP hydrolysis activity	molecular_function	ECO:0000501	IEA	GO_REF:0000120	InterPro:IPR003439|InterPro:IPR017871|InterPro:IPR043686|UniRule:UR001336782	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	UniProt	ATP-binding protein Uup	20260706"]
- [file:PSEPK/uup/uup-uniprot.txt "DE   RecName: Full=ATP-binding protein Uup {ECO:0000256|HAMAP-Rule:MF_00848};"]
- [file:PSEPK/uup/uup-uniprot.txt "DR   GO; GO:0016887; F:ATP hydrolysis activity; IEA:UniProtKB-UniRule."]
- [file:PSEPK/uup/uup-uniprot.txt "CC   -!- FUNCTION: Probably plays a role in ribosome assembly or function. May"]
- [file:PSEPK/uup/uup-uniprot.txt "CC   -!- CATALYTIC ACTIVITY:"]
- [file:PSEPK/uup/uup-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000256|HAMAP-Rule:MF_00848}."]
- [file:PSEPK/uup/uup-uniprot.txt "CC   -!- SIMILARITY: Belongs to the ABC transporter superfamily. ABCF family."]
- [file:PSEPK/uup/uup-uniprot.txt "DR   PANTHER; PTHR42855; ABC TRANSPORTER ATP-BINDING SUBUNIT; 1."]
- [file:PSEPK/uup/uup-uniprot.txt "DR   Pfam; PF00005; ABC_tran; 2."]
- [file:PSEPK/uup/uup-uniprot.txt "KW   ATP-binding {ECO:0000256|ARBA:ARBA00022840, ECO:0000256|HAMAP-"]

Decision: curate conservatively inside the repair-helicase/recombination boundary; do not promote ProtNLM-only names to GO functions.
