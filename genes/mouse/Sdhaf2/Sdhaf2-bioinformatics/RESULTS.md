# Sdhaf2: exact selected product and same-gene reference

Selected A0A494B8X4 has 135 residues; reference Q8C6I2 has 164 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–122 | 1–122 | 121 |
| 126–138 | 123–135 | 3 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Transit peptide: Mitochondrion | 1–27 | 27 / 27 | 27 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.

## Re-run 2026-10-20: target sequence read from the UniProt record

The analysis script was revised so it reads the target sequence from the gene's UniProt record rather than from the ProtNLM2 source file, and was re-run; `results.json` and related outputs now reflect this re-run. The original results above are kept unchanged for the record.

Selected A0A494B8X4 has 135 residues; reference Q8C6I2 has 164 residues.

Script: `compare_products.py` (standard library only; reads `../Sdhaf2-uniprot.txt`, fetches
Q8C6I2 and Q9NX18 from UniProt REST and Pfam coordinates from the InterPro API). Raw output:
`compare_products.out`. Reproduce with `python3 compare_products.py`.

### Sequence relationship

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

### Domains and conserved features

| Feature | Q8C6I2 (canonical) | A0A494B8X4 | Q9NX18 (human) |
|---|---|---|---|
| Pfam PF03937 Sdh5 | 66-141 | 66-124 (truncated) | 68-143 |
| Predicted mitochondrial transit peptide (UniProt Q8C6I2, ECO:0000255) | 1-27 | 1-27 retained, identical | n/a |
| RGxxE motif (RGMLE; human G78 is in it) | 75-79 | 75-79 retained | 77-81 |

The mouse-to-human offset is +2 (mouse 31-60 aligns at human 33), so the paraganglioma variant
human G78 corresponds to mouse G76, which A0A494B8X4 retains. The product lacks canonical residues 122-141
of the Pfam Sdh5 domain (the Pfam hit on A0A494B8X4 extends to 124 only by matching the divergent tail) and the entire canonical C-terminal segment 122-164.

### Interpretation

The N-terminal targeting sequence and the SDHA-interacting RGxxE region are retained, so mitochondrial
import is expected. Whether the truncated Sdh5 fold folds and supports SDHA flavinylation is not
determined by sequence analysis; this is neither evidence of activity nor of loss of activity.
