# A0A2I4G8T1 (walnut LOC109005703) - UGT73C relationship check

Script: `compare_ugt73c.py` (run with `uv run --with biopython python compare_ugt73c.py`).
Raw output: `compare_ugt73c_output.txt`. Sequences and PANTHER subfamilies are fetched live from UniProt REST.

## Method

Global Needleman-Wunsch alignment (BLOSUM62, gap open -10, extend -0.5) of the 488-aa
target against Arabidopsis UGT73C1-C7, UGT73B1 and the two UGT89 proteins that seed the
PAINT node PTN008730368. Identity is counted over aligned (non-gap) columns.
The PSPG (plant secondary product glycosyltransferase) box was located by regex.

## Results

- Target length 488 aa, PANTHER PTHR48047:SF229 (UDP-GLYCOSYLTRANSFERASE 73C3-RELATED). The protein is full length (comparable to the 490-496 aa Arabidopsis UGT73C proteins); it is not a fragment.
- PSPG box (44 aa, residues 348-391): WAPQLLILSHPSVGGFLTHCGWNSCIEGISAGVPMLTWPLFGDQ; last residue: Q
- Identity to Arabidopsis UGT73C members is essentially flat: UGT73C5 58.7%, UGT73C3 58.4%, UGT73C1 58.2%, UGT73C4 58.2%, UGT73C6 58.0%, UGT73C2 57.2%, UGT73C7 54.8%.
- Lower identity to UGT73B1 (43.8%) and UGT89B1/UGT89A2 (36.6% / 35.3%).

## Interpretation

The walnut protein is a UGT73C-group enzyme, but it is equidistant from all members of the
Arabidopsis UGT73C1-C6 tandem cluster. This is the pattern expected if that cluster
expanded within the Brassicales after divergence from the Fagales lineage, so the walnut
protein is best read as a co-ortholog of the cluster as a whole rather than an ortholog of
any one member. Pairwise identity alone cannot resolve the PANTHER SF229 placement
(with UGT73C3/C4) versus SF153 (UGT73C5/C6) or SF88 (UGT73C1); we record the PANTHER
assignment as given. Acceptor specificities that differ between UGT73C members
(brassinosteroids, cytokinins, flavonols, trichothecenes) are therefore not transferable
to the walnut protein.

The PSPG box is intact, including the conserved HCGWNS core. Its final residue is Q, the
residue commonly associated with UDP-glucose use in plant family-1 UGTs; this is
consistent with, but does not prove, a UDP-glucose donor preference.
