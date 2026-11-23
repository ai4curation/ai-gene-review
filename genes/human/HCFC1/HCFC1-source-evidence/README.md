# HCFC1 source evidence

`check_sources.py` retrieves selected source-linked IntAct records from the official PSICQUIC endpoint. It checks the HCFC1 accession, publication identifier and record identifier before retaining an association. `checks.json` records the retrieval time, response hashes, selected source fields and unresolved expectations; `RESULTS.md` is generated from those checked fields.

The recorded data index the cited experiments. They are not independent replication, proof of a direct binary interface, or evidence for a new catalytic function. Organism identifiers refer to interacting proteins; assay-host fields and fragment features remain separate in the JSON.

Run from the repository root with its existing runtime:

```
python genes/human/HCFC1/HCFC1-source-evidence/check_sources.py
```

The script refuses to overwrite retained results. To refresh, choose a new versioned output directory, for example:

```
python genes/human/HCFC1/HCFC1-source-evidence/check_sources.py --output-dir /tmp/hcfc1-source-checks-2026-11-16
```

The directory is created if needed; existing `checks.json` or `RESULTS.md` files cause an error before any requests. The committed results retain the hash of the script revision that generated them. Keep that evidence revision until its replacement has been checked and recorded. The script does not install dependencies, create an environment, or retain complete API payloads. Missing records remain unresolved instead of being converted into negative evidence.
