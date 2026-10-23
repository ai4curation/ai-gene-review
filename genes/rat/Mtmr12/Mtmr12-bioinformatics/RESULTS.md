# Mtmr12: exact selected product and same-gene reference

Selected A0A8I5ZMD5 has 732 residues; reference Q5FVM6 has 748 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–7 | 1–7 | 1 |
| 8–8 | 23–23 | 1 |
| 17–29 | 24–36 | 6 |
| 45–48 | 37–40 | 3 |
| 57–748 | 41–732 | 691 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Domain: Myotubularin phosphatase | 206–644 | 439 / 439 | 439 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
