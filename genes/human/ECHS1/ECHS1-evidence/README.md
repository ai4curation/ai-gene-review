# Reproduce selected ECHS1 source records

This small extraction contains five IntAct records from three LRRK studies, six MINT records from the STAT3 study, and two literal ECHS1 rows from the MitoCoP supplementary workbook. The [records](records.json) preserve every field of each selected MITAB interaction and a bounded set of workbook identity/classification fields. They are measurements and curated source records, not independent curation conclusions.

[Source URLs and hashes](source-manifest.json) identify the original inputs. IntAct and MINT endpoints are live resources, so later downloads may differ; the script deliberately rejects bytes that do not match this snapshot. The MitoCoP URL supplies an archive: extract `mmc2.xlsx` and verify its member hash. No large archive or article body is bundled.

Run with Python 3.9 or newer and saved original inputs:

```sh
python reproduce.py --intact /path/to/intact-P30084.tsv --mint /path/to/mint-P30084.tsv --mitocop /path/to/mmc2.xlsx --output regenerated.json
```

The script uses only the Python standard library. It makes no network requests and requires no API key. Source counts and selected rows are derived from the inputs. `--target` allows a different literal accession filter; the input hashes remain fixed. The saved replay exactly matched independently extracted source records and the selected workbook cells.

There are 87 total IntAct records and 15 total MINT records in these saved target queries. The selected records retain physical file-line numbers (including any header/comment lines), stable interaction identifiers and full species/feature fields. All 42 MITAB fields are retained; host organism and participant organism must be read separately. A recorded sequence checksum refers to the reference sequence, not automatically a sequenced experimental insert. MitoCoP physical spreadsheet row numbers include its header rows.

Read [the evidence guide](../ECHS1-source-guide.md) for the experimental and biological limits. In particular, an association screen does not establish ECHS1 phosphorylation or a native pathway role, and the STAT3 records include both human and mouse partners. The workbook supports mitochondrial residence without proving matrix topology or isoform specificity.
