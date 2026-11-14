# PA14 to PAO1 mapping of the P. aeruginosa BCCT transporters BetT1, BetT2, BetT3

Question: Malek et al. 2011 (PMID:21478341) name the three BCCT transporters by PA14
locus tag (BetT1 PA14_70980, BetT2 PA14_12990, BetT3 PA14_69850). Which PAO1 loci are
they?

Method: `map_pa14_betT.py` fetches the PA14 and PAO1 protein sequences from UniProt and
computes global (Needleman-Wunsch, BLOSUM62) percent identity over aligned columns.
Run: `uv run --no-project --with biopython python map_pa14_betT.py`. Raw output: `output.tsv`.

## Results

| PA14 protein | PAO1 PA5375 (Q9HTI9) | PAO1 PA3933 (Q9HX83) | PAO1 PA5291 (Q9HTR3) |
|---|---|---|---|
| PA14_70980 BetT1 (A0A0H2ZIB8, 516 aa) | 99.2% | 54.8% | 46.8% |
| PA14_12990 BetT2 (A0A0H2ZFQ2, 653 aa) | 54.6% | 100.0% (identical) | 49.3% |
| PA14_69850 BetT3 (A0A0H2ZJC5, 661 aa) | 47.2% | 49.3% | 100.0% (identical) |

## Conclusion

PA14_12990 BetT2 is identical to PAO1 PA3933, and PA14_69850 BetT3 is identical to PAO1
PA5291. BetT1 is PA5375. So in PAO1, BetT2 = PA3933 and BetT3 = PA5291.
