# EARS2 source audit

This package reconstructs the PAINT lineage, chemical and domain mappings, metal-site sequence correspondences and EARS2 detection in the MitoCoP supplement. These computations trace evidence; they do not independently measure enzymatic activity or localization.

The smaller exact historical database inputs are bundled in `raw-inputs.tar.gz`. **The 13.9 MB publisher Table S1 workbook is not bundled.** `input-manifest.json` records its actual publisher URL, acquisition date, SHA-256 and the MD5 published in the article. The authentic acquisition returned HTTP 200; both hashes were verified.

With Python 3, `beautifulsoup4` and `openpyxl` installed, supply that workbook explicitly:

```sh
python reproduce.py --workbook /path/to/34800366-TableS1-publisher.xlsx --output observed.json
```

Alternatively, download the external workbook with both checksum checks, then replay:

```sh
python fetch_inputs.py --output external-inputs
python reproduce.py --workbook external-inputs/34800366-TableS1-publisher.xlsx --output observed.json
```

The replay performs no network requests and fails clearly when the external workbook is absent or any checksum differs. `fetch_inputs.py` refuses to overwrite a differing existing input or save changed live content. Optional `--all` retrieval also attempts the smaller database inputs; live databases may have changed, so the bundled historical versions remain the reproducible baseline. A complete authenticated directory can instead be passed with `reproduce.py --inputs DIRECTORY`.

The workbook is read-only. An openpyxl warning about unsupported sparklines concerns display features and does not change the source or numeric values. `results.json` is the minimal target-derived output. The query file declares identities and source assertions, not expected biological outcomes. Tree nodes, IBD matches, alignment coordinates, ligand features and table values are derived from the raw data; missing records are not filled with expected results. Imported GO compartment flags remain distinguishable from measurements, and the source workbook preserves their surrounding context.

The bacterial Zn-site comparison is an alignment-based correspondence, not a conclusion that the human protein binds or fails to bind zinc. Current ARBA output is shown without pretending that a broad structural-superfamily match reconstructs a FunFam trigger. Grouped mass-spectrometry identifiers do not establish separate measurements for each natural product.
