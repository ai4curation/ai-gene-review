# Interaction reference identity audit

This analysis verifies the database sequences named by selected IntAct records. It does **not** establish that the experimental cloned insert had that sequence, that an association was direct, or that it occurred physiologically.

`records.mitab` preserves all columns of 95 original source lines selected by exact publication and partner identity from the 43 reviewed protein-binding assertions. `source-manifest.json` records the source URL, full-snapshot hash and original line indices. `reference-sequences.fasta` contains the corresponding 26 official UniProt reference sequences, with accession and taxon in each header. Its provenance and sequence hashes are also in the manifest. These finite inputs are included so the published computation remains reproducible if live database records change.

Python 3.11 or newer is sufficient; the script uses only the standard library. Run from this directory:

```sh
python3 verify_records.py --mitab records.mitab --fasta reference-sequences.fasta --target Q96EV8 --output result.json
python3 verify_records.py --mitab records.mitab --fasta reference-sequences.fasta --target O95295 --output control-snapin.json
```

For each side, the script computes SHA1 of the uppercase amino-acid sequence, encodes the digest in base64 without padding, and appends the numeric taxonomy identifier. It compares that value with the literal `rogid:` field and checks the stated taxon. Missing supplied sequences are reported explicitly. No expected sequence length, number of matches, gene function or curation action is encoded in the algorithm.

The second command tests the same algorithm on a different target, SNAPIN. Both targets draw from the actual source records; this is an input-control check, not an additional functional inference about SNAPIN. Stable IntAct/IMEx identifiers, PSI-MI detection methods, spoke-expansion markers, negative flags and side-specific features remain in the output for inspection.

The DTNBP1–SYBU record illustrates why side preservation matters: the `binding-associated region:1-189` feature is on the DTNBP1 side, while the SYBU side is unspecified. The separately inspected original supplementary screen table does not independently resolve that residue extent. The molecular identity and the assay-construct question therefore remain distinct.
