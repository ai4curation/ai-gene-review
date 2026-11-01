# LPXD1 / LPXD2 alignment to E. coli LpxD

Script: `align_lpxd.py` (fetches F4JGP6, F4JIP6 and P21645 from UniProt REST;
global Needleman-Wunsch alignment, BLOSUM62, gap open -10 / extend -0.5, free
end gaps). Raw output: `align_output.txt`.

## Results (run 2026-10-26)

- AtLpxD1 vs EcLpxD: identity 104/280 aligned = 37.1%
- AtLpxD2 vs EcLpxD: identity 104/278 aligned = 37.4%
- AtLpxD1 vs AtLpxD2: identity 215/288 aligned = 74.7%
- EcLpxD catalytic H239 -> AtLpxD1 H217, AtLpxD2 H216 (both conserved; these match the UniProt ACT_SITE positions 217 and 216).
- EcLpxD R293 -> AtLpxD1 K271, AtLpxD2 R270. The Arg-to-Lys substitution in AtLpxD1 reported by Li et al. 2011 is present in the current gene model.
- Both current gene models align over a similar part of the EcLpxD N-terminal region (68/100 and 66/100 of EcLpxD residues 1-100 aligned).

## Interpretation

The catalytic histidine is conserved in both paralogs, so neither is an obvious
pseudoenzyme. AtLpxD1 carries the R293K substitution at a residue implicated in
acyl-ACP binding. Li et al. 2011 stated that only AtLpxD2 has the N-terminal
nucleotide-binding domain; in the current UniProt gene models both proteins
align comparably over this region, so that statement may reflect the 2011
gene models and should not be relied on without re-checking. The aromatic
acceptor-binding residues mentioned by Li et al. were not named in the paper
and were not checked here. Pairwise alignment cannot establish activity.
