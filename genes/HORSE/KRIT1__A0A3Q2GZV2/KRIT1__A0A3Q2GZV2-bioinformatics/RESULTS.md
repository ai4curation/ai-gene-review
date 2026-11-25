# KRIT1 (horse, A0A3Q2GZV2): comparison with human KRIT1 (O00522)

Script: `compare_to_human.py` (run with `uv run compare_to_human.py`); raw output in `compare_to_human.out`.
Inputs are the local UniProt flat files `../KRIT1__A0A3Q2GZV2-uniprot.txt` and
`genes/human/KRIT1/KRIT1-uniprot.txt`.

## Results

- Global alignment (BLOSUM62, gap open -10, extend -0.5): horse 736 aa vs human 736 aa,
  736 aligned pairs, 726 identical (98.6%), no gaps in either sequence.
- All three N-terminal NPx(Y/F) motifs are present at the same positions in both proteins:
  NPAY (192), NPLF (231), NPYF (250).
- Region identity, using the regions annotated in human O00522:
  - Nudix-like N-terminal domain 1-170: 167/170 identical
  - ITGB1BP1 (ICAP1) interaction region 172-195: 24/24 identical
  - ANK repeats 287-419: 131/133 identical
  - RAP1B interaction region 430-452: 23/23 identical
  - FERM domain 420-734: 310/315 identical
- The 10 substitutions (T7I, S61N, A109S, N309S, V380T, K521Q, L679I, A693T, I719V, I723M,
  horse/human) are conservative or lie outside the mapped interaction regions.

## Interpretation

The horse protein is a full-length KRIT1 with every mapped interaction surface of the human
protein intact. Orthology does not rest on this similarity alone: the UniProt record places
A0A3Q2GZV2 in PANTHER PTHR13283:SF11 (KREV INTERACTION TRAPPED PROTEIN 1), the same subfamily
as human O00522, mouse Q6S5J6 and zebrafish F1REV3, and separate from the FRMD8 subfamilies of
the same family. The horse protein also receives IBAs from the PAINT nodes PTN002665063,
PTN002665064 and PTN004412369. This analysis supports transferring molecular functions that are
established experimentally for human or mouse KRIT1, but it is not itself evidence of function
in horse cells.
