# mnaT notes

2026-07-10: First-pass glutathione/thiol detoxification stress-bucket curation.
mnaT encodes a GNAT/acyltransferase-family methionine-derivative detoxifier in Pseudomonas putida KT2440. Existing GOA supports L-amino-acid N-acetyltransferase activity, consistent with acetylation of L-methionine sulfoximine or L-methionine sulfone.

Primary provenance:
- [file:PSEPK/mnaT/mnaT-goa.tsv "UniProtKB	Q88DH9	mnaT	enables	GO:0140085	L-amino-acid N-acetyltransferase activity	molecular_function	ECO:0007322	IEA	GO_REF:0000116	RHEA:47656|RHEA:47660	160488	Pseudomonas putida (strain ATCC 47054 / DSM 6125 / CFBP 8728 / NCIMB 11950 / KT2440)	RHEA	L-methionine sulfoximine/L-methionine sulfone acetyltransferase	20260706"]
- [file:PSEPK/mnaT/mnaT-uniprot.txt "DE   RecName: Full=L-methionine sulfoximine/L-methionine sulfone acetyltransferase {ECO:0000256|ARBA:ARBA00072269};"]
- [file:PSEPK/mnaT/mnaT-uniprot.txt "DE   AltName: Full=Methionine derivative detoxifier A {ECO:0000256|ARBA:ARBA00078632};"]
- [file:PSEPK/mnaT/mnaT-uniprot.txt "CC   -!- CATALYTIC ACTIVITY:"]
- [file:PSEPK/mnaT/mnaT-uniprot.txt "DR   InterPro; IPR016181; Acyl_CoA_acyltransferase."]

Decision: keep the assignment conservative. Use broad transferase or oxidoreductase activity where family evidence does not resolve substrate chemistry, and avoid asserting a glutathione metabolic process unless gene-specific evidence supports it.
