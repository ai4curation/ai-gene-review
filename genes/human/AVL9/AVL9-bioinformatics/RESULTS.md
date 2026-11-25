# AVL9 localization resources

Script: `opencell_localization.py`. It fetches OpenCell's line annotations (PMID:35271311; endogenous tags in HEK293T) and the Human Protein Atlas subcellular-location call. Run on 2026-10-05; raw output is in `results.txt`.

```
OpenCell lines: 1310
AVL9	not in OpenCell
HPA	AVL9	main=['Endoplasmic reticulum']	additional=None
```

AVL9 has no OpenCell line. HPA antibody staining calls it endoplasmic reticulum, with no additional location.
