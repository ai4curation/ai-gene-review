# SEC23A (donkey canonical A0A9L0JMP6): ortholog and paralog comparison

Reproduce (from this folder):
`uv run --script compare_orthologs.py > compare_orthologs_output.txt`

The script fetches sequences live from UniProt and globally aligns each comparator to the
donkey canonical SEC23A product A0A9L0JMP6 (Biopython PairwiseAligner, BLOSUM62, gap open
-10, extend -0.5). Raw output is in `compare_orthologs_output.txt`.

## Findings

- A0A9L0JMP6 is 765 aa, the same length as human SEC23A Q15436 and mouse Sec23a Q01405.
- Human SEC23A Q15436 (PTHR11141:SF7): 760 identical of 765 aligned pairs (99.35%), no gaps.
- Mouse Sec23a Q01405 (PTHR11141:SF7): 760 identical of 765 aligned pairs (99.35%).
- Human SEC23B Q15437 (paralog, PTHR11141:SF10): 651 identical of 765 aligned pairs (85.10%).
- Yeast Sec23 P15303 (PTHR11141:SF0): 384 identical of 753 aligned pairs (51.00%).
- Every characterised functional residue of human SEC23A is present at the identical position
  in the donkey protein: zinc-finger ligands C61, C66, C85, C88; F382 (the residue mutated
  in cranio-lenticulo-sutural dysplasia); gelsolin-like domain PPP-motif-binding residues
  F628, Y672, Y678, F681.
- The yeast Sec23 arginine finger R722 (inserted into the Sar1 active site) aligns to donkey R716.

## Interpretation

The donkey canonical SEC23A product is essentially identical to human and mouse SEC23A,
in the same PANTHER subfamily (UniProt cross-reference PTHR11141:SF7), and markedly more
similar to SEC23A orthologs than to the SEC23B paralog subfamily (SF10). The residues
needed for zinc binding, the SAR1 GAP arginine finger and PPP-motif binding are retained,
so there is no sequence evidence of loss or divergence of the SEC23A functions. No
experimental data exist for the donkey protein itself; all functional statements for it
are inferences from orthologs within SF7 (human, mouse) and from the SEC23 family (yeast).
