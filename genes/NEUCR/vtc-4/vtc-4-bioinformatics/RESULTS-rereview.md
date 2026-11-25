# VTC-4 (Q7SCX0) phylogenetic placement and catalytic-site check (re-review, 2026-10-21)

Script: `vtc_placement_rereview.py` (run with `uv run --script vtc_placement_rereview.py`);
raw output: `vtc_placement_rereview.out.txt`; alignment: `vtc_family_rereview.aln.fasta` (MAFFT --auto).

## Sequences
Target Q7SCX0 (771 aa, full-length canonical TrEMBL product; SPX 1-151, VTC core, 3 C-terminal TM helices),
its N. crassa SPX-VTC paralog Q1K5R9 (NCU01745), S. cerevisiae Vtc4/Vtc3/Vtc2 (P47075/Q02725/P43585),
S. pombe vtc4/vtc2 (P78810/O13718), Chaetomium thermophilum Vtc4 (G0SCH1), T. brucei vtc4 (Q382V9, outgroup).

## PANTHER
All Vtc4 orthologs, including the target, are PTHR46140:SF1; yeast Vtc2, Vtc3, S. pombe vtc2 and the
N. crassa paralog NCU01745 are PTHR46140:SF2.

## Tree
NJ (BLOSUM62) groups the target with C. thermophilum Vtc4 (80.5% identity), then with S. cerevisiae Vtc4
and S. pombe vtc4 (~57% identity) in a Vtc4 clade separate from the Vtc2/Vtc3 clade (~31-34% identity
to the target), which contains the N. crassa paralog NCU01745. The target is therefore the N. crassa
Vtc4 ortholog, not a Vtc2/Vtc3-type accessory subunit.

## Catalytic / ATP-binding residues (yeast Vtc4 numbering, UniProt P47075 FT from PubMed:19390046)
The target retains all eight mapped residues: K203 (K200), R268 (R264), R270 (R266), K285 (K281),
K298 (K294), Y363 (Y359), R365 (R361) and the active-site lysine K462 (K458). Yeast Vtc2 (I522) and
Vtc3 (L527) carry the non-catalytic substitutions at the active-site lysine.

## SPX inositol-polyphosphate-binding region (yeast Vtc4 126-133)
Target G129-F-Y-K-I-I-K-K136 is conserved with the yeast and Chaetomium Vtc4 basic surface motif
(GF.KI.KK).

## Limitations
NJ distance tree on a small taxon set, not a maximum-likelihood tree; residue conservation does not
prove catalytic activity, which has not been assayed for the N. crassa protein.
