# PA4088 paralog identity analysis

Script: `paralog_identity.py` (run with `uv run python paralog_identity.py`;
raw output in `RESULTS_raw.txt`). Sequences are fetched live from UniProt and
aligned globally with Biopython PairwiseAligner (BLOSUM62, gap open -10,
extend -0.5); identity is identical columns over aligned columns after
trimming end gaps.

## Question

PANTHER node PTN000241400 (glutamate-1-semialdehyde 2,1-aminomutase IBD, 15
leaves) holds both the canonical PAO1 HemL (PA3977, P48247) and PA4088
(Q9HWU0), plus PA5523 and two Bradyrhizobium paralogs. Is PA4088 a HemL
ortholog or a divergent paralog?

## Result

| pair | % identity |
|---|---|
| E. coli HemL P23893 vs PAO1 HemL P48247 | 65.7 |
| E. coli HemL vs PA4088 | 26.9 |
| PAO1 HemL vs PA4088 | 26.5 |
| PA4088 vs PA5523 | 49.9 |
| PA4088 vs other PAO1 class-III aminotransferases (BioA, SpuC, DavT, AruC) | 21.3-24.3 |

All sequences carry a lysine at the position aligned to E. coli HemL Lys265
(the PLP Schiff-base lysine), as expected for any class-III
aminotransferase-fold enzyme.

## Interpretation

PA4088 and PA5523 form a paralogous pair that is only marginally closer to
HemL (about 27%) than to other class-III aminotransferases of the same genome
(21-24%), whereas HemL orthologs from E. coli and P. aeruginosa are 66%
identical. The data fit PA4088 being a divergent member of the GSAM-like
family rather than a second HemL. Sequence identity alone cannot show what
PA4088 catalyses; it is a reason to doubt, not to refute, GSAM activity.
