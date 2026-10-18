# Reproduce DNM2 interaction selections

This is a saved-input analysis using Python 3.9+ and its standard library. It computes the selections in the DNM2 review from genuine public AP-MS, OpenCell and PSI-MITAB records. It neither predicts interactions nor downloads data silently.

1. Obtain the four exact files named in [source-manifest.json](source-manifest.json) from its public URLs, or supply previously saved copies. Place them together in an input directory. The script verifies every SHA-256 digest and rejects changed snapshots. A current live download may differ from the recorded release; that is a provenance mismatch, not a negative interaction.
2. Run from this directory:

```sh
python3 replay.py --inputs-dir /path/to/saved-inputs --check
```

Without `--check`, the same command writes the two derived JSON outputs. `--check` recomputes the complete outputs and compares their bytes with the checked-in results. No third-party package is required.

`selection.json` specifies the gene and partners in seven imported AP-MS/OpenCell source assertions. `binding-selection.json` contains all 52 imported generic protein-binding source contexts. Those are selection criteria, not hardcoded measured results. `extract.py` traverses the full AP-MS graph and CSV; `replay.py` additionally matches MITAB publication, target orientation and literal partner identifiers.

[dataset-results.json](dataset-results.json) retains all incident graph/CSV records as context and separately marks the selected subset. [binding-results.json](binding-results.json) retains complete matching MITAB fields and physical line numbers. Identical records from different services are not deduplicated into invented independent experiments. An unmatched source row can reflect database coverage or identifier representation and is not called negative.

AP-MS edges preserve their source/target direction and all available attributes. OpenCell records preserve bait direction, complete accession groups and the original numeric fields. Do not read a protein group as proof of an individual splice product, a co-complex result as purified direct binding, or an omitted partner as absent. CSV `csv_line_start_one_based_including_header` and `csv_line_end_one_based_including_header` are one-based including the header; `data_index_zero_based` is zero-based excluding the header. MITAB lines are one-based physical lines in each saved response.

The analysis was executed on the authenticated raw inputs; [RESULTS.md](RESULTS.md) summarizes the computed counts. The source guide and annotation reasons supply the biological interpretation.
