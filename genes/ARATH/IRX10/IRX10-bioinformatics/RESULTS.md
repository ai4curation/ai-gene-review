# IRX10 clade: which GT47 protein is the ortholog in each comparator species?

Script: `irx10_clade_identity.py` (run from the repository root with
`uv run python genes/ARATH/IRX10/IRX10-bioinformatics/irx10_clade_identity.py`).
Output: `identity.tsv` (71 proteins). Sequences and PANTHER subfamilies come
from the EBI Proteins API, and Pfam PF03016 (Exostosin_GT47) members per taxon from
the InterPro API. Identity is identical positions in a global BLOSUM62 alignment
divided by the length of the shorter sequence. Generated 2026-10-30.

## Reference proteins

| Accession | Name | Length | Id. vs AtIRX10 | Id. vs AtIRX10L | PANTHER |
|---|---|---|---|---|---|
| A0A2K2BTI7 | poplar POPTR_001G068100 | 412 | 0.908 | 0.854 | PTHR11062:SF370, PTHR11062 |
| A0A2K2B808 | poplar POPTR_003G162000 | 413 | 0.891 | 0.85 | PTHR11062:SF339, PTHR11062 |
| Q8S1X7 | rice IRX10 (LOC_Os01g70200) | 417 | 0.85 | 0.834 | PTHR11062:SF200, PTHR11062 |
| A9RGD8 | Physcomitrium GT47A | 449 | 0.767 | 0.773 | PTHR11062:SF200, PTHR11062 |
| Q9ZUV3 | Arabidopsis IRX7/FRA8 (GT47, other clade) | 448 | 0.388 | 0.402 | PTHR11062, PTHR11062:SF229 |
| Q16394 | human EXT1 (GT47 outgroup) | 746 | 0.308 | 0.299 | PTHR48261, PTHR48261:SF3 |

Land-plant IRX10-clade members are 77-91% identical to Arabidopsis IRX10/IRX10L.
Other GT47 proteins (IRX7/FRA8, human EXT1) sit at 30-40%, the background for the
shared GT47 fold. Poplar POPTR_001G068100 shares PANTHER subfamily SF370 with
AtIRX10; its paralog POPTR_003G162000 is in SF339. Rice IRX10 and moss GT47A are
in SF200 with AtIRX10L.

## Klebsormidium nitens (charophyte alga): 23 GT47 proteins, top 6

| Accession | Name | Length | Id. vs AtIRX10 | Id. vs AtIRX10L | PANTHER |
|---|---|---|---|---|---|
| A0A1Y1IIS5 | KFL_003980130 | 470 | 0.704 | 0.718 | PTHR11062:SF200, PTHR11062 |
| A0A1Y1I9J6 | KFL_002540250 | 564 | 0.466 | 0.472 | PTHR11062:SF200, PTHR11062 |
| A0A1Y1I3M1 | KFL_001440240 | 695 | 0.439 | 0.441 | PTHR11062:SF200, PTHR11062 |
| A0A1Y1INC8 | KFL_010030010 | 733 | 0.335 | 0.337 | PTHR11062:SF376, PTHR11062 |
| A0A1Y1IGR4 | KFL_005030040 | 1439 | 0.33 | 0.333 | PTHR11062:SF376, PTHR11062 |
| A0A1Y1I9M4 | KFL_003690050 | 501 | 0.32 | 0.323 | PTHR11062, PTHR11062:SF281 |

Exactly one protein, A0A1Y1IIS5 (KFL_003980130), falls in the IRX10 range. The
next best is at 0.472. Jensen et al. 2018 (PMID:29460505)
report KfXYS1 at 75% identity to AtXYS1/IRX10L over 376 residues. The peptides
encoded by their cloning primers match this entry: the forward primer encodes
RSSLF, found at residue 26 (the paper starts its construct at residue 27), and the
reverse primer encodes the C-terminus RGDDEN, which is the end of A0A1Y1IIS5
(`kfxys1_primer_check.txt`, written by the same script).
A0A1Y1IIS5 is therefore the KfXYS1 locus (K. flaccidum NIES-2285 is now
K. nitens). The paper's construct ends at residue 445, while the UniProt model
has 470 residues with the same ends, so the two gene models differ internally by
about 25 residues (not resolved here).

## Chlamydomonas reinhardtii (chlorophyte alga): 42 GT47 proteins, top 6

| Accession | Name | Length | Id. vs AtIRX10 | Id. vs AtIRX10L | PANTHER |
|---|---|---|---|---|---|
| A0A2K3DZ60 | CHLRE_03g204100v5 | 803 | 0.35 | 0.357 | PTHR11062, PTHR11062:SF268 |
| A0A2K3DFW9 | CHLRE_09g414900v5 | 824 | 0.345 | 0.349 | PTHR11062, PTHR11062:SF268 |
| A0A2K3DDH5 | CHLRE_09g390750v5 | 826 | 0.335 | 0.347 | PTHR11062, PTHR11062:SF268 |
| A0A2K3DJA5 | CHLRE_07g325050v5 | 768 | 0.345 | 0.347 | PTHR11062, PTHR11062:SF268 |
| A8ILW6 | CHLRE_06g311950v5 | 815 | 0.342 | 0.345 | PTHR11062, PTHR11062:SF268 |
| A0A2K3CXZ5 | CHLRE_14g619854v5 | 1020 | 0.347 | 0.34 | PTHR11062:SF376, PTHR11062 |

No Chlamydomonas GT47 protein exceeds 0.357 identity to IRX10L, the same as the
unrelated-GT47 background, and none is in subfamily SF200 or SF370. This agrees
with Jensen et al. 2018, who found no IRX10/XYS1 orthologs outside
Klebsormidiophyceae and Zygnematophyceae among algae. Absence is shown for one
chlorophyte genome only.

## Caveats

- Pairwise identity is not a phylogeny; subfamily assignments come from PANTHER.
- PF03016 membership relies on InterPro's Pfam matches; a protein with an
  unrecognised GT47 domain would be missed.
