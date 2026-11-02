# Reproduce DST sequence and source joins

This Python 3.9+ standard-library analysis computes four bounded checks: exact curated interaction joins, OpenCell target accession groups, deposited 3GJO peptide correspondence to current products, and the literal PAINT IBD/target lineage. It does not infer biological function from a score or turn an absent current interaction record into a negative experiment.

The nine unmodified official FASTA responses are concatenated in products.fasta. source-contexts.json contains the 68 unchanged normalized source dictionaries used as join keys. source-manifest.json gives exact URLs and SHA256 hashes for these inputs and the six external source snapshots. Large full datasets are not bundled. Supply those saved/downloaded files explicitly; current upstream datasets can change, and a hash mismatch is reported rather than silently analyzing different evidence.

```sh
python3 replay.py --intact /data/intact-Q03001.tsv \
  --opencell /data/OpenCell-protein-interactions.csv \
  --cif /data/3GJO.cif --tree /data/PTHR23169-treeinfo.json \
  --msa /data/PTHR23169-msa.json --ibd /data/IBD.gaf --check
```

Use `--output results.json` to regenerate the computed output. `--check` compares every result against measurements.json. No network calls, credentials or external libraries are used by the script. IBD.gaf is the uncompressed PANTHER ancestral-annotation file; the tree/MSA are the v19 family captures, and their exact hashes distinguish them from later revisions.

The executed result is summarized in RESULTS.md. Zero-based source-row and data-record indexes are labeled explicitly; OpenCell physical line numbers include its header. All accession groups, fragment features and taxonomic fields remain visible. ROGID checks authenticate the reference sequence represented by an interaction record, not an entire assayed construct. The 3GJO historical accession and actual peptide sequence are both preserved.
