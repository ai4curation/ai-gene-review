# Historical DOCK11 construct comparison

Run `just compare` here to compare the two saved amino-acid FASTAs with Python 3.12 (standard library only; no package dependencies). The script accepts input/output paths and calculates every difference; it contains no gene identifiers, expected residues or expected counts. Inputs are the NCBI AY692226.1 CDS translation AAU04438.1 and the reviewed human UniProt Q5JSL3 record retrieved during this review. Output records include complete input SHA-256 values and FASTA headers.

`just refresh` downloads current records to a separate folder and repeats the comparison. The checked-in snapshots remain the inputs for the reported result. A position-by-position comparison is appropriate only for equal-length sequences; unequal lengths return an explicitly inconclusive result instead of pretending to align them. This analysis makes no functional prediction.

The script was also run on a different protein, human DOCK6 Q96HP0 compared with itself, and on the two different-length DOCK2 Q92608-1/-2 sequences. Their result receipts are included. Those independent verification inputs can be retrieved from `https://rest.uniprot.org/uniprotkb/Q96HP0.fasta`, `https://rest.uniprot.org/uniprotkb/Q92608-1.fasta` and `https://rest.uniprot.org/uniprotkb/Q92608-2.fasta`; their exact observed input hashes are in the receipts. The identity comparison returned no differences; the different-length comparison returned inconclusive.

## Saved controls

Run `just controls` to reproduce both control JSON files from the included immutable FASTAs. The DOCK6 identity control uses the same official sequence twice; the DOCK2 control compares the two official products and returns an unequal-length limitation. These are software controls, not additional biological conclusions.

- `Q96HP0.fasta`: [official UniProt source](https://rest.uniprot.org/uniprotkb/Q96HP0.fasta); SHA256 `737ec5929349dcba7f80c390ad5c78ffb1a3d1d51f1028dae877328ff40462f6`.
- `Q92608-1.fasta`: [official UniProt source](https://rest.uniprot.org/uniprotkb/search?query=accession:Q92608&format=fasta&includeIsoform=true); SHA256 `861020bed38f2bcd3b2e946f9e03d06eb0227338085cc308beddf84e0fbf8107`.
- `Q92608-2.fasta`: [official UniProt source](https://rest.uniprot.org/uniprotkb/search?query=accession:Q92608&format=fasta&includeIsoform=true); SHA256 `d4c0320d787dbb846c22e1944f3b57ae091731e0096d12525b5a122c0af27861`.
