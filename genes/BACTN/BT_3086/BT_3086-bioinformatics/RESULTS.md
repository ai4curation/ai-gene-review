# BT_3086 (Q8A369) vs FjDex31A (A5FBI1): active-site residue conservation

Script: `residue_check.py` (run: `uv run --with biopython python residue_check.py`);
raw output in `residue_check.out`. Sequences fetched live from UniProt.

Global pairwise alignment (BLOSUM62, gap open -10, extend -0.5) of BT_3086 (834 aa)
with the structurally characterized *Flavobacterium johnsoniae* GH31 dextranase
FjDex31A (Fjoh_4430, A5FBI1, 836 aa): 830 aligned positions, 535 identical
(64.5% identity over aligned positions).

FjDex31A residues singled out by the crystal-structure study (PMID:31552702) as
unique to this GH31 dextranase (subsite -2 Gly273/Tyr524, Trp376, Leu308-cisGln309)
plus Asp412 (the D412A substrate-complex mutant; catalytic nucleophile position):

| FjDex31A | BT_3086 position | BT_3086 residue | conserved |
|---|---|---|---|
| G273 | 271 | G | yes |
| L308 | 306 | L | yes |
| Q309 | 307 | Q | yes |
| W376 | 374 | W | yes |
| D412 | 410 | D | yes |
| Y524 | 522 | Y | yes |

Conclusion: every dextranase-specific active-site residue reported for FjDex31A is
conserved in BT_3086, consistent with BT_3086 being a GH31 dextranase-type
alpha-1,6-glucan hydrolase rather than a canonical exo-acting alpha-glucosidase
(alpha-glucosidase II), which is how it is named in UniProt/GenBank.
