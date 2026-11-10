# P (C6G8B2) bioinformatics notes

## Comparison with Swiss-Prot P27898 (Myb-related protein P)

Script: `align_P27898.py` (fetches both sequences from UniProt REST, global
BLOSUM62 alignment, gap open -10, extend -0.5).

Output summary (run 2026-10-28):

- P27898 length 399; C6G8B2 length 336.
- Identical residues in positions 1-250: 249/250 (single difference at
  position 4, T in P27898 vs A in C6G8B2).
- The two R2R3 MYB repeats (C6G8B2 residues 9-61 and 62-116, PROSITE PS51294)
  lie entirely inside the identical N-terminal region.
- After about residue 250 the two sequences diverge completely. The P27898
  C-terminus (for example runs of LLLLLL and RRR) does not align with the
  C6G8B2 C-terminus, which instead carries the Pfam P_C domain (PF06640,
  InterPro IPR010588 Myb-rel_proteinP/Y1_C).

Interpretation: C6G8B2 and P27898 are products of the same p1 gene (same
R2R3 MYB domain and N-terminal half). The divergent C-terminus is consistent
with a frameshift or different splice/annotation in one of the two
sequences; this analysis cannot tell which is correct, so no source defect
is asserted.

## Domain architecture (from the UniProt C6G8B2 record)

- R2R3 MYB DNA-binding domain: two HTH myb-type repeats, residues 9-61 and
  62-116 (PROSITE PS51294, Pfam PF00249 x2).
- Disordered region 138-222 (MobiDB-lite).
- C-terminal P_C domain (PF06640), shared with maize P2 and Y1-type MYBs.
