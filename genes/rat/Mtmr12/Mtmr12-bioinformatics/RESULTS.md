# Mtmr12: exact selected product and same-gene reference

Selected A0A8I5ZMD5 has 732 residues; reference Q5FVM6 has 748 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–7 | 1–7 | 1 |
| 8–8 | 23–23 | 1 |
| 17–29 | 24–36 | 6 |
| 45–48 | 37–40 | 3 |
| 57–748 | 41–732 | 691 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Domain: Myotubularin phosphatase | 206–644 | 439 / 439 | 439 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.

## Re-run 2026-10-20: target sequence read from the UniProt record

The analysis script was revised so it reads the target sequence from the gene's UniProt record rather than from the ProtNLM2 source file, and was re-run; `results.json` and related outputs now reflect this re-run. The original results above are kept unchanged for the record.

Target A0A8I5ZMD5 (732 aa) from `Mtmr12-uniprot.txt`; reviewed rat Q5FVM6 (748 aa); human MTMR12 Q9C0I1 (747 aa); human MTM1 Q13496 (603 aa).

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

Target N-terminal 40 aa: `MVVSWVIRKFLCFCCKVCFPFPGYPSFLSFPKPWRISLLP`

Reviewed rat N-terminal 56 aa: `MLGKGGVGGGGGTKAPKPSFVSYVRPEEIHTNEKEVTEKEEVTLHLLPGEQLLCEA`

### Target vs reviewed rat Q5FVM6

| Reference interval | Target interval | Identical residues |
|---|---|---|
| 1–7 | 1–7 | 1 |
| 8–8 | 23–23 | 1 |
| 17–29 | 24–36 | 6 |
| 45–48 | 37–40 | 3 |
| 57–748 | 41–732 | 691 |

| Reference domain | Interval | Mapped | Identical |
|---|---|---|---|
| Myotubularin phosphatase | 206–644 | 439 | 439 |

### Target vs human MTMR12

Identical aligned residues: 619 of 732 target residues.

| Human interval | Target interval | Identical residues |
|---|---|---|
| 1–7 | 1–7 | 2 |
| 8–8 | 23–23 | 1 |
| 17–29 | 24–36 | 6 |
| 44–47 | 37–40 | 3 |
| 56–95 | 41–80 | 30 |
| 96–187 | 82–173 | 83 |
| 189–747 | 174–732 | 494 |

### MTM1 catalytic loop (active-site C375, CX5R motif 375–381) mapped to target

| MTM1 pos | MTM1 res | Target pos | Target res |
|---|---|---|---|
| 373 | V | 374 | L |
| 374 | H | 375 | L |
| 375 | C | 376 | E |
| 376 | S | 377 | E |
| 377 | D | 378 | N |
| 378 | G | 379 | A |
| 379 | W | 380 | S |
| 380 | D | 381 | D |
| 381 | R | 382 | L |
| 382 | T | 383 | C |
| 383 | A | 384 | C |

Sequence correspondence does not establish expression, folding, localization or binding.
