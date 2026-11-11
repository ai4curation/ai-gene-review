# EEF1A2 source replay

Run `python3 reproduce.py --output replay.json`, then compare `replay.json` with `results.json`. Python 3 and its standard library are sufficient. The bundled compressed archive contains exact saved API/database responses and the 44 imported source dictionaries. Every input and the archive are checked against SHA-256 before parsing. `--input-dir DIR` instead consumes the same exact raw files supplied by the reader; missing or changed inputs fail explicitly. No network request or mutable current database is required for replay.

The script resolves the target leaf in the complete PANTHER tree, checks its ungapped alignment against the official human sequence, finds literal ancestral IBDs and loss records, joins current donor records, matches both participant sides and the publication in IntAct, recomputes sequence/taxon ROGIDs, and extracts the two target pairs from the original AP-MS network. The queried partner/source identities come from the imported annotations. It preserves tags, fragments, mutations, interaction methods and expansion flags. URLs and hashes are in `input-manifest.json`; stable interaction URLs and PSI-MI methods are in `results.json`.

A matching ROGID authenticates the database reference sequence, not the DNA insert used experimentally. Coimmunoprecipitation, affinity purification and spoke expansion establish association at their reported resolution. Independent partner classification can justify a binding-class refinement without giving EEF1A2 the partner's catalytic activity. The AP-MS graph is the primary network, not the derived embedding. PAINT inference is assessed from ancestral placement and target descent, not donor count. Original-paper interpretation remains in the source guide and cited literature; this computation does not recreate an experiment.


## BioPlex confidence records

`bioplex-selection.json` is generated from the four full upstream tables identified by URL, size and SHA-256 in `bioplex-inputs.json`. Supply those exact files in one directory, then run:

```sh
python3 bioplex_reproduce.py --input-dir /path/to/saved-bioplex-tables --output bioplex-replay.json
```

Compare the output with `bioplex-selection.json`. The extractor verifies every full input before counting EEF1A2-incident records and selecting TBXAS1, ST6GALNAC1 and SLC13A5. Counts cannot be reproduced from the small selected output alone. Physical lines include the header and start at one. The extractor performs no network requests and does not package an article body or another large archive.

The reviewed input sources are the [BioPlex data downloads](https://bioplex.hms.harvard.edu/interactions.php) and [original Methods](https://pmc.ncbi.nlm.nih.gov/articles/PMC8165030/). The exact download URLs are recorded individually in the manifest. BioPlex 3.0 reanalyses earlier 2.0 data; paired entries are not independent experimental confirmations. Scores and filtering support the reported associations without proving direct native binding or ruling out abundant-protein background. The raw spectra and prey-discriminating peptides were not independently reanalysed.

The source replay was checked with ordinary Python and `python3 -O`; both produced the same bytes as the published results. Deliberately changed saved inputs were rejected by checksum checks in both extractors. Errors use explicit exceptions rather than optimization-sensitive assertions. The preserved archive is still required for the original PAINT/IntAct/graph replay; the BioPlex extractor uses its separate four-file manifest.
