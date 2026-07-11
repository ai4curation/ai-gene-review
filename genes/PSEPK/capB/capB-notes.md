# capB notes

2026-07-10: First-pass cold/heat-shock stress-bucket curation.
capB encodes a small cytosolic cold-shock-domain protein in Pseudomonas putida KT2440. It contains a CspA-like cold-shock/OB-fold nucleic-acid-binding domain and is best treated as a cold-shock-domain nucleic-acid-binding protein; the first-pass evidence does not resolve a specific RNA or DNA target.

Primary provenance:
- [file:PSEPK/capB/capB-goa.tsv "UniProtKB	Q88NV5	capB	enables	GO:0003676	nucleic acid binding	molecular_function	ECO:0000256	IEA	GO_REF:0000002	InterPro:IPR002059|InterPro:IPR011129|InterPro:IPR012156	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	InterPro	CSD domain-containing protein	20260706"]
- [file:PSEPK/capB/capB-uniprot.txt "DE   SubName: Full=Cold shock protein CapB {ECO:0000313|EMBL:AAN66724.1};"]
- [file:PSEPK/capB/capB-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000256|ARBA:ARBA00004496,"]
- [file:PSEPK/capB/capB-uniprot.txt "DR   PANTHER; PTHR46565; COLD SHOCK DOMAIN PROTEIN 2; 1."]
- [file:PSEPK/capB/capB-uniprot.txt "DR   Pfam; PF00313; CSD; 1."]
- [file:PSEPK/capB/capB-uniprot.txt "FT   DOMAIN          4..68"]
- [file:PSEPK/capB/capB-uniprot.txt "DR   InterPro; IPR012156; Cold_shock_CspA."]
- [file:PSEPK/capB/capB-uniprot.txt "DR   InterPro; IPR011129; CSD."]

Decision: keep the call at the family/domain-supported level. Cold-shock proteins are retained as nucleic-acid-binding CSD proteins without a specific RNA/DNA target; HSP20-family proteins are treated as putative unfolded-protein-binding holdases without assigning specific clients.
