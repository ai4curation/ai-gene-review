# AMZ2 zinc-binding motif check

Script: `zinc_motif_check.py` (fetches live UniProt sequences). Output: `results.tsv`.

Metzincins coordinate the catalytic zinc with three histidines in HEXXHXXGXXH, followed by the Met-turn. The table gives the residue at the third-ligand position for each protein.

| Protein | Motif window | Third ligand |
|---|---|---|
| human AMZ2 (Q86W34) | HEIGHIFGLRHCQW | H (His264) |
| human AMZ1 (Q400G9) | HELCHLLGLGNCRW | N (Asn271) |
| M. kandleri AmzA (Q8TXW1) | HELGHTFGLGHCPD | H |
| A. fulgidus AmzA (O29917) | HEIGHVLGLKHCSN | H |

Conclusion: human AMZ2 keeps all three zinc-binding histidines and the catalytic glutamate (Glu255), as the structurally characterized archaeal enzymes do. Its paralog AMZ1 has lost the third histidine.

An intact motif makes metallopeptidase activity plausible but does not demonstrate it. No valid activity measurement exists for AMZ2.
