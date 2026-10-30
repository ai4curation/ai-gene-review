# ORC5 (horse A0A3Q2KSP7): comparison with human and mouse ORC5

Script: `compare_orc5.py` (run with `uv run --script compare_orc5.py`); raw output in `compare_orc5.out`.
Inputs: horse sequence from `../ORC5-uniprot.txt`; human O43913 and mouse Q9WUV0 sequences
downloaded from the UniProt REST API (`human_O43913.fasta`, `mouse_Q9WUV0.fasta`).
Alignment: Biopython PairwiseAligner, global, BLOSUM62, gap open -10, gap extend -0.5.

## Family placement

UniProt lists the horse protein in PANTHER PTHR12705 (ORIGIN RECOGNITION COMPLEX SUBUNIT 5),
subfamily PTHR12705:SF0. The family has a single subfamily; the human (O43913), mouse (Q9WUV0),
fly (Q24169), budding yeast (P50874) and fission yeast (O43114) ORC5 proteins are all in
PTHR12705:SF0 (`interpro/panther/PTHR12705/PTHR12705-entries.csv`). The IBA rows on the horse
protein come from PAINT node PTN000295037.

## Sequence comparison

- Horse A0A3Q2KSP7 is 437 aa; human O43913 is 435 aa.
- Horse vs human: 432 paired positions, 391 identical (90.51% of paired), covering 99.31% of the
  human sequence and 98.86% of the horse sequence.
- Horse vs mouse: 432 paired positions, 376 identical (87.04%).
- The horse protein is therefore a full-length ORC5, not a fragment.

## Residues mapped from human ORC5 sites described in PMID:28112645

| Human site | Human | Horse | Horse position |
|---|---|---|---|
| Walker A P-loop 37-44 | GHTASGKT | GHTASGKT | 37-44 |
| tether R104 | R | R | 104 |
| Walker B 125-128 | DKAE | DKAE | 125-128 |
| P139 | P | P | 139 |
| arginine finger R143 | R | R | 143 |
| Y182 (adenine contact) | Y | Y | 182 |
| R226 (adenine contact) | R | R | 226 |

All ATP-site and inter-subunit residues described for human ORC5 are conserved in the horse protein.
This is consistent with the horse protein binding ATP the way human ORC5 does; it does not show that
the horse protein hydrolyses ATP (human ORC5 is not the catalytic ATPase of ORC; its Walker B motif
is non-canonical DKAE).
