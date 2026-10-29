# ANKK1 kinase catalytic-residue check

Script: `kinase_motif_check.py`. ANKK1 is read from the cached `ANKK1-uniprot.txt`; the RIPK2 control is fetched from UniProt. To reproduce: `uv run python kinase_motif_check.py > results.tsv`.

The script anchors on each protein's own UniProt feature table: the ATP-binding glycine-rich loop, the beta-3 lysine and the catalytic Asp (ACT_SITE, proton acceptor). It then reports the catalytic loop and the first DFG downstream.

| Protein | Gly-rich loop | beta-3 Lys | Catalytic loop | DFG |
|---|---|---|---|---|
| ANKK1 (Q8NFD2) | VASGGFSQV | K51 | HLDLKPGNI (Asp145) | 163 |
| RIPK2 (O43353, active control) | LSRGASGTV | K47 | HHDLKTQNI (Asp146) | 164 |

Conclusion: ANKK1 keeps every canonical catalytic element at the same positions as the active RIP-family kinase RIPK2: the glycine-rich loop, the beta-3 lysine, the HxD...KxxN catalytic loop and DFG. It is therefore expected to be catalytically competent. No study has measured ANKK1 kinase activity directly.
