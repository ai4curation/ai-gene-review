# asr1 (O94400) relative comparison

Script: `compare_relatives.py` (run with `uv run --script compare_relatives.py`); raw output in
`compare_relatives_results.json`. Sequences are fetched live from UniProt REST.

Method: Smith-Waterman local alignment, BLOSUM62, gap open -11, extend -1; z-score against 200
shuffles of the second sequence.

## PANTHER placement (PANTHER 19.0 classification files)

- S. pombe asr1 O94400: PTHR12618:SF20 (PHD AND RING FINGER DOMAIN-CONTAINING PROTEIN 1)
- Human PHRF1 Q9P1Y6: PTHR12618:SF20
- K. phaffii Atg35 C4QVX6: PTHR12618:SF20
- S. cerevisiae Asr1 Q06834: PTHR45798:SF97 (family RING-H2 FINGER PROTEIN ATL61-RELATED-RELATED), a different PANTHER family

S. cerevisiae has no PTHR12618 member in the PANTHER 19.0 budding-yeast file.

## Pairwise results

| Pair | identity | aligned columns | range in first | range in second | z |
|---|---|---|---|---|---|
| O94400 vs Q06834 (Sc Asr1) | 0.326 | 95 | 56-152 | 23-148 | 14.0 |
| O94400 vs Q9P1Y6 (PHRF1) | 0.319 | 276 | 34-318 | 104-420 | 28.2 |
| O94400 vs C4QVX6 (Atg35) | 0.287 | 363 | 55-545 | 21-387 | 22.7 |
| Q06834 vs Q9P1Y6 | 0.288 | 191 | 2-233 | 106-301 | 17.0 |
| Q06834 vs C4QVX6 | 0.314 | 140 | 1-183 | 1-141 | 13.6 |
| O94400[1-200] vs Q9P1Y6 | 0.384 | 125 | 34-167 | 104-230 | 39.0 |

## Interpretation

All four proteins share a homologous N-terminal RING + PHD module (all z > 13). O94400 is
more similar to the PTHR12618:SF20 members PHRF1 and Atg35 than to S. cerevisiae Asr1, and its
similarity to Asr1 is confined to the RING/PHD region. Sc Asr1 is homologous to the SF20 members
over the same module, so its placement in a separate PANTHER family (PTHR45798, plant ATL-type
RING-H2 proteins) looks like a divergent sequence classified by its RING alone. Pairwise scores do
not resolve orthology; the PomBase asr1-ASR1 ortholog call is consistent with the shared module
but is not confirmed by PANTHER. Only properties of the shared RING module (E3 ubiquitin ligase
activity) are safe to transfer; Asr1-specific features such as Ser5P/Ser7P CTD recognition are not.
