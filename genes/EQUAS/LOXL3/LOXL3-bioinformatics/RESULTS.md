# LOXL3: donkey-human sequence comparison

Script: `align_to_human.py` (Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5; with per-50-residue identity windows).
Command: `uv run python align_to_human.py ../LOXL3-uniprot.txt ../../../human/LOXL3/LOXL3-uniprot.txt 1 25 26 607 609 611 634 670`
Raw output: `alignment_output.txt`.

## Results

- The donkey sequence A0A9L0K7N3 (824 residues) aligns to human P58215 (753 residues) with 95.62% identity across 753 paired residues, covering 100% of the human sequence.
- Human Met1 aligns to donkey Met53: the donkey model has a 52-residue N-terminal extension upstream of the region corresponding to the human signal peptide (human 1-25 = donkey 53-77), plus an ~18-residue insertion near donkey 283-300.
- The copper-binding histidines (human His607, His609, His611 = donkey His678, His680, His682) and the lysine tyrosylquinone (LTQ) cofactor residues (human Lys634 and Tyr670 = donkey Lys705 and Tyr741) are conserved.
- Donkey 651-800 are 150/150 identical to human 580-729, i.e. the C-terminal lysyl oxidase catalytic domain is invariant.

## Interpretation

The donkey protein retains the complete catalytic lysyl oxidase domain and all four SRCR domains. Because the signal-peptide-equivalent segment is internal in this gene model, the N-terminal extension is probably a gene-model artefact; the real donkey protein is expected to be secreted like human LOXL3.
