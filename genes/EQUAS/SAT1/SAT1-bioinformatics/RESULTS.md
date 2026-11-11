# SAT1: donkey-human sequence comparison

Script: `align_to_human.py` (Biopython PairwiseAligner, global, BLOSUM62, gap open -10, extend -0.5; with per-50-residue identity windows).
Command: `uv run python align_to_human.py ../SAT1-uniprot.txt ../../../human/SAT1/SAT1-uniprot.txt 27 28 92 140 152`
Raw output: `alignment_output.txt`.

## Results

- The donkey sequence A0A9L0KCT9 (171 residues) aligns to human P21673 (171 residues) with 97.08% identity across 171 paired residues, without gaps.
- The human catalytic Tyr140 is conserved (donkey Tyr140), as are the substrate/acetyl-CoA binding residues checked (Tyr27, Glu28, Glu92, Glu152).

## Interpretation

The donkey protein is a full-length SAT1 (SSAT1) ortholog with the catalytic machinery intact.
