# Reproduce ENTPD1 product projections

The scripts use only Python's standard library. Inputs are frozen official UniProt JSON records and separately requested isoform FASTA records. Source URLs and SHA256 digests are in inputs.json; no network request is needed for replay. The script is input-driven and contains no gene-specific sequence or expected length. It checks alternative-sequence preimages, overlapping edits, and exact reconstruction of the separate FASTA before projecting unchanged canonical residues. Read RESULTS.md for the biological limits.

Run from this folder with an existing Python 3 interpreter; choose output paths outside the checked-in results:

```sh
python3 reconstruct_products.py --uniprot inputs/P49961.json --fasta inputs/P49961-isoforms.fasta --output /tmp/ENTPD1-products-replay.json
python3 reconstruct_products.py --uniprot inputs/P97687.json --fasta inputs/P97687-isoforms.fasta --output /tmp/ENTPD1-rat-replay.json
python3 check_reconstruction.py --uniprot inputs/P49961.json --fasta inputs/P49961-isoforms.fasta
python3 check_reconstruction.py --uniprot inputs/P97687.json --fasta inputs/P97687-isoforms.fasta
diff results/products.json /tmp/ENTPD1-products-replay.json
diff results/rat-control-products.json /tmp/ENTPD1-rat-replay.json
```

The human reconstruction preserves all six imported products. The rat input is an independently acquired control, not a substitute for the human record. Neither sequence agreement nor retention of catalytic/site coordinates establishes biological equivalence, catalytic activity or membrane topology for any untested product. Do not overwrite these snapshots with later live records; a newer analysis requires a separately identified input set.
