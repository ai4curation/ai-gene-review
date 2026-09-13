# Pnkd: exact selected product and same-gene reference

Selected B4F7D2 has 369 residues; reference D3ZXB0 has 424 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–79 | 1–79 | 79 |
| 119–379 | 80–340 | 251 |
| 395–406 | 341–352 | 6 |
| 408–424 | 353–369 | 2 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Transmembrane: Helical | 74–92 | 6 / 19 | 6 |
| Domain: Metallo-beta-lactamase | 168–330 | 163 / 163 | 163 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
