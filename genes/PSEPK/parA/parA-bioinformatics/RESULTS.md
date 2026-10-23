# ParA and ParB: P. putida KT2440 vs P. aeruginosa PAO1

Script: `compare_orthologs.py` (run from the repository root with
`uv run python genes/PSEPK/parA/parA-bioinformatics/compare_orthologs.py`).
Input: the cached UniProt records P0A149 and P0A151 (P. putida parA/parB, PP_0002/PP_0001)
and Q9HT11 and Q9HT12 (P. aeruginosa parA/parB, PA5563/PA5562). Global alignment,
BLOSUM62, gap open -10, extend -0.5.

| protein | P. putida length | P. aeruginosa length | identical positions | identity | motif | P. putida position | P. aeruginosa position |
|---|---:|---:|---:|---:|---|---|---|
| parA | 263 | 262 | 219/262 | 83.6% | deviant Walker A (KGGxxK[ST]) | KGGVGKT 11-17 | KGGVGKT 11-17 |
| parB | 290 | 290 | 229/290 | 79.0% | ParB CTP-binding box II (GERRxRA) | GERRWRA 91-97 | GERRWRA 91-97 |

## Interpretation

The P. putida proteins are close orthologs of the P. aeruginosa proteins, at
84% (ParA) and 79% (ParB) identity over their full length. Both genes sit at
the same place in the two genomes, at the start of the chromosome next to oriC.

The motifs that define the two activities are identical and at the same
positions in both species. ParA has the deviant Walker A box KGGVGKT at 11-17,
the ATP-binding signature of the ParA/MinD family. ParB has the CTP-binding box
GERRWRA at 91-97, which coordinates the CTP phosphates in characterized ParB
CTPases.

This is the basis for transferring the biochemical evidence measured on the
P. aeruginosa proteins to the P. putida proteins: ATP hydrolysis by ParA
(PMID:25139949) and parS-stimulated CTP hydrolysis by ParB (PMID:38843873).
