# Sdhaf2: exact selected product and same-gene reference

Selected A0A494B8X4 has 135 residues; reference Q8C6I2 has 164 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–122 | 1–122 | 121 |
| 126–138 | 123–135 | 3 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Transit peptide: Mitochondrion | 1–27 | 27 / 27 | 27 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
