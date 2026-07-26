# MutL pairwise identity analysis

This analysis reproduces the sequence-identity statement used to transfer
Pseudomonas aeruginosa MutL endonuclease evidence to Pseudomonas putida KT2440
MutL. It also runs the same script on UvrD proteins as an independent smoke
test.

Inputs are canonical FASTA records fetched from UniProtKB:

- Q88DD1: P. putida KT2440 MutL
- Q9HUL8: P. aeruginosa PAO1 MutL
- Q88C31: P. putida KT2440 UvrD
- P03018: Escherichia coli K-12 UvrD

Run the complete workflow:

```bash
just --justfile genes/PSEPK/mutL/mutL-bioinformatics/justfile all
```

`pairwise_identity.py` uses a global Biopython `PairwiseAligner`. All input and
output paths and all alignment scores are command-line parameters. The recorded
analysis uses match `2`, mismatch `-1`, gap-open `-5`, and gap-extension `-0.5`.
The result TSV records sequence SHA-256 digests, lengths, alignment parameters,
Biopython version, aligned residue pairs, identical pairs, and percent identity.
