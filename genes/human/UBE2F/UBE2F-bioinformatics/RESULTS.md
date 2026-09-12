# UBE2F: exact selected product and same-gene reference

Selected F8WDQ9 has 101 residues; reference Q969M7 has 185 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–94 | 1–94 | 94 |
| 179–185 | 95–101 | 2 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Domain: UBC core | 32–185 | 70 / 154 | 65 |
| Active site: Glycyl thioester intermediate | 116–116 | 0 / 1 | 0 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
