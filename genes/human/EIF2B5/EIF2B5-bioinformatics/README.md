# EIF2B5 database evidence replay

Run from this directory with Python 3.10 or newer (standard library only):

```sh
python3 reproduce.py --output /tmp/eif2b5-results.json
```

Choose a new output path; existing outputs are deliberately not overwritten. `--inputs PATH` selects another compatible package. No network access, installed package, repository checkout or environment creation is needed.

`inputs.json` records the exact SHA256 of `config.json`, the approximately 0.5 MB archive and all 31 members. The archive contains database snapshots, source contexts and a literal four-line PAINT IBD extract, not publication bodies. The extract records the original complete-file hash and physical line positions; it proves those positive records, not global absence. `original-locators.json` supplies the separately inspected publications' routes and scope. Unavailable full text is not pretended to be bundled.

The program derives source/GOA joins, target sequence and tree ancestry, interaction pairs and partner records, ARBA predicate matches, current donor records, typed Reactome paths and HPA location/cell-line text. It preserves evidence codes, species, features and original identities. It does not compute biological verdicts, identify an experimental insert from a reference sequence, or inspect image pixels.

Inputs are checked before computation. Missing files, changed hashes, unsafe/duplicate archive members, unsupported rule predicates, incomplete donor responses and inconsistent joins fail explicitly. The archive is read in memory without extracting paths and has a bounded uncompressed size. Results are written only after derivation succeeds.

Verification performed:

- [x] Normal and `python -O` runs reproduce `results.json` byte-for-byte.
- [x] The same script reproduces the independent EIF2B2 input package's existing results exactly.
- [x] An altered configuration fails under `python -O` with no result file.
- [x] Missing inputs and attempts to overwrite an output fail.
- [x] All 58 source contexts and the official 721-residue sequence are derived from inputs.

The checked JSON is intentionally detailed; [RESULTS.md](RESULTS.md) explains the finite findings and their limits.
