# EIF2B1 source identity and propagation analysis

This analysis reconstructs the database evidence used to review human EIF2B1: PAINT ancestry, interaction partners and reference sequences, natural products, and the Reactome paths assigning the target to cytosol. It does not infer experimental insert sequences from reference checksums or make functional decisions automatically.

## Reproduce offline

Python 3.10 or later and its standard library are sufficient:

```sh
python3 reproduce.py --output replay.json
```

The script reads `source-inputs.zip`, checks the archive and every member against `source-manifest.json`, and writes the complete selected records to the requested new file. Compare that file with `records.json`. An extracted copy can be supplied with `--inputs-dir /path/to/inputs`; the same member hashes are required. Changed inputs fail before output is written. The normal and `python3 -O` runs produced identical results, and a deliberately changed input was rejected under `-O`.

The archive contains 34 input files, including the complete captured IntAct response, official UniProt records, both official product FASTAs, the complete saved PAINT ancestral-assertion file, family tree/alignment, the complete rat-donor QuickGO response, six Reactome records and selected ontology responses. The 53 source dictionaries and manual replacement-term selection are distinguished from database downloads in the manifest. Source URLs, capture metadata and hashes are included. Current service downloads can change; the frozen inputs reproduce this assessment.

`records.json` is machine-generated. The biological interpretation and partner-class judgments in [RESULTS.md](RESULTS.md) are manual assessments. Full article bodies are not included. Literature access and assay limits are documented in the [source guide](../EIF2B1-source-guide.md).
