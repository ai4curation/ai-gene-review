# DOCK2 interaction source records

This is a projection of original IntAct and MINT records for the 46 literal target/partner/publication assertions in the DOCK2 seed. It contains 142 matching records: 139 IntAct screening records and three MINT RAC1 records. Multiple records for a pair are retained as records, not counted as independent physiological validations. [sources.yaml](sources.yaml) identifies the two public inputs, retrieval times, hashes and output inventory. [selection.json](selection.json) supplies the selected assertions; [records.json](records.json) preserves the measured/curated record fields.

Run with Python 3 and the two saved raw responses:

```sh
python3 extract.py --intact /path/to/intact-Q92608-tab27.tsv --mint /path/to/mint-Q92608-tab27.tsv --out /tmp/DOCK2-records.json
```

Or request the public current records without credentials:

```sh
python3 extract.py --download /tmp/DOCK2-current-inputs --out /tmp/DOCK2-current-records.json
```

The saved-input command reproduces the committed projection exactly when input hashes match. The live command may return changed records; its output reports the actual raw hashes. A custom `--selection` JSON may be supplied. No unpublished API key, private database or manually entered result is required.

The extractor does not infer protein function. Sequence/isoform reconstruction, experimental limitations and the annotation judgments are described in the [source evidence guide](../DOCK2-source-evidence.md). A full parent-sequence checksum and a separately annotated sufficient-binding-region feature are different pieces of information. The record preserves both. Assay host species is also distinct from the species of a protein construct.
