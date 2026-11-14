# PP_4348 bioinformatics results

Script: `align_to_metC.py` (Biopython global alignment, BLOSUM62, gap open -10, extend -0.5), run from the repository root on 2026-11-13.

```
MetC length 395, PP_4348 length 364
aligned pairs 357, identical 109 (30.5% of aligned)
MetC K210 aligns to PP_4348 position 186: K
```

Interpretation: PP_4348 shares about 30% identity with E. coli MetC over almost its full length, and its PLP-binding Lys186 (UniProt PIRSR001434 feature) aligns with MetC Lys210, the Schiff-base lysine seen in the MetC crystal structure. This is consistent with family membership (both are PTHR43500:SF1) but does not by itself show that PP_4348 prefers cystathionine as substrate.
