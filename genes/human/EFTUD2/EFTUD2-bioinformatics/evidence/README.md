# EFTUD2 literal-data evidence replay

Run with Python3.10 or later; no external package or network is required:

```bash
python replay.py --check
python replay.py --output /tmp/eftud2-results.json
```

The script verifies the archive SHA256, every original input SHA256/size and exact archive membership before parsing. It reads archive members directly without extracting paths. Missing or changed input gives an explicit error, including under Python optimization.

The archive contains original database responses only: PANTHER tree/MSA, literal PAINT IBD records, UniProt identity/partner records, InterPro/ARBA, official GO definitions, RCSB deposited entities, IntAct MITAB and the Reactome nodes needed for literal target paths. It contains no primary article body. input-manifest.json records source addresses when present in the original acquisition receipt; missing receipt URLs are left unspecified. Hashes identify the captured versions, not current live content.

config.json contains the unchanged imported source assertions and target identifiers. The parser finds the target in the tree/MSA, evaluates rule conditions, joins deposited entities to Q15029, selects source-specific interaction records with features on their original sides, and traverses curated model edges. It does not hardcode annotation verdicts or generate experimental results. results.json is recomputed by --check.

No IntAct hit in this capture is not a negative experiment. Proximity labeling, AP-MS and binary interaction methods remain distinct. Sequence equality concerns deposited reference sequences, not complete model coverage or experimental insert sequencing. PAINT donor count and target self-donors do not measure support quality. Reactome paths establish model content rather than independent biological experiments. Clinical, assay and source-access interpretation remains in the review and source guide.
