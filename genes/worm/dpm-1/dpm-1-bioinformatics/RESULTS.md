# dpm-1: exact selected product and same-gene reference

Selected U4PF58 has 51 residues; reference Q9TYJ7 has 239 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 189–239 | 1–51 | 51 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Domain: Glycosyltransferase 2-like | 8–176 | 0 / 169 | 0 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.

## Re-run 2026-10-20: target sequence read from the UniProt record

The analysis script was revised so it reads the target sequence from the gene's UniProt record rather than from the ProtNLM2 source file, and was re-run; `results.json` and related outputs now reflect this re-run. The original results above are kept unchanged for the record.

Selected U4PF58: 51 residues. Same-gene full-length Q9TYJ7: 239 residues. Human DPM1 O60762: 260 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

### Selected product vs full-length same-gene product

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 189–239 | 1–51 | 51 |

| Reference feature | Interval | Mapped / length |
|---|---|---|
| Domain: Glycosyltransferase 2-like | 8–176 | 0 / 169 |

### Full-length worm DPM-1 vs human DPM1

Aligned columns: 238; identical: 154 (64.7% over aligned columns).

The fragment's residues map to human DPM1 positions [211, 260], with 33 identical residues.

### DXD-type motif start positions

- Q9TYJ7: [96]
- U4PF58: []
- O60762: [118]

A shared segment does not establish that a truncated product is expressed, folds, localizes, or catalyzes the full-length reaction.

Inputs: dpm-1-uniprot.txt, dpm-1-same-gene-reference.json, human/DPM1/DPM1-uniprot.txt. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
