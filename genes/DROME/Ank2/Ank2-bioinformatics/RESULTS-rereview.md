# Ank2-PE (Q3KN55) versus giant Ank2 isoforms: re-review sequence mapping (2026-10-20)

Script: `compare_isoforms_rereview.py` (stdlib only; fetches current UniProt sequences and ANK repeat features).
Raw output: `compare_isoforms_rereview-output.txt`.

## Results

- Q3KN55 (Ank2-PE) is 697 aa. Residues 159-667 of Q3KN55 are identical to residues 9-517 of both the UniProt gene-centric canonical Ank2 product M9MRX4 (isoform U, 13559 aa) and Ank2-L Q7KU92 (4083 aa), a 509-aa shared block.
- Q3KN55 has 158 N-terminal residues and a 30-residue C-terminal tail (KDLIAKKITDHIDTVYLMQLFWIRHQEFFI) that are not shared with Ank2-L.
- Of the 21 UniProt ANK repeat features on M9MRX4 and on Q7KU92, 13 lie fully inside the block shared with Q3KN55. Q3KN55 therefore lacks the C-terminal third of the ankyrin repeat domain and all of the giant-isoform sequence C-terminal to residue 517, which includes the extended C-terminal regions of Ank2-L/XL.
- Q3KN55 covers 3.8% of M9MRX4 and 12.5% of Q7KU92.
- Q3KN55 and the 547-aa short product M9PBV0 (isoform X) share 539 identical residues (Q3KN55 159-697 = M9PBV0 9-547); they differ only at the N terminus.

## Interpretation

Q3KN55 is a genuine alternative product of Ank2 made of an isoform-specific His-rich N terminus plus the first 13 ANK repeats. It has none of the domains that the literature uses to explain the microtubule-organising and synapse-stabilising activities of giant Ank2. Weber et al. 2019 (PMID:31475145) place the L1-CAM-dependent synaptic targeting determinants of Ank2-L in the central and C-terminal part of the ARD; Q3KN55 keeps the N-terminal and part of the central repeats but lacks the C-terminal repeats, so whether it can bind L1-family CAMs or reach the presynaptic membrane cannot be predicted from the sequence alone.
This is a sequence-mapping result only. It does not show what the short product does.
