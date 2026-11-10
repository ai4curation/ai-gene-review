# Svil (M9MRN1) isoform comparison

Script: `compare_isoforms.py` (fetches UniProt records at run time; Biopython local
alignment, BLOSUM62, gap open -11 / extend -1). Raw output: `analysis-output.txt`.

## Results

- M9MRN1 (Svil isoforms AG/AH, 1872 aa) has no InterPro or Pfam match. Its only
  annotated features are two predicted coiled coils (865-919, 1627-1654) and one
  Phobius transmembrane helix at the extreme C terminus (1853-1871).
- Residues 1-1292 of M9MRN1 are identical to residues 62-1353 of the longest Svil
  isoform AE (X2JAM4, 4526 aa). Residues 1293-1872 (including the predicted TM helix)
  are not shared with X2JAM4 in any exact block of 30 aa or more.
- X2JAM4 carries the supervillin/villin headpiece (HP, 4463-4526) and gelsolin-like
  InterPro signatures (IPR029006, IPR036180, IPR007122), all far downstream of the
  segment shared with M9MRN1. M9MRN1 therefore lacks every gelsolin-like repeat and the
  headpiece domain.
- The best local alignment of M9MRN1 with human supervillin (O95425) has a raw score
  of 63 over 213 aligned pairs at 23.9% identity (M9MRN1 1304-1531 vs O95425
  828-1053). This is weak, compositionally biased similarity and is not taken as
  evidence of shared function.

## Interpretation

M9MRN1 is an N-terminal-region Svil product with an isoform-specific C-terminal
tail. The gelsolin-repeat and headpiece regions that confer F-actin binding on
vertebrate supervillin are absent from this product, so actin-binding functions
predicted for the domain-bearing Svil isoforms cannot be transferred to M9MRN1 by
domain inference. The C-terminal hydrophobic segment suggests a possible
tail-anchored membrane protein, but this rests on a single prediction.
