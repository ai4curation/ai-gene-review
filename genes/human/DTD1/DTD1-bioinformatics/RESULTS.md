# DTD1: exact selected product and same-gene reference

Selected A0A2R8YCT7 has 127 residues; reference Q8TEA8 has 209 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–127 | 1–127 | 125 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Motif: Gly-cisPro motif, important for rejection of L-amino acids | 139–140 | 0 / 2 | 0 |
| Binding site:  | 4–4 | 1 / 1 | 1 |
| Binding site:  | 6–6 | 1 / 1 | 1 |
| Binding site:  | 28–28 | 1 / 1 | 1 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
