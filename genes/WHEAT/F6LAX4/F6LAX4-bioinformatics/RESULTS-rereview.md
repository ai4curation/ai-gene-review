# F6LAX4 phylogenetic placement among PP2A scaffold A subunits (re-review, 2026-10-20)

Script: `phylogeny_rereview.py` (run with `uv run --no-project --with biopython python phylogeny_rereview.py`).
Raw output: `phylogeny_rereview.out`; sequences `pp2aa_rereview.fa`; MAFFT alignment `pp2aa_rereview.aln.fa`.

Method: 21 full-length PTHR10648 A-subunit sequences (grasses, Amborella, tomato, Physcomitrium,
Arabidopsis PP2AA1-3, human PPP2R1A/B, fly Pp2A-29B, budding/fission yeast) fetched from UniProt,
aligned with MAFFT --auto, percent identity over gap-free columns, neighbour-joining tree on
identity distance rooted on the two yeasts. NJ on identity distance is a coarse method; no bootstrap
was run, so only the large-scale groupings below are interpreted.

## Results

- F6LAX4 is 587 aa, full length relative to Arabidopsis PP2AA1-3 (587-588 aa) and human PPP2R1A (589 aa); it is not a fragment.
- Percent identity of F6LAX4: Brachypodium 98.1, maize 96.9-97.3, rice 95.7, Amborella 87.0-91.0, tomato 88.1-89.9, Arabidopsis PP2AA2 89.8, PP2AA3 88.6, PP2AA1/RCN1 85.2, Physcomitrium 84.6-85.0, human PPP2R1A 59.3, fly Pp2A-29B 57.8, fission yeast paa1 51.5, budding yeast TPD3 45.6.
- In the NJ tree F6LAX4 groups with the other grass A subunits; the eudicot A subunits (tomato and all three Arabidopsis paralogs) form a separate group, so the Arabidopsis PP2AA1/PP2AA2/PP2AA3 paralogs arose after the monocot-eudicot split and F6LAX4 is a co-ortholog of all three.
- PANTHER places all grass A subunits (wheat, rice, maize, Brachypodium) and Amborella/Physcomitrium A subunits in PTHR10648:SF4 together with the animal/fungal scaffolds Pp2A-29B, paa-1, TPD3, paa1 and pppA, whereas Arabidopsis PP2AA1 is in SF29 and PP2AA2/PP2AA3 in SF36. The sequence data show this split is a subfamily-HMM boundary, not a functional divergence: F6LAX4 is more similar to the eudicot SF29/SF36 proteins (85-90%) than to any non-plant SF4 member (at most 57.8%).
