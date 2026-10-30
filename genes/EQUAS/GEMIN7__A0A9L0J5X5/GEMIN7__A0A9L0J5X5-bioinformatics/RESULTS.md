# Donkey GEMIN7 (A0A9L0J5X5): orthology and sequence comparison

Reproduce (from this folder): `uv run --script compare_orthologs.py`
Raw output: `compare_orthologs_output.txt`.

## Method

The script fetches UniProt JSON entries for the donkey target A0A9L0J5X5 and for five comparators
(human Q9H840, bovine Q17QA0, S. pombe G2TRR1, horse A0A9L0T0I7 and the longer donkey gene model
A0A9L0ICL9), reports each entry's PANTHER cross-references, and computes global pairwise identity
(Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5) against the donkey sequence,
expressed over aligned columns. It also tests whether the donkey sequence is an exact substring of
each comparator.

## Results (from compare_orthologs_output.txt)

- A0A9L0J5X5: 131 aa, PANTHER PTHR14679 / PTHR14679:SF1, unreviewed (TrEMBL).
- Human Q9H840 (Swiss-Prot): 131 aa, PTHR14679:SF1, 115/131 identical (87.8%).
- Bovine Q17QA0 (Swiss-Prot): 125 aa, PTHR14679:SF1, 108/131 aligned columns identical (82.4%).
- Horse A0A9L0T0I7: 131 aa, PTHR14679:SF1, 130/131 identical (99.2%).
- Donkey A0A9L0ICL9: 206 aa, PTHR14679:SF1; A0A9L0J5X5 is an exact substring of it (its C-terminal 131 residues).
- S. pombe G2TRR1 (Swiss-Prot gem7): 91 aa, PTHR14679:SF1, 25/140 aligned columns identical (17.9%).

## Interpretation

The donkey protein sits in the same PANTHER family and subfamily (PTHR14679:SF1, the only subfamily of
PTHR14679) as the experimentally characterised human GEMIN7 and S. pombe Gem7. It is the same length as
human GEMIN7 and highly identical across its full length, so it is a full-length ortholog of the human
protein. Transfer of the human/fission yeast SMN-complex functions is grounded on this subfamily
membership. The fission yeast identity is low, as expected for a small, fast-evolving protein, and is
reported only to document that the subfamily spans fungi and mammals. These are statements about
predicted sequences only; no donkey protein has been studied experimentally.
