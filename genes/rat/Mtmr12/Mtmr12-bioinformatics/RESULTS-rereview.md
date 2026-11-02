# Mtmr12 re-review sequence comparison (2026-10-21)

Script: `compare_sequences_rereview.py` (PEP 723; run with `uv run --script compare_sequences_rereview.py > results-rereview.json`).
Sequences are fetched live from UniProt REST; no prediction files are used as input.
Global alignment: Biopython PairwiseAligner, BLOSUM62, gap open -10, extension -0.5.

## Lengths

| Accession | Description | Length |
|---|---|---|
| A0A8I5ZMD5 | rat TrEMBL product (Ensembl ENSRNOP00000078948) | 732 |
| Q5FVM6 | rat Swiss-Prot canonical (cDNA BC089876) | 748 |
| Q80TA6 | mouse Swiss-Prot | 747 |
| Q9C0I1 | human Swiss-Prot | 747 |

All four are in PANTHER subfamily PTHR10807:SF37 (MYOTUBULARIN-RELATED PROTEIN 12).

## Alignment to the canonical rat product

A0A8I5ZMD5 residues 41-732 align to Q5FVM6 residues 57-748 with 691 identical residues (691/692).
The first 40 residues of A0A8I5ZMD5 align to Q5FVM6 1-56 with only scattered identities (1, 1, 6 and 3 identical residues in four short blocks), i.e. the N-terminal segment is unrelated.

Against mouse Q80TA6, A0A8I5ZMD5 41-732 aligns to 56-747 with 651 identities; against human Q9C0I1 the same region aligns with 607 identities across three blocks.

## N-terminus

| Accession | First 60 residues |
|---|---|
| A0A8I5ZMD5 | MVVSWVIRKFLCFCCKVCFPFPGYPSFLSFPKPWRISLLPYTVLKYVQEDSCQLGICGRL |
| Q5FVM6 | MLGKGGVGGGGGTKAPKPSFVSYVRPEEIHTNEKEVTEKEEVTLHLLPGEQLLCEASTVL |
| Q80TA6 | MLGKGGVGGGGGTKAPKPSFVSYVRPEEIHTDEKEVTEKEVTLHLLPGEQLLCEASTVLK |
| Q9C0I1 | MLGKGVVGGGGGTKAPKPSFVSYVRPEEIHTNEKEVTEKEVTLHLLPGEQLLCEASTVLK |

The canonical N-terminus (MLGKG...GGGGGTKAPKPSF) is conserved between rat, mouse and human. The A0A8I5ZMD5 N-terminus is not found in the mouse or human orthologs. Its maximum 11-residue Kyte-Doolittle hydropathy within residues 1-40 is 1.9 (window starting at residue 10), against 0.29-0.71 for the canonical orthologs; this hydrophobic segment is what the UniProt SignalP feature (residues 1-20) calls.

## Catalytic motif

MTM1 (Q13496) catalytic CX5R motif CSDGWDR starts at residue 375. The aligned segment is EENASDL in A0A8I5ZMD5, Q5FVM6 and Q9C0I1: the catalytic cysteine and arginine are absent in every MTMR12 product, so the selected product is a pseudophosphatase like the canonical protein.

## Interpretation (limits)

- A0A8I5ZMD5 is an alternative gene model of rat Mtmr12 that differs from the cDNA-supported canonical product only in its first 40 residues (canonical 1-56 replaced). Whether the alternative first exon is transcribed and translated is not established by this analysis.
- The core of the protein (the myotubularin-like pseudophosphatase domain and the C-terminal region) is identical to the canonical rat product.
- Sequence identity does not establish folding, localization or MTM1 binding of A0A8I5ZMD5.
