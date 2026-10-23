# RHOJ: exact selected product and same-gene reference

Selected G3V4H1 has 153 residues; reference Q9H4E5 has 214 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–103 | 1–103 | 103 |
| 115–115 | 104–104 | 1 |
| 121–127 | 105–111 | 3 |
| 160–181 | 112–133 | 5 |
| 182–184 | 140–142 | 2 |
| 195–201 | 143–149 | 2 |
| 205–208 | 150–153 | 1 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Motif: Effector region | 50–58 | 9 / 9 | 9 |
| Binding site:  | 31–31 | 1 / 1 | 1 |
| Binding site:  | 33–33 | 1 / 1 | 1 |
| Binding site:  | 34–34 | 1 / 1 | 1 |
| Binding site:  | 35–35 | 1 / 1 | 1 |
| Binding site:  | 35–35 | 1 / 1 | 1 |
| Binding site:  | 36–36 | 1 / 1 | 1 |
| Binding site:  | 50–50 | 1 / 1 | 1 |
| Binding site:  | 53–53 | 1 / 1 | 1 |
| Binding site:  | 53–53 | 1 / 1 | 1 |
| Binding site:  | 75–75 | 1 / 1 | 1 |
| Binding site:  | 78–78 | 1 / 1 | 1 |
| Binding site:  | 136–136 | 0 / 1 | 0 |
| Binding site:  | 177–177 | 1 / 1 | 0 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
