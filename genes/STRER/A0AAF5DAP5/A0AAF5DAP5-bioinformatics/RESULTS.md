# Strongyloides stercoralis beta-tubulin alignment

The local helper globally aligns the UniProt sequences for four S. stercoralis
beta-tubulins: the cloned Q4KS25/BTUB entry and predicted entries A0A0K0DXA9,
A0A0K0EJ28 and A0AAF5DAP5.

Q4KS25, A0A0K0DXA9 and A0A0K0EJ28 all start at the conserved beta-tubulin
MREIV sequence, while A0AAF5DAP5 starts with five additional modeled residues,
LFNII, before the same MREIV sequence.

```text
reference	query	reference_length	query_length	alignment_columns	identities	substitutions	gap_columns	Q4KS25_F168	Q4KS25_E199	Q4KS25_F201
Q4KS25	A0A0K0DXA9	447	444	448	419	24	5	F168	E199	F201
Q4KS25	A0A0K0EJ28	447	442	451	380	58	13	F167	E198	F200
Q4KS25	A0AAF5DAP5	447	450	453	420	24	9	F173	E204	F206
```

Q4KS25 F168/E199/F201 align to A0AAF5DAP5 F173/E204/F206.
