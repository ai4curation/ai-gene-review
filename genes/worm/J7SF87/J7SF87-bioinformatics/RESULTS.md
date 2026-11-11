# J7SF87 (SQRD-2, Y9C9A.16b) sequence comparison with human SQOR

Script: `align_sqor.py` (Biopython global alignment, BLOSUM62, gap open -10 / extend -0.5).
Inputs downloaded from UniProt REST: J7SF87 (Y9C9A.16b, 422 aa), Q9N2S1 (Y9C9A.16a, 361 aa),
C6KRP5 (SQRD-1, 422 aa), Q9Y6N5 (human SQOR, 450 aa, with its flat file for feature positions).
Raw output: `alignment_output.txt`.

## Results

- J7SF87 is 45.3% identical to human SQOR over 417 aligned positions.
- Both catalytic cysteines of human SQOR (Cys201 and Cys379, the cysteine persulfide intermediates,
  experimentally defined in Q9Y6N5) are conserved in J7SF87, as Cys169 and Cys351.
- All human FAD-binding feature positions align to identical or conservative residues in J7SF87
  (human S53 aligns to Ala; the other positions are identical), and J7SF87 carries the N-terminal
  GxGxxG dinucleotide-binding motif (GGGAGG at residue 18).
- J7SF87 begins 17 residues before that motif, so it has no counterpart of the N-terminal
  extension (mitochondrial transit peptide) of human SQOR. The same is true of the SQRD-1 model
  C6KRP5.
- The shorter Y9C9A.16a product (Q9N2S1) lacks the first 61 residues of J7SF87, including the
  GxGxxG FAD motif, but keeps both catalytic cysteines.
- J7SF87 and SQRD-1 (C6KRP5) share 317 of 422 residues (75.1%).

## Interpretation

J7SF87 retains the catalytic and FAD-binding residues of a functional type II (animal) SQR, so
there is no sequence argument for a pseudoenzyme. The sequence alone cannot say which sulfane
acceptor it uses, and the missing presequence leaves mitochondrial targeting supported only by
family membership.
