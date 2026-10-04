# ANKAR hydropathy check

Script: `hydropathy_check.py` (fetches the live UniProt sequence). To reproduce: `uv run python hydropathy_check.py > results.tsv`.

UniProt annotates one helical transmembrane segment (residues 309-329) from sequence prediction (ECO:0000305). This check scores it with Kyte-Doolittle hydropathy over 19-residue windows; 1.6 is the classic threshold for a candidate membrane-spanning helix.

| Item | Result |
|---|---|
| Annotated segment 309-329 (IRRGIGYLKLICFLIPFLLSL) | mean KD 1.50 over the 21 residues |
| Best windows overlapping it (start 311, 312) | 1.66, 1.69 |
| Other windows at or above 1.6 | start 605 (inside ANK repeat 3), start 1099 |
| N-terminal signal-like window | none |

Conclusion: the predicted transmembrane helix is borderline. Windows over it only just pass the threshold, and a window inside an ankyrin repeat, which is a soluble fold, scores about as high. The single-pass membrane assignment is therefore weakly supported by sequence, and no experiment has localized ANKAR.
