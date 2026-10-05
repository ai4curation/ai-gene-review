# ANKRD40 OpenCell localization

Script: `opencell_localization.py`. It fetches OpenCell's line annotations (PMID:35271311; endogenous N-terminal tags in HEK293T) and reads the grade legend from the OpenCell web bundle. Run on 2026-10-04.

```
AHCY	cell_line_id=1761	terminus=N	categories=['publication_ready', 'salvageable_re_sort', 'cytoplasmic_3', 'nucleoplasm_3']
ANKRD40	cell_line_id=1389	terminus=N	categories=['publication_ready', 'pretty', 'cytoplasmic_1', 'vesicles_1', 'golgi_3']
grade 3 = Prominent signal
grade 2 = Clearly detectable signal
grade 1 = Detectable but subtle and/or weak signal
```

Endogenously tagged ANKRD40 gives a prominent (grade 3) Golgi signal, with weak (grade 1) cytoplasmic and vesicle signals. Its partner AHCY is prominently cytoplasmic and nucleoplasmic, and has no Golgi annotation.
