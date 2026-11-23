# Horse LOXL3 (A0A9L0TKN1) vs human LOXL3 (P58215)

Script: `compare_to_human.py` (PEP 723; run with `uv run --script compare_to_human.py`).
Raw output: `compare_to_human_output.txt`.

## Method

Global Needleman-Wunsch alignment (Biopython PairwiseAligner, BLOSUM62, gap open -10,
extend -0.5) of the horse unreviewed entry against the reviewed human canonical isoform
P58215-1. Human UniProt catalytic features (Cu-binding His607/His609/His611, LTQ
cross-link Lys634-Tyr670, both ECO:0000255/ECO:0000250) were mapped through the alignment.

## Results

- Horse A0A9L0TKN1 length: 753 aa; human P58215 length: 753 aa.
- Gapless end-to-end alignment: 753 aligned positions, 720 identical (95.6% identity).
- All copper-binding histidines conserved: human H607 (Cu-binding His) -> horse H607;
  H609 -> H609; H611 -> H611. Copper-binding motif segment identical
  (SWVWHECHGHYHSMDI).
- LTQ cofactor residues conserved: human K634 -> horse K634; human Y670 -> horse Y670.

## Interpretation

A0A9L0TKN1 is a full-length LOXL3 gene model (not a fragment or isoform): same length as
the human canonical product, with the signal peptide, four SRCR domains and the complete
lysyl-oxidase catalytic domain. UniProt and PANTHER place it in PTHR45817:SF2 (LYSYL
OXIDASE HOMOLOG 3), the same subfamily as human P58215 and mouse Q9Z175. Nothing in the
sequence argues against transfer of the conserved lysyl-oxidase catalytic function.
