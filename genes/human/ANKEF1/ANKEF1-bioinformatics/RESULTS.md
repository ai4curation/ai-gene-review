# ANKEF1 EF-hand loop check

Script: `ef_hand_check.py` (fetches live UniProt sequences). To reproduce: `uv run python ef_hand_check.py > results.tsv`.

A canonical EF-hand binds calcium through a 12-residue loop, with ligands at positions 1, 3, 5, 7, 9 and 12, an invariant Gly at 6, and a bidentate Glu at 12. The script scores the best 12-residue window in each domain against these seven features. Calmodulin EF-hand 1 is the positive control.

| Protein | Best loop | Score | Glu at 12 |
|---|---|---|---|
| ANKEF1 EF-hand (335-369) | LDRGDGSISKND | 4/7 | no |
| Calmodulin EF-hand 1 (control) | DKDGDGTITTKE | 7/7 | yes |

Conclusion: the ANKEF1 EF-hand loop departs from the canonical calcium-binding pattern and lacks the Glu at position 12, consistent with UniProt annotating no calcium-binding sites. This is a crude motif score; it suggests, but does not prove, that the EF-hand does not bind calcium.
