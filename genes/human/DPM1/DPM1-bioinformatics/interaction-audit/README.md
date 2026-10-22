# DPM1 interaction and participant-sequence audit

This saved-input analysis reproduces source-specific interaction records and sequence identities. It does not infer a native pathway from a positive screen or replace the primary experiments.

## Reproduce

Python 3.9 or later is required; only the standard library is used.

```sh
python3 replay.py --check
# Recompute outputs:
python3 replay.py
# Optional alternative target in the same captured network:
python3 replay.py --target P48775 --output /tmp/dpm1-tdo2-check
```

Run from this directory, or supply `--directory /path/to/interaction-audit`. Input hashes are verified before computation. The alternative-target run was executed separately and returned six TDO2 records, showing that target filtering is computed rather than encoded as a DPM1 result.

## Inputs and conventions

`sources.json` lists the public download URLs, retrieval metadata and SHA-256 hashes. `inputs/intact-O60762.tsv` is the unchanged headerless IntAct PSI-MITAB response with 42 columns. Physical lines are one-based newline-delimited records; no header is subtracted. All 42 fields are retained in `outputs/selected-records.json`, including source publication, participant accession, host, roles, checksums, features and negative-interaction flag. `selection.json` defines the target and seven source PMIDs corresponding to the historical binding assertions. It does not encode expected measurements.

The UniProt JSON inputs provide complete reference sequences and their source identities. `outputs/sequence-checks.json` recomputes the ROGID as base64(SHA1(sequence)) without padding, followed by the taxon identifier, and compares it with selected MITAB checksums. It also tests every possible single-residue deletion between the MEOX2 clone and canonical reference. Sequence agreement is not proof that every assay tested an unmodified endogenous protein or a native complex.

The snapshot contains more target records than the selected historical source contexts. Unselected records are not negative evidence. The absence of a particular primary DPM3 co-immunoprecipitation from this response does not negate the independently read original experiment. See [RESULTS.md](RESULTS.md) for the executed results and biological scope.
