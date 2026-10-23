# FTSH12: exact selected product and same-gene reference

Selected A0A1P8ARD2 has 991 residues; reference Q9SAJ3 has 1008 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–987 | 1–987 | 983 |
| 1005–1008 | 988–991 | 1 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Transit peptide: Chloroplast | 1–49 | 49 / 49 | 49 |
| Transmembrane: Helical | 154–174 | 21 / 21 | 21 |
| Transmembrane: Helical | 427–447 | 21 / 21 | 21 |
| Active site:  | 770–770 | 1 / 1 | 1 |
| Binding site:  | 533–540 | 8 / 8 | 8 |
| Binding site:  | 769–769 | 1 / 1 | 1 |
| Binding site:  | 773–773 | 1 / 1 | 1 |
| Binding site:  | 849–849 | 1 / 1 | 1 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
