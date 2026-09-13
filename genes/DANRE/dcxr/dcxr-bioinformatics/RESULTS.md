# dcxr: exact selected product and human ortholog reference

Selected Q567K5 has 244 residues; reference Q7Z4W1 has 244 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–244 | 1–244 | 169 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Active site: Nucleophile | 136–136 | 1 / 1 | 1 |
| Active site: Proton acceptor | 149–149 | 1 / 1 | 1 |
| Active site: Proton donor | 153–153 | 1 / 1 | 1 |
| Binding site:  | 17–17 | 1 / 1 | 1 |
| Binding site:  | 19–19 | 1 / 1 | 1 |
| Binding site:  | 38–38 | 1 / 1 | 0 |
| Binding site:  | 39–39 | 1 / 1 | 1 |
| Binding site:  | 40–40 | 1 / 1 | 1 |
| Binding site:  | 60–60 | 1 / 1 | 1 |
| Binding site:  | 61–61 | 1 / 1 | 1 |
| Binding site:  | 83–83 | 1 / 1 | 1 |
| Binding site:  | 134–134 | 1 / 1 | 1 |
| Binding site:  | 149–149 | 1 / 1 | 1 |
| Binding site:  | 153–153 | 1 / 1 | 1 |
| Binding site:  | 182–182 | 1 / 1 | 1 |
| Binding site:  | 184–184 | 1 / 1 | 1 |
| Binding site:  | 185–185 | 1 / 1 | 0 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and human ortholog reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
