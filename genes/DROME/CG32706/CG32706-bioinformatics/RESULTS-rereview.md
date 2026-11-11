# CG32706 (Q8IRM9) re-review sequence comparison

Script: `compare_sequences_rereview.py` (raw output: `compare_sequences_rereview.out`).
Sequences fetched live from UniProt REST; global Needleman-Wunsch alignment, BLOSUM62,
gap open -10, extend -0.5.

## Phylogenetic placement (input to the comparison, not output of it)

PANTHER places Q8IRM9 in PTHR12311:SF7 (ACTIVATOR OF BASAL TRANSCRIPTION 1), the only
subfamily of PTHR12311, together with S. cerevisiae ESF2 (P53743), S. pombe esf2
(O74362) and vertebrate ABT1 (human Q9ULW3, mouse Q9QYL7). The GOA IBA rows derive from
PAINT node PANTHER:PTN000267771. Q8IRM9 is the only UniProt entry for FlyBase FBgn0052706.

## Results

| Pair | Lengths | Aligned columns | Identity | Similarity |
|------|---------|-----------------|----------|------------|
| Q8IRM9 vs Q9ULW3 (human ABT1) | 230 vs 272 | 211 | 0.294 | 0.526 |
| Q8IRM9 vs P53743 (yeast ESF2) | 230 vs 316 | 217 | 0.336 | 0.548 |

Observations from the alignment output:

- The RRM (Q8IRM9 62-140) and the conserved post-RRM segment (fly `GWVEFISKSGAKKIALELNNKP`
  / yeast `GWAEFIRKRDAKLCAETLNGNI`; fly `LPRFKWYYLTD` / yeast `LPGFKWADLTE`) align
  without gaps, i.e. the ABT1/Esf2 core is intact.
- The fly protein is shorter because it lacks the long acidic/low-complexity N-terminal
  extension of yeast Esf2 (yeast residues ~1-110 are largely gapped) and ends in a
  Lys/Ala-rich repeat (`EMAAKKAEMAAKK`) rather than the yeast C-terminal tail.
  The yeast C-terminal region (residues 206-317) needed for Dbp8 binding is only
  partly represented, so conservation of the Dbp8-cofactor interaction cannot be
  inferred from sequence.
- Q8IRM9 is a complete protein (start Met, full RRM and family core), not a fragment.
