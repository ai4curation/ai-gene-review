# NARF: exact selected product and same-gene reference

Selected J3KS48 has 217 residues; reference Q9UHQ1 has 456 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–128 | 1–128 | 128 |
| 174–258 | 129–213 | 85 |
| 383–385 | 214–216 | 2 |
| 456–456 | 217–217 | 1 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling frozen ProtNLM source and same-gene reference JSON files. Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.

## Re-run 2026-10-20: target sequence read from the UniProt record

The analysis script was revised so it reads the target sequence from the gene's UniProt record rather than from the ProtNLM2 source file, and was re-run; `results.json` and related outputs now reflect this re-run. The original results above are kept unchanged for the record.

Selected J3KS48 has 217 residues; reference Q9UHQ1 has 456 residues.

Biopython PairwiseAligner global BLOSUM62, gap open -10, extension -0.5.

| Reference interval | Selected interval | Identical residues |
|---|---|---|
| 1–128 | 1–128 | 128 |
| 174–258 | 129–213 | 85 |
| 383–385 | 214–216 | 2 |
| 456–456 | 217–217 | 1 |

Reference feature mapping (sequence coverage does not establish retained function):

| Reference feature | Interval | Mapped / length | Identical |
|---|---|---|---|

Reference cysteines (candidate metal-ligand positions; no ligand role is asserted here):

| Reference Cys | Context | Selected position | Cys retained |
|---|---|---|---|
| 3 | MKCEHC | 3 | yes |
| 6 | CEHCTRK | 6 | yes |
| 11 | RKECSKK | 11 | yes |
| 53 | LSDCLAC | 53 | yes |
| 56 | CLACDSC | 56 | yes |
| 59 | CDSCMTA | 59 | yes |
| 86 | NKKCDTS | 86 | yes |
| 99 | VSVCPQS | 99 | yes |
| 122 | RRLCGFL | 122 | yes |
| 172 | TSACPGW | - | no |
| 192 | AHLCTAK | 147 | yes |
| 228 | VAPCYDK | 183 | yes |
| 252 | GADCVLT | 207 | yes |
| 374 | VLACAGG | - | no |
| 378 | AGGCLNG | - | no |

A shared segment does not establish that a truncated product folds, is expressed, localizes, or catalyzes the full-length reaction.

Inputs are the sibling UniProt flat file for the selected product (`NARF-uniprot.txt`) and the same-gene reference JSON (Q9UHQ1 UniProt record). Reproduce with `UV_NO_SYNC=1 uv run python compare_sequences.py` from this directory.
