# ANKRD46 OpenCell localization

Script: `opencell_localization.py`. It fetches OpenCell line annotations (PMID:35271311; endogenous tags in HEK293T) and reads the grade legend from the OpenCell web bundle. Run on 2026-10-04.

```
ANKRD46	cell_line_id=1394	terminus=N	categories=['publication_ready', 'er_3', 'vesicles_1']
grade 3 = Prominent signal
grade 2 = Clearly detectable signal
grade 1 = Detectable but subtle and/or weak signal
```

Endogenously tagged ANKRD46 gives a prominent (grade 3) endoplasmic reticulum signal and a weak (grade 1) vesicle signal, consistent with its single predicted C-terminal transmembrane helix.
