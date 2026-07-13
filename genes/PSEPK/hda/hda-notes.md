# hda notes

2026-07-10: First-pass replication-accessory/polymerase split curation.
hda encodes a DnaA/Hda-family replication-initiation regulator. Current GOA, InterPro, Pfam, and PANTHER evidence support a role in preventing premature DNA replication reinitiation rather than a standalone replication enzyme activity.

Primary provenance:
- [file:PSEPK/hda/hda-goa.tsv "UniProtKB	Q88MA6	hda	involved_in	GO:0032297	negative regulation of DNA-templated DNA replication initiation	biological_process	ECO:0000501	IEA	GO_REF:0000120	InterPro:IPR017788|PANTHER:PTN002409083	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	UniProt	Regulator of DnaA that prevents premature reinitiation of DNA replication	20260706"]
- [file:PSEPK/hda/hda-uniprot.txt "DE   SubName: Full=Regulator of DnaA that prevents premature reinitiation of DNA replication {ECO:0000313|EMBL:AAN67289.1};"]
- [file:PSEPK/hda/hda-uniprot.txt "DR   GO; GO:0032297; P:negative regulation of DNA-templated DNA replication initiation; IEA:InterPro."]
- [file:PSEPK/hda/hda-uniprot.txt "DR   PANTHER; PTHR30050; CHROMOSOMAL REPLICATION INITIATOR PROTEIN DNAA; 1."]
- [file:PSEPK/hda/hda-uniprot.txt "DR   Pfam; PF00308; Bac_DnaA; 1."]
- [file:PSEPK/hda/hda-uniprot.txt "FT   DOMAIN          16..161"]
- [file:PSEPK/hda/hda-uniprot.txt "DR   InterPro; IPR013317; DnaA_dom."]
- [file:PSEPK/hda/hda-uniprot.txt "DR   InterPro; IPR017788; Hda."]
- [file:PSEPK/hda/hda-uniprot.txt "DR   InterPro; IPR055199; Hda_lid."]
- [file:PSEPK/hda/hda-uniprot.txt "DR   InterPro; IPR027417; P-loop_NTPase."]

Decision: route as replication accessory/polymerase boundary context; do not over-promote weak product names.
