# uap1.S re-review: Q6DCZ6 vs human UAP1 Q16222

Inputs: `../uap1.S-uniprot.txt` (frog sequence) and `../uap1.S-human-ortholog.json` (human UniProt record).
Global Biopython PairwiseAligner, BLOSUM62, gap open -10, extend -0.5.

Frog Q6DCZ6 length: 507; human Q16222 (displayed isoform AGX2) length: 522.
Aligned residue pairs: 505; identical: 382 (75.6%).

## Aligned blocks

| Human interval | Frog interval |
|---|---|
| 1-453 | 1-453 |
| 471-522 | 454-505 |

## Human alternative-sequence features

| Human interval | Description | Human positions aligned to frog |
|---|---|---|
| 454-470 | in isoform AGX1 | 0 |
| 454-454 | in isoform 3 | 0 |

## Human UDP-HexNAc binding-site residues mapped to frog

| Human pos | Human res | Frog pos | Frog res | Conserved | Ligands |
|---|---|---|---|---|---|
| 108 | L | 108 | L | yes | UDP-N-acetyl-alpha-D-galactosamine; UDP-N-acetyl-alpha-D-glucosamine |
| 110 | G | 110 | G | yes | UDP-N-acetyl-alpha-D-galactosamine; UDP-N-acetyl-alpha-D-glucosamine |
| 111 | G | 111 | G | yes | UDP-N-acetyl-alpha-D-galactosamine; UDP-N-acetyl-alpha-D-glucosamine |
| 196 | Q | 196 | Q | yes | UDP-N-acetyl-alpha-D-galactosamine; UDP-N-acetyl-alpha-D-glucosamine |
| 222 | G | 222 | G | yes | UDP-N-acetyl-alpha-D-galactosamine; UDP-N-acetyl-alpha-D-glucosamine |
| 223 | N | 223 | N | yes | UDP-N-acetyl-alpha-D-galactosamine; UDP-N-acetyl-alpha-D-glucosamine |
| 251 | C | 251 | C | yes | UDP-N-acetyl-alpha-D-galactosamine; UDP-N-acetyl-alpha-D-glucosamine |
| 252 | V | 252 | V | yes | UDP-N-acetyl-alpha-D-galactosamine; UDP-N-acetyl-alpha-D-glucosamine |
| 290 | G | 290 | G | yes | UDP-N-acetyl-alpha-D-galactosamine; UDP-N-acetyl-alpha-D-glucosamine |
| 303 | E | 303 | E | yes | UDP-N-acetyl-alpha-D-galactosamine; UDP-N-acetyl-alpha-D-glucosamine |
| 304 | Y | 304 | Y | yes | UDP-N-acetyl-alpha-D-galactosamine; UDP-N-acetyl-alpha-D-glucosamine |
| 327 | N | 327 | N | yes | UDP-N-acetyl-alpha-D-galactosamine; UDP-N-acetyl-alpha-D-glucosamine |
| 381 | F | 381 | F | yes | UDP-N-acetyl-alpha-D-glucosamine |
| 407 | K | 407 | K | yes | UDP-N-acetyl-alpha-D-galactosamine; UDP-N-acetyl-alpha-D-glucosamine |
| 472 | K | 455 | K | yes | UDP-N-acetyl-alpha-D-galactosamine; UDP-N-acetyl-alpha-D-glucosamine |

Binding-site positions conserved: 15 of 15.

Conservation of contact residues is consistent with, but does not by itself prove, retained catalysis;
substrate preference (GlcNAc-1-P vs GalNAc-1-P) of the frog product has not been measured.
