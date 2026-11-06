# DgcA/DgcB versus the characterized Chromohalobacter DdhC system

Script: `pairwise_orthologs.py` (Biopython PairwiseAligner, global, BLOSUM62,
gap open -11, extend -1), run from the repository root with
`uv run python genes/PSEPK/dgcA/dgcA-bioinformatics/pairwise_orthologs.py`.
Sequences are read from the cached UniProt flat files. Raw output:
`pairwise_orthologs.out` (the alignment table, then the motif table).

## Results

| Query (KT2440) | Length | Target (C. salexigens DSM 3043) | Length | Identical / aligned | Identity |
|---|---|---|---|---|---|
| Q88R24 DgcA (PP_0310) | 686 | Q1QYW1 DdhC (Csal_0990) | 694 | 557 / 686 | 81.2% |
| Q88R23 DgcB (PP_0311) | 650 | Q1QYW0 Csal_0991 | 670 | 469 / 650 | 72.2% |

## 4Fe-4S ferredoxin-type cysteine motifs

The script also scans DgcB and Csal_0991 for the CxxCxxCxxxC ferredoxin motif.

| Protein | Motif 1 | Motif 2 |
|---|---|---|
| Q88R23 DgcB | 245 CVQCGKCEAMC | 319 CTTCRACVEEC |
| Q1QYW0 Csal_0991 | 250 CVQCGRCEAVC | 328 CTTCRACVEEC |

DgcB keeps both cysteine motifs of Csal_0991, although the unreviewed DgcB
record lists only one PROSITE PS00198/PS51379 match.

## Interpretation

Q88R24 and Q1QYW1 share 81.2% identity over their full length, and Q88R23 and
Q1QYW0 share 72.2% identity over their full length. Both pairs are full-length,
same-architecture orthologs at a level that supports transferring the
biochemically characterized DdhC activity and the Csal_0991 electron-acceptor
role to the KT2440 proteins. DgcB conserves both cysteine motifs that UniProt
assigns to the two [4Fe-4S] clusters of Csal_0991. The alignment does not by
itself show which flavin the KT2440 protein binds or which electron acceptors
it uses.
