# PP_3509 notes

2026-07-10: First-pass miscellaneous stress/detoxification spillover curation.
PP_3509 encodes a small VOC-domain bleomycin-resistance-family protein in Pseudomonas putida KT2440. UniProt/InterPro metadata supports antibiotic response context through the Bleomycin-R family and antibiotic-resistance keyword, but no precise molecular function is resolved in the fetched data. The first pass retains the broad response-to-antibiotic annotation and suggests the more specific response-to-bleomycin process as a conservative family-based refinement.

Primary provenance:
- [file:PSEPK/PP_3509/PP_3509-goa.tsv "UniProtKB	Q88H56	PP_3509	involved_in	GO:0046677	response to antibiotic	biological_process	ECO:0000256	IEA	GO_REF:0000002	InterPro:IPR000335	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	InterPro	Bleomycin resistance protein	20260706"]
- [file:PSEPK/PP_3509/PP_3509-uniprot.txt "DE   RecName: Full=Bleomycin resistance protein {ECO:0000256|ARBA:ARBA00021572};"]
- [file:PSEPK/PP_3509/PP_3509-uniprot.txt "DR   GO; GO:0046677; P:response to antibiotic; IEA:UniProtKB-KW."]
- [file:PSEPK/PP_3509/PP_3509-uniprot.txt "CC   -!- SIMILARITY: Belongs to the bleomycin resistance protein family."]
- [file:PSEPK/PP_3509/PP_3509-uniprot.txt "DR   CDD; cd08349; BLMA_like; 1."]
- [file:PSEPK/PP_3509/PP_3509-uniprot.txt "DR   Pfam; PF19581; Glyoxalase_7; 1."]
- [file:PSEPK/PP_3509/PP_3509-uniprot.txt "KW   Antibiotic resistance {ECO:0000256|ARBA:ARBA00023251};"]
- [file:PSEPK/PP_3509/PP_3509-uniprot.txt "FT   DOMAIN          4..118"]
- [file:PSEPK/PP_3509/PP_3509-uniprot.txt "DR   InterPro; IPR000335; Bleomycin-R."]
- [file:PSEPK/PP_3509/PP_3509-uniprot.txt "DR   InterPro; IPR029068; Glyas_Bleomycin-R_OHBP_Dase."]

Decision: accept response to antibiotic and add a more specific response-to-bleomycin recommendation; no molecular function is asserted.
