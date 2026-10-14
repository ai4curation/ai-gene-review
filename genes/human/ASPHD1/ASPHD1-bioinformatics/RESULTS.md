# ASPHD1 catalytic-residue check

Script: `asphd1_sites.py` (run with `uv run python asphd1_sites.py`; raw output in `results.txt`). It fetches sequences and features live from UniProt and prints a ±6-residue window around every site.

## Alignment

Human ASPHD1 (Q5U4P2, 390 aa) aligns locally to the C-terminal catalytic domain of aspartyl/asparaginyl beta-hydroxylase ASPH (Q12797). The alignment covers ASPH 518-755 and ASPHD1 134-382: 219 aligned positions, 83 identical (37.9%).

## Fe(II)- and 2-oxoglutarate-binding residues of ASPH

ASPH binds Fe(II) through two histidines, H679 and H725.

- **ASPH H679 (Fe ligand) aligns to ASPHD1 R304.** The window shows no histidine nearby in ASPHD1 (ASPH 673-685 GTHVWPHTGPTNC / ASPHD1 GARLEGRCGPTNA), so this Fe ligand is lost, not merely offset.
- **ASPH H725 (Fe ligand) aligns to ASPHD1 H349 (conserved).**
- 2-oxoglutarate contacts W625, S668, R688, H690 and R735 are conserved (ASPHD1 W241, S293, R313, H315, R362). M689 is substituted (C314).

## Conclusion

ASPHD1 keeps most of the 2-oxoglutarate pocket but lacks one of the two iron-binding histidines of ASPH. A 2-His iron site missing one histidine is not expected to support Fe(II)/2-oxoglutarate-dependent hydroxylation, so ASPHD1 is likely a non-catalytic paralog. This is a sequence inference: no activity, or lack of it, has been measured.
