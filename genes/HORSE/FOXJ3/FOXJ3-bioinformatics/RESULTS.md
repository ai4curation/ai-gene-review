# FOXJ3 (horse F6SCJ5): sequence comparison with reviewed human and mouse FOXJ3

Script: `compare_sequences.py` (run with `uv run --script compare_sequences.py`); raw output in `compare_sequences.out`.
Inputs: `../FOXJ3-uniprot.txt` (F6SCJ5), `human-Q9UPW0-uniprot.txt`, `mouse-Q8BUR3-uniprot.txt` (downloaded from UniProt REST 2026-10-21).

## Results

- Horse F6SCJ5 is 623 aa; human Q9UPW0 is 622 aa; mouse Q8BUR3 is 623 aa.
- Horse vs human: 611 identical positions, 98.1% identity over the horse length, no gap columns in horse and one in human.
- Horse vs mouse: 594 identical positions, 95.3% identity over the horse length.
- The fork-head DNA-binding domain (horse 78-173) is 95/96 identical to both human and mouse, with no gaps.
- F6SCJ5 is therefore a full-length FOXJ3 product, not a fragment or truncated gene model.

## Family placement

All three proteins carry the same PANTHER assignments in UniProt: PTHR46078 (FORKHEAD BOX PROTEIN J2 FAMILY MEMBER) and subfamily PTHR46078:SF3 (FORKHEAD BOX PROTEIN J3). The FOXJ2 paralogs (human Q9P0K8, mouse Q9ES18) sit in PTHR46078:SF1.
