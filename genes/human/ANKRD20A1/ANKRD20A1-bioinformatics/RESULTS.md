# ANKRD20A1 paralog identity

Script: `paralog_identity.py` (run with `uv run --with biopython python paralog_identity.py`).
It fetches the reviewed human ANKRD20A-family entries from UniProt and aligns each one to ANKRD20A1 (Q5TYW2), using a global BLOSUM62 alignment.

Output:

```
target Q5TYW2 ANKRD20A1 len=823
A0PJZ0	ANKRD20A5P	len=165	identical_positions=150	identity_over_target=0.182
Q4UJ75	ANKRD20A4P	len=823	identical_positions=814	identity_over_target=0.989
Q5CZ79	ANKRD20A8P	len=823	identical_positions=798	identity_over_target=0.970
Q5SQ80	ANKRD20A2P	len=823	identical_positions=818	identity_over_target=0.994
Q5VUR7	ANKRD20A3P	len=823	identical_positions=818	identity_over_target=0.994
Q8NF67	ANKRD20A12P	len=263	identical_positions=94	identity_over_target=0.114
```

Four full-length paralogs (ANKRD20A2P, ANKRD20A3P, ANKRD20A4P, ANKRD20A8P) are 97–99.4% identical to ANKRD20A1 across all 823 residues. They differ from ANKRD20A1 at only 5 to 25 positions. A polyclonal antibody raised against ANKRD20A1 is therefore unlikely to distinguish it from these paralogs, unless its epitope covers one of those few positions.
