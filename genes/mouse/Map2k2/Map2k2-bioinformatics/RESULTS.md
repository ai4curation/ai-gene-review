# Map2k2 (Q63932) sequence comparison: results

Script: `compare_mek_sequences.py` (Biopython global alignment, BLOSUM62, gap open -10, extend -0.5),
reading sequences from the cached UniProt flat files in this repository. Raw output: `compare_mek_sequences.out`.

## Results

- Mouse Map2k2 (401 aa) vs human MAP2K2 P36507 (400 aa): 377 identical residues over 400 aligned pairs (identity 0.9425).
- Mouse Map2k2 vs human MAP2K1 Q02750 (393 aa): 322 identical residues over 392 aligned pairs (identity 0.8214).
- The UniProt-annotated catalytic and regulatory residues of mouse Map2k2 (ATP-binding K101, catalytic D194, activation-loop S222 and S226) align to identical residues in human MAP2K2 (K101, D194, S222, S226) and in human MAP2K1 (K97, D190, S218, S222).

## Interpretation

Sequence identity is not used here to establish the relationship. Orthology to human MAP2K2 rests on
PANTHER subfamily membership: both Q63932 and P36507 are classified in PTHR47448:SF3 (MITOGEN-ACTIVATED
PROTEIN KINASE KINASE 2), whereas MAP2K1 (Q02750, mouse P31938) is in PTHR47448:SF2. The alignment is
consistent with that placement (higher identity to human MAP2K2 than to MAP2K1) and shows that the
residues required for catalysis and for RAF-dependent activation are conserved, so there is no
sequence-level indication of loss of MAP2K catalytic activity in the mouse protein.
