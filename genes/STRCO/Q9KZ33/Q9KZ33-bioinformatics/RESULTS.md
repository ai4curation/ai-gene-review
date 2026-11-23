# Q9KZ33 (SCO7099) bioinformatics: comparison with M. tuberculosis ECF41 sigma factors

Script: `compare_ecf41_relatives.py` (output in `compare_ecf41_relatives.out`). Sequences fetched
live from UniProt REST; global Needleman-Wunsch alignment, BLOSUM62, gap open -10 / extend -0.5.

## Results

| Pair | Full-length identity | N-terminal sigma2/sigma4 region (1-170) | C-terminal extension |
|---|---|---|---|
| Q9KZ33 vs P9WGH3 (Mtb SigI, same PANTHER subfamily SF43) | 33.0% (273 cols) | 34.2% | 31.2% |
| Q9KZ33 vs L0TCG5 (Mtb SigJ, PANTHER SF36, IBA seed) | 34.7% (271 cols) | 35.0% | 34.2% |

## Interpretation

- Q9KZ33 aligns over essentially its full length (~270 of 300 residues) to both Mtb ECF41 sigma
  factors, including the ~130-residue C-terminal extension. The UniProt record lists an NTF2-like
  superfamily match (SSF54427; IPR032710) for this extension, the same fold class (SnoaL_2) that
  defines the C-terminal regulatory extension of group ECF41 sigma factors.
- Pairwise identity does not discriminate SigI from SigJ (both ~33-35%); the subfamily placement
  (SF43 with SigI) therefore rests on PANTHER's HMM classification, not on this pairwise check.
- No residue-level conclusion about activity is drawn; the sigma2 and sigma4 regions are intact by
  InterPro/SUPFAM matches (IPR052704, IPR013324, SSF88659).
