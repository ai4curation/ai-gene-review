# wdr-23: exact selected product and same-gene reference

Selected S6FN32 has 498 residues; reference P90794 has 571 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 74–571 | 1–498 | 498 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Repeat: WD 1 | 162–201 | 40 / 40 | 40 |
| Repeat: WD 2 | 266–305 | 40 / 40 | 40 |
| Repeat: WD 3 | 309–349 | 41 / 41 | 41 |
| Repeat: WD 4 | 357–396 | 40 / 40 | 40 |
| Repeat: WD 5 | 435–479 | 45 / 45 | 45 |
| Repeat: WD 6 | 482–521 | 40 / 40 | 40 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
