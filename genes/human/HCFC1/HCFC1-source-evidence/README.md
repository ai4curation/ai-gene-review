# HCFC1 source evidence

`check_sources.py` retrieves selected source-linked IntAct records from the official PSICQUIC endpoint. It checks the HCFC1 accession, publication identifier and record identifier before retaining an association. `checks.json` records the retrieval time, response hashes, selected source fields and unresolved expectations; `RESULTS.md` is generated from those checked fields.

The recorded data index the cited experiments. They are not independent replication, proof of a direct binary interface, or evidence for a new catalytic function. Organism identifiers refer to interacting proteins; assay-host fields and fragment features remain separate in the JSON.

Run from the repository root with its existing runtime:

```
python genes/human/HCFC1/HCFC1-source-evidence/check_sources.py
```

The script refuses to overwrite retained results. To refresh, first choose explicit versioned outputs and preserve this evidence revision. It does not install dependencies, create an environment, or retain complete API payloads. Missing records remain unresolved instead of being converted into negative evidence.
