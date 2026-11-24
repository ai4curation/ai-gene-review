# HRDE-1 slicer catalytic tetrad check

Script: `catalytic_tetrad.py` (local BLOSUM62 pairwise alignment of HRDE-1/Q09249
against human AGO2/Q9UKV8, fetched live from UniProt).

| AGO2 position | AGO2 residue | HRDE-1 position | HRDE-1 residue | conserved |
|---|---|---|---|---|
| 597 | D | 749 | E | False |
| 637 | E | 797 | Y | False |
| 669 | D | 829 | V | False |
| 807 | H | 966 | E | False |

Alignment score: 385.0.

Interpretation: none of the four AGO2 slicer (DEDH) catalytic positions is
conserved in HRDE-1 in this pairwise alignment. This is consistent with the
published statement that WAGO-clade Argonautes lack key catalytic residues
(Shirayama et al. 2012, PMID:22738726). Caveat: a single pairwise alignment
can shift by a few residues in poorly conserved regions; a family MSA would be
more definitive, but no residue matching the tetrad pattern was observed.
