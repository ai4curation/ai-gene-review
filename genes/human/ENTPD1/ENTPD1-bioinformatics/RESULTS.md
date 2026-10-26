# ENTPD1 product reconstruction

The six source-described human products reconstruct exactly from the captured UniProt alternative-sequence records and match the independently retrieved isoform FASTA records. The calculation retains every imported product. It does not establish their enzyme activity or biological interchangeability.

| Product | Length | Unchanged N-terminal TM segment projected to | Unchanged C-terminal TM segment projected to | Canonical active-site residue projected to | Canonical lipidation-site residue projected to |
| --- | ---: | --- | --- | ---: | --- |
| P49961-1 | 510 | 17–37 | 479–499 | 174 | 13 |
| P49961-2 | 517 | 24–44 | 486–506 | 181 | 20 |
| P49961-3 | 306 | 24–44 | absent | 181 | 20 |
| P49961-4 | 372 | absent | 341–361 | 36 | absent |
| P49961-5 | 402 | absent | 371–391 | 66 | absent |
| P49961-6 | 522 | 29–49 | 491–511 | 186 | 25 |

These are sequence-coordinate consequences, not a topology predictor or new experimental evidence. A retained catalytic residue does not prove activity. Products -3, -4 and -5 lose different canonical segments; no general claim of soluble enzyme function is justified. The placental clone study's 517/306-residue products and native placental enzyme preparations remain distinct evidence objects. Synthetic deletions used in palmitoylation or rat structural experiments are not treated as these natural products. Primary assay and preparation boundaries are documented in [the public original-evidence guide](../ENTPD1-reference-guide.md).

The reusable standard-library script applies exact VSP coordinates after checking any supplied sequence preimages, checks nonoverlap, and compares the full resulting sequence with the separate FASTA. It projects only unchanged canonical residues. It uses no sequence-similarity threshold, random model, gene-specific coordinate, or encoded biological verdict. Human input is the unchanged inputs/P49961.json and inputs/P49961-isoforms.fasta. Direct output is results/products.json.

The same script ran successfully on the independent rat Entpd1 record P97687 and its separate FASTA: one 511-residue displayed product matched exactly. Corruption checks reject wrong displayed FASTA, missing alternative-sequence definitions, wrong variant preimages and extra FASTA records. The reusable check_reconstruction.py runs these checks from the exact supplied inputs; replay receipts are preserved with the curation session. This is a different input from the human target, although an ortholog rather than an unrelated family.

Runtime: Python 3.12.9; only the standard library is required. These frozen results can be reproduced offline using the README commands. No new environment, topology prediction or activity model is required. The separate annotation-source/PAINT judgment remains in the review and reference guide.
