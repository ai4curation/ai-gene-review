# Ptk7: exact selected product and human ortholog reference

Selected A0A8I6ALM9 has 1079 residues; reference Q13308 has 1070 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–4 | 1–4 | 3 |
| 5–7 | 6–8 | 2 |
| 8–15 | 13–20 | 5 |
| 23–25 | 21–23 | 1 |
| 26–1070 | 35–1079 | 972 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Signal:  | 1–30 | 23 / 30 | 12 |
| Transmembrane: Helical | 705–725 | 21 / 21 | 21 |
| Domain: Ig-like C2-type 1 | 31–120 | 90 / 90 | 83 |
| Domain: Ig-like C2-type 2 | 128–218 | 91 / 91 | 86 |
| Domain: Ig-like C2-type 3 | 225–317 | 93 / 93 | 86 |
| Domain: Ig-like C2-type 4 | 309–407 | 99 / 99 | 83 |
| Domain: Ig-like C2-type 5 | 412–497 | 86 / 86 | 79 |
| Domain: Ig-like C2-type 6 | 503–586 | 84 / 84 | 81 |
| Domain: Ig-like C2-type 7 | 578–680 | 103 / 103 | 99 |
| Domain: Protein kinase; inactive | 796–1066 | 271 / 271 | 257 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and human ortholog reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.

## Structural landmarks from PMID:32619402

| Human position | Human residue | Selected position | Selected residue |
|---|---|---|---|
| 828 | L | 837 | L |
| 877 | Y | 886 | Y |
| 948 | A | 957 | A |
| 949 | L | 958 | L |
| 950 | G | 959 | G |

Residue conservation supports comparison with the human structure; it does not itself measure ATP binding or structure in rat.
