# Spcs2: exact selected product and same-gene reference

Selected A0A140LHW5 has 74 residues; reference Q9CYN2 has 226 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–66 | 1–66 | 66 |
| 110–112 | 67–69 | 1 |
| 144–147 | 70–73 | 2 |
| 226–226 | 74–74 | 0 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Transmembrane: Helical | 87–107 | 0 / 21 | 0 |
| Transmembrane: Helical | 112–132 | 1 / 21 | 1 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
