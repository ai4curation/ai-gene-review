# EIF2B2 evidence replay

This small package reproduces literal sequence, annotation, interaction and pathway joins used in the EIF2B2 review. It requires Python 3.10 or later and the standard library only.

```sh
python reproduce.py --output /tmp/EIF2B2-results.json
```

The output path must not already exist. Compare the resulting JSON with `results.json`. The script verifies the archive, configuration and every member by SHA256 before processing. It reads the archive without extracting files, rejects unsafe or duplicate names, checks response completeness, and fails explicitly on missing inputs, mismatched sequences or unsupported ARBA predicates. It performs no network requests and installs nothing.

`source-inputs.zip` contains 25 database records or extracts. `inputs.json` identifies their exact bytes, available acquisition URLs and timestamps. The PAINT GAF extract preserves all four rows for PTN000027996, their original line numbers and the complete source-file hash; it is explicitly an extract, not a complete family annotation file. Other API records retain their complete selected response bytes. The 42 source dictionaries and normal GOA are included without curation decisions so their join can be independently replayed.

Outputs cover:

- Official sequence versus the target PAINT alignment, ancestral-node placement and literal IBD records.
- Complete saved IntAct records and the eight source/partner joins, preserving mutation sides, tags, methods and reference sequence identifiers.
- Current partner classifications and donor records, with propagated and experimental annotations kept distinguishable by their original evidence codes.
- Literal ARBA condition sets matched against the official target record.
- Typed Reactome paths from the two cited events to the exact human beta entity and cytosol.

The replay does not make biological decisions or evaluate publication methods. Reference sequence checksums do not prove experimental insert identity. An interaction record is not automatically a direct binary interface; current donor annotations are not automatically independent experiments. The accompanying source guide and [RESULTS](RESULTS.md) explain those limits. No publication body is bundled in this archive.
