# DSP source measurements

These files expose the measured target records behind the RNA-capture, extracellular-vesicle and sperm-nucleus assessments, and the exact Reactome membership paths. They are source extracts, not independent experiments or annotation verdicts.

`measurements.yaml` contains five records: the HeLa RNA-capture row and whole-lysate control row; the human parotid exosome row; the human urinary exosome row; and the study-specific sperm-nucleus row in the author's thesis. Original accession groups and quantitative fields are retained. Historical protein labels do not establish current isoform-specific localization or function. Functional annotations copied into the original spreadsheets are deliberately excluded from the measurement extraction.

`reactome-paths.yaml` contains 24 input/output paths through 12 events. Each path preserves the literal `hasComponent`, `hasMember`, `hasCandidate` or `repeatedUnit` relationships and the target's compartment and sequence-boundary fields. Membership in a curated model does not establish that DSP catalyzes the modeled reaction. The ficolin-rich granule measurement remains unresolved even though the corresponding curated membership is positive.

`source-manifest.yaml` records 77 raw sources, their public URLs and SHA-256 checksums: two original supplementary workbooks, one original article HTML, one author thesis PDF, and 73 Reactome entity/event responses. The full raw articles and workbooks are not republished here. The thesis is catalogued at [Universitat de Barcelona](https://diposit.ub.edu/dspace/handle/2445/60858); Annex 8.2/Table 8.1 belongs to PMID:21630459. Later chromatin-study tables in that thesis are different evidence.

## Reproduce

The script uses `uv` to install its declared Python dependencies. The thesis extraction also needs the Poppler `pdftotext` executable on `PATH`.

```bash
uv run reproduce.py --download --output-dir reproduced
```

Public endpoints may serve a new version, require browser access or return a challenge. The script fails on a checksum mismatch rather than treating such a response as the original. It does not require API keys or pretend to bypass access controls.

Saved originals can be supplied instead. Create a YAML or JSON mapping from each manifest `key` to the corresponding local raw file, then run:

```bash
uv run reproduce.py --input-map /path/to/saved-input-map.yaml --output-dir reproduced
```

The completed saved-input run authenticated all 77 source files and produced the five measurement records and 24 Reactome paths. The target values were independently compared with the source workbooks and the separately traversed Reactome graph. The parser bounds the thesis extraction to Annex 8.2, including its repeated contents-page heading without confusing that heading with measured data. It derives records from the files; no measured result or annotation decision is hard-coded.

## Interpretation limits

- UV capture supplies RNA-contact evidence under the study's stringent capture protocol, without identifying a DSP regulatory RNA target.
- Urinary and parotid fractions contain measured DSP peptides. Their preparation controls do not establish a DSP-specific intravesicular protection result or a role in vesicle production.
- Sperm-nucleus detection is positive fraction evidence, with three peptides and 2.1% coverage. It does not independently establish the nuclear mechanism reported in other cultured-cell experiments.
- Source fields and gene/protein groups remain distinct from assay-construct sequence authentication and from the three current natural DSP products.
