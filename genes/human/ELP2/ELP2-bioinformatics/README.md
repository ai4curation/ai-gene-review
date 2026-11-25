# ELP2 offline evidence

Run with Python 3.10 or later; only the standard library is used:

```sh
python reproduce.py
python -O reproduce.py
python reproduce.py --output /tmp/elp2-recomputed.json
```

The script reads database-inputs.zip in memory, verifies its checksum and the exact input manifest, reconstructs the output and compares it byte-for-byte with results.json. It never extracts files or uses the network. An output path must be new. The package can be moved to another directory without repository imports, an environment installation or absolute private paths.

The archive holds official database responses, seven sequence FASTAs, the normal GOA table and frozen source dictionaries. Its GAF member is explicitly the selected human ancestral-path subset of the full captured IBD file; the manifest records the parent hash and line numbers. The replay checks that positive join and does not establish global absence of other annotations or historical losses. Current complete donor query snapshots are not a complete historical literature census.

Input names, regular-file modes, member set, size and SHA-256 are checked. Duplicate, unsafe-path, non-regular, encrypted, oversized or corrupted members are rejected. SHA-256 provides recorded-input integrity, not an independent signature authenticating a modified manifest.

No article bodies, figures, provider logs or private file paths are bundled. original-locators.json records article routes, inspected sections and hashes, which are navigation/integrity evidence rather than offline redistribution of those originals. The script does not infer annotation actions, assay mechanisms or equivalent function across seven products.
