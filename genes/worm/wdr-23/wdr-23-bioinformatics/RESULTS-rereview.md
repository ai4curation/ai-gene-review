# wdr-23 re-review: S6FN32 versus the reviewed WDR-23A/B isoforms

Script: `compare_isoforms_rereview.py` (stdlib only; run with `uv run --script compare_isoforms_rereview.py`
from this directory). Output: `RESULTS-rereview.json`. Inputs are the S6FN32 UniProt flat file
(`wdr-23-uniprot.txt`) and the Swiss-Prot P90794 isoform FASTA files in the gene folder. No prediction
output is read.

## Identity

S6FN32 (WormBase D2030.9d, 498 aa) is an exact substring of both reviewed products:

- WDR-23A (P90794, canonical, 571 aa): S6FN32 starts at residue 74.
- WDR-23B (P90794-2, 530 aa): S6FN32 starts at residue 33.

S6FN32 is therefore an N-terminally shortened alternative gene model of wdr-23 that begins at an
internal methionine (Met74 of WDR-23A). It lacks:

- the WDR-23A-specific N terminus MGNWITSTFLRFDLFQRHQPNRFLEYTRVQHSNQSPAYSVRTAAEIVAHQRMKP (54 aa),
- the WDR-23B-specific N terminus MPYKRHSSSNLKR (13 aa, basic),
- the 19-residue segment NHSNDSDTDFSSDDEGCPK shared by A and B.

## Retained features

All six WD repeats annotated on P90794 lie within the retained region (see the earlier
`RESULTS.md` feature table). Four (W/Y)DxR motifs, the DDB1-binding "DxR box" signature of DCAF
WD40 proteins, are present at S6FN32 positions 266 (WDKR), 313 (WDLR), 336 (WDYR) and 440 (WDER).
Motif presence is a sequence observation only; DDB-1 binding of this product has not been assayed.

## Interpretation limits

The isoform-specific N termini are the regions associated with the distinct cytoplasmic (A) and
nuclear (B) localization of the assayed isoforms, so the localization of the S6FN32 product cannot
be inferred from either. Whether D2030.9d is translated in vivo is not established by this analysis.
