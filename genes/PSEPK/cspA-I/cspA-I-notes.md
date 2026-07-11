# cspA-I notes

2026-07-10: First-pass cold/heat-shock stress-bucket curation.
cspA-I encodes a small cytosolic major cold-shock protein in Pseudomonas putida KT2440. Its CspA-like cold-shock/OB-fold domain supports nucleic-acid binding, consistent with a cold-shock-domain protein whose specific RNA or DNA targets remain unresolved.

Primary provenance:
- [file:PSEPK/cspA-I/cspA-I-goa.tsv "UniProtKB	Q88MP8	cspA-I	enables	GO:0003676	nucleic acid binding	molecular_function	ECO:0000256	IEA	GO_REF:0000002	InterPro:IPR002059|InterPro:IPR011129|InterPro:IPR012156	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	InterPro	CSD domain-containing protein	20260706"]
- [file:PSEPK/cspA-I/cspA-I-uniprot.txt "DE   SubName: Full=Major cold shock protein {ECO:0000313|EMBL:AAN67143.1};"]
- [file:PSEPK/cspA-I/cspA-I-uniprot.txt "DR   GO; GO:0003676; F:nucleic acid binding; IEA:InterPro."]
- [file:PSEPK/cspA-I/cspA-I-uniprot.txt "CC   -!- SUBCELLULAR LOCATION: Cytoplasm {ECO:0000256|ARBA:ARBA00004496,"]
- [file:PSEPK/cspA-I/cspA-I-uniprot.txt "DR   PANTHER; PTHR11544; COLD SHOCK DOMAIN CONTAINING PROTEINS; 1."]
- [file:PSEPK/cspA-I/cspA-I-uniprot.txt "DR   Pfam; PF00313; CSD; 1."]
- [file:PSEPK/cspA-I/cspA-I-uniprot.txt "FT   DOMAIN          4..68"]
- [file:PSEPK/cspA-I/cspA-I-uniprot.txt "DR   InterPro; IPR012156; Cold_shock_CspA."]

Decision: keep the call at the family/domain-supported level. Cold-shock proteins are retained as nucleic-acid-binding CSD proteins without a specific RNA/DNA target; HSP20-family proteins are treated as putative unfolded-protein-binding holdases without assigning specific clients.
