# Rhp (Q9XYY9) re-review: relationship to vertebrate rhophilins

Script: `compare_rhophilins_rereview.py` (raw output: `compare_rhophilins_rereview.out`).
Global Needleman-Wunsch alignments (BLOSUM62, gap open -10, extend -0.5) of the
full-length UniProt sequences.

| Pair | Identity | Aligned columns |
|---|---|---|
| Q9XYY9 fly Rhp vs Q8IUC4 human RHPN2 | 0.356 | 755 |
| Q9XYY9 fly Rhp vs Q8TCX5 human RHPN1 | 0.339 | 758 |
| Q9XYY9 fly Rhp vs Q61085 mouse Rhpn1 | 0.347 | 730 |
| Q9XYY9 fly Rhp vs Q8BWR8 mouse Rhpn2 | 0.354 | 773 |
| Q8IUC4 human RHPN2 vs Q8TCX5 human RHPN1 | 0.408 | 703 |

Interpretation: fly Rhp is roughly equidistant (34-36% identity) from both
vertebrate paralogs, which are more similar to each other (41%). This is the
pattern expected if the RHPN1/RHPN2 split is a vertebrate duplication and fly Rhp
is a single pre-duplication co-ortholog of both. It agrees with PANTHER placing
Rhp in its own subfamily (PTHR23031:SF15) outside RHPN1 (SF6) and RHPN2 (SF5), and
with the PAINT node PTN001126281 that propagates GO:0051497 to fly Rhp from both a
RHPN1 donor (mouse, MGI:1098783) and a RHPN2 donor (human, Q8IUC4). Pairwise
identity alone does not define orthology; the phylogenetic placement comes from
PANTHER/PAINT, and these numbers are only consistent with it.
