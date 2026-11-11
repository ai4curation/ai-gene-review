# P91866 (F32H2.6) ketosynthase-region alignment

Script: `align_ks.py` (Biopython local alignment, BLOSUM62, gap open -10, extend -0.5).
Raw output: `align_ks_output.txt`. Run with `uv run python align_ks.py` from the repository environment.

## Results

- P91866 is 187 residues long.
- Against residues 1-500 of C. elegans FASN-1 (P91871, F32H2.5), P91866 residues 1-167 align
  to FASN-1 residues 28-194 with 111/165 identical aligned pairs (67.3%).
- Against residues 1-500 of human FASN (P49327), P91866 residues 11-167 align to FASN
  residues 2-158 with 62/155 identical aligned pairs (40.0%).
- The alignment to both proteins stops at P91866 residue 167 (the "FDLQGPSHSAD" segment), which
  corresponds to human FASN residue 158, immediately before the human KS active-site motif
  "DTACSSS" (FASN Cys161). The remaining 20 residues of P91866 (168-187,
  "KINFSTKKRMTKLRNRNSIV") show no similarity to the FASN KS sequence; the KS catalytic
  cysteine (FASN C161) and the two catalytic histidines (H293, H331) have no counterpart in P91866.
- P91866 contains four cysteines (positions 23, 38, 120, 139), none of which aligns to FASN C161.

## Interpretation

P91866 corresponds only to the N-terminal half of the KS N-terminal (Pfam PF00109) subdomain of
FASN-1 and lacks all three residues of the KS Cys-His-His catalytic triad, as well as the KS
C-terminal subdomain (PF02801) and every downstream FAS domain. It cannot form the acyl-enzyme
intermediate and therefore cannot have beta-ketoacyl-ACP synthase (acyltransferase) activity on its
own. The high nucleotide/protein identity to the 5' part of fasn-1 in the neighbouring locus
F32H2.5 is consistent with a partial duplication of fasn-1 (Kniazeva et al. 2004 note the extended
nucleotide identity). Whether the F32H2.6 product is made as a stable protein is not known.
