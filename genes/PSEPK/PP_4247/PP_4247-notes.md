# PP_4247 notes

2026-07-10: First-pass nuclease/DNase/toxin side-node split curation.
PP_4247 is an ERI-1/RNase-H-like 3'-5' exonuclease-family protein. GOA/InterPro support 3'-5'-RNA exonuclease activity, making this an RNA-processing nuclease side node rather than DNA repair core.

Primary provenance:
- [file:PSEPK/PP_4247/PP_4247-goa.tsv "UniProtKB	Q88F52	PP_4247	enables	GO:0000175	3'-5'-RNA exonuclease activity	molecular_function	ECO:0000256	IEA	GO_REF:0000002	InterPro:IPR047201	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	InterPro	Exonuclease domain-containing protein	20260706"]
- [file:PSEPK/PP_4247/PP_4247-uniprot.txt "DE   SubName: Full=Exonuclease {ECO:0000313|EMBL:AAN69827.1};"]
- [file:PSEPK/PP_4247/PP_4247-uniprot.txt "DR   GO; GO:0000175; F:3'-5'-RNA exonuclease activity; IEA:InterPro."]
- [file:PSEPK/PP_4247/PP_4247-uniprot.txt "DR   PANTHER; PTHR23044; 3'-5' EXONUCLEASE ERI1-RELATED; 1."]
- [file:PSEPK/PP_4247/PP_4247-uniprot.txt "DR   Pfam; PF00929; RNase_T; 1."]
- [file:PSEPK/PP_4247/PP_4247-uniprot.txt "KW   Exonuclease {ECO:0000256|ARBA:ARBA00022839, ECO:0000313|EMBL:AAN69827.1};"]
- [file:PSEPK/PP_4247/PP_4247-uniprot.txt "FT   DOMAIN          3..183"]
- [file:PSEPK/PP_4247/PP_4247-uniprot.txt "DR   InterPro; IPR051274; 3-5_Exoribonuclease."]
- [file:PSEPK/PP_4247/PP_4247-uniprot.txt "DR   InterPro; IPR047201; ERI-1_3'hExo-like."]
- [file:PSEPK/PP_4247/PP_4247-uniprot.txt "DR   InterPro; IPR013520; Ribonucl_H."]

Decision: route as nuclease/toxin/RNA side-node context rather than as a single DNA repair pathway.
