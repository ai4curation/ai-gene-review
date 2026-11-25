# EFEMP1 evidence extract

This folder reproduces selected database records, proteomic table rows and a PAINT target path from nine hash-checked inputs. It does not calculate GO verdicts, infer direct binding from co-immunoprecipitation, or identify natural splice products from shared peptides. The underlying sources and their access limits are explained in the [source guide](../EFEMP1-source-guide.md).

- `source-manifest.json` gives public URLs, exact SHA256 values and archive-member identities. It contains no credentials. A current URL may return updated data or an access challenge; a hash mismatch is a reason to stop and investigate.
- `selection.json` contains the target accession, literal imported reference/partner joins and ancestral-node identifiers. Counts and selected records are derived from the raw inputs.
- `records.json` preserves full fields for 46 selected interaction joins, workbook headers and target rows, three human-aorta tables, and the target's tree path plus literal ancestral GAF assertions.
- `partner-classes.yaml` contains authored, source-linked interpretations of partner classes. These interpretations are not computation inputs and are distinct from the literal interaction records.
- `reproduce.py` is the extraction program. It needs Python 3.9 or later and `xlrd==2.0.1` for the older HCV XLS workbook; other parsing uses the standard library.
- `RESULTS.md` explains the observed counts and their limits.

Download the inputs from the URLs in `source-manifest.json` or use saved copies with the listed hashes. For the two supplementary ZIP URLs, extract the named workbook member without editing it. The directory passed below must contain all nine listed filenames, including the extracted workbooks. Article bodies and large database snapshots are not bundled here.

```sh
uv run reproduce.py --raw-dir /path/to/saved-inputs --output reproduced-records.json
```

Without `uv`, install the declared `xlrd` version in an isolated Python environment and run the script with that environment's Python. Inputs may also be supplied individually, which permits files to remain in separate archives:

```sh
uv run reproduce.py \
  --raw-dir /path/to/saved-inputs \
  --source ibd=/path/to/immutable/IBD.gaf \
  --output reproduced-records.json
```

`--source ID=PATH` overrides the directory location for that source. The script checks every input hash before extracting any records. It performs no network requests or source-file edits. Run it from any working directory: the manifest and selection are resolved beside the script. Compare the parsed JSON with `records.json`; paths and timestamps are not inserted in the computed result.

Physical table/TSV row numbers are one-based, including headers. OOXML can omit an entirely empty row, so the number of stored physical rows may differ from a workbook application's maximum row number. Selected cells retain their original accession groups and numerical values. Database parent-sequence checksums and interaction-feature intervals are separate evidence; neither proves an experimental insert was full length.
