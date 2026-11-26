# DSG2 assay provenance

This analysis checks deposited reference-sequence identities for the DSG2–DSC2 interaction, traces the published affinity measurement in the 2022 network, and extracts the target record from the human parotid-exosome table. It does not convert reference sequences into experimentally sequenced inserts, infer direct binding from co-immunoprecipitation, or assign a function from a table's background annotation columns.

Use Python with the pinned packages declared by `reproduce.py` (or `uv run --script reproduce.py`). `fetch_inputs.py --output-dir inputs` downloads the public inputs and checks the recorded hashes; the network workbook is extracted from its genuine supplementary ZIP. Public services may change their responses or deny access. A changed hash or failed request stops the fetch; no replacement data or synthetic result is produced.

Run `uv run --script reproduce.py --input-dir inputs --output results.json`. To use already saved genuine files, supply `--input-map paths.json`, mapping the five manifest keys to local files. The results are calculated from the supplied records. Snapshot hashes support exact reproduction; a new version requires a separately reviewed manifest.

The ordinary publication cache is separate from these raw assay inputs. Public identifiers and method codes remain available in the output even when a future service response changes.
