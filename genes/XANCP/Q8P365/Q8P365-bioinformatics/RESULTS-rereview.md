# Q8P365 (btuE, XCC4213) re-review bioinformatics

Scripts: `align_btuE_rereview.py` (output `align_btuE_rereview.out`) and
`panther_tree_path_rereview.py` (output `panther_tree_path_rereview.out`).

## Phylogenetic placement (PANTHER 19 tree, PTHR11592)

Q8P365 descends from PTN000173904 (Gammaproteobacteria, subfamily PTHR11592:SF40), the same node that contains experimentally characterized E. coli BtuE (P06610).
Q8P365 and the Xanthomonas paralog Q8PAI2 (XCC1501) arise from a lineage-specific duplication node PTN008521337 beneath PTN000173904.
PAINT placed GO:0008379 thioredoxin peroxidase activity at PTN000173904 by IBD with P06610 as the seed, and GO:0004602 glutathione peroxidase activity and GO:0034599 cellular response to oxidative stress at the family root PTN002480721.

## Pairwise comparison with E. coli BtuE

Q8P365 is 181 aa and is 49.2% identical to E. coli BtuE (P06610, 183 aa) over the global alignment, with no internal gaps except a two-residue gap near position 120.
Q8P365 C37 aligns to P06610 C37 (peroxidatic cysteine), and Q8P365 C83 aligns to P06610 C83 (resolving-cysteine position on helix alpha2 of atypical 2-Cys GPx-like peroxiredoxins).
The remaining catalytic tetrad residues are conserved: Q8P365 Q71 aligns to P06610 Q71, and W143/N144 align to P06610 W145/N146.
Q8P365 has no selenocysteine and no apparent N-terminal signal peptide by inspection (no predictor was run), consistent with a cytoplasmic Cys-GPx.
The paralog Q8PAI2 has a hydrophobic N-terminal extension (MSLNRLLVLVFAGLFSTAAVAAG), which looks like a signal peptide, and keeps both cysteines (C60, C106).

## Conclusion

Q8P365 is a full-length, catalytically complete member of the BtuE subfamily, and phylogeny places it in the same PAINT clade as E. coli BtuE.
Transfer of BtuE's thioredoxin-dependent hydroperoxide reductase activity is supported by node placement and by conservation of both the peroxidatic and resolving cysteines.
No species-specific experiment has been reported.
