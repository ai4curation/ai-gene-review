# PRECISE321 checked membership export

This folder contains 84 published modules and measured member weights, independently
checked against the named columns of the source M matrix and all 84 source thresholds.
It is an expression-association dataset, not an experimentally established target network.

- [dataset.json](dataset.json): modules, metrics, memberships, source identity tables and provenance.
- [memberships.tsv](memberships.tsv): module–gene membership rows and measured weights.
- [manifest.json](manifest.json): raw source URLs, retrieval times, checksums, importer hash and checks.
- [calibration-results.md](calibration-results.md): all 20 calibration queries, with individual report pairs.
- [calibration-manifest.json](calibration-manifest.json): generated calibration output checksums.

Raw downloads remain in the ignored cache. To reproduce from the repository root:

```bash
uv run python scripts/compare_with_imodulondb_v2.py PSEPK \
  --cache-dir .cache/imodulondb-repaired \
  --export-dataset projects/P_PUTIDA/tf_census/imodulon
uv run python projects/P_PUTIDA/calibrate_tf_imodulons.py
uv run python projects/P_PUTIDA/build_tf_census.py
```

Use `--offline` on the export command when raw downloads are already cached.
Calibration alone reads the committed export without network access. Its script updates
only `importer_assessment` fields in the manual assessments and regenerated reports.
The manual biological assessments remain independent of module calls.

Sources: [modulytics](https://github.com/SBRG/modulytics/tree/01af982cb604eef842df4209abe39b033d9067d5/organisms/p_putida/precise321)
and the [authors' supplement](https://github.com/SBRG/modulome_ppu/blob/f63a0dfab124ea9022123ce6227d132f39de0108/Manuscript_supp_data/Supplementary_Data.xlsx).
Source licensing notices are retained in [modulytics.LICENSE](modulytics.LICENSE)
and [modulome_ppu.LICENSE](../sources/modulome_ppu.LICENSE).
See the [integration documentation](../../../../docs/imodulondb_integration.md)
for limitations, CLI behavior and evidence interpretation.
