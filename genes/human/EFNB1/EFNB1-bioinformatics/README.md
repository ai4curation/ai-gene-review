# EFNB1 saved-data evidence replay

This analysis reconstructs target-specific records from the original saved interaction, sequence, phylogeny, pathway and supplementary-table inputs. It does not assign biological verdicts or infer native interfaces from reference-sequence identity.

The 8.46 MB `inputs.zip` contains 147 dataset files. It includes the whole IntAct query, PANTHER tree/MSA/IBD inputs, target and donor official records, the successful Reactome responses needed for the target traversal, two original supplementary workbooks, the original AP-MS network and the original urinary-exosome table. It contains no primary article main text or PDF. The parent supplementary ZIP is not redistributed; its member paths and hash document the already verified extraction of the unchanged workbooks.

Use Python 3.9 or later with `requirements.txt` installed, then run from any working directory:

```sh
python reproduce.py
python reproduce.py --inputs /path/to/inputs.zip --output replay.json
```

No network call is made. The script verifies the complete archive hash and every member before parsing. It derives and compares the selected records, sequence checksums, graph paths, raw table cells and incident-record counts with the machine-generated `source-projections.json`, then emits a compact JSON summary. `source-manifest.json` records the public source URLs, exact hashes and acquisition scope. The original inputs may also be obtained independently from those sources, but a changed release must not silently replace the recorded snapshot.

The IntAct fields use named MITAB columns, with literal taxon, host, bait/prey, detection method, features and reference checksum fields preserved. A matching ROGID verifies a curated reference sequence; it does not prove that the experiment used the entire natural product, that a tag was absent or that a specific interface was mapped. Screening validation is not assumed for every individual pair. The Reactome traversal includes named ephrin branches that do not lead to the target, so a positive target path is independently reproducible.

`source-assertions.json` retains the 66 original source dictionaries. `source-projections.json` exposes the complete selected cells and source fields, including the distinction between new SPR measurements and literature affinities. The readable interpretation and its limits are in [RESULTS.md](RESULTS.md) and the [source guide](../EFNB1-source-guide.md).
