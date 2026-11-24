# Sur (Q9VL32) nucleotide-binding domain motif scan

Script: `nbd_motifs.py` (run as `python -I nbd_motifs.py ../Sur-uniprot.txt`); raw output in `results.txt`.

## Results

- Walker A motifs at the two UniProt ATP-binding ranges: NBD1 874-881 GKNGSGKT; NBD2 2016-2023 GRTGSGKS. Both are intact P-loops.
- Candidate Walker B motifs: NBD1 VVIMDD at 986 (aspartate in place of the catalytic glutamate), NBD2 LVLDE at 2141 (catalytic glutamate retained).
- ABC signature: ISGGQ at 966 (NBD1 region). The simple regex did not find a canonical signature in NBD2; this is inconclusive and was not examined further.

## Interpretation

The pattern (degenerate NBD1 with D in Walker B, consensus NBD2 with E) is the asymmetric
ABCC-type arrangement also seen in mammalian SUR1/SUR2, where NBD2 is the hydrolytically
competent site. It is consistent with ATP binding at both NBDs and ATP hydrolysis at NBD2,
but no hydrolysis has been measured for the Drosophila protein.
