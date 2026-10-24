# GEMIN5: human–horse sequence comparison

The downloaded human Q8TEQ6 sequence (1508 residues) and selected horse A0A9L0R5P7 sequence (1433 residues) share 89.2% identity among 1431 paired residues. Paired coverage is 94.9% of human and 99.9% of horse.

Full alignments, sequence hashes and calculation details: [GEMIN5.json](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/GEMIN5.json). Reproduce with [compare.py](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/compare.py) using the two downloaded UniProt text records. See the [methods and limitations](../../../../projects/PROTNLM_EVALUATION/mammal-benchmark/paired-sequences/README.md).

- [x] Computed from sequence inputs; no hardcoded results.
- [x] The same script was run on ten different gene pairs.
- [x] Alignment completed and full output retained.
- [ ] Orthology, gene-model completeness and conservation of each biological claim require additional evidence. Sequence similarity alone does not establish them.

Current UniProt sequences were compared; their identity with the original ProtNLM input sequences has not been established.

## Internal deletion at the RNA-recognition module boundary

The horse sequence lacks the aligned human segment 723–798. This spans the end of the tandem WD40 RNA-recognition region (the human structural construct extends to residue 739) and adjacent sequence, rather than just an arbitrary low-complexity tail. The C-terminal RNA-binding and dimerization regions are retained in the global alignment. The deletion raises a specific question about the integrity of the N-terminal RNA-recognition module; it does not demonstrate loss of all GEMIN5 activities or localization. See PMID:27881601 for the WD40 structure.
