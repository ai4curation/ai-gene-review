# PP_0312 / PP_0313: dimethylglycine-locus ETF versus canonical ETF paralogs

Question: are the ETF subunits encoded beside dgcAB (PP_0312/PP_0313 in
*P. putida* KT2440; Csal_0992/Csal_0993 in *C. salexigens* DSM 3043) orthologs
of the canonical ETF pairs that, in human, serve acyl-CoA dehydrogenases, or a
separate paralog group?

Method: `paralog_identity.py` fetches the UniProt sequences and computes global
pairwise identity (Biopython PairwiseAligner, BLOSUM62, gap open -10, extend
-0.5) over aligned columns. Run from the repository root:

    uv run python genes/PSEPK/PP_0312/PP_0312-bioinformatics/paralog_identity.py

The second ETF pair of each genome (PP_4201/PP_4202, Csal_1614/Csal_1613) was
identified by a UniProt query for PANTHER PTHR43153/PTHR21294 members of
taxon 160488 and 290398; each genome has exactly two alpha and two beta ETF
genes, all in subfamilies PTHR43153:SF1 and PTHR21294:SF8.

## Output (run 2026-11-04)

## ETF alpha
- Q88R22 PP_0312 (KT2440, dgc-locus ETF alpha): 410 aa
- Q1QYV9 Csal_0992 EtfA (C. salexigens, dgc-locus ETF alpha): 422 aa
- Q88F97 PP_4201 EtfA (KT2440, second ETF alpha): 309 aa
- Q1QX41 Csal_1614 (C. salexigens, second ETF alpha): 308 aa
- P13804 human ETFA: 333 aa
| A | B | identical/aligned | identity |
|---|---|---|---|
| Q88R22 | Q1QYV9 | 266/406 | 65.5% |
| Q88R22 | Q88F97 | 102/296 | 34.5% |
| Q88R22 | Q1QX41 | 103/298 | 34.6% |
| Q88R22 | P13804 | 102/308 | 33.1% |
| Q1QYV9 | Q88F97 | 105/282 | 37.2% |
| Q1QYV9 | Q1QX41 | 107/294 | 36.4% |
| Q1QYV9 | P13804 | 100/307 | 32.6% |
| Q88F97 | Q1QX41 | 223/308 | 72.4% |
| Q88F97 | P13804 | 192/309 | 62.1% |
| Q1QX41 | P13804 | 180/308 | 58.4% |

## ETF beta
- Q88R21 PP_0313 (KT2440, dgc-locus ETF beta): 256 aa
- Q1QYV8 Csal_0993 EtfB (C. salexigens, dgc-locus ETF beta): 267 aa
- Q88F96 PP_4202 EtfB (KT2440, second ETF beta): 249 aa
- Q1QX42 Csal_1613 (C. salexigens, second ETF beta): 250 aa
- P38117 human ETFB: 255 aa
| A | B | identical/aligned | identity |
|---|---|---|---|
| Q88R21 | Q1QYV8 | 154/256 | 60.2% |
| Q88R21 | Q88F96 | 65/201 | 32.3% |
| Q88R21 | Q1QX42 | 56/204 | 27.5% |
| Q88R21 | P38117 | 70/208 | 33.7% |
| Q1QYV8 | Q88F96 | 66/215 | 30.7% |
| Q1QYV8 | Q1QX42 | 55/213 | 25.8% |
| Q1QYV8 | P38117 | 61/202 | 30.2% |
| Q88F96 | Q1QX42 | 184/249 | 73.9% |
| Q88F96 | P38117 | 152/248 | 61.3% |
| Q1QX42 | P38117 | 147/248 | 59.3% |

## Interpretation

The dgc-locus alpha subunits are 65.5% identical to each other but only about
33-37% identical to the canonical ETF alpha subunits of the same genomes and to
human ETFA, whereas the canonical bacterial alpha subunits are 58-62% identical
to human ETFA. The beta subunits show the same pattern (dgc-locus pair 60.2%
identical; about 26-34% to canonical ETF beta and human ETFB, against 59-61%
between canonical bacterial ETFB and human ETFB). The dgc-locus ETF is
therefore a distinct paralog group conserved between the two genera, not the
ortholog of the human acyl-CoA-dehydrogenase ETF. PANTHER places both groups in
the same subfamilies, so the subfamily call does not separate them.
Identity values are pairwise and are not a phylogenetic reconstruction.
