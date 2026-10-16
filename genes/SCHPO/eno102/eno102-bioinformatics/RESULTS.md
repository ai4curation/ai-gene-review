# eno102 (Q8NKC2) vs eno101 (P40370): paralog comparison

Script: `compare_enolases.py` (run with `uv run --with biopython python genes/SCHPO/eno102/eno102-bioinformatics/compare_enolases.py`).
Inputs are the UniProt flat files already fetched into `genes/SCHPO/eno101/` and `genes/SCHPO/eno102/`.

Method: global BLOSUM62 alignment (Biopython PairwiseAligner, gap open -10, extend -0.5); the
residues UniProt annotates as ACT_SITE or BINDING (substrate, Mg2+) in eno101 are mapped through
the alignment to eno102.

Output (2026-10-06):

```
eno101 length 439, eno102 length 440
aligned pairs 439, identical 288, identity over eno101 length 65.6%
Annotated eno101 functional residues -> aligned eno102 residue:
  H159 -> H160, E168 -> E169, E211 -> E212 (proton donor), D246 -> D247 (Mg),
  E295 -> E296 (Mg), D320 -> D321 (Mg), K345 -> K346 (proton acceptor),
  S372-S375 -> S373-S376, K396 -> K397
All annotated functional residues conserved: True
```

Interpretation: eno102 is a divergent (about 66% identical) paralog of eno101, not a recent
duplicate, but every catalytic, substrate-binding and Mg2+-binding residue annotated for the
enolase family is retained at the aligned position. Nothing in the sequence suggests loss of
phosphopyruvate hydratase activity; note that the UniProt residue annotations themselves are
by similarity (ECO:0000250), so this is consistency evidence, not a direct activity measurement.
