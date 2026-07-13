# dps notes

2026-07-10: First-pass miscellaneous stress/detoxification spillover curation.
dps (PP_1210) encodes a Dps/ferritin-like stress protein in Pseudomonas putida KT2440. The protein has a ferritin/Dps domain, EC-derived ferroxidase activity, ferric-iron-binding annotation, and UniProt/domain support for DNA binding. In this first pass it is curated as a Dps-family iron-sequestration and DNA-binding stress protein rather than as a fully experimentally characterized KT2440 DNA-protection factor.

Primary provenance:
- [file:PSEPK/dps/dps-goa.tsv "UniProtKB	Q88NJ7	dps	enables	GO:0004322	ferroxidase activity	molecular_function	ECO:0000501	IEA	GO_REF:0000003	EC:1.16.3.1	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	UniProt	Ferritin/DPS domain-containing protein	20260706"]
- [file:PSEPK/dps/dps-uniprot.txt "DE   SubName: Full=DNA-binding stress protein {ECO:0000313|EMBL:AAN66834.1};"]
- [file:PSEPK/dps/dps-uniprot.txt "DR   GO; GO:0004322; F:ferroxidase activity; IEA:UniProtKB-EC."]
- [file:PSEPK/dps/dps-uniprot.txt "CC   -!- SIMILARITY: Belongs to the Dps family. {ECO:0000256|ARBA:ARBA00009497,"]
- [file:PSEPK/dps/dps-uniprot.txt "DR   CDD; cd01043; DPS; 1."]
- [file:PSEPK/dps/dps-uniprot.txt "DR   PANTHER; PTHR42932:SF3; DNA PROTECTION DURING STARVATION PROTEIN; 1."]
- [file:PSEPK/dps/dps-uniprot.txt "DR   Pfam; PF00210; Ferritin; 1."]
- [file:PSEPK/dps/dps-uniprot.txt "KW   DNA-binding {ECO:0000313|EMBL:AAN66834.1};"]
- [file:PSEPK/dps/dps-uniprot.txt "FT   DOMAIN          17..156"]
- [file:PSEPK/dps/dps-uniprot.txt "DR   InterPro; IPR002177; DPS_DNA-bd."]

Decision: accept Dps ferroxidase/iron-binding evidence, mark the broad oxidoreductase parent as over-annotated, and add DNA binding.
