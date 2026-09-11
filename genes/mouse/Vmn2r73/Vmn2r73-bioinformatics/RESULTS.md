# Vmn2r73: exact selected product and same-gene reference

Selected A0A3B2WCZ5 has 496 residues; reference D3Z7M3 has 851 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–429 | 1–429 | 429 |
| 506–548 | 430–472 | 41 |
| 566–568 | 473–475 | 3 |
| 631–640 | 476–485 | 4 |
| 698–708 | 486–496 | 3 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Signal:  | 1–18 | 18 / 18 | 18 |
| Transmembrane: Helical | 584–606 | 0 / 23 | 0 |
| Transmembrane: Helical | 618–639 | 9 / 22 | 4 |
| Transmembrane: Helical | 651–675 | 0 / 25 | 0 |
| Transmembrane: Helical | 695–718 | 11 / 24 | 3 |
| Transmembrane: Helical | 738–762 | 0 / 25 | 0 |
| Transmembrane: Helical | 774–794 | 0 / 21 | 0 |
| Transmembrane: Helical | 800–822 | 0 / 23 | 0 |
| Domain: G-protein coupled receptors family 3 profile | 581–844 | 21 / 264 | 7 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
