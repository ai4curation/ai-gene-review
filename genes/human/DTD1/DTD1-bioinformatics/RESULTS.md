# DTD1: exact selected product and same-gene reference

Selected A0A2R8YCT7 has 127 residues; reference Q8TEA8 has 209 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–127 | 1–127 | 125 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Motif: Gly-cisPro motif, important for rejection of L-amino acids | 139–140 | 0 / 2 | 0 |
| Binding site:  | 4–4 | 1 / 1 | 1 |
| Binding site:  | 6–6 | 1 / 1 | 1 |
| Binding site:  | 28–28 | 1 / 1 | 1 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.

## Re-run 2026-10-20: target sequence read from the UniProt record

The analysis script was revised so it reads the target sequence from the gene's UniProt record rather than from the ProtNLM2 source file, and was re-run; `results.json` and related outputs now reflect this re-run. The original results above are kept unchanged for the record.

Selected A0A2R8YCT7: 127 residues; reference Q8TEA8: 209 residues.
Exact shared N-terminal prefix: residues 1-124. Selected C-terminal tail after the prefix: `TLF` (reference continues `GKFGAYMQVH...`).

Ensembl transcript encoding the selected product (Ensembl REST lookup of ENSG00000125821):

| Transcript | Biotype | Canonical | Protein | Length |
|---|---|---|---|---|
| ENST00000647441 | nonsense_mediated_decay | False | ENSP00000493969 | 127 |

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1-127 | 1-127 | 125 |

Reference feature mapping (coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Motif: Gly-cisPro motif, important for rejection of L-amino acids | 139-140 | 0 / 2 | 0 |
| Binding site:  | 4-4 | 1 / 1 | 1 |
| Binding site:  | 6-6 | 1 / 1 | 1 |
| Binding site:  | 28-28 | 1 / 1 | 1 |
| Beta strand:  | 2-15 | 14 / 14 | 14 |
| Beta strand:  | 18-32 | 15 / 15 | 15 |
| Helix:  | 39-51 | 13 / 13 | 13 |
| Helix:  | 67-70 | 4 / 4 | 4 |
| Beta strand:  | 73-78 | 6 / 6 | 6 |
| Helix:  | 80-82 | 3 / 3 | 3 |
| Beta strand:  | 87-90 | 4 / 4 | 4 |
| Helix:  | 99-116 | 18 / 18 | 18 |
| Helix:  | 119-121 | 3 / 3 | 3 |
| Beta strand:  | 122-124 | 3 / 3 | 3 |
| Beta strand:  | 131-146 | 0 / 16 | 0 |

All Ensembl transcripts of the gene:

| Transcript | Biotype | Canonical | Protein length |
|---|---|---|---|
| ENST00000377452 | protein_coding | True | 209 |
| ENST00000647441 | nonsense_mediated_decay | False | 127 |
| ENST00000494921 | protein_coding | False | 213 |
| ENST00000916786 | protein_coding | False | 206 |
| ENST00000916787 | protein_coding | False | 235 |
| ENST00000916788 | protein_coding | False | 246 |
| ENST00000916789 | protein_coding | False | 209 |
| ENST00001007920 | nonsense_mediated_decay | False | 139 |
| ENST00001051436 | protein_coding | False | 272 |
| ENST00001076986 | nonsense_mediated_decay | False | 53 |
| ENST00001107262 | protein_coding | False | 198 |
| ENST00001125480 | protein_coding | False | 209 |
| ENST00001131918 | protein_coding | False | 209 |

A shared segment does not establish that a truncated product is stable, folds, dimerizes or catalyzes.
