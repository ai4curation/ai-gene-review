# tpx notes

2026-07-10: First-pass peroxide/peroxiredoxin stress-detoxification curation.
tpx encodes the Tpx-family thiol peroxidase/peroxiredoxin in Pseudomonas putida KT2440. HAMAP and GOA support thioredoxin-dependent peroxiredoxin activity, peroxide detoxification, and oxidative-stress response context.

Primary provenance:
- [file:PSEPK/tpx/tpx-goa.tsv "UniProtKB	Q88GY0	tpx	involved_in	GO:0098869	cellular oxidant detoxification	biological_process	ECO:0000501	IEA	GO_REF:0000120	GO:0008379|GO:0140824	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	UniProt	Thiol peroxidase	20260706"]
- [file:PSEPK/tpx/tpx-uniprot.txt "DE   RecName: Full=Thiol peroxidase {ECO:0000256|HAMAP-Rule:MF_00269};"]
- [file:PSEPK/tpx/tpx-uniprot.txt "CC   -!- FUNCTION: Thiol-specific peroxidase that catalyzes the reduction of"]
- [file:PSEPK/tpx/tpx-uniprot.txt "CC   -!- SIMILARITY: Belongs to the peroxiredoxin family. Tpx subfamily."]
- [file:PSEPK/tpx/tpx-uniprot.txt "DR   InterPro; IPR013740; Redoxin."]

Decision: represent this gene in the oxidative-stress/peroxide-detoxification boundary. Keep broad stress-response, redox-homeostasis, antioxidant, electron-transfer, and cofactor-binding rows as non-core context when they are not the most informative functional statement.
