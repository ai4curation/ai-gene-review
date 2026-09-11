# Lcp3 accession identity

The selected A0A0B4KEF3 sequence is identical to reviewed Lcp3 P07188: 112 of 112 residues match without gaps. Both records map to FlyBase FBgn0002534 and RefSeq NP_001260803.1 / NP_476621.1. Thus the reviewed Lcp3 evidence concerns the same current polypeptide, despite the separate UniProt accessions and the target's isoform-B label.

The related Lcp4 P07189 control is also 112 residues long but differs at 14 positions (98/112 positional matches). A shared cuticle fold does not make the target Lcp4. This comparison establishes current record identity; it does not establish which sequence was supplied to ProtNLM at prediction time.

## Reproduction and provenance

Run `just --justfile genes/DROME/Lcp3/Lcp3-bioinformatics/justfile` from the repository root. `compare.py` parses complete sequences from the frozen local UniProt text records and computes exact equality, SHA-256, length, and ungapped positional matches. No alignment or structure prediction is necessary for the identity claim. The Lcp4 count is a positional comparison, not a phylogenetic analysis.

Sources fetched 2026-09-08: [A0A0B4KEF3](https://rest.uniprot.org/uniprotkb/A0A0B4KEF3.txt), [P07188](https://rest.uniprot.org/uniprotkb/P07188.txt), [P07189](https://rest.uniprot.org/uniprotkb/P07189.txt). Raw records are in the parent directory; direct outputs are [results.json](results.json) and [lcp4-control.json](lcp4-control.json). Python standard library only; Python 3, no external dependencies.

- [x] Inputs are command-line paths; results are calculated, not hardcoded.
- [x] The script was run against another gene product, Lcp4 P07189.
- [x] Both comparisons completed and the output sequences match the records.
- [x] Direct JSON outputs are retained.
- [x] The identity conclusion is limited to the current retrieved sequences.
