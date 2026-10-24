# Glorund isoform comparison (re-review, 2026-10-21)

Script: `compare_isoforms_rereview.py` (fetches live UniProt sequences; output in `results-rereview.json`).

## Result

- Q8INJ6 (Glorund isoform C) is 179 residues; Q9VGH5 (Glorund isoforms A/B/D) is 586 residues.
- The first 168 residues of Q8INJ6 are identical to residues 1-168 of Q9VGH5. Q8INJ6 then ends in an 11-residue isoform-C-specific tail, ILRYSAARLLK, where Q9VGH5 continues LDIKTDREGILF.
- Using the qRRM boundaries from PMID:35699205 (qRRM1 45-141, qRRM2 142-234, qRRM3 475-562), Q8INJ6 contains all of qRRM1, only 27 residues (142-168) of qRRM2, and none of qRRM3 or the glycine-rich region.
- The qRRM1 RNA-contact residues identified in PMID:28380354 (R52, W58) are inside the shared prefix. qRRM2 residues K149 and Y155 are also inside the prefix, but the qRRM2 fold is truncated, so the isoform cannot be assumed to contain a functional second qRRM.

## Interpretation

Q8INJ6 is a short alternative product of the glo gene with one complete qRRM. Warden et al. 2023 (PMID:37427795) found that Glo proteins with only one intact qRRM do not bind or repress nanos mRNA in vivo. Isoform C alone is therefore not expected to carry out nanos repression. Whether isoform C is made as a protein, and what it does, has not been tested.
