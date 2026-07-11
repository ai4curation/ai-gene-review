# cpo notes

2026-07-10: First-pass peroxide/peroxiredoxin stress-detoxification curation.
cpo encodes a bacterial non-heme chloroperoxidase/AB-hydrolase-family enzyme in Pseudomonas putida KT2440. Existing GOA supports chloride peroxidase activity and cellular oxidant detoxification; this first pass does not assign a narrower physiological substrate or pathway role.

Primary provenance:
- [file:PSEPK/cpo/cpo-goa.tsv "UniProtKB	Q88FR2	cpo	enables	GO:0016691	chloride peroxidase activity	molecular_function	ECO:0000501	IEA	GO_REF:0000003	EC:1.11.1.10	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	UniProt	AB hydrolase-1 domain-containing protein	20260706"]
- [file:PSEPK/cpo/cpo-uniprot.txt "DE   SubName: Full=Non-heme chloroperoxidase {ECO:0000313|EMBL:AAN69615.1};"]
- [file:PSEPK/cpo/cpo-uniprot.txt "CC   -!- SIMILARITY: Belongs to the AB hydrolase superfamily. Bacterial non-heme"]
- [file:PSEPK/cpo/cpo-uniprot.txt "DR   InterPro; IPR050471; AB_hydrolase."]
- [file:PSEPK/cpo/cpo-uniprot.txt "DR   Pfam; PF00561; Abhydrolase_1; 1."]

Decision: represent this gene in the oxidative-stress/peroxide-detoxification boundary. Keep broad stress-response, redox-homeostasis, antioxidant, electron-transfer, and cofactor-binding rows as non-core context when they are not the most informative functional statement.
