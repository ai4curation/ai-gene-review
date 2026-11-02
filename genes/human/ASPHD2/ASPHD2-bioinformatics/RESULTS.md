# ASPHD2 catalytic-residue check

Script: `asphd2_sites.py` (run with `uv run python asphd2_sites.py`; raw output in `results.txt`). It fetches sequences and features live from UniProt and prints a ±6-residue window around every site.

## Alignment

Human ASPHD2 (Q6ICH7, 369 aa) aligns locally to the C-terminal catalytic domain of aspartyl/asparaginyl beta-hydroxylase ASPH (Q12797). The alignment covers ASPH 526-758 and ASPHD2 125-364: 224 aligned positions, 75 identical (33.5%).

## Fe(II)- and 2-oxoglutarate-binding residues of ASPH

- **Both iron-binding histidines are conserved:** ASPH H679 aligns to ASPHD2 H283, and ASPH H725 aligns to ASPHD2 H328.
- 2-oxoglutarate contacts W625, S668, R688, H690 and R735 are conserved (ASPHD2 W228, S272, R292, H294, R341). M689 is substituted (C293), as in ASPHD1.

## Conclusion

ASPHD2 keeps the complete Fe(II) and 2-oxoglutarate binding site of ASPH, consistent with UniProt's suggestion that it may be a 2-oxoglutarate-dependent dioxygenase. Its substrate is unknown, and no activity has been measured. By contrast, the paralog ASPHD1 lacks the first iron-binding histidine.
