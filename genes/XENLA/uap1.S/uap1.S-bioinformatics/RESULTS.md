# uap1.S: exact selected product and human ortholog reference

Selected Q6DCZ6 has 507 residues; reference Q16222 has 522 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–453 | 1–453 | 342 |
| 471–522 | 454–505 | 40 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Binding site:  | 108–108 | 1 / 1 | 1 |
| Binding site:  | 108–108 | 1 / 1 | 1 |
| Binding site:  | 110–110 | 1 / 1 | 1 |
| Binding site:  | 110–110 | 1 / 1 | 1 |
| Binding site:  | 111–111 | 1 / 1 | 1 |
| Binding site:  | 111–111 | 1 / 1 | 1 |
| Binding site:  | 196–196 | 1 / 1 | 1 |
| Binding site:  | 196–196 | 1 / 1 | 1 |
| Binding site:  | 222–222 | 1 / 1 | 1 |
| Binding site:  | 222–222 | 1 / 1 | 1 |
| Binding site:  | 223–223 | 1 / 1 | 1 |
| Binding site:  | 223–223 | 1 / 1 | 1 |
| Binding site:  | 251–251 | 1 / 1 | 1 |
| Binding site:  | 251–251 | 1 / 1 | 1 |
| Binding site:  | 252–252 | 1 / 1 | 1 |
| Binding site:  | 252–252 | 1 / 1 | 1 |
| Binding site:  | 290–290 | 1 / 1 | 1 |
| Binding site:  | 290–290 | 1 / 1 | 1 |
| Binding site:  | 303–303 | 1 / 1 | 1 |
| Binding site:  | 303–303 | 1 / 1 | 1 |
| Binding site:  | 304–304 | 1 / 1 | 1 |
| Binding site:  | 304–304 | 1 / 1 | 1 |
| Binding site:  | 327–327 | 1 / 1 | 1 |
| Binding site:  | 327–327 | 1 / 1 | 1 |
| Binding site:  | 381–381 | 1 / 1 | 1 |
| Binding site:  | 407–407 | 1 / 1 | 1 |
| Binding site:  | 407–407 | 1 / 1 | 1 |
| Binding site:  | 472–472 | 1 / 1 | 1 |
| Binding site:  | 472–472 | 1 / 1 | 1 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and human ortholog reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
