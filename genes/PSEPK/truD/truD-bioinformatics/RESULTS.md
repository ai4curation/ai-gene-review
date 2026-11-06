# truD (PP_1619, Q88MF2): identity and catalytic-site check

Script: `analyze.py` (Biopython global alignment, BLOSUM62, gap open -11 / extend -1, free end gaps).
Recorded as BERIL run `projects/hackathon/runs/20261030T211234Z-trud-identity-catalytic-site` (output `results.json`).
Inputs in `data/`: the dashboard sequence DOAB01000105.1_3, UniProt Q88MF2 (P. putida KT2440 TruD) and Q57261 (E. coli K-12 TruD).

## Identity

- DOAB01000105.1_3 vs Q88MF2: 351/352 identical, 99.7% over the full 352 residues, no gaps.
- DOAB01000105.1_3 vs E. coli TruD Q57261: 128/343 identical, 37.3% identity over 343 aligned positions (query 1-345, E. coli 1-349).

## E. coli TruD functional residues mapped onto the query

All six E. coli TruD residues annotated in UniProt Q57261 as catalytic, mutationally important or substrate-binding are conserved in the query.

| E. coli Q57261 | Role (source) | Query |
|---|---|---|
| Phe27 | binding (ECO:0000250) | Phe28 |
| Glu31 | proposed general base; E31Q loses activity (PMID:19664587) | Glu32 |
| Lys79 | K79L 20-fold decrease (PMID:19664587) | Lys80 |
| Asp80 | catalytic nucleophile; D80N/T inactive (PMID:12756329) | Asp81 |
| Asn129 | binding (ECO:0000305) | Asn130 |
| Phe329 | binding (ECO:0000250) | Phe329 |

The catalytic Asp is conserved: the GXKD motif II of Kaya and Ofengand (2003) reads GLKD at query residues 78-81 (E. coli GQKD 77-80), and query Asp81 is the residue UniProt annotates as the nucleophile of Q88MF2 by HAMAP rule MF_01082.

Note: UniProt P33643 is E. coli RluD (23S rRNA pseudouridine synthase D, catalytic Asp139), not TruD. E. coli TruD is Q57261 (TRUD_ECOLI).
