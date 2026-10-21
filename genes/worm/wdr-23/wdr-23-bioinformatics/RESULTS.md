# wdr-23: exact selected product and same-gene reference

Selected S6FN32 has 498 residues; reference P90794 has 571 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 74–571 | 1–498 | 498 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Repeat: WD 1 | 162–201 | 40 / 40 | 40 |
| Repeat: WD 2 | 266–305 | 40 / 40 | 40 |
| Repeat: WD 3 | 309–349 | 41 / 41 | 41 |
| Repeat: WD 4 | 357–396 | 40 / 40 | 40 |
| Repeat: WD 5 | 435–479 | 45 / 45 | 45 |
| Repeat: WD 6 | 482–521 | 40 / 40 | 40 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.

## Re-run 2026-10-20: target sequence read from the UniProt record

The analysis script was revised so it reads the target sequence from the gene's UniProt record rather than from the ProtNLM2 source file, and was re-run; `results.json` and related outputs now reflect this re-run. The original results above are kept unchanged for the record.

Target S6FN32 has 498 residues; WDR-23A P90794 has 571 residues; WDR-23B P90794-2 has 530 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

### Aligned segments vs WDR-23A (P90794)

| Reference interval | Target interval | Identical residues |
|---|---|---|
| 74-571 | 1-498 | 498 |

### Aligned segments vs WDR-23B (P90794-2)

| Reference interval | Target interval | Identical residues |
|---|---|---|
| 33-530 | 1-498 | 498 |

### P90794 features mapped onto the target

| Feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Repeat: WD 1 | 162-201 | 40 / 40 | 40 |
| Repeat: WD 2 | 266-305 | 40 / 40 | 40 |
| Repeat: WD 3 | 309-349 | 41 / 41 | 41 |
| Repeat: WD 4 | 357-396 | 40 / 40 | 40 |
| Repeat: WD 5 | 435-479 | 45 / 45 | 45 |
| Repeat: WD 6 | 482-521 | 40 / 40 | 40 |
| Region: Disordered | 51-75 | 2 / 25 | 2 |

### DDB1-binding DxR boxes (Staab et al. 2013, R342H/R389H in WDR-23A)

| WDR-23A R | WDR-23A motif | Target R | Target motif | Retained |
|---|---|---|---|---|
| 342 | DKR | 269 | DKR | True |
| 389 | DLR | 316 | DLR | True |

Interpretation: the target is an N-terminally shorter product of the same gene. Every residue of the target is identical to the C-terminal part of both characterised isoforms; the target lacks only the isoform-specific N-terminal extensions. A shared segment does not by itself establish that the shorter product is expressed, folds or localises like either isoform.

Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
