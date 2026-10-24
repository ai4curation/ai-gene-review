# NARF: exact selected product and same-gene reference

Selected J3KS48 has 217 residues; reference Q9UHQ1 has 456 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–128 | 1–128 | 128 |
| 174–258 | 129–213 | 85 |
| 383–385 | 214–216 | 2 |
| 456–456 | 217–217 | 1 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
