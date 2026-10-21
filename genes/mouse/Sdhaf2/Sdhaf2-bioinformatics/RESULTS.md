# Sdhaf2: A0A494B8X4 product versus canonical mouse and human SDHAF2

Selected A0A494B8X4 has 135 residues; reference Q8C6I2 has 164 residues.

Script: `compare_products.py` (standard library only; reads `../Sdhaf2-uniprot.txt`, fetches
Q8C6I2 and Q9NX18 from UniProt REST and Pfam coordinates from the InterPro API). Raw output:
`compare_products.out`. Reproduce with `python3 compare_products.py`.

## Sequence relationship

| Item | Result |
|---|---|
| Identical prefix with Q8C6I2 | residues 1-121 of both sequences |
| A0A494B8X4 divergent tail | residues 122-135, DTPEEGVGSHCRWL (14 aa) |
| Q8C6I2 residues absent from A0A494B8X4 | 122-164 (43 aa) |
| Tail present in Q8C6I2 or human Q9NX18 | no |

UniProt Q8C6I2 lists three Swiss-Prot isoforms. Isoform 2 replaces 122-164 with GMPYAELHLGIIR,
and isoform 3 lacks residues 1-94. The A0A494B8X4 tail is neither of these, so A0A494B8X4 is a third,
Ensembl-predicted alternative C-terminus (ENSMUST00000237827) that shares its first 121 residues
with the canonical product.

## Domains and conserved features

| Feature | Q8C6I2 (canonical) | A0A494B8X4 | Q9NX18 (human) |
|---|---|---|---|
| Pfam PF03937 Sdh5 | 66-141 | 66-124 (truncated) | 68-143 |
| Predicted mitochondrial transit peptide (UniProt Q8C6I2, ECO:0000255) | 1-27 | 1-27 retained, identical | n/a |
| RGxxE motif (RGMLE; human G78 is in it) | 75-79 | 75-79 retained | 77-81 |

The mouse-to-human offset is +2 (mouse 31-60 aligns at human 33), so the paraganglioma variant
human G78 corresponds to mouse G76, which A0A494B8X4 retains. The product lacks canonical residues 122-141
of the Pfam Sdh5 domain (the Pfam hit on A0A494B8X4 extends to 124 only by matching the divergent tail) and the entire canonical C-terminal segment 122-164.

## Interpretation

The N-terminal targeting sequence and the SDHA-interacting RGxxE region are retained, so mitochondrial
import is expected. Whether the truncated Sdh5 fold folds and supports SDHA flavinylation is not
determined by sequence analysis; this is neither evidence of activity nor of loss of activity.
