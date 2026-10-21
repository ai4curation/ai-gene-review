# uap1.S: exact selected product and human ortholog reference

Selected Q6DCZ6 has 507 residues; reference Q16222 has 522 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–453 | 1–453 | 342 |
| 471–522 | 454–505 | 40 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|
| Binding site:  | 108–108 | 1 / 1 | 1 |
| Binding site:  | 108–108 | 1 / 1 | 1 |
| Binding site:  | 110–110 | 1 / 1 | 1 |
| Binding site:  | 110–110 | 1 / 1 | 1 |
| Binding site:  | 111–111 | 1 / 1 | 1 |
| Binding site:  | 111–111 | 1 / 1 | 1 |
| Binding site:  | 196–196 | 1 / 1 | 1 |
| Binding site:  | 196–196 | 1 / 1 | 1 |
| Binding site:  | 222–222 | 1 / 1 | 1 |
| Binding site:  | 222–222 | 1 / 1 | 1 |
| Binding site:  | 223–223 | 1 / 1 | 1 |
| Binding site:  | 223–223 | 1 / 1 | 1 |
| Binding site:  | 251–251 | 1 / 1 | 1 |
| Binding site:  | 251–251 | 1 / 1 | 1 |
| Binding site:  | 252–252 | 1 / 1 | 1 |
| Binding site:  | 252–252 | 1 / 1 | 1 |
| Binding site:  | 290–290 | 1 / 1 | 1 |
| Binding site:  | 290–290 | 1 / 1 | 1 |
| Binding site:  | 303–303 | 1 / 1 | 1 |
| Binding site:  | 303–303 | 1 / 1 | 1 |
| Binding site:  | 304–304 | 1 / 1 | 1 |
| Binding site:  | 304–304 | 1 / 1 | 1 |
| Binding site:  | 327–327 | 1 / 1 | 1 |
| Binding site:  | 327–327 | 1 / 1 | 1 |
| Binding site:  | 381–381 | 1 / 1 | 1 |
| Binding site:  | 407–407 | 1 / 1 | 1 |
| Binding site:  | 407–407 | 1 / 1 | 1 |
| Binding site:  | 472–472 | 1 / 1 | 1 |
| Binding site:  | 472–472 | 1 / 1 | 1 |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and human ortholog reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.

## Re-run 2026-10-20: target sequence read from the UniProt record

The analysis script was revised so it reads the target sequence from the gene's UniProt record rather than from the ProtNLM2 source file, and was re-run; `results.json` and related outputs now reflect this re-run. The original results above are kept unchanged for the record.

Target Q6DCZ6: 507 aa (sequence from `uap1.S-uniprot.txt`). Reference Q16222: 522 aa (canonical isoform AGX2, from `uap1.S-human-ortholog.json`).

Method: Biopython PairwiseAligner global, BLOSUM62, gap open -10, extend -0.5.

Aligned residue pairs: 505; identical: 382 (75.6% of aligned pairs).

| Human interval | Frog interval | Identical |
|---|---|---|
| 1-453 | 1-453 | 342 |
| 471-522 | 454-505 | 40 |

Human positions with no frog counterpart: 454-470.

Human alternative-sequence features (UniProt):

- 454-470: in isoform AGX1
- 454-454: in isoform 3

UniProt UDP-GlcNAc/UDP-GalNAc binding-site residues conserved in frog: 15 of 15.

| Human pos | Human aa | Frog pos | Frog aa | Conserved | Ligands |
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

Residues named as nucleotide-sugar contacts in the human AGX1/AGX2 structures (PMID:11707391):

| AGX1 pos (paper) | Canonical pos | Human aa | Frog pos | Frog aa |
|---|---|---|---|---|
| 223 | 223 | N | 223 | N |
| 290 | 290 | G | 290 | G |
| 303 | 303 | E | 303 | E |
| 327 | 327 | N | 327 | N |
| 331 | 331 | H | 331 | H |
| 381 | 381 | F | 381 | F |
| 383 | 383 | F | 383 | F |
| 453 | 453 | R | 453 | L |
| 455 | 472 | K | 455 | K |

Human UniProt mutagenesis sites mapped to frog:

| Human interval | Human aa | Frog aa (aligned) | Human mutant phenotype |
|---|---|---|---|
| 115-122 | RLGVAYPK | RLGVSYPK | Abolished UDP-N-acetylhexosamine pyrophosphorylase and protein-pyrophosphorylation activities. |
| 407-407 | K | K | Abolished UDP-N-acetylhexosamine pyrophosphorylase and protein-pyrophosphorylation activities. |
| 453-453 | R | L | Decreased interaction with IRF3, leading to decreased pyrophosphorylation of IRF3. |
