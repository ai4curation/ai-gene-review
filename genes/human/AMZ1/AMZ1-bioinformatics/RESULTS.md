# AMZ1 zinc-binding motif check

Script: `zinc_motif_check.py` (fetches live UniProt sequences). Output: `results.tsv`.

Metzincins coordinate the catalytic zinc with three histidines in HEXXHXXGXXH. The table gives the residue at the third-ligand position for each protein.

| Protein | Motif window | Third ligand |
|---|---|---|
| human AMZ1 (Q400G9) | HELCHLLGLGNCRW | N (Asn271) |
| human AMZ2 (Q86W34) | HEIGHIFGLRHCQW | H (His264) |
| M. kandleri AmzA (Q8TXW1) | HELGHTFGLGHCPD | H |
| A. fulgidus AmzA (O29917) | HEIGHVLGLKHCSN | H |

Conclusion: human AMZ1 lacks the third zinc-binding histidine; asparagine replaces it. AMZ2 and both structurally characterized archaeal enzymes keep it. This agrees with the remark by Graef et al. (PMID:22937112): "AMZ1 has the third histidine of the metzincins' consensus sequence replaced by asparagine, serine or threonine, depending on the organism."

Residue identity alone does not show that AMZ1 is inactive. It does mean the canonical catalytic zinc site cannot be assumed.
