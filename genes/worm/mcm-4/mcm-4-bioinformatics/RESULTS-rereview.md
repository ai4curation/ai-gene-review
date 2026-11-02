# mcm-4 (Q95XQ8) catalytic-motif check (re-review, 2026-10-21)

Script: `motif_check_rereview.py` (reads `../mcm-4-uniprot.txt`); raw output in
`motif_check_rereview.out`.

| Motif (UniProt FT, PROSITE-ProRule PRU01410) | Position | Residues |
|---|---|---|
| Walker A | 469-476 | GDPGTSKS |
| Walker B | 533-536 | DEFD |
| Arginine-finger region (SRF motif start) | 601 | SRF |

Interpretation: the Walker A lysine (K475) and Walker B acidic residues (D533, E534) are
retained, and the SRF arginine-finger motif is present. Nothing in the sequence suggests
loss of the catalytic machinery. This check only shows the motifs are intact; it does not
show ATPase or helicase activity, which in MCM2-7 is a property of the assembled ring
(each ATPase site is built from one subunit's Walker A/B and its neighbour's arginine finger).
