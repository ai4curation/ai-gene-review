# Vmn2r73: benchmark product A0A3B2WCZ5 vs canonical product D3Z7M3

Selected A0A3B2WCZ5 has 496 residues (Ensembl ENSMUSP00000156768, transcript Vmn2r73-203, non-canonical); reference D3Z7M3 has 851 residues (Ensembl canonical transcript ENSMUST00000077478, Vmn2r73-201).

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5; Kyte-Doolittle 19-residue window, threshold 1.6.

## Aligned segments

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1-429 | 1-429 | 429 |
| 506-548 | 430-472 | 41 |
| 566-568 | 473-475 | 3 |
| 631-640 | 476-485 | 4 |
| 698-708 | 486-496 | 3 |

## Reference features mapped onto the selected product

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Signal:  | 1-18 | 18 / 18 | 18 |
| Transmembrane: Helical | 584-606 | 0 / 23 | 0 |
| Transmembrane: Helical | 618-639 | 9 / 22 | 4 |
| Transmembrane: Helical | 651-675 | 0 / 25 | 0 |
| Transmembrane: Helical | 695-718 | 11 / 24 | 3 |
| Transmembrane: Helical | 738-762 | 0 / 25 | 0 |
| Transmembrane: Helical | 774-794 | 0 / 21 | 0 |
| Transmembrane: Helical | 800-822 | 0 / 23 | 0 |
| Domain: G-protein coupled receptors family 3 profile | 581-844 | 21 / 264 | 7 |

## Kyte-Doolittle hydrophobic windows (candidate TM helices)

| Sequence | Start | End | Max mean KD |
|---|---|---|---|
| A0A3B2WCZ5 | 1 | 21 | 1.84 |
| D3Z7M3 | 1 | 21 | 1.84 |
| D3Z7M3 | 581 | 606 | 2.42 |
| D3Z7M3 | 616 | 677 | 2.48 |
| D3Z7M3 | 686 | 715 | 2.22 |
| D3Z7M3 | 727 | 762 | 1.88 |
| D3Z7M3 | 772 | 793 | 2.11 |
| D3Z7M3 | 799 | 826 | 2.34 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or signals. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py`.
