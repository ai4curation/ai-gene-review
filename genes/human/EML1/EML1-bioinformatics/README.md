# EML1 portable database evidence

Run with Python 3.9 or later and its standard library:

```sh
python3 reproduce.py
python3 reproduce.py --output replay.json
```

The second command creates a new file and refuses to overwrite an existing one. Run from any directory; inputs are resolved beside the script. No installation, network request, article download or archive extraction occurs.

The visible `inputs.json` lists 43 members with SHA-256 hashes, sizes, modes and origins. `config.json` pins the ZIP. The script rejects unsafe paths, duplicate or unexpected members, nonregular files, encrypted members, oversized inputs and changed hashes. It then reconstructs `results.json` from literal inputs and fails if the result differs.

The replay checks 39 GOA source joins, both official product sequences, human/mouse MSA identities, three PAINT IBD ancestry joins, current donor records, rule predicates, typed GO ancestry and eight source-specific interaction pairs. The BioPlex input contains only the declared positive EML1-to-NUDC edge and its header; it cannot support a global absence claim. Rule clause matching to the target is not inferred from output descriptions.

Only database, sequence and source-annotation inputs are bundled. No original article bodies, figures, provider outputs or annotation review decisions are in the archive. Primary access routes, file hashes and inspected scope are documented in `original-locators.json`; this package does not reproduce the biological experiments. See [RESULTS](RESULTS.md) for the interpretation and limits.
